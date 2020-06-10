# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json, time


def disableStreams(access_key, secret_key, hub, streamTitle, disabledTill):
    """
    禁播流
    https://developer.qiniu.com/pili/api/2775/off-the-air-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名
    :param disabledTill: 整数，Unix 时间戳，表示流禁播的结束时间，单位 s(秒)，-1 表示永久禁播。0 表示解除禁播。

    :return:
            200 {}
            612 {
                "error": "stream not found"
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/disabled'

    # 请求体
    body = {
        "disabledTill": disabledTill
    }

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

# 整数，Unix 时间戳，表示流禁播的结束时间，单位 s(秒)，-1 表示永久禁播。0 表示解除禁播。
disabledTill = -1

headers, result = disableStreams(access_key, secret_key, hub, streamTitle, disabledTill)
print(f'{headers}\n{result}')
