HEADER = {
    'Host': '192.1.34.31:8080',
    'Connection': 'keep-alive',
    #'Content-Length': '864',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'http://192.1.34.31:8080',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'Referer': 'http://192.1.34.31:8080/mall/admin.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

METHOD = {
    'Update': {'URL': 'http://192.1.34.31:8080/mall/admin/product/update'},
    'Add': {'URL': 'http://192.1.34.31:8080/mall/admin/product/add'},
    'PicUpload': {'URL': 'http://192.1.34.31:8080/mall/admin/product/batch/image'},
    'PicUploadExamine': {'URL': 'http://192.1.34.31:8080/mall/admin/product/keep/submit?0=%7B%22audit'},
}

LOGIN_URL = 'http://192.1.34.31:8080/mall/admin/login?'

TempXLSXMD5 = "385af58f01fa876fc285b3c1dff1b6f8"