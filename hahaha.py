import requests as r

data = {
    "stock":"AAA",
    "__RequestVerificationToken":"_t0lEz5TMBzRbgutYVhC6Aql888xePFILbcF8rdAM_qpxUT47yrc4i9_j_1n3G5ePe7JVsng5vSYhYlb_l4LvjPIblxFWkmVCFOWEaJGaebgcN6nyuOGKrLf4u44oLdj0"
}
cookie = {}
header = {'Accept': '/', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}
rs = r.post("https://finance.vietstock.vn/data/GetListReportNormByStockCode",data=data,headers=header)
print(rs.content)
