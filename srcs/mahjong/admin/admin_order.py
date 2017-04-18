#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
   订单模块
"""


from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH
from common.utilt import *
from web_db_define import *
from datetime import datetime

@admin_app.get('/order/buy')
def getBuyPage(redis,session):
    """
        购买房卡
    """
    curTime = datetime.now()
    lang    = getLang()

    selfAccount = session['account']
    agentTable = AGENT_TABLE%(selfAccount)

    parent_id = redis.hget(agentTable,'parent_id')
    parentAg  = ''
    if not parentAg:
        parentAg = '总公司'

    info = {
                'title'               :       '线上购卡 [上级代理:%s]'%(parentAg),
                'parentAccount'       :        parentAg,
                'backUrl'             :       '/admin/order/buy',
                'submitUrl'           :       '/admin/order/buy',
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_buy',info=info,lang=lang)

@admin_app.post('/order/buy')
def do_BuyPage(redis,session):
    """
        购买房卡操作
    """
    curTime = datetime.now()

    selfAccount,selfId = session['account'],session['uid']
    parentAg  =  request.forms.get('parentAg','').strip()
    cardNums  =  request.forms.get('cardNums','').strip()
    present_card = request.forms.get('parent_card','').strip()
    passwd    =  request.forms.get('passwd','').strip()
    note      =  request.forms.get('note','').strip()

    #[print]
    print '[%s][orderBuy][info] selfAccount[%s] parentAg[%s] cardNums[%s] present_card[%s] passwd[%s] note[%s]'\
                %(curTime,selfAccount,cardNums,present_card,passwd,note)
    
    checkNullFields = [
            {'field':parentAg,'msg':'售卡方不存在'},
            {'field':cardNums,'msg':'请选择充值卡数'},
            {'field':passwd,'msg':'请填写你的登录密码'}
    ]

    for check in checkNullFields:
        if not check['field']:
            return {'code':1,'msg':check['msg']}

    adminTable = ADMIN_TABLE%(selfAccount)
    selfPasswd,selfRoomCard,type,parent_id = redis.hmget(adminTable,('passwd','roomcard','type','parent_id'))

    #生成充值订单号
    orderNo = getOrderNo()

    orderInfo = {
            'orderNo'                :       orderNo,
            'cardNums'               :       cardNums,
            'card_present'           :       present_card,
            'applyAccount'           :       selftAccount,
            'status'                 :       0,
            'apply_date'             :       curTime.strftime('%Y-%m-%d %H:%M:%S'),
            'finish_date'            :       '',
            'type'                   :       0,
            'price'                  :       price,
            'note'                   :       note,
            'saleAccount'            :       parentAg
    }

    if createOrder(redis,orderInfo):
        dateStr = curTime.strftime('%Y-%m-%d')
        pipe = redis.pipeline()
        #将订单写入购卡订单
        pipe.lpush(AGENT_BUY_ORDER_LIST%(selfId,dateStr),orderNo)
        pipe.lpush(AGENT_BUYPEDDING_ORDER_LIST%(selfId,dateStr),orderNo)
        #将订单写入售卡订单
        pipe.lpush(AGENT_SALE_ORDER_LIST%(parent_id,dateStr),orderNo)
        pipe.lpush(AGENT_SALEPENDING_ORDER_LIST%(parent_id,dateStr),orderNo)

        pipe.execute()
        return {'code':0,'msg':'申请购卡成功,订单号[%s]'%(orderNo),'jumpUrl':BACK_PRE+'/order/buy/record'}

    return {'code':1,'msg':'申请购卡失败,订单号[%s]'%(orderNo)}

@admin_app.get('/order/buy/record')
def getBuyRecordPage(redis,session):
    """
        获取购买房卡记录
    """
    curTime = datetime.now()
    lang    = getLang()

    info = {
                'title'               :       '购卡记录',
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_buy_record',info=info,lang=lang)

@admin_app.get('/order/sale/record')
def getSaleRecordPage(redis,session):
    """
        获取售卖房卡记录
    """
    curTime = datetime.now()
    lang    = getLang()

    info = {
                'title'               :       '售卡记录',
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_sale_record',info=info,lang=lang)

@admin_app.post('/order/comfirm')
def do_orderComfirm(redis,session):
    """
    代理订单确认
    """
    pass

@admin_app.get('/order/info')
def getOrderInfo(redis,session):
    """
    订单信息查询
    """
    pass