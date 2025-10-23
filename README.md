client
	client(encrypted payload)->request->server
	server(encrypted response )->response->client
	
for example requesting password to server
	client creating encrypted payload 
		{"data":"yJtRL9GzPQp/40HxriVmJM685uVcww8tjEklZCPEC/qXiNfyl1Y+z7HXTGGraeDmsGxMa9EJkj7BPk1ZIO7gI2pTyR6sFpg0ha5fYBCC54WC6hlUrklt3X1XUkn8wMwh9l8CgC/4ZSqhvbeib6OTVNXz6ixx7jyVA1lgjWhlTJro385b/ZK0ZF/JUwTHr3tWLOtbX++YHHkzaUIKhag3orI32/rtHosfb7nYFPxcfgI=","req_code":4,"key":"GRRUcm+7hF1WrmtGdn161TrjbaWXubQSi2xvFSHGLeouJggd2PD+v0lHTfSDDlq8SXe9dKfmD+h/Rp/FHRu512dEQzaIa/txSKiiyeJejFTwjmYbdFjSF3g2zl3EDWRJsY0LIK1wRfOrKB9pao+bWKXeCe8eTVix1qhO5DVXpBk=","iv":"LZFrxz2rtMUrGquaR3IyiMhJhyc7fpgCngOjNgPQK5W3Dc6kQNKOpW3vblum1ofI7mEoML1UwREDxKCrKB5n6pKqO95rMdf3JSKs4KCde0t6cdmzZk7XpS3A5Pg/osrhL6w0txd2XZH7dAEN2a1XsTdimC0nMHxJ14sgpkb+xlM="}
		
	server sending encrypted response 
	{
    "code": 202,
    "data": "miyXxy2l19mwjbzMLeKMTRH9C0jGXqea7L6v/uCs0lhjBQMxlhHix/EXRnQAc0zBMw7+VvpIoF4bpi+NnNTCubtNWyszeZIR0yWQ1EGKWSYp8R6p/NvT0nO1Shn1yLlRWa//2QE15gmPAgQG3K8my1GozgAy7GO6pigW8oZLUqTkSDIJrFGuk1xtKg+LQG9Tt4e6w3U9H0Gf+Lh7KyAREBtgBQUvC4eOPHplk4ocDo5XyWQcr8AA3/KGfvHYQhCOLe/GUSTewAe2xtfvSa24FWecIYZA+qlkLjpJUul8Klz/TsepuwAOmTwx/BJxVlOAn+DrWaM8GdOYS8iEJaovlKkbRIcaRD4tTxilZBozsLUcDU17ZmGkDF3P7/efzmC7bxX786Qd2leI7QRJVJ0kwbKTQavkCHHlDBGVTyy5UA8="
}

goal:
	what is the actual decrypted data | or orginal strings |data
	what the data that there on client before it make payload
	main goal data before and after decryption and encryption 
	
	eg:
	in payload 
		"data":"yJtRL9GzPQp/40HxriVmJM685uVcww8tjEkl .....
		we need to see what is actual data before encoding
	in response 
		"data": "miyXxy2l19mwjbzMLeKMTRH9C0jGXqea7L6v/uCs0lhj
		what is theere in the response 
		
Problems faced in local Crypto Class | library analysis :
	to many decyrptor functions
	not human readable 
	for example 
	logging the decryptor function 
	
	 decrypt: function(e, t, n, r) {
                        r = this.cfg.extend(r),
                        t = this._parse(t, r.format);
                        var i = e.createDecryptor(n, r).finalize(t.ciphertext);
                        console.log(i);
                        return i
                    },
                    
                    
                   r.init {words: Array(80), sigBytes: 315}sigBytes: 315words: (80) [1834011474, -1020261124, 396309388, -1825124589, 1466866872, 2060736585, 1293106069, -1656690188, -548336479, 818105818, -1787382342, -1965481175, -1555721270, 1951917941, 629875842, 373691469, 744602268, -566338037, -1861719078, -738259924, 276854915, -1485831117, 1893278041, -1327853266, 529477292, -398201914, 1833053512, -1506559814, 662876247, -1045649815, -1177590447, 1731937915, -1273341610, 652369960, 473259076, 1676108120, 2079810823, -2079312912, 1357604379, -392013145, -671885014, -1206691282, 252865168, 311104202, -1563811373, 2040136086, -2006069791, 1260281292, -1534268072, -165018020, -1875660636, -973627202, 1539237947, -20196429, -459978530, -1584127550, -211023659, -460583426, 783414587, -912089485, 695041212, 936277124, -1468340300, 1468293414, -338331274, 31617826, -640794952, 1364065354, -1217319915, 969024258, 2031648273, -1688119572, 322015723, 163446585, -349234573, 1812722114, -83733877, 914925226, 1857507077, 84215045][[Prototype]]: Object
