/**
    gulp 构建项目后台
    david 2017-02-27
*/
'use stice'
var gulp  =  require('gulp');

//引入组件
var path = require('path'),
    fse  = require('fs-extra');

//获取当前文件路径
var PWD = process.env.PWD || process.cwd();

gulp.task('init',function(){

     var dirs = [
                        'i18n',                                     // 语言包
                        'server_common',                            // 公共文件
                        'paste',                                    // paste服务器
                        'fish_web',                                 // 项目入口目录
                        'fish_web/admin',                           // 后台应用目录
                        'fish_web/common',                          // 后台通用目录
                        'fish_web/template',                        // 后台模板目录
                        'fish_web/template/default',                // 后台模板目录
                        'fish_web/static',                          // 静态资源文件夹目录
                        'fish_web/static/assest',                   // 静态资源文件夹子目录
                        'fish_web/static/assest/layui/'             // layui框架
     ];

     dirs.forEach(function(item,index){

            fse.mkdirSync(path.join(PWD+'/'+item));
     });

     var template = '#-*- coding:utf-8 -*- \
                     #!/usr/bin/python\
                     """\
                        Author:$Author$\
                        Date:$Date$\
                        Revision:$Revision$\
                        Description:\
                            this is Description\
                     """';

     fse.writeFileSync(path.join(PWD+'/index.py'),template);
     fse.writeFileSync(path.join(PWD+'/bottle_redis.py'),'');
     fse.writeFileSync(path.join(PWD+'/bottle_session.py'),'');
});