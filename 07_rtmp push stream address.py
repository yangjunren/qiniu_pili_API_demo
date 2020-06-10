# -*- coding: utf-8 -*-

import pili, base64, hmac, hashlib, time


def noneRtmpUrl(domain, hub, stream_title):
    """
    无校验鉴权 推流地址
    https://developer.qiniu.com/pili/api/6678/push-the-current-authentication#1
    :param domain: 推流域名
    :param hub: 直播空间
    :param stream_title: 流名

    :return:
        推流地址
    """
    noneRtmpUrl = f"rtmp://{domain}/{hub}/{stream_title}"
    return noneRtmpUrl


def staticRtmpUrl(domain, hub, stream_title, publishKey):
    """
    静态鉴权 推流地址
    https://developer.qiniu.com/pili/api/6678/push-the-current-authentication#2
    :param domain: 推流域名
    :param hub: 直播空间
    :param stream_title: 流名
    :param publishKey: 推流秘钥

    :return:
        推流地址
    """
    staticRtmpUrl = f"rtmp://{domain}/{hub}/{stream_title}?key={publishKey}"
    return staticRtmpUrl


def expiryRtmpUrl(access_key, secret_key, domain, hub, stream_title, publishKey, expiry):
    """
    限时鉴权（expiry） 推流地址
    https://developer.qiniu.com/pili/api/6678/push-the-current-authentication#3
    :param domain: 推流域名
    :param hub: 直播空间
    :param stream_title: 流名
    :param publishKey: 推流秘钥
    :param expireAt: 过期时间

    :return:
        推流地址
    """
    mac = pili.Mac(access_key, secret_key)
    expireAt = int(time.time()) + expiry
    path = f"{hub}/{stream_title}?expire={expireAt}"
    data = base64.urlsafe_b64decode(hmac.new(path, publishKey, hashlib.sha1).digest())
    token = f"{mac.__auth__.access_key}:{data}"
    expiryRtmpUrl = f"rtmp://{domain}/{path}&token={token}"

    return expiryRtmpUrl


def expirySkRtmpUrl(access_key, secret_key, domain, hub, stream_title, expiry):
    """
    限时鉴权sk（expiry_sk） 推流地址
    https://developer.qiniu.com/pili/api/6678/push-the-current-authentication#4
    :param domain: 推流域名
    :param hub: 直播空间
    :param stream_title: 流名
    :param expiry: 过期时间

    :return:
        推流地址
    """
    mac = pili.Mac(access_key, secret_key)
    expireAt = int(time.time()) + expiry
    path = f"{hub}/{stream_title}?e={expireAt}"
    data = base64.urlsafe_b64decode(hmac.new(path, mac.__auth__.secret_key, hashlib.sha1).digest())
    token = f"{mac.__auth__.access_key}:{data}"
    expirySkRtmpUrl = f"rtmp://{domain}/{path}&token={token}"

    return expirySkRtmpUrl