chunk-vendors.5aa273bf.js:15393 r.init {words: Array(168), sigBytes: 668}sigBytes: 668words: (168) [-1651090609, -483389307, -7674475, 2016045715, -1875988390, -1582824312, -1774004981, 316298952, 946778522, -631383231, 1418264526, -1527508361, -1046745525, -274865284, 1944472670, -247150212, -1907392577, 1654579795, -810819188, -1956008398, 2089453429, 777188946, 1015915930, 298034488, 733839072, -380686400, 896305306, 805568376, 2026670232, -1037598004, 415002381, 2063457142, -599409224, 2073539682, -131669222, 2126108171, -136955022, -380557044, -1593383654, -1076537705, 351022049, 1411419954, -1209271434, 2110641203, -1486071681, 1658420312, -7130275, 1886625274, 176064858, 1276684016, -613911568, 1723461687, 1468128981, 1839698908, 1554180146, -1091984437, 1097998045, 2084764539, -1184721426, 983292879, -1923834780, 1540630390, -47230820, -2123523378, -893579386, 438149131, -961102348, 462751042, -821711669, 1286505542, 1151641803, -960935871, 1682169527, 1525294303, -1980834944, 481569887, -79976845, -1854874963, -873966799, 1550370508, -1823721560, -39597532, -1700689084, -2027100507, 385497859, -382158633, 1880509962, 998991206, -1878240827, 1382944805, 179200267, -634215411, 1521708044, 123667913, 2038210012, -975307841, 1075829532, -1936418530, -695494269, -1134383573, …][[Prototype]]: Object
chunk-vendors.5aa273bf.js:15393 r.init {words: Array(48), sigBytes: 191}sigBytes: 191words: (48) [1439780619, -2109730811, -252759436, 215603573, 733731158, 109463778, 564872063, 335684392, 1033173213, -753995018, -120053873, -1713797430, -71589127, -1583223821, -1764516788, -1264111171, -833282088, 291338367, 513239001, -983343852, -1180273092, -399222514, 1513663609, 175932466, 1489250393, 697368418, 1186876023, -929713991, 350694386, 2015035863, -627228165, -145224842, 637151427, -1180328371, -1069049547, -1180738986, 1236581957, -1922084383, 1101771108, 312501327, -1153428597, -1697834378, 1663648246, 1878007078, 185051676, -167454032, 1065597009, 2070576897][[Prototype]]: Object
chunk-vendors.5aa273bf.js:15393 r.init {words: Array(4), sigBytes: 13}sigBytes: 13words: (4) [-1420408114, 801975121, -1305303035, 197379][[Prototype]]: Object
chunk-vendors.5aa273bf.js:15393 

Note :- so logging direct crypto classes | funcitons are not efficient 
NOte2:- one more thing mentions is that analysis the scope variables is also 
	inefficient

