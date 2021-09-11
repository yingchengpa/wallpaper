# -*- coding: utf-8 -*-

import os

_rootpath = 'd:/github/wallpaper'
# rootpath = '/wallpath'

bingpath = _rootpath + '/bingwall'
nationpath = _rootpath + '/nation'

htmlpath = _rootpath + '/font'

os.makedirs(_rootpath,exist_ok=True)
os.makedirs(bingpath,exist_ok=True)
os.makedirs(nationpath,exist_ok=True)
os.makedirs(htmlpath,exist_ok=True)