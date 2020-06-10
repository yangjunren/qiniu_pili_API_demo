# -*- coding: utf-8 -*-

def playUrl(domain, hub, stream_title):
    """
    播放地址
    https://developer.qiniu.com/pili/api/2768/rtmp-broadcast-address
    https://developer.qiniu.com/pili/api/2769/hls-broadcast-address
    https://developer.qiniu.com/pili/api/2770/hdl-http-flv-broadcast-address
    :param domain: 直播域名
    :param hub: 直播空间
    :param stream_title: 流名

    :return:
        播放地址
    """
    rtmpPlayUrl = f"rtmp://{domain}/{hub}/{stream_title}"

    hlsPlayUrl = f"http://{domain}/{hub}/{stream_title}.m3u8"

    hdlPlayUrl = f"http://{domain}/{hub}/{stream_title}.flv"

    return rtmpPlayUrl, hlsPlayUrl, hdlPlayUrl
