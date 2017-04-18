#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: $Author$
Date: $Date$
Revision: $Revision$

Description:
    权限名及路径表配置
"""

from config.config import BACK_PRE
from common.utilt import getLang

class AccessObj(object):
    def __init__(self, tree, method, field, check=False):
        self.tree = tree
        self.method = method
        if method in ('GET', 'POST'):
            self.url = BACK_PRE + '/'.join(tree)
            self.accessTag = '%s:'%(method) + self.url
        else:
            self.url = '#'
            self.accessTag = ''
        self.field = field
        self.check = check

    def getTxt(self, lang):
        return getattr(lang, self.field)

MENU_MODULES = (
    AccessObj(("self",), None, 'MENU_PAGE_ACCOUNT_INFO_TXT'), \
    AccessObj(("self", "info"), 'GET', 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("self", "modifyPasswd"), 'GET', 'MENU_PAGE_MODIFY_PASSWD_TXT'), \
    AccessObj(("self", "syslog"), 'GET', 'MENU_PAGE_SYS_OP_INFOS_TXT'), \

    AccessObj(("announce",), None, 'MENU_PAGE_ANNOUNCE_TXT'), \
    AccessObj(("announce", "list"), 'GET', 'MENU_PAGE_ANNOUNCE_LIST_TXT'), \

    AccessObj(("subAccount",), None, 'MENU_PAGE_AG_SUB_ACCOUNT_TXT'), \
    AccessObj(("subAccount", "list"), 'GET', 'MENU_PAGE_AG_SUB_ACCOUNT_LIST_TXT'), \

    AccessObj(("ag",), None, 'MENU_PAGE_AG_TXT'), \
    AccessObj(("ag", "list"), 'GET', 'MENU_PAGE_AG_LIST_TXT'), \
    AccessObj(("ag", "cashReport"), 'GET', 'MENU_PAGE_AG_CASH_REPORT_TXT'), \
    AccessObj(("statistics", "online"), 'GET', 'MENU_PAGE_STATISTICS_ONLINE_TXT'), \
    AccessObj(("statistics", "onlineCount"), 'GET', 'MENU_PAGE_ONLINE_COUNT_TXT'), \
    AccessObj(("statistics", "retentionMorrow"), 'GET', 'MENU_PAGE_STATISTICS_RETENTION_MORROW_TXT'), \
    AccessObj(("statistics", "retention"), 'GET', 'MENU_PAGE_STATISTICS_RETENTION_TXT'), \

    AccessObj(("currencyDict",), None, 'MENU_PAGE_CURRENCY_TXT'), \
    AccessObj(("currencyDict", "list"), 'GET', 'MENU_PAGE_CURRENCY_LIST_TXT'), \

    AccessObj(("operatorSetting",), None, 'MENU_PAGE_OPERATOR_SETTING'), \
    AccessObj(("operatorSetting", "operatorGolden"), 'GET', 'MENU_PAGE_OPERATOR_TXT'), \

    AccessObj(("fishGame",), None, 'MENU_PAGE_FISHGAME_TXT'), \
    AccessObj(("fishGame", "setting"), 'GET', 'MENU_PAGE_SETTING_TXT'), \
    AccessObj(("fishGame", "broadcast"), 'GET', 'MENU_PAGE_BROADCAST'), \

    AccessObj(("statistics",), None, 'MENU_PAGE_STATISTICS_TXT'), \
    AccessObj(("statistics", "agTotalCash"), 'GET', 'MENU_PAGE_STATISTICS_TOTAL_CASH_TXT'), \
    AccessObj(("statistics", "agCash"), 'GET', 'MENU_PAGE_STATISTICS_CASH_TXT'), \
)

ACCESS_CURRENCY_CREATE = AccessObj(("currencyDict", "create"), 'GET', 'SUB_MENU_CURRENCY_ADD_TXT')

ACCESS_CURRENCY_LIST_MODULES = (
    AccessObj(("currencyDict", "modify"), 'GET', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("currencyDict", "del"), 'POST', 'SUB_MENU_DELETE_TXT'), \
)

ACCESS_AG_CREATE = AccessObj(("ag", "create"), 'POST', 'SUB_MENU_DIRECT_AGENT_ADD_TXT')

ACCESS_AG_LIST_MODULES = (
    AccessObj(("ag", "info"), 'GET', 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("ag", "privilege"), 'GET', 'SUB_MENU_PRIVILEGE'), \
    AccessObj(("ag", "modify"), 'GET', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("ag", "modifyPasswd"), 'GET', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("ag", "depositMoney"), 'GET', 'SUB_MENU_DEPOSIT_TXT'), \
    AccessObj(("ag", "drawMoney"), 'GET', 'SUB_MENU_WITHDRAW_TXT'), \
    AccessObj(("ag", "freeze"), 'POST', 'SUB_MENU_FREEZE_TXT'), \
    AccessObj(("ag", "create"), 'GET', 'SUB_MENU_AGENT_ADD_TXT'), \
    AccessObj(("ag/member", "create"), 'GET', 'SUB_MENU_MEMBER_ADD_TXT'), \
)

ACCESS_MEMBER_CREATE = AccessObj(("ag/member", "create"), 'POST', 'SUB_MENU_DIRECT_MEMBER_ADD_TXT')

ACCESS_MEMBER_LIST_MODULES = (
    AccessObj(("ag/member", "info"), 'GET', 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("ag/member", "modify"), 'GET', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("ag/member", "modifyPasswd"), 'GET', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("ag/member", "depositMoney"), 'GET', 'SUB_MENU_DEPOSIT_TXT'), \
    AccessObj(("ag/member", "drawMoney"), 'GET', 'SUB_MENU_WITHDRAW_TXT'), \
    AccessObj(("ag/member", "freeze"), 'POST', 'SUB_MENU_FREEZE_TXT'), \
)

ACCESS_ANNOUNCE_CREATE = AccessObj(("announce", "create"), 'POST', 'SUB_MENU_MARQUEE_ADD_TXT')

ACCESS_ANNOUNCE_LIST_MODULES = (
    AccessObj(("announce", "del"), 'POST', 'SUB_MENU_DELETE_TXT'), \
)

ACCESS_SUB_ACCOUNT_CREATE = AccessObj(("subAccount", "create"), 'POST', 'SUB_MENU_SUB_ACCOUNT_ADD_TXT')

ACCESS_SUB_ACCOUNT_LIST_MODULES = (
    AccessObj(("subAccount", "info"), 'GET', 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("ag", "privilege"), 'GET', 'SUB_MENU_PRIVILEGE'), \
    AccessObj(("subAccount", "modify"), 'GET', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("subAccount", "modifyPasswd"), 'GET', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("subAccount", "freeze"), 'POST', 'SUB_MENU_FREEZE_TXT'), \
)

ACCESS_CTRL_MODULES = (
    AccessObj(("self",), None, 'MENU_PAGE_ACCOUNT_INFO_TXT'), \
    AccessObj(("self", "info"), None, 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("self", "info"), 'GET', 'MENU_PAGE_SELF_INFO_TXT'), \
    AccessObj(("self", "modifyPasswd"), None, 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("self", "modifyPasswd"), 'POST', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("self", "syslog"), 'GET', 'MENU_PAGE_SYS_OP_INFOS_TXT'), \

    AccessObj(("subAccount",), None, 'MENU_PAGE_AG_SUB_ACCOUNT_TXT'), \
    AccessObj(("subAccount", "list"), 'GET', 'SUB_MENU_VIEW_TXT'), \
    AccessObj(("subAccount", "info"), 'GET', 'SUB_MENU_VIEW_SINGLE_TXT'), \
    AccessObj(("subAccount", "create"), 'POST', 'SUB_MENU_ADD_TXT'), \
    AccessObj(("subAccount", "modify"), 'POST', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("subAccount", "freeze"), 'POST', 'SUB_MENU_PRIVG_FREEZE_TXT'), \
    AccessObj(("ag", "privilege"), 'POST', 'SUB_MENU_PRIVILEGE'), \

    AccessObj(("ag",), None, 'MENU_PAGE_AG_TXT'), \
    AccessObj(("ag", "list"), None, 'MENU_PAGE_AG_LIST_TXT'), \
    AccessObj(("ag", "list"), 'GET', 'SUB_MENU_VIEW_TXT'), \
    AccessObj(("ag", "info"), 'GET', 'SUB_MENU_VIEW_SINGLE_TXT'), \
    AccessObj(("ag", "create"), 'POST', 'SUB_MENU_ADD_TXT'), \
    AccessObj(("ag", "modify"), 'POST', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("ag", "modifyPasswd"), 'POST', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("ag", "depositMoney"), 'POST', 'SUB_MENU_DEPOSIT_TXT'), \
    AccessObj(("ag", "drawMoney"), 'POST', 'SUB_MENU_WITHDRAW_TXT'), \
    AccessObj(("ag", "freeze"), 'POST', 'SUB_MENU_PRIVG_FREEZE_TXT'), \
    AccessObj(("ag", "privilege"), 'POST', 'SUB_MENU_PRIVILEGE'), \
    AccessObj(("ag", "cashReport"), None, 'MENU_PAGE_AG_CASH_REPORT_TXT'), \
    AccessObj(("ag", "cashReport"), 'GET', 'MENU_PAGE_AG_CASH_REPORT_TXT'), \
    AccessObj(("statistics", "online"), None, 'MENU_PAGE_STATISTICS_ONLINE_TXT'), \
    AccessObj(("statistics", "online"), 'GET', 'MENU_PAGE_STATISTICS_ONLINE_TXT'), \
    AccessObj(("statistics", "onlineCount"), None, 'MENU_PAGE_ONLINE_COUNT_TXT'), \
    AccessObj(("statistics", "onlineCount"), 'GET', 'MENU_PAGE_ONLINE_COUNT_TXT'), \
    AccessObj(("statistics", "retention"), None, 'MENU_PAGE_STATISTICS_RETENTION_TXT'), \
    AccessObj(("statistics", "retention"), 'GET', 'MENU_PAGE_STATISTICS_RETENTION_TXT'), 
    AccessObj(("statistics", "retentionMorrow"), None, 'MENU_PAGE_STATISTICS_RETENTION_MORROW_TXT'), \
    AccessObj(("statistics", "retentionMorrow"), 'GET', 'MENU_PAGE_STATISTICS_RETENTION_MORROW_TXT'), \

    AccessObj(("announce",), None, 'MENU_PAGE_ANNOUNCE_TXT'), \
    AccessObj(("announce", "list"), None, 'MENU_PAGE_ANNOUNCE_LIST_TXT'), \
    AccessObj(("announce", "list"), 'GET', 'SUB_MENU_VIEW_TXT'), \
    AccessObj(("announce", "create"), 'POST', 'SUB_MENU_ADD_TXT'), \
    AccessObj(("announce", "del"), 'POST', 'SUB_MENU_DELETE_TXT'), \

    AccessObj(("ag/member",), None, 'MENU_PAGE_MEMBER_TXT'), \
    AccessObj(("ag/member", "info"), 'GET', 'SUB_MENU_VIEW_SINGLE_TXT'), \
    AccessObj(("ag/member", "create"), 'POST', 'SUB_MENU_ADD_TXT'), \
    AccessObj(("ag/member", "modify"), 'POST', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("ag/member", "modifyPasswd"), 'POST', 'SUB_MENU_MODIFY_PASSWD_TXT'), \
    AccessObj(("ag/member", "depositMoney"), 'POST', 'SUB_MENU_DEPOSIT_TXT'), \
    AccessObj(("ag/member", "drawMoney"), 'POST', 'SUB_MENU_WITHDRAW_TXT'), \
    AccessObj(("ag/member", "freeze"), 'POST', 'SUB_MENU_PRIVG_FREEZE_TXT'), \

    AccessObj(("currencyDict",), None, 'MENU_PAGE_CURRENCY_TXT'), \
    AccessObj(("currencyDict", "list"), 'GET', 'SUB_MENU_VIEW_TXT'), \
    AccessObj(("currencyDict", "info"), 'GET', 'SUB_MENU_VIEW_SINGLE_TXT'), \
    AccessObj(("currencyDict", "create"), 'POST', 'SUB_MENU_ADD_TXT'), \
    AccessObj(("currencyDict", "modify"), 'POST', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("currencyDict", "del"), 'POST', 'SUB_MENU_DELETE_TXT'), \

    AccessObj(("operatorSetting",), None, 'MENU_PAGE_OPERATOR_SETTING'), \
    AccessObj(("operatorSetting", "operatorGolden"), None, 'MENU_PAGE_OPERATOR_TXT'), \
    AccessObj(("operatorSetting", "operatorGolden"), 'POST', 'SUB_MENU_MODIFY_TXT'), \

    AccessObj(("fishGame",), None, 'MENU_PAGE_FISHGAME_TXT'), \
    AccessObj(("fishGame", "setting"), None, 'MENU_PAGE_SETTING_TXT'), \
    AccessObj(("fishGame", "setting"), 'POST', 'SUB_MENU_MODIFY_TXT'), \
    AccessObj(("fishGame", "serviceSwitch"), 'POST', 'SUB_MENU_ONOFF_GAME_TXT'), \
    AccessObj(("fishGame", "broadcast"), None, 'MENU_PAGE_BROADCAST'), \
    AccessObj(("fishGame", "broadcast"), 'POST', 'MENU_PAGE_BROADCAST'), \

    AccessObj(("statistics",), None, 'MENU_PAGE_STATISTICS_TXT'), \
    AccessObj(("statistics", "agTotalCash"), None, 'MENU_PAGE_STATISTICS_TOTAL_CASH_TXT'), \
    AccessObj(("statistics", "agTotalCash"), 'GET', 'MENU_PAGE_STATISTICS_TOTAL_CASH_TXT'), \
    AccessObj(("statistics", "agCash"), None, 'MENU_PAGE_STATISTICS_CASH_TXT'), \
    AccessObj(("statistics", "agCash"), 'GET', 'MENU_PAGE_STATISTICS_CASH_TXT'), \
)

ACCESS_SADMIN_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount",), None, ''), \
    AccessObj(("subAccount", "list"), 'GET', '', True), \
    AccessObj(("subAccount", "info"), 'GET', '', True), \
    AccessObj(("subAccount", "create"), 'POST', '', True), \
    AccessObj(("subAccount", "modify"), 'POST', '', True), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("subAccount", "freeze"), 'POST', '', True), \

    AccessObj(("ag", "list"), 'GET', '', True), \
    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "privilege"), 'POST', '', True), \
    AccessObj(("ag", "create"), 'POST', '', True), \
    AccessObj(("ag", "modify"), 'POST', '', True), \
    AccessObj(("ag", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag", "freeze"), 'POST', '', True), \
    AccessObj(("ag", "cashReport"), 'GET', '', True), \

    AccessObj(("announce", "list"), 'GET', '', True), \
    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \
    AccessObj(("announce", "create"), 'POST', '', True), \
    AccessObj(("announce", "del"), 'POST', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \
    AccessObj(("ag/member", "create"), 'POST', '', True), \
    AccessObj(("ag/member", "modify"), 'POST', '', True), \
    AccessObj(("ag/member", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag/member", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "freeze"), 'POST', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \
    AccessObj(("currencyDict", "create"), 'POST', '', True), \
    AccessObj(("currencyDict", "modify"), 'POST', '', True), \
    AccessObj(("currencyDict", "del"), 'POST', '', True), \

    AccessObj(("operatorSetting", "operatorGolden"), 'POST', '', True), \

    AccessObj(("fishGame", "setting"), 'POST', '', True), \
    AccessObj(("fishGame", "serviceSwitch"), 'POST', '', True), \
    AccessObj(("fishGame", "broadcast"), 'POST', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "agTotalCash"), 'GET', '', True), \
    AccessObj(("statistics", "memberCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
    AccessObj(("statistics", "retention"), 'GET', '', True), \
    AccessObj(("statistics", "retentionMorrow"), 'GET', '', True), \
    AccessObj(("statistics", "onlineCount"), 'GET', '', True), \
)

ACCESS_ADMIN_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount",), None, ''), \
    AccessObj(("subAccount", "list"), 'GET', '', True), \
    AccessObj(("subAccount", "info"), 'GET', '', True), \
    AccessObj(("subAccount", "create"), 'POST', '', True), \
    AccessObj(("subAccount", "modify"), 'POST', '', True), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("subAccount", "freeze"), 'POST', '', True), \

    AccessObj(("ag", "list"), 'GET', '', True), \
    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "privilege"), 'POST', '', True), \
    AccessObj(("ag", "create"), 'POST', '', True), \
    AccessObj(("ag", "modify"), 'POST', '', True), \
    AccessObj(("ag", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag", "freeze"), 'POST', '', True), \
    AccessObj(("ag", "cashReport"), 'GET', '', True), \

    AccessObj(("announce", "list"), 'GET', '', True), \
    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \
    AccessObj(("announce", "create"), 'POST', '', True), \
    AccessObj(("announce", "del"), 'POST', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \
    AccessObj(("ag/member", "create"), 'POST', '', True), \
    AccessObj(("ag/member", "modify"), 'POST', '', True), \
    AccessObj(("ag/member", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag/member", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "freeze"), 'POST', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \
    AccessObj(("currencyDict", "create"), 'POST', '', True), \
    AccessObj(("currencyDict", "modify"), 'POST', '', True), \
    AccessObj(("currencyDict", "del"), 'POST', '', True), \

    AccessObj(("fishGame", "setting"), 'POST', '', True), \
    AccessObj(("fishGame", "broadcast"), 'POST', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "agTotalCash"), 'GET', '', True), \
    AccessObj(("statistics", "memberCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
    AccessObj(("statistics", "retention"), 'GET', '', True), \
    AccessObj(("statistics", "retentionMorrow"), 'GET', '', True), \
    AccessObj(("statistics", "onlineCount"), 'GET', '', True), \
)

ACCESS_OPERATOR_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount",), None, ''), \
    AccessObj(("subAccount", "list"), 'GET', '', True), \
    AccessObj(("subAccount", "info"), 'GET', '', True), \
    AccessObj(("subAccount", "create"), 'POST', '', True), \
    AccessObj(("subAccount", "modify"), 'POST', '', True), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("subAccount", "freeze"), 'POST', '', True), \

    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "modify"), 'POST', '', True), \
    AccessObj(("ag", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag", "privilege"), 'POST', '', True), \

    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \
    AccessObj(("ag/member", "freeze"), 'POST', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
)

ACCESS_AG_HIGH_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount",), None, ''), \
    AccessObj(("subAccount", "list"), 'GET', '', True), \
    AccessObj(("subAccount", "info"), 'GET', '', True), \
    AccessObj(("subAccount", "create"), 'POST', '', True), \
    AccessObj(("subAccount", "modify"), 'POST', '', True), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("subAccount", "freeze"), 'POST', '', True), \

    AccessObj(("ag", "list"), 'GET', '', True), \
    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "privilege"), 'POST', '', True), \
    AccessObj(("ag", "create"), 'POST', '', True), \
    AccessObj(("ag", "modify"), 'POST', '', True), \
    AccessObj(("ag", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag", "freeze"), 'POST', '', True), \
    AccessObj(("ag", "access"), 'POST', '', True), \
    AccessObj(("ag", "cashReport"), None, '', True), \
    AccessObj(("ag", "cashReport"), 'GET', '', True), \

    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \
    AccessObj(("ag/member", "create"), 'POST', '', True), \
    AccessObj(("ag/member", "modify"), 'POST', '', True), \
    AccessObj(("ag/member", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag/member", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "freeze"), 'POST', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "agTotalCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
)

ACCESS_AG_LOW_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount",), None, ''), \
    AccessObj(("subAccount", "list"), 'GET', '', True), \
    AccessObj(("subAccount", "info"), 'GET', '', True), \
    AccessObj(("subAccount", "create"), 'POST', '', True), \
    AccessObj(("subAccount", "modify"), 'POST', '', True), \
    AccessObj(("subAccount", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("subAccount", "freeze"), 'POST', '', True), \

    AccessObj(("ag", "list"), 'GET', '', True), \
    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "privilege"), 'POST', '', True), \
    AccessObj(("ag", "modify"), 'POST', '', True), \
    AccessObj(("ag", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag", "freeze"), 'POST', '', True), \
    AccessObj(("ag", "access"), 'POST', '', True), \
    AccessObj(("ag", "cashReport"), None, '', True), \
    AccessObj(("ag", "cashReport"), 'GET', '', True), \

    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \
    AccessObj(("ag/member", "create"), 'POST', '', True), \
    AccessObj(("ag/member", "modify"), 'POST', '', True), \
    AccessObj(("ag/member", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("ag/member", "depositMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "drawMoney"), 'POST', '', True), \
    AccessObj(("ag/member", "freeze"), 'POST', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "agTotalCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
)

ACCESS_SUB_ACCOUNT_MODULES = (
    AccessObj(("self", "info"), 'GET', '', True), \
    AccessObj(("self", "modifyPasswd"), 'POST', '', True), \
    AccessObj(("self", "syslog"), 'GET', '', True), \

    AccessObj(("subAccount", "info"), 'GET', '', True), \

    AccessObj(("ag", "list"), 'GET', '', True), \
    AccessObj(("ag", "info"), 'GET', '', True), \
    AccessObj(("ag", "cashReport"), None, '', True), \
    AccessObj(("ag", "cashReport"), 'GET', '', True), \

    AccessObj(("announce", "get"), 'GET', '', True), \
    AccessObj(("announce", "info"), 'GET', '', True), \

    AccessObj(("ag/member", "info"), 'GET', '', True), \

    AccessObj(("currencyDict", "list"), 'GET', '', True), \
    AccessObj(("currencyDict", "info"), 'GET', '', True), \

    AccessObj(("statistics", "agCash"), 'GET', '', True), \
    AccessObj(("statistics", "agTotalCash"), 'GET', '', True), \
    AccessObj(("statistics", "online"), 'GET', '', True), \
)

ACCESS_AGENT_LIST = (
    {'url':'/admin/agent/create','method':'GET','txt':'创建代理'},
    {'url':'/admin/agent/modifyPasswd','method':'GET','txt':'修改'},
    {'url':'/admin/agent/info','method':'GET','txt':'查看'},
    {'url':'/admin/agent/freeze','method':'GET','txt':'冻结'},
    {'url':'/admin/agent/del','method':'GET','txt':'删除'}
)

