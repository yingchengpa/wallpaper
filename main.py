# -*- coding: utf-8 -*-

import threading
import bingwall
from flask import Flask
import response
import datetime
import time
import nation

app = Flask(__name__)


@app.route('/wallpaper/bingwall', methods=['GET'])
def getbingwalls():
    return response.response_success_data(bingwall.getallimg())


@app.route('/wallpaper/bingwall/<string:day>', methods=['GET'])
def getbingwall(day):
    return response.response_success_data(bingwall.getimg(day))


@app.route('/wallpaper/nation', methods=['GET'])
def getnations():
    return response.response_success_data(nation.getallimg())


@app.route('/wallpaper/nation/<string:day>', methods=['GET'])
def getnation(day):
    return response.response_success_data(nation.getimg(day))


def _time_task():
    """ 定时任务； 每天凌晨2点清理数据
    """
    while True:
        if datetime.datetime.now().hour == 2:
            bingwall.downimg()
            nation.downimg()
            time.sleep(4000)
        else:
            time.sleep(3500)


if __name__ == '__main__':
    """ 
    每天凌晨2点，定时获取
    """
    t1 = threading.Thread(target=_time_task, daemon=True)
    t1.start()

    """启动flask 处理请求"""
    app.run(host="0.0.0.0", port=6000, debug=False)  # 调试环境