Better Solution : 
	before : analyzing static crypto classes  and its importan to note 
		that we kept break points at local ovverides the main drawback
		are unreadable data , we not getting the actual backtrace of 
		network request . 
			we are unable to find the acutal strings 
			{
    "code": 202,
    "data": "lifOEdfQUWcDztBeHJGraTJWeJpilArgTOfLPiIB5/cDfivvXmTNS90/vRtHNksskxlFyXRDsRNlmPfLuf0n53iGmNJD4sjUSZPPZ9kbcjEKv6QJfirgVll6DqqfDkxHwcftZvDjnwTl44T97nZfXbgKNfJQYbNhPM13flOubNGFYFwyBfxhjTrvNMKwIzW0j8Nz4IFbpC/XGkIyn0aBk18Er4ZsMBBYOU/27nRJLk1hw+cPq9U8O7bfXdEmg404IkmX9Ia+9S9OXF71A99qjBgGsts4XKmIPvxSTUpkzL0Ox2VyCeRRxd2mfb+bOHKPin7oLHdtRtpmbRnl8wXvw2L/DMM3wsO0BnlqMrQhqxHcRXOWHI85dOMyKZ+8y7GsJe975BF8SsL9M11EqA0AKHYGYOW/DVbqBCo9qERKm1A="
}

	we kept backtract the crypto classes and focused on crypto outputs 
	and ignored the network request

	AFter: we back the network request 
	for example lets take new url request and response as follows 
	
	
	fetch("https://hbapi.kakobuy.com/api/user/info", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "lang": "en",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "_ga=GA1.1.301576879.1756756682; lang=en; GET_AREA_LIST=true; uuidv1=595b4a40-876f-11f0-b93a-f968e8b925b2; PHPSESSID=04a0037568de7f81f1ea5f4c9317072a; _gcl_au=1.1.432581121.1756756682.1525846810.1756836045.1756836044; token=b0a9a00e67a7685a2d512ae7eec91017; crisp-client%2Fsession%2Fe7abe8bf-2b51-4810-838a-d9bdeb20edb1=session_7662a61d-f6d1-4cbb-b2a4-62489cde22b0; _rdt_uuid=1756756681820.0c4b9178-98d4-4072-8ab0-cfc6082dcd8f; _ga_N33P988ESZ=GS2.1.s1756836001$o4$g1$t1756836838$j59$l0$h0",
    "Referer": "https://kakobuy.com/"
  },
  "body": "{\"data\":\"Gro6Y9prsBOdJ8ZJGbXSZfifq+Tq9fdg4L/stAYEhv8Mqg9IkifGZ2JWctV0umfycrVvTmcYOJjS0LNw/wV4qRxxb/99xsz/SkMGTViES2PwzGcoIm7Rpxa8jLjdgvapWFsUtpCClVfVB0Cz/ZfB9xZWhV4cVgxShzb3ut9uwnuLx1P8a0JHbaHo1Cems0Y+/6VCmVVG9Q0SvYzNygdb9w==\",\"req_code\":4,\"key\":\"F5YSwoZijjWL4g+5LKg7nYutqynzJpv6tmoyq/nd/Dr/B4oyejr2oYsNnvZVkBxLLHHCG1LPI0LMzH3VDT6IQFbK1E+j74ejQHdbxmEb2tA7gBgsJkl+uRP+Tc3NLqdZVmg9Rvk7/QKF6i/iR2zbPznXZHhTELp0KxDJCE2tb2o=\",\"iv\":\"CuyuMvH4H80kLXmBY/wEl/MpLQnkH352tiBXURquodFI0J8KtOTvpYheSoTLXZIEez1aGO8wmBHy4lb5U5QfeLsdmNorF5s46A8e+N0fMtNs47grmcCfVHpvWeoHNRtDy57EVqMCUc2JOJ0lhZU50G/M0d9KW5Hb8b2HUdqXHxQ=\"}",
  "method": "POST"
});
	lets focus on initiator:
		why ? we get the back of the actual data 
		for eg:
		
		
				XMLHttpRequest.send	@	content_script.js:265
