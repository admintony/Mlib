import requests
import time

# 改责记录查询接口

ip = "http://manager.qcs.test.sankuai.com/"
headers = {"Content-Type": "application/json", "Cookie": "_lxsdk_cuid=16420072be6c8-0c78177bb7213b-17376952-13c680-16420072be6c8; _lxsdk=16420072be6c8-0c78177bb7213b-17376952-13c680-16420072be6c8; _ga=GA1.2.1010336327.1529571237; uu=df32a820-79e9-11e8-9739-2b58b2c51edf; cid=1; ai=1; skmtutc=I7CTou7XEukj2lRE77Qlga69sj0OjblFOnegjTvwcBFJez4/F4QUkxwHjeF5vUcD-6kQ0JMTRNLimd0CPFNBHL0OHs+M=; koa:sess=eyJzaWQiOiJhZDhjYzk4YTY3KjM0MjJjOTA3MWVmYjMxYzFkYTJkYSIsIl9leHBpcmUiOjE1MzM3ODE3MDA1NDUsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==; koa:sess.sig=_QtxPlDW3SsPkKdReFJCck1JSiFaVhCD1e_FLZ_K_o0; ssoid=ad8cc98a67*3422c9071efb31c1da2da; _lxsdk_s=165175eb3d1-4e8-575-d97%7C%7C7"}
url = ip + "api/uc/order/disclaim/his.ajax"


def getOrderDisclaimer(orderId):
    param = {"orderId": orderId}
    r = requests.get(url, param, headers=headers)
    return r

# 无改责记录 102526125604872197402669100000
r = getOrderDisclaimer("102526125604872197402669100000")
print(r.json())

# 有改责记录
