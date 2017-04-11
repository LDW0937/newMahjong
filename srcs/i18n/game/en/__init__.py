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

REG_TIPS_ALREADY_LOGON = "Logon already.".decode(LANG_CODE)
REG_TIPS_EMPTY_ACCOUNT_PASSWD = "Account/Password can't be empty!".decode(LANG_CODE)
REG_TIPS_INVALID_ACCOUNT = "Invalid account name (The account name must be between 4-18 characters,start with letters(a-z),contains letters,numbers and underscore).".decode(LANG_CODE)
REG_TIPS_INVALID_PASSWD = "Invalid password (The password length must be between 6-20 characters).".decode(LANG_CODE)
REG_TIPS_ACCOUNT_EXIST = "Account name already exists, please input again.".decode(LANG_CODE)


LOGIN_TIPS_INVALID_ACCOUNT_PASSWD = "Account name or password incorrect, please input again.".decode(LANG_CODE)
LOGIN_TIPS_ALREADY_LOGON = "This account is logged.".decode(LANG_CODE)
LOGIN_TIPS_TIMEOUT = "Login time out, please login again.".decode(LANG_CODE)
LOGIN_TIPS_INVALID_ACCOUNT = "Login failed, this account is locked, please contact our CS agent.".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENABLE_GAME = "You don't have right to login this game, please contact our agent。".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENOUGH_TRIAL = "Too many trail player, please retry later.".decode(LANG_CODE)

LOGIN_TIPS_LOGIN_INTERNAL_ERROR = "Operator system is under maintenance, please try again later.".decode(LANG_CODE)

TRANSFER_TIPS_NOT_ENOUGH = "You don't have enough amount, please deposit to your account or turn down transfer amount.".decode(LANG_CODE)
TRANSFER_TIPS_INTERNAL_ERROR = "Wallet system is under maintenance, please try again later.".decode(LANG_CODE)
TRANSFER_TIPS_ALREADY_DO = "Transferring, please wait".decode(LANG_CODE)

OLD_PASSWORD_NOT_MATCH = "The current password is incorrect, please enter again.".decode(LANG_CODE)

DISCONNECTED_TIPS_LONG_IDLE = "You did not do for long time operation, is disconnected, please login again.".decode(LANG_CODE)
DISCONNECTED_TIPS_NORMAL = "Network disconnected, please check and re-login.".decode(LANG_CODE)
DISCONNECTED_TIPS_CLOSE_SERVER = "Our system for maintenance, temporarily closed, please try again later.".decode(LANG_CODE)
DISCONNECTED_TIPS_FREEZE = "Your account has been frozen administrator, please consult the agent know details please.".decode(LANG_CODE)
DISCONNECTED_TIPS_REPEAT_LOGIN = "Your login account has from other location, please consult the agent for details.".decode(LANG_CODE)

GAME_CLOSE_TIPS = "Our system is under maintenance, please try again later!".decode(LANG_CODE)
MAINTAIN_TIPS = "Our system is under maintenance, please try again later.".decode(LANG_CODE)