(anonymous)	@	chunk-vendors.5aa273bf.js:57463
xhr	@	chunk-vendors.5aa273bf.js:57382
Fe	@	chunk-vendors.5aa273bf.js:57754
Promise.then		
_request	@	chunk-vendors.5aa273bf.js:57887
request	@	chunk-vendors.5aa273bf.js:57825
(anonymous)	@	chunk-vendors.5aa273bf.js:4671
(anonymous)	@	app.a2a74907.js:1
x	@	app.a2a74907.js:1
s	@	app.a2a74907.js:1
(anonymous)	@	app.a2a74907.js:1
getInfo	@	app.a2a74907.js:1
(anonymous)	@	chunk-vendors.5aa273bf.js:14039
y.dispatch	@	chunk-vendors.5aa273bf.js:14151
dispatch	@	chunk-vendors.5aa273bf.js:13862
getInfo	@	app.a2a74907.js:1
initData	@	app.a2a74907.js:1
mounted	@	app.a2a74907.js:1
Rn	@	chunk-vendors.5aa273bf.js:10256
Rr	@	chunk-vendors.5aa273bf.js:10828
insert	@	chunk-vendors.5aa273bf.js:11043
D	@	chunk-vendors.5aa273bf.js:12222
(anonymous)	@	chunk-vendors.5aa273bf.js:12314
Pr.e._update	@	chunk-vendors.5aa273bf.js:10701
r	@	chunk-vendors.5aa273bf.js:10740
e.get	@	chunk-vendors.5aa273bf.js:10502
e	@	chunk-vendors.5aa273bf.js:10495
Ar	@	chunk-vendors.5aa273bf.js:10748
ia.$mount	@	chunk-vendors.5aa273bf.js:13248
56d7	@	app.a2a74907.js:1
s	@	app.a2a74907.js:1
0	@	app.a2a74907.js:1
s	@	app.a2a74907.js:1
a	@	app.a2a74907.js:1
(anonymous)	@	app.a2a74907.js:1
(anonymous)	@	app.a2a74907.js:1

	Before going to undestand the initiator or stack tract there also a fuctionality like breakpoint of source . to the urls . its usuall y called XHR|fetch Breakpoints 
	IMportant observations: 
		1. XMLHttpRequest.send	send the payload and it send the data mainly 
		
		
		const send = XMLHttpRequest.prototype.send;
XMLHttpRequest.prototype.send = function(postData) {// post data is argument to be sended 
    this.addEventListener('load', async function() {
        if (this._method === "GET") {
            let body = void 0;
            switch (this.responseType) {
                case "":
                case "text":
                    body = this.responseText ?? this.response;
                    break;
                case "json":
                    // TODO: untested
                    body = JSON.stringify(this.response);
                    break;
                case "arraybuffer":
                    // TODO: untested
                    if (this.response.byteLength) {
                        const response = new Uint8Array(this.response);
                        body = uint8ArrayToString(new Uint8Array([...response.slice(0, 2000), ...response.slice(-2000)]));
                    }
                    break;
                case "document":
                    // todo
                    break;
                case "blob":
                    body = await this.response.text();
                    break;
            }
            if (body) {
                const manifest_type = Evaluator.getManifestType(body);
                if (manifest_type) {
                    emitAndWaitForResponse("MANIFEST", JSON.stringify({
                        "url": this.responseURL,
                        "type": manifest_type,
                    }));
                }
            }
        }
    });
    return send.apply(this, arguments);
};

Now refresh the set and let the breakpoint stop at XHR/class 
	so keep the XHR break Point for a specific url your wish 
	
	now the ouput is :
		when you log the fuction argument you get what is going to be send to server
			for eg; 
				temp1
