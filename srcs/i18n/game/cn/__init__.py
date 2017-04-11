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

REG_TIPS_ALREADY_LOGON = "已登录。".decode(LANG_CODE)
REG_TIPS_EMPTY_ACCOUNT_PASSWD = "账号和密码不能为空。".decode(LANG_CODE)
REG_TIPS_INVALID_ACCOUNT = "账号不合法（必须为字母开头，总长度4-18的大小写字母、数字、下划线）。".decode(LANG_CODE)
REG_TIPS_INVALID_PASSWD = "密码不合法（必须为总长度6-20的合法字符）。".decode(LANG_CODE)
REG_TIPS_ACCOUNT_EXIST = "账号已存在，请重新输入。".decode(LANG_CODE)


LOGIN_TIPS_INVALID_ACCOUNT_PASSWD = "账号或密码不正确，请重新输入。".decode(LANG_CODE)
LOGIN_TIPS_ALREADY_LOGON = "账号已登录。".decode(LANG_CODE)
LOGIN_TIPS_TIMEOUT = "登录超时或不合法，请重新进入游戏。".decode(LANG_CODE)
LOGIN_TIPS_INVALID_ACCOUNT = "登录失败，账号已被冻结，请联系管理员。".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENABLE_GAME = "无权限进入本游戏，请联系代理商开通权限。".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENOUGH_TRIAL = "试玩人数过多，请稍候再试。".decode(LANG_CODE)

LOGIN_TIPS_LOGIN_INTERNAL_ERROR = "运营商系统正在维护中，请稍后再试。".decode(LANG_CODE)

TRANSFER_TIPS_NOT_ENOUGH = "钱包余额不足，请充值或调小转账金额。".decode(LANG_CODE)
TRANSFER_TIPS_INTERNAL_ERROR = "钱包系统正在维护中，请稍后再试。".decode(LANG_CODE)
TRANSFER_TIPS_ALREADY_DO = "正在转账处理中，请稍候。".decode(LANG_CODE)

OLD_PASSWORD_NOT_MATCH = "原密码不正确，请重新输入。".decode(LANG_CODE)

DISCONNECTED_TIPS_LONG_IDLE = "你因长时间未做操作，被断开连接，请重新登录。".decode(LANG_CODE)
DISCONNECTED_TIPS_NORMAL = "网络中断，请检查网络并重新进入游戏。".decode(LANG_CODE)
DISCONNECTED_TIPS_CLOSE_SERVER = "系统因进行维护暂已关闭，请稍后再进。".decode(LANG_CODE)
DISCONNECTED_TIPS_FREEZE = "你的账号已被管理员冻结，请咨询代理商了解详请。".decode(LANG_CODE)
DISCONNECTED_TIPS_REPEAT_LOGIN = "你的账号已从其它位置登录，请咨询代理商了解详情。".decode(LANG_CODE)

GAME_CLOSE_TIPS = "游戏服务因进行维护即将关闭，我们将尽快重新开启服务，详情请留意网站公告。".decode(LANG_CODE)
MAINTAIN_TIPS = "系统正在维护中，请稍后再试。".decode(LANG_CODE)