# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


def saveasStreams(access_key, secret_key, hub, streamTitle, body):
    """
    修改流转码配置
    https://developer.qiniu.com/pili/api/2521/modify-the-flow-configuration
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名
    :param body: 请求体

    :return:
        200 {}
        400 {
            "error": "invalid stream key" // 只能修改原始流，包含@的流不允许
        }
        400 {
            "error": "invalid args" // 转码配置不存在
        }
        612 {
            "error": "stream not found"
        }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求地址
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/converts'

    # 发起post请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体内容
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
    "converts": ["720p", "480p"]  # 数组，转码配置，如果提交的 ProfileName 为空数组，那么之前的转码配置将被取消
}

headers, result = saveasStreams(access_key, secret_key, hub, streamTitle, body)
print(f'{headers}\n{result}')
