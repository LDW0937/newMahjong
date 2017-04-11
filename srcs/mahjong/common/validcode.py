#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: $Author$
Date: $Date$
Revision: $Revision$

Description:
    验证码模块
"""

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
 
_numbers = ''.join(map(str, range(0, 10))) # 数字
init_chars = _numbers #''.join((_letter_cases, _upper_cases, _numbers))
 
def create_validate_code(size=(115, 39),# modify by ldw 2016/05/03
                         chars=init_chars,
                         mode="RGB",
                         bg_color=(232, 211, 210),
                         fg_color=((0, 0, 0), (255,0,0), (0,255,0), (0,0,255)),
                         point_color=((0, 0, 0), (255,0,0), (0,255,0), (0,0,255),(255,255,0),(0,255,255)),
                         font_size=28,
                         font_type="roboto_bold.ttf",
                         length=4,
                         draw_lines=True,
                         n_line=(2, 3),
                         draw_points=True,
                         point_chance = 5):
    '''
    @todo: 生成验证码图片
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [1]: 验证码图片中的字符串 
    '''
 
    width, height = size # 宽， 高
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔
 
    def get_chars():
        '''生成给定长度的字符串，返回列表格式'''
        return random.sample(chars, length)
 
    def create_lines():
        '''绘制干扰线'''
        line_num = random.randint(*n_line) # 干扰线条数
 
        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            #结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
 
    def create_points():
        '''绘制干扰点'''
        chance = min(100, max(0, int(point_chance))) # 大小限制在[0, 100]

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=random.choice(point_color))
 
    def create_strs():
        '''绘制验证码字符'''
        c_chars = get_chars()
        print font_type, font_size
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize('W')
        x = random.randint(0,5)
        for char in c_chars:
            y = random.randint(0,3)
            draw.text((x, y), char, font=font, fill=random.choice(fg_color))
            x += font_width + random.randint(0,5)

        return ''.join(c_chars)
 
    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()
 
    return img, strs
 
if __name__ == "__main__":
    code_img, digit = create_validate_code()
    code_img.save("validate.jpg", "GIF")
