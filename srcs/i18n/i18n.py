#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: $Author$
Date: $Date$
Revision: $Revision$

Description:
    翻译模块
"""

LANGS = {}

def initializeWeb():
    global LANGS
    langModules = __import__('i18n.web', fromlist=['cn', 'tw', 'en'])
    LANGS['CHN'] = langModules.cn
    setattr(LANGS['CHN'], '__code__', 'CHN')
    LANGS['TW'] = langModules.tw
    setattr(LANGS['TW'], '__code__', 'TW')
    LANGS['EN'] = langModules.en
    setattr(LANGS['EN'], '__code__', 'EN')
    LANGS['VN'] = None #langModules.viet
    #setattr(LANGS['VN'], '__code__', 'VN')

def initializeGame():
    global LANGS
    langModules = __import__('i18n.game', fromlist=['cn', 'tw', 'en', 'viet'])
    LANGS['CHN'] = langModules.cn
    LANGS['TW'] = langModules.tw
    LANGS['EN'] = langModules.en
    LANGS['VN'] = langModules.viet

def isValidLang(lang):
    global LANGS
    return lang in LANGS

def getLangInst(lang = 'CHN'):
    global LANGS
    assert lang in LANGS
    return LANGS[lang]
