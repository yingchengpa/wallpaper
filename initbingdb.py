# -*- coding: utf-8 -*-


DB_SCRIPT = """
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