#备注参考 https://github.com/Ayayaneru/python3-webapp/blob/day03/www/app.py

#输出日志到控制台
#basicConfig配置level信息为INFO，只输出INFO级别的信息
import logging
logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
#from datetime import datetime
#加不加上面这行目前没看出区别

from aiohttp import web

#前面的async是异步io，不加也可以运行
async def index(request):
  return web.Response(body=b'<h1>Awsome</h1>',content_type='text/html')

def init():
    #web app的骨架
     app=web.Application()
     app.router.add_get('/',index)
     web.run_app(app,host='127.0.0.1',port=7000)

if __name__=='__main__':
    init()
