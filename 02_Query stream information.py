# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json


def streamsInfo(access_key, secret_key, hub, streamTitle):
    """
    查询流信息
    https://developer.qiniu.com/pili/api/2773/query-stream
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名

    :return:
        200 {
            "createdAt": <CreatedAt>, // Unix Time
            "updatedAt": <UpdatedAt>, // Unix Time，更新流配置时会自动更新这个时间
            "expireAt": <ExpireAt>, // Unix Time，过期时间
            "converts": ["<Profile1>", "<Profile2>"], // 流的转码规格
            "disabledTill": <DisabledTill> // 禁用的结束时间，-1 表示永久禁用
        }
    """
    auth = QiniuMacAuth(access_key, secret_key)

    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}'

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

headers, result = streamsInfo(access_key, secret_key, hub, streamTitle)
print(f'{headers}\n{result}')
