# -*- coding: utf-8 -*-

import threading
import bingwall
from flask import Flask, send_file
import response
import datetime
import time
import nation
import utils.log as log
from flask_cors import CORS
import initres


app = Flask(__name__)

CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def getweb():
    return send_file(initres.htmlpath + '/index.html')


@app.route('/bingwall', methods=['GET'])
def getbingwalls():
    return response.response_success_data(bingwall.getallimg())

@app.route('/bingwall/day/<string:day>', methods=['GET'])
def getbingwall(day):
    return response.response_success_data(bingwall.getimg(day))

@app.route('/bingwall/img/<string:day>', methods=['GET'])
def getbingimg(day):
    url = initres.bingpath + "/{}_hd.jpg".format(day)
    return send_file(url)



@app.route('/nation', methods=['GET'])
def getnations():
    return response.response_success_data(nation.getallimg())

@app.route('/nation/day/<string:day>', methods=['GET'])
def getnation(day):
    return response.response_success_data(nation.getimg(day))

@app.route('/nation/img/<string:day>', methods=['GET'])
def getnationimg(day):
    url = initres.nationpath + "/{}.jpg".format(day)
    return send_file(url)


def _time_task():
    """ 定时任务； 每天凌晨2点清理数据
    """
    while True:                                                        
        log.logger.info('time_task do ')
        if datetime.datetime.now().hour == 2:
            log.logger.info('download pic start !!!!')  
            try:
                bingwall.downimg()
                nation.downimg()
                log.logger.info('download pic end !!!!')
            except Exception as e:
                log.logger.error('error:{}'.format(e))
            finally:
                pass
            time.sleep(4000)
        else:
            time.sleep(3500)


if __name__ == '__main__':
    """ 
    定时获取
    """
    t1 = threading.Thread(target=_time_task, daemon=True)
    t1.start()

    """启动flask 处理请求"""
    app.run(host="0.0.0.0", port=5000, debug=False)  # 调试环境
