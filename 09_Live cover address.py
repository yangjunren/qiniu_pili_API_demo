# -*- coding: utf-8 -*-

def broadcastUrl(domain, hub, stream_title):
    """
    直播封面地址
    https://developer.qiniu.com/pili/api/2771/broadcast-address-the-cover
    :param domain: 直播域名
    :param hub: 直播空间
    :param stream_title: 流名

    :return:
        直播封面地址
    """
    imagePlayUrl = f"http://{domain}/{hub}/{stream_title}.jpg"

    return imagePlayUrl
