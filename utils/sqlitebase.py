# -*- coding: utf-8 -*-

"""
sqlite base
"""

import sqlite3
import utils.log as log
import utils.sqlbase as sqlbase
import os


class SqliteBase:

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

        # 设置返回的数据库信息中携带 表字段名

        # dict_factory 一定要设置为静态函数，否正会导致变量引用计数多+1,
        # 最后导致局部变量永远无法删除，这个bug没找到具体原因
        self.conn.row_factory = sqlbase.dict_factory

    def __del__(self):
        self.conn.close()

    # 初始化数据库，执行脚本语句
    @staticmethod
    def initdb(dbname, script):
        if os.path.exists(dbname):
            return

        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()

        try:
            cursor.executescript(script)
            conn.commit()
        except Exception as e:
            log.logger.warning('error: {}'.format(e))
        finally:
            cursor.close()
            conn.close()

    # 初始化数据库，执行脚本语句
    @staticmethod
    def initdb2(dbname, script):

        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()

        try:
            cursor.executescript(script)
            conn.commit()
        except Exception as e:
            log.logger.warning('error: {}'.format(e))
        finally:
            cursor.close()
            conn.close()

    # 执行sql
    # 返回错误
    def exec(self, sql):
        ret = True
        cursor = self.conn.cursor()
        try:
            # print('[{}]: {}'.format(dt.datetime.now().strftime('%F %T'), sql))
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.logger.warning('sql {} , error: {}'.format(sql, e))
            ret = False
        finally:
            pass
        return ret

    # 执行sql任务
    # 返回列表数据

    def exec_fetchall(self, sql):
        lnt = []
        cursor = self.conn.cursor()
        try:
            # print("[{}]: {}".format(dt.datetime.now().strftime('%F %T'), sql))
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.logger.warning('sql {} , error: {}'.format(sql, e))
        else:
            lnt = cursor.fetchall()
        finally:
            pass
        return lnt

    def exec_fetchone(self, sql):
        dic = {}
        cursor = self.conn.cursor()
        try:
            # print("[{}]: {}".format(dt.datetime.now().strftime('%F %T'), sql))
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.logger.warning('sql {} , error: {}'.format(sql, e))
        else:
            dic = cursor.fetchone()
        finally:
            pass
        return dic

    #  插入数据后，并返回最后的id
    def getlastrowid(self):
        sql = 'select last_insert_rowid() '
        dic = self.exec_fetchone(sql)
        if 'last_insert_rowid()' in dic:
            return dic['last_insert_rowid()']
        else:
            return 0
