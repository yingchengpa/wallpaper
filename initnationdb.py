# -*- coding: utf-8 -*-


DB_SCRIPT = """
CREATE TABLE tbl_nation (
                "day" VARCHAR(128) NOT NULL default '',
                "srcimg"  VARCHAR(256) NOT NULL default '',
                "title" VARCHAR(256) NOT NULL default '',
                "discription" VARCHAR(1024) NOT NULL default '',
                "hd" VARCHAR(256) NOT NULL default '',
                "download" INTEGER NOT NULL default 0,
                "share" INTEGER NOT NULL default 0,
                PRIMARY KEY ("day")
                );

"""