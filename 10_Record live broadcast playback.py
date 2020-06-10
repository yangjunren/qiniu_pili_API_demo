# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


def saveasPlayBack(access_key, secret_key, hub, streamTitle, body):
    """
    录制直播回放
    https://developer.qiniu.com/pili/api/2777/save-the-live-playback
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名
    :param body: 请求体

    :return:
        200 {
            "fname": "<Fname>",
            "persistentID": "<PersistentID>"
        }
        612 {
            "error": "stream not found"
        }
        619 {
            "error": "no data" // 没有直播数据
        }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/saveas'

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

# 流名
streamTitle = ""

# 请求体
body = {
    "start": 0,
    "end": 0
}

headers, result = saveasPlayBack(access_key, secret_key, hub, streamTitle, body)
print(f'{headers}\n{result}')