'{"data":"4jKgd86eYfmnhG8Vl44COjuhx8OW9GluYkfn2NMhgp+KlLg1VXt5PsOD0xFuM7moJC1tNsMUXVY5Q2j/eeygMuwTlVMTPotsP+lbSX+rG4OT2bC99SP2ncHDtObAniGtth0DHpoEm0uvjnDY0RC97A1rfxIPX1LKCcrGEynv+hA/dsfmRq9PNalwDDv8vPc3","req_code":4,"key":"EZQE4XEsi1Ofcbnjl8KpMchxK6inmuutYTttvlg7B/MxYE3kOChT95giYc84g7DS0z/sR2aZwzJjD6oWKv29Fagrw3us9c28UqKge/FTP+ORCtfisEgwheM/npZwjOK4QSWAlpHg8e55n69AjdykN1Onh7SHA8lEVuCNNuD82Mo=","iv":"n6Y/h3V7T3zokDrBnBwOkdr1Jx1WophPWvBGi7AX0QAlmPDM2t1Xsu0CTy0R95uQZ8/9nEX9p9nvE5+nAwOA71J5tWIgZwzt7b959Nu7O5ACyFZaUiDhW6FlvEsRP4+AhmDtktzflbOBogmBWW/ekCk0uvBmbddMti/b2p26zps="}'

	Now our goal to find where this is actually comming from 
	so again look it the stack 
	2.The data is pobably comming from _request
		 _request(e, t) {
                "string" === typeof e ? (t = t || {},
                t.url = e) : t = e || {},
                t = fe(this.defaults, t);
                const {transitional: n, paramsSerializer: r, headers: a} = t;
                void 0 !== n && Be.assertOptions(n, {
                    silentJSONParsing: We.transitional(We.boolean),
                    forcedJSONParsing: We.transitional(We.boolean),
                    clarifyTimeoutError: We.transitional(We.boolean)
                }, !1),
                null != r && (i["a"].isFunction(r) ? t.paramsSerializer = {
                    serialize: r
                } : Be.assertOptions(r, {
                    encode: We.function,
                    serialize: We.function
                }, !0)),
                void 0 !== t.allowAbsoluteUrls || (void 0 !== this.defaults.allowAbsoluteUrls ? t.allowAbsoluteUrls = this.defaults.allowAbsoluteUrls : t.allowAbsoluteUrls = !0),
                Be.assertOptions(t, {
                    baseUrl: We.spelling("baseURL"),
                    withXsrfToken: We.spelling("withXSRFToken")
                }, !0),
                t.method = (t.method || this.defaults.method || "get").toLowerCase();
                let o = a && i["a"].merge(a.common, a[t.method]);
                a && i["a"].forEach(["delete", "get", "head", "post", "put", "patch", "common"], e => {
                    delete a[e]
                }
                ),
                t.headers = K.concat(o, a);
                const s = [];
                let c = !0;
                this.interceptors.request.forEach((function(e) {
                    "function" === typeof e.runWhen && !1 === e.runWhen(t) || (c = c && e.synchronous,
                    s.unshift(e.fulfilled, e.rejected))
                }
                ));
                const l = [];
                let u;
                this.interceptors.response.forEach((function(e) {
                    l.push(e.fulfilled, e.rejected)
                }
                ));
                let d, h = 0;
                if (!c) {
                    const e = [Fe.bind(this), void 0];
                    e.unshift.apply(e, s),
                    e.push.apply(e, l),
                    d = e.length,
                    u = Promise.resolve(t);
                    while (h < d)
                        u = u.then(e[h++], e[h++]);
                    return u
                }
                 
                 
                 now keep breakpoint at return 
                 and see the local scopes
                 
e
: 
data
: 
data
: 
"yjTTY3vAxPtPhTirLOc/N2OWADCEjAop++XBlllHnsWvDGyKQAih3E8BnLC/6KaML3NnMuybaU2Biwlhykpwxeka6LhyNA0wiR0157zbub0YHjDrz8EIOWqhdHSSt0VtzFczHDCPtkhdh9wLvMcOFkCyYmQIhwiGv4h99MQ6vndNjQg14JFCaOoiLUwY3gYy"
iv
: 
"JRzdbT35+wUkbq/GM6FM7UTbvXfpGqCQiPpc7/lnvphxU7YlHuVDJU5gIYXJ0Cr4tuSEI7eV970CFy8TSYT/hdH2q8kaaHC9jX3EYiu1lyGPL8c9ctjCSzbHxFKgIwz74DNCWlGh5DFZi5a3TGPPo/uMm8ftFRU1yW0HsLPHApQ="
key
: 
"LnmOY7vB3e/yPxyqDviSXPuTiUz55cdwOmBkqc5dx26ViiMTDHaUnV7oh8YXvSQlpGolBf/zjNRVso56OnzLb86FUSMdPfEtXUq1/vPprYmT7hseHiGCxFcmQlGcDYoXBEr9fuYdca3f/sy6w9OrtBQIr5rwWRob5YV7zcFia2s="
req_code
: 
4

Sorry: the data iam seeing is variable to time to time so it may not same and dont confuse understand the concept
	
	Now we can clearly see that encrypted payload is there in e data 

	3. we need to back the object or variable 3 from wher the data is getting 
		now again look it the stack 
		
		function x(e="", t={}, a=!0, r=!1) {
            z.fp = Object(_["c"])(_["a"].HB_fp),
            z.referer = document.referrer || "",
            z.uuid = Object(_["c"])(_["a"].uuid),
            z.cur = Object(_["c"])(_["a"].cur) || "USD",
            z.token = Object(_["b"])();
            let i = {
                ...z,
                ...t
            }
              , n = {
                data: "",
                req_code: 4
            };
            const {image: c} = t;
            c && (n.image = c,
            delete i.image);
            let m = b();
            const {key: p, iv: g} = m;
            if (4 === n.req_code) {
                const e = v(i, p, g);
                Object.assign(n, e)
            } else
                i = JSON.stringify(i),
                n.data = i;
            let f = {
                method: "post",
                url: e,
                data: n,
                isFile: !!c,
                isInterfaceBgOperation: r
            };
            
            now log the Scopt 
            k
c
: 
undefined
f
: 
{method: 'post', url: '/api/index/config', data: {…}, isFile: false, isInterfaceBgOperation: false}
g
: 
"a079352c98684132"
i
: 
{versionCode: '211', from: '1201', fp: 'f271d21900168bbf9125654e33b3b6db', referer: '', uuid: 'f6d98180-876d-11f0-bd09-fdf3fcb93db6', …}
m
: 
iv
: 
"a079352c98684132"
key
: 
"f148f35715ef6341bbf0382b06a19d5a"
[[Prototype]]
: 
Object
n
: 
data
: 
"yjTTY3vAxPtPhTirLOc/N2OWADCEjAop++XBlllHnsWvDGyKQAih3E8BnLC/6KaML3NnMuybaU2Biwlhykpwxeka6LhyNA0wiR0157zbub0YHjDrz8EIOWqhdHSSt0VtzFczHDCPtkhdh9wLvMcOFkCyYmQIhwiGv4h99MQ6vndNjQg14JFCaOoiLUwY3gYy"
iv
: 
"JRzdbT35+wUkbq/GM6FM7UTbvXfpGqCQiPpc7/lnvphxU7YlHuVDJU5gIYXJ0Cr4tuSEI7eV970CFy8TSYT/hdH2q8kaaHC9jX3EYiu1lyGPL8c9ctjCSzbHxFKgIwz74DNCWlGh5DFZi5a3TGPPo/uMm8ftFRU1yW0HsLPHApQ="
key
: 
"LnmOY7vB3e/yPxyqDviSXPuTiUz55cdwOmBkqc5dx26ViiMTDHaUnV7oh8YXvSQlpGolBf/zjNRVso56OnzLb86FUSMdPfEtXUq1/vPprYmT7hseHiGCxFcmQlGcDYoXBEr9fuYdca3f/sy6w9OrtBQIr5rwWRob5YV7zcFia2s="
req_code
: 
4
[[Prototype]]
: 
Object
p
: 
"f148f35715ef6341bbf0382b06a19d5a"

this is what is get 
	i am back the function
	
	4.impoortant observation 
		m has aes key parameters 
		n has encrypted data
		i is probably the data before encrypted 
		so here look at function v(i,p,g)
			its send the nn encrypted data , aes key , iv
			
	5.now back Tracking the v function 
	function v(e, t, a) {
            const r = JSON.stringify(e)
              , i = f["a"].deflateRaw(r, {
                level: 1
            })
              , o = p.a.lib.WordArray.create(i)
              , _ = p.a.AES.encrypt(o, p.a.enc.Utf8.parse(t), {
                iv: p.a.enc.Utf8.parse(a),
                mode: p.a.mode.CBC,
                padding: p.a.pad.Pkcs7
            })
              , n = _.toString()
              , s = k(t)
              , c = k(a);
            return {
                data: n,
                key: s,
                iv: c
            }
        }
        now its clear observable , e in not encrypted data , t is key , a is iv
        now log the funtion as you wish , using break piont or watch scope or using console.log()
        observer the function carefully its returning the encrypted data 
        so log e to see the data before encrypring
        
        no REeal Observations 
        no i logged into some account 
        so now my payload is 
        {"data":"skTordBLGSNpmK0KXe30DDIlF342lWbf89GgA7YjY3S4Qejsch5Tipxj7MVfKGJBVN34bRs4uIkqa6gPS+8QeHPfpY7K9GIEqgroMTYFkqJMR8kKq1jlgfi/552LqLNBnueFIIws7BAM3g/NCsGOkL3dGNklKY3EAGg1vhUeBNiQ03Vy4BLtjgpl/TAg6fMZu6OySKSuQUFOl1oNe4knAanAARY26qFEwLMupOqEHK0=","req_code":4,"key":"S0cjrn3f3rMmxf/ikTQtpvN1kRNoLmPVnHiDaDqM/xBT7CpzV57Oe8zxsxoC6njKh4lU5v4kxwgjAzb3DpkbLnw52rrra2awsFq/1yqNj0Cs7Dtd70D/jteoDvbYm04URI0nlgLqfk1MOUzTFkZw1m4PGy6ItMyNR0pP9t8+YS0=","iv":"BCAuTuZN7LnHtnS5M7yIE/AxUHyMh9wlyMOD8Gx9akE3i8Zed5m9pLkTM4l3EdNRVHqMyepk6XPD37QDv4TfCWdHRMmh/JrbLJxZW6ZvGcjRfaB+ResxXn5QD8sR/8s1/EYbhT2amHZNyk/eE6Y9q3Hgl9Guk8hLSj/s6DX+RZg="}
        so what is the actuall data here 
        
        data before decrypted
app.a2a74907.js:19619 {versionCode: '211', from: '1201', fp: 'f271d21900168bbf9125654e33b3b6db', referer: '', uuid: 'f6d98180-876d-11f0-bd09-fdf3fcb93db6', …}captcha: ""cur: "USD"fp: "f271d21900168bbf9125654e33b3b6db"from: "1201"password: "1998gato"referer: ""token: undefinedusername: "fernandord7@hotmail.com"uuid: "f6d98180-876d-11f0-bd09-fdf3fcb93db6"versionCode: "211"[[Prototype]]: Object
app.a2a74907.js:19633 data after encrypted
app.a2a74907.js:19634 skTordBLGSNpmK0KXe30DDIlF342lWbf89GgA7YjY3S4Qejsch5Tipxj7MVfKGJBVN34bRs4uIkqa6gPS+8QeHPfpY7K9GIEqgroMTYFkqJMR8kKq1jlgfi/552LqLNBnueFIIws7BAM3g/NCsGOkL3dGNklKY3EAGg1vhUeBNiQ03Vy4BLtjgpl/TAg6fMZu6OySKSuQUFOl1oNe4knAanAARY26qFEwLMupOqEHK0=
chunk-vendors.5aa273bf.js:15393 

	encrypted data coming from server
	for example
		gBnehu63f0icOUMhMJKiS4diWMc6uQuGF5R3HMN6wVKxBDd2zlQeMlnZ8AZ5JXsLqOfCpk05z0qyE7u3v4FdPyyhFVqsM4VsrWjcCpbqZY5DFxZFC2FrGNBTqxS/VUFh9zZm5SDrysoUm3QUs51o0dBh3PWeg11SIzRq7g0LlGoTFvqh3DTU6h1JFS+doFS5wqd2RKxiVyxscE6rV7HOF5sr4x6eOIMpgPDxEUjON3E=
	{"list":[{"id":30,"createtime":1744889816,"title":"Kakobuy provides tax-free routes for American users announcement","description":"Kakobuy provides tax-free routes for American users announcement"},{"id":1,"createtime":1726988332,"title":"New users sign up and get $410 coupons!","description":"New users sign up and get $410 coupons!"}]}
	
	so i hope its helpful :)
	so finalyy iam able to the data before encrypting 
			
