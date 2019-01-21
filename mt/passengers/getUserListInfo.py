import requests
import time

# 改责记录查询接口

ip = "http://manager.qcs.test.sankuai.com/"
headers = {"Content-Type": "application/json", "Cookie": "_lxsdk_cuid=16420072be6c8-0c78177bb7213b-17376952-13c680-16420072be6c8; _lxsdk=16420072be6c8-0c78177bb7213b-17376952-13c680-16420072be6c8; _ga=GA1.2.1010336327.1529571237; uu=df32a820-79e9-11e8-9739-2b58b2c51edf; cid=1; ai=1; skmtutc=N38kup8dnpwUzR5Wt7M43J4HwfgvscQBSFGR2j+Sj+UF4596+uPY2ztaLLOupYOX-BKGUDyzaeGpHrH6GWUfOSRF8Leg=; koa:sess=eyJzaWQiOiJiOTc5NWVmZjQyKjE0OWMzYWQ0OTcxZWZhMTM1ODkyMyIsIl9leHBpcmUiOjE1Mzc5MzA2NDUxNTAsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==; koa:sess.sig=VeLdhyAoeSLrbUAc0Ahy-_SDSoL2spP84h8s-GbF1CQ; ssoid=b9795eff42*149c3ad4971efa1358923"}
url = ip + "api/uc/user/list/getUserListInfo"


def getUserListInfo(phone):
    param = {"phone": phone}
    r = requests.post(url, param, headers=headers)
    return r

# 获取用户列表
r = getUserListInfo("18610669397")
print(r.json())