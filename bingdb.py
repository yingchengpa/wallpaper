# -*- coding: utf-8 -*-


import sqlbase
import sqlitebase
import initbingdb as initsql

TBL_NAME = 'tbl_wall'
DB_NAME = '/bingwall/wall.db'


class CSqlite:

    def __init__(self):
        self.conn = None
        self.sqlbase = sqlitebase.SqliteBase(DB_NAME)

    def __del__(self):
        pass

    def getimg(self, day):
        sql = ''' select * from {} where day = \'{}\'  '''.format(TBL_NAME, day)

        return self.sqlbase.exec_fetchall(sql)

    def getall(self, limit):
        sql = "select * from {} LIMIT {}".format(TBL_NAME, limit)

        return self.sqlbase.exec_fetchall(sql)

    # 增加
    def add(self, dic):
        sql = sqlbase.dic2insertsql(dic, TBL_NAME)
        if self.sqlbase.exec(sql):
            return self.sqlbase.getlastrowid()

        return 0


sqlitebase.SqliteBase.initdb(DB_NAME, initsql.DB_SCRIPT)
