# -*- coding: utf-8 -*-

import threading
import bingwall
from flask import Flask
import response
import datetime
import time
import nation

app = Flask(__name__)


@app.route('/bingwall/<string:day>', methods=['GET'])
def getwall(day):
    return response.response_success_data(bingwall.getimg(day))


def _time_task():
    """ 定时任务； 每天凌晨2点清理数据
    """
    while True:
        if datetime.datetime.now().hour == 2:
            bingwall.downimg()
            nation.downimg()
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
