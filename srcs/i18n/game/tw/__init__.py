#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: $Author$
Date: $Date$
Revision: $Revision$

Description:
    翻译文本
"""

from pickfish.protocols.pickfish_consts import LANG_CODE

REG_TIPS_ALREADY_LOGON = "已登錄。".decode(LANG_CODE)
REG_TIPS_EMPTY_ACCOUNT_PASSWD = "賬號和密碼不能為空。".decode(LANG_CODE)
REG_TIPS_INVALID_ACCOUNT = "賬號不合法（必須為字母開頭，總長度4-18的大小寫字母、數字、下劃線）。".decode(LANG_CODE)
REG_TIPS_INVALID_PASSWD = "密碼不合法（必須為總長度6-20的合法字符）。".decode(LANG_CODE)
REG_TIPS_ACCOUNT_EXIST = "賬號已存在，請重新輸入。".decode(LANG_CODE)


LOGIN_TIPS_INVALID_ACCOUNT_PASSWD = "賬號或密碼不正確，請重新輸入。".decode(LANG_CODE)
LOGIN_TIPS_ALREADY_LOGON = "賬號已登錄。".decode(LANG_CODE)
LOGIN_TIPS_TIMEOUT = "登錄超時或不合法，請重新進入遊戲。".decode(LANG_CODE)
LOGIN_TIPS_INVALID_ACCOUNT = "登錄失敗，賬號已被凍結，請聯繫管理員。".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENABLE_GAME = "無權限進入本遊戲，請聯繫代理商開通權限。".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENOUGH_TRIAL = "試玩人數過多，請稍後再試。".decode(LANG_CODE)

LOGIN_TIPS_LOGIN_INTERNAL_ERROR = "運營商系統正在維護中，請稍後再試。".decode(LANG_CODE)

TRANSFER_TIPS_NOT_ENOUGH = "錢包餘額不足，請充值或調小轉賬金額。".decode(LANG_CODE)
TRANSFER_TIPS_INTERNAL_ERROR = "錢包系統正在維護中，請稍後再試。".decode(LANG_CODE)
TRANSFER_TIPS_ALREADY_DO = "正在轉賬處理中，請稍後。".decode(LANG_CODE)

OLD_PASSWORD_NOT_MATCH = "原密碼不正確，請重新輸入。".decode(LANG_CODE)

DISCONNECTED_TIPS_LONG_IDLE = "你因長時間未做操作，被斷開連接，請重新登錄。".decode(LANG_CODE)
DISCONNECTED_TIPS_NORMAL = "網路中斷，請檢查網路並重新進入遊戲。".decode(LANG_CODE)
DISCONNECTED_TIPS_CLOSE_SERVER = "系統因進行維護暫已關閉，請稍後再進。".decode(LANG_CODE)
DISCONNECTED_TIPS_FREEZE = "你的賬號已被管理員凍結，請咨詢代理商了解詳請。".decode(LANG_CODE)
DISCONNECTED_TIPS_REPEAT_LOGIN = "你的賬號已從其他位置登錄，請咨詢代理商了解詳情。".decode(LANG_CODE)

GAME_CLOSE_TIPS = "遊戲服務因進行維護即將關閉，我們將盡快重新開啟服務，詳情請留意網站公告。".decode(LANG_CODE)
MAINTAIN_TIPS = "系統正在維護中，請稍后再進。".decode(LANG_CODE)