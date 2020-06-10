# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json, time


def historyactivity(access_key, secret_key, hub, streamTitle, startTime, endTime):
    """
    直播历史查询
    https://developer.qiniu.com/pili/api/2778/live-history
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名
    :param startTime: 整数，Unix 时间戳，起始时间，不指定或 0 值表示不限制起始时间。
    :param endTime: 整数，Unix 时间戳，结束时间，不指定或 0 值表示当前时间。

    :return:
            200
            {
                "items": [
                    {
                        "start": <Start>,
                        "end": <End>
                    },
                    ...
                ]
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)
    l = []

    # 日期转时间戳
    def time2timestamp(datetime):
        # 日期格式
        # datetime = '2020-06-08 00:00:00'
        # 转为时间数组
        timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    start = time2timestamp(startTime)

    end = time2timestamp(endTime)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/historyactivity?start={start}&end={end}'

    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

    # 格式化响应体
    result = ret["items"]
    for i in result:
        t = i["end"] - i["start"]
        l.append(t)

    return sum(l) / 60


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

# 直播空间名
hub = ""

# 流名
streamTitle = ""

# 查询时间
startTime = "2020-06-01 00:00:00"
endTime = "2020-06-09 00:00:00"

result = historyactivity(access_key, secret_key, hub, streamTitle, startTime, endTime)
print(f'2020-06-01 至 06-08 直播总时长 {result} min')
print(f'2020-06-01 至 06-08 直播平均值 {result / 8} min/天')
