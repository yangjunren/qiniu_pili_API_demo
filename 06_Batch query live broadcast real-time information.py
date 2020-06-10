# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json, time


def batchListOnlineStreamsInfo(access_key, secret_key, hub, body):
    """
    批量查询直播实时信息
    https://developer.qiniu.com/pili/api/3764/batch-query-broadcast-real-time-information
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param body: 请求体

    :return:
        200 {
                "items": [
                    {
                        "key": "<StreamTitle>",
                        "startAt": <StartAt>,
                        "clientIP": "<ClientIP>",
                        "bps": <Bps>, // 当前码率
                        "fps": {
                            "audio": <Audio>,
                            "video": <Video>,
                            "data": <Data>
                    },
                    ...
                ]
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/livestreams'

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

# 直播空间名
hub = ""

# 要查询的流名字符串数组，最大长度为100
body = {
    "items": [
        "test001",
        "test02",
        "0320test"
    ]
}

headers, result = batchListOnlineStreamsInfo(access_key, secret_key, hub, body)
print(f'{headers}\n{result}')
