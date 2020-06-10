# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http


def listStreams(access_key, secret_key, hub):
    """
    查询流列表
    https://developer.qiniu.com/pili/api/2774/current-list
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间

    :return:
            200 {
                # 数组，流列表，数组的元素是结构体，key 字段是流名。
                "items": [
                    {
                        "key": "<StreamKey>"
                    },
                    ...
                ],
                # 字符串，此次遍历到的标记，用于下次遍历提示起始位置，"" 表示已经查询完所有。
                "marker": "<Marker>"
            }
    """
    auth = QiniuMacAuth(access_key, secret_key)
    l = []

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams'
    # "?liveonly={liveonly}&prefix={prefix}&limit={limit}"

    # 发起GET请求
    ret, res = http._get_with_qiniu_mac(url=url, params=None, auth=auth)

    # 格式化响应体
    result = ret["items"]
    for i in result:
        t = i["key"]
        l.append(t)
    return hub, l


# 七牛账号 AK、SK
access_key = '<access_key>'
secret_key = '<secret_key>'

# 直播空间名
hub = ""

# # 布尔值，true 表示查询的是正在直播的流，不指定表示返回所有的流。
# liveonly = False
#
# # 字符串，限定只返回带以 prefix 为前缀的流名，不指定表示不限定前缀。
# prefix = None
#
# # 整数，限定返回的流个数，不指定表示遵从系统限定的最大个数。
# limit = 1000
# ", liveonly, prefix, limit"
hub, result = listStreams(access_key, secret_key, hub)
print(f'直播空间 {hub} 的流列表为\n {result}')
print(f'直播空间 {hub} 的流列表总数是 {len(result)}')
