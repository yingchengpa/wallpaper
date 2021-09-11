# -*- coding: utf-8 -*-

"""国家地理 每日故事壁纸"""

import requests
import utils.log as log
import json
import time
from utils import nationdb
import  initres

def _html2dict(html):
    """
    通过返回的html内容中，截取 "app" 信息作为json内容
    :param html:
    :return:
    """
    dic = {}
    index = html.find("""{\"app\"""")
    if index == -1:
        return False, dic
    htmlstart = html[index:]

    index = htmlstart.find(""";</script>""")
    if index == -1:
        return False, dic
    htmlend = htmlstart[:index]
    return True, json.loads(htmlend)


def _getdaywall() -> dict:
    """
    通过解析返回的html内容提取json信息
    :return:
    """
    dic = {}
    url = "https://www.nationalgeographic.com/photo-of-the-day/"
    r = []
    try:
        r = requests.get(url, timeout=10)
    except Exception as e:
        log.logger.warning('error: {}'.format(e))
        return dic
    else:
        if r.status_code == 200:
            r = r.text

            # 解析html 文件 获取 ”app“ 这段信息
            b, dic = _html2dict(r)
            if not b:
                return dic

    return dic['page']['meta']['ogMetadata']


def _downimg(baseurl, filepath):
    """
    :return:
    """
    r = requests.get(baseurl)
    with open(filepath, 'wb') as f:
        f.write(r.content)


def _writetodb(d):
    """

    :param d:
    :return:
    """
    o = nationdb.CSqlite()
    o.add(d)


def downimg():
    """

    :return:
    """

    ''' 获取一天的json 描述'''
    d = _getdaywall()

    day = time.strftime('%Y%m%d')
    srcimg = d['sclImg']
    title = d['title']
    discription = d['description']
    ''' 本地文件路径 '''
    hdname = initres.nationpath + '/{}.jpg'.format(day)

    dic = {
        'day': day,
        'srcimg': srcimg,
        'title': title.replace('\'', '\'\''),
        'discription': discription.replace('\'', '\'\''),
        'hd': hdname,
        'download': 0,
        'share': 0
    }
    
    log.logger.warning(dic)    

    '''下载图片'''
    _downimg(srcimg, hdname)

    ''' 写入数据库'''
    _writetodb(dic)


def getimg(day):
    """
    获取某天的壁纸
    :return:
    """
    return nationdb.CSqlite().getimg(day)


def getallimg():
    """
    获取最近的n张图片
    :return:
    """
    return nationdb.CSqlite().getall(50)


if __name__ == '__main__':
    print(downimg())
