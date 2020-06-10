# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json, time


def createStreams(access_key, secret_key, hub, streamTitle):
    """
    创建流
    https://developer.qiniu.com/pili/api/2515/create-a-flow
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名

    :return:
            200 {}
            614 {
                "error": "stream already exists"
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 请求体
    body = {
        "key": streamTitle
    }

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams'

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

headers, result = createStreams(access_key, secret_key, hub, streamTitle)
print(f'{headers}\n{result}')
