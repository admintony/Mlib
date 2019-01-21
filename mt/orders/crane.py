import requests
import time


# import pymysql "1910002111",

# 返回当前时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def ds_test():
    driver_ids = ["1910010357", "1900000266"]
    ip = "http://10.23.4.139:8413"

    with open('/Users/yangjiao/Desktop/dsmessage.txt', 'a+') as f:
        f.write(str(GetNowTime()) + " test执行结果：\n")
        print("test执行结果：")

        for driver_id in driver_ids:
            url = ip + "/driver/" + driver_id + "?biz_type=1"
            r = requests.get(url=url)
            workType = r.json()["workType"]
            utimestamp = time.localtime(r.json()["utime"]/1000)
            utime = time.strftime("%Y-%m-%d %H:%M:%S", utimestamp)

            print(driver_id, workType, utime)


            f.write(str(driver_id) + " " + str(workType) + " " + str(utime) + "\n")
        print("-------\n")
        f.write("\n")

# http://10.23.109.230:8413/driver/316789423?biz_type=1
def ds_stage():
    driver_ids = ["66422983", "1894477879"]
    ip = "http://10.23.109.230:8413"

    with open('/Users/yangjiao/Desktop/dsmessage.txt', 'a+') as f:
        f.write(str(GetNowTime()) + " stage执行结果：\n")
        print("stage执行结果：")

        for driver_id in driver_ids:
            url = ip + "/driver/" + driver_id + "?biz_type=1"
            r = requests.get(url=url)
            workType = r.json()["workType"]
            utimestamp = time.localtime(r.json()["utime"] / 1000)
            utime = time.strftime("%Y-%m-%d %H:%M:%S", utimestamp)

            print(driver_id, workType, utime)
            # print("-------")

            f.write(str(driver_id) + " " + str(workType) + " " + str(utime) + "\n")
        print("-------\n")
        f.write("\n")

# http://10.7.202.234:8413/driver/162507853?biz_type=1
def ds_prod():
    driver_ids = ["66422983", "1894477879"]
    ip = "http://10.7.202.234:8413"

    with open('/Users/yangjiao/Desktop/dsmessage.txt', 'a+') as f:
        f.write(str(GetNowTime()) + " stage执行结果：\n")
        print("prod执行结果：")

        for driver_id in driver_ids:
            url = ip + "/driver/" + driver_id + "?biz_type=1"
            r = requests.get(url=url)
            workType = r.json()["workType"]
            utimestamp = time.localtime(r.json()["utime"] / 1000)
            utime = time.strftime("%Y-%m-%d %H:%M:%S", utimestamp)
            print(driver_id, workType, utime)
            # print("-------")

            f.write(str(driver_id) + " " + str(workType) + " " + str(utime) + "\n")
        print("-------\n")
        f.write("\n")

# ds_test()
ds_stage()
ds_prod()

