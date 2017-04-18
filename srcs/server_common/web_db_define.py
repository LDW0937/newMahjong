#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    web数据表及关系对应
"""


"""
agent
  {
        id          :    代理的ID
        account     :    账号
        passwd      :    密码
        name        :    昵称
        shareRate   :    占成
        valid       :    是否有效 0-冻结 1-有效
        isCreate    :    是否允许创建下级代理 0-不允许 1-允许
        roomcard_id :    当前货币ID
        parent_id   :    上线代理id
        roomcard    :    房卡数
        regIp       :    注册IP
        regDate     :    注册日期
        lastLoginIP :    注册IP
        lastLoginDate :  注册日期
        type        :    账号类型 0-系统管理员 1-总公司 2-一级代理 3-二级代理
  }
"""
AGENT_COUNT         =     'agents:id:count'
AGENT_TABLE         =     'agents:account:%s'
AGENT_CHILD_TABLE   =     'agents:id:%s:child'

"""
Game 游戏表
{
       id        :     游戏ID
       name      :     游戏名称
       version   :     游戏版本号
       web_tag   :     web启动地址
       ipa_tag   :     ios启动标志
       apk_tag   :     android启动标志
       minVersion  :   android版本号
       iosVersion  :   ios版本号
       pack_name   :   游戏包名称
       downloadUrl :   游戏包下载地址
       IPAURL      :   
       apk_size    :   apk大小
       apk_md5     :   apkmd5验证
       game_rule   :   游戏规则(创建房间时使用)
       module_id   :   游戏模块ID

}
"""
GAME_COUNT      =       'games:id:count'
GAME_LIST       =       'games:list'
GAME_TABLE      =       'games:id:%s'

"""
gameModule
游戏模块表
{
    id      :    游戏模块ID
    path    :    游戏路径
    remart  :    备注
    name    :    游戏模块名称
}
"""
GAMEMODULE_COUNT   =   'gameModule:id:count'
GAMEMODULE_TABLE   =   'gameModule:id:%s'


"""
agent_own_game
代理游戏映射
agent:ID:own:games  set
"""
AGENT_OWN_GAME     =    'agent:%s:own:games'


"""
agent2access
代理权限表
agent:ID:accesses  set
"""
AGENT2ACCESS     =    'agent:%s:accesses'

"""
agent_op_log
代理操作日志
{
    'id'            :       代理ID
    'datetime'      :       操作时间
    'desc'          :       操作描述
}
"""
AGENT_OP_COUNT              = 'agent:op:count'
AGENT_OP_LOG_TABLE          = 'agent:%s:op:%s:log'
AGENT_OP_LOG_LIST           = 'agent:%s:op:log:list'
AGENT_OP_LOG_DATESET_TABLE  = 'agent:%s:op:log:dateset:%s'


"""
order
订单表
{
        'id'            :       订单ID
        'order_no'      :       订单编号
        'card_nums'     :       购卡数
        'card_present'  :       赠送卡数
        'apply_date'    :       申请购卡日期
        'finish_date'   :       确认订单信息
        'note'          :       备注
        'type'          :       充卡类型 0-代理充卡 1-会员充卡
        'price'         :       每张房卡价格
        'status'        :       0-等待卖卡房确认 1-卖卡房已确认
        'applyAccount'  :       购卡方账号
        'saleAccount'   :       售卡方账号
}
"""
ORDER_COUNT     =    'orders:count'
ORDER_TABLE     =    'orders:id:%s'


"""
buy_order_success_date
代理成功列表
agent:ID:buySuccess:datestr
"""
AGENT_BUY_ORDER_LIST         = 'agent:%s:buy:order:%s'
AGENT_BUYSUCCESS_ORDER_LIST  = 'agent:%s:buySuccess:%s'
AGENT_BUYPENDING_ORDER_LIST  = 'agent:%s:buyPending:%s'

AGENT_SALE_ORDER_LIST         = 'agent:%s:sale:order:%s'
AGENT_SALESUCCESS_ORDER_LIST  = 'agent:%s:saleSuccess:%s'
AGENT_SALEPENDING_ORDER_LIST  = 'agent:%s:salePending:%s'


"""
agent_buyOrder_card_date
代理购卡报表统计
agent:ID:buy:card:%s:dateStr
"""
AGENT_BUY_CARD_DATE = 'agent:%s:buy:card:%s:%s'


"""
agent_buyOrder_card_date
代理售卡报表统计
agent:ID:sale:card:%s:dateStr
"""
AGENT_SALE_CARD_DATE = 'agent:%s:sale:card:%s:%s'


"""
roomcard_info
房卡信息
{
            id     :  房卡ID
            money  :  房卡单价
            date   :  设置日期
}
roomcard:id:%s
"""
ROOMCARD_COUNT    = 'roomcard:count'
ROOMCARD_TABLE    = 'roomcard:id:%s'


"""
agent2roomcard
代理对应房卡列表
agent:%s:roomcard:list
"""
AGENT2ROOMCARD     =    'agent:%s:roomcard:list'