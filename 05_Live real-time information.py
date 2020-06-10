# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json, time


def listOnlineStreamsInfo(access_key, secret_key, hub, streamTitle):
    """
    查询实时信息
    https://developer.qiniu.com/pili/api/2776/live-broadcast-of-real-time-information
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名

    :return:
        200 {
                "startAt": <StartAt>,
                "clientIP": "<ClientIP>",
                "bps": <Bps>, // 当前码率
                "fps": {
                    "audio": <Audio>,
                    "video": <Video>,
                    "data": <Data>
                }
            }
        404 {
            "error": "stream not found"
            }
        619 {
            "error": "no live" // 流不在直播
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/live'

    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)
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

headers, result = listOnlineStreamsInfo(access_key, secret_key, hub, streamTitle)
print(f'{headers}\n{result}')
