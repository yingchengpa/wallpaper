# -*- coding: utf-8 -*-

"""bing 壁纸"""

import requests
import utils.log as log
import json
import utils.bingdb as bingdb
import initres


def _getyesterdaywall() -> dict:
    """
    获取昨日图片
    :return:
    1天的json内容
{
    "startdate": "20210415",
    "fullstartdate": "202104151600",
    "enddate": "20210416",
    "url": "/th?id=OHR.FlowerTown_ZH-CN6364330124_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
    "urlbase": "/th?id=OHR.FlowerTown_ZH-CN6364330124",
    "copyright": "Dinan镇的鹅卵石铺成的街道，法国布列塔尼 (© Scott Wilson/Alamy)",
    "copyrightlink": "https://www.bing.com/search?q=Dinan%E9%95%87&form=hpcapt&mkt=zh-cn",
    "title": "",
    "quiz": "/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20210415_FlowerTown%22&FORM=HPQUIZ",
    "wp": true,
    "hsh": "428bfc89d6a4390c8856e2885a6f4e1a",
    "drk": 1,
    "top": 1,
    "bot": 1,
    "hs": []
}
    """

    '''  
    n

    必填，表示返回照片数量。
    
    idx
    
    非必填，用于指定获取哪天的壁纸，0：表示当天，1：表示昨天，2：表示前天，这样依此类推。
    
    format
    
    非必填，用于指定输出格式，默认是 XML 的，传入 js 表示返回 JSON 格式。
    
    mkt
    
    非必填，用于指定推送地区，如：en-US，zh-CN，ja-JP，en-AU，en-UK，de-DE，en-NZ，en-CA

    最迟只能获取昨天数据，最多只能获取8天数据 '''
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn"
    r = []
    try:
        r = requests.get(url, timeout=5)
    except Exception as e:
        log.logger.warning('error: {}'.format(e))
    else:
        if r.status_code == 200:
            r = json.loads(r.text)['images'][0]

    return r


def _downhdimg(baseurl, filepath):
    """
    下载高清图片 1080p
    :return:

    url = https://cn.bing.com/ + urlbase + _1920x1080.jpg
    """

    url = """https://cn.bing.com/{}_1920x1080.jpg""".format(baseurl)
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)


def _downuhdimg(baseurl, filepath):
    """
    下载4k分辨率

    url = https://cn.bing.com/ + urlbase + _UHD.jpg
    :return:
    """
    url = """https://cn.bing.com/{}_UHD.jpg""".format(baseurl)
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)


def _writetodb(d):
    """

    :param d:
    :return:
    """
    o = bingdb.CSqlite()
    o.add(d)


def downimg():
    """

    :return:
    """

    ''' 获取一天的json 描述'''
    d = _getyesterdaywall()
    day = d['enddate']
    baseurl = d['urlbase']

    ''' 本地文件路径 '''
    hdname = initres.bingpath +"/{}_hd.jpg".format(day)
    uhdname = initres.bingpath + "/{}_uhd.jpg".format(day)

    dic = {
        'day': day,
        'urlbase': baseurl,
        'copyright': d['copyright'].replace('\'', '\'\''),
        'copyrightlink': d['copyrightlink'].replace('\'', '\'\''),
        'hd': hdname,
        'uhd': uhdname,
        'download': 0,
        'share': 0
    }
    log.logger.info(dic)

    '''下载图片'''
    # _downhdimg(baseurl, hdname)
    _downuhdimg(baseurl, uhdname)

    ''' 写入数据库'''
    _writetodb(dic)


def getimg(day):
    """
    获取某天的壁纸
    :return:
    """
    return bingdb.CSqlite().getimg(day)


def getallimg():
    """
    获取最近的n张图片
    :return:
    """
    return bingdb.CSqlite().getall(50)


if __name__ == '__main__':
    downimg()
