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

REG_TIPS_ALREADY_LOGON = "Đã Đăng Nhập .".decode(LANG_CODE)
REG_TIPS_EMPTY_ACCOUNT_PASSWD = "Tài khoản và mật khẩu rỗng.".decode(LANG_CODE)
REG_TIPS_INVALID_ACCOUNT = "Tài khoản không hợp lệ (Chữ cái bắt đầu, gồm 4-18 chữ Hoa/Thường, số, dấu gạch dưới).".decode(LANG_CODE)
REG_TIPS_INVALID_PASSWD = "Mật khẩu không hợp lệ (Bao gồm 6-20 ký tự ).".decode(LANG_CODE)
REG_TIPS_ACCOUNT_EXIST = "Tài khoản đã tồn tại, xin nhập lại.".decode(LANG_CODE)


LOGIN_TIPS_INVALID_ACCOUNT_PASSWD = "Tài khoản hoặc mật khẩu không đúng, xin nhập lại.".decode(LANG_CODE)
LOGIN_TIPS_ALREADY_LOGON = "Tài khoản đã đăng nhập.".decode(LANG_CODE)
LOGIN_TIPS_TIMEOUT = "Tài khoản lố giờ hoặc không hợp lệ, xin đăng nhập lại.".decode(LANG_CODE)
LOGIN_TIPS_INVALID_ACCOUNT = "Đăng nhập thất bại, tài khoản đã bị đóng băng, xin liên hệ người quản lý.".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENABLE_GAME = "Không có quyền vào Game, xin liên hệ đại lý.".decode(LANG_CODE)
LOGIN_TIPS_NOT_ENOUGH_TRIAL = "Người chơi thử quá nhiều, xin thử lại sau.".decode(LANG_CODE)

LOGIN_TIPS_LOGIN_INTERNAL_ERROR = "Hệ thống Hoàng Kim Thế Kỹ đang bảo trì, xin thử lại sau.".decode(LANG_CODE)

TRANSFER_TIPS_NOT_ENOUGH = "Không đủ xu, xin nạp hoặc chỉnh nhỏ số xu chuyển khoản.".decode(LANG_CODE)
TRANSFER_TIPS_INTERNAL_ERROR = "Hệ thống Tiền xu đang bảo trì, xin thử lại sau.".decode(LANG_CODE)
TRANSFER_TIPS_ALREADY_DO = "Đang tiến hành chuyển khoản, xin đợi.".decode(LANG_CODE)

OLD_PASSWORD_NOT_MATCH = "Sai Mật Khẩu, hãy nhập lại.".decode(LANG_CODE)

DISCONNECTED_TIPS_LONG_IDLE = "Bạn hoãn quá lâu, hãy đăng nhập lại.".decode(LANG_CODE)
DISCONNECTED_TIPS_NORMAL = "Đứt kết nối, xin kiểm tra và đăng nhập lại.".decode(LANG_CODE)
DISCONNECTED_TIPS_CLOSE_SERVER = "Hệ thống bảo trì, thử lại sau.".decode(LANG_CODE)
DISCONNECTED_TIPS_FREEZE = "Tài khoản bị khóa, liên hệ đại lý.".decode(LANG_CODE)
DISCONNECTED_TIPS_REPEAT_LOGIN = "TK đăng nhập ở máy khác, liên hệ đại lý.".decode(LANG_CODE)

GAME_CLOSE_TIPS = "Để tiến hành bảo trì nên server sẽ đóng, chúng tôi sẽ mở lại trong thời gian nhanh nhất, hãy để ý bảng thông báo.".decode(LANG_CODE)
MAINTAIN_TIPS = "Đang bảo trì, thử lại sau.".decode(LANG_CODE)