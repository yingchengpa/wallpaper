# -*- coding: utf-8 -*-

"""
上传文件到oss
"""

import oss2

def upload2oss_bing(filename, filepath):
    # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
    # return oss url
    bucketname = 'bing-pic'
    auth = oss2.Auth('LTAI5tEDq9Va5MHKMswUJbRs', '9SPENIDYOgdQlnUBsHRRATAGVSH0QO')
    # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
    # 填写Bucket名称。
    bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', bucketname)

    # 必须以二进制的方式打开文件。
    bucket.put_object_from_file(filename, filepath)

    # https://BucketName.Endpoint/ObjectName
    return 'https://{}.oss-cn-hangzhou.aliyuncs.com/{}'.format(bucketname,filename)
