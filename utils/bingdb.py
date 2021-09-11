# -*- coding: utf-8 -*-


import utils.sqlbase as sqlbase
import utils.sqlitebase as sqlitebase
import initres

TBL_NAME = 'tbl_wall'
DB_NAME = initres.bingpath + '/wall.db'

_DB_SCRIPT = """
CREATE TABLE tbl_wall (
                "day" VARCHAR(128) NOT NULL default '',
                "urlbase"  VARCHAR(256) NOT NULL default '',
                "copyright" VARCHAR(256) NOT NULL default '',
                "copyrightlink" VARCHAR(256) NOT NULL default '',
                "hd" VARCHAR(256) NOT NULL default '',
                "uhd" VARCHAR(256) NOT NULL default '',
                "download" INTEGER NOT NULL default 0,
                "share" INTEGER NOT NULL default 0,
                PRIMARY KEY ("day")
                );

"""

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


sqlitebase.SqliteBase.initdb(DB_NAME, _DB_SCRIPT)
