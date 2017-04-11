<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" />
    <meta name="renderer" content="webkit|ie-comp|ie-stand">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <meta name="keywords" content="scclui框架">
    <meta name="description" content="scclui为轻量级的网站后台管理系统模版。">
    <title>{{lang.MAHJONG_TITLE_TXT}}</title>
    
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/css/sccl.css">
    <link rel="stylesheet" type="text/css" href="{{info['STATIC_ADMIN_PATH']}}/skin/blue/skin.css" id="layout-skin"/>
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.css">
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/lib/jquery-1.9.0.min.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.js"></script>
  </head>
  
  <body>
    <div class="layout-admin">
        %include admin_header
        <aside class="layout-side">
            <ul class="side-menu"></ul>
        </aside>
        
        <div class="layout-side-arrow"><div class="layout-side-arrow-icon"><i class="icon-font">&#xe60d;</i></div></div>
        
        <section class="layout-main">
            <div class="layout-main-tab">
                <button class="tab-btn btn-left"><i class="icon-font">&#xe60e;</i></button>
                <nav class="tab-nav">
                    <div class="tab-nav-content">
                        <a href="javascript:;" class="content-tab active" data-id="home.html">首页</a>
                    </div>
                </nav>
                <button class="tab-btn btn-right"><i class="icon-font">&#xe60f;</i></button>
            </div>
            <div class="layout-main-body">
                <iframe class="body-iframe" name="iframe0" width="100%" height="99%" src="{{info['ADMIN_DEFAULT_PAGE']}}" frameborder="0" data-id="home.html" seamless></iframe>
            </div>
        </section>
        <div class="layout-footer">{{lang.COPY_RIGHT_TXT}}</div>
    </div>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/sccl.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/sccl-util.js"></script>
    <script type="text/javascript">
        /*
          初始化加载
        */
        $(function(){
            /*获取皮肤*/

            /*菜单json*/
            var menu = [
                            {"id":"1","name":"主菜单","parentId":"0","url":"","icon":"","order":"1","isHeader":"1",
                                    "childMenus":[
                                            {"id":"3","name":"权限管理","parentId":"1","url":"","icon":"&#xe604;","order":"1","isHeader":"0",
                                                        "childMenus":[
                                                                {"id":"4","name":"添加模块","parentId":"3","url":"test1.html","icon":"","order":"1","isHeader":"0","childMenus":""},
                                                                {"id":"5","name":"模块列表","parentId":"3","url":"test2.html","icon":"","order":"1","isHeader":"0","childMenus":""}
                                            ]},

                                            {"id":"6","name":"代理管理","parentId":"1","url":"","icon":"&#xe602;","order":"1","isHeader":"0",
                                                        "childMenus":[
                                                                {"id":"7","name":"代理列表","parentId":"6","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""}
                                            ]},                                            

                                            {"id":"30","name":"会员管理","parentId":"1","url":"","icon":"&#xe602;","order":"1","isHeader":"0",
                                                        "childMenus":[
                                                                {"id":"7","name":"会员列表","parentId":"30","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""},

                                                                {"id":"8","name":"会员查询","parentId":"30","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""},

                                                                {"id":"9","name":"实时在线","parentId":"30","url":"/admin/member/curOnline","icon":"","order":"1","isHeader":"0","childMenus":""}
                                            ]},

                                            {"id":"20","name":"线上充值","parentId":"1","url":"","icon":"&#xe602;","order":"1","isHeader":"0",
                                                        "childMenus":[
                                                                {"id":"21","name":"购买房卡","parentId":"7","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""},                                                          {"id":"22","name":"购买房卡记录","parentId":"7","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""},

                                                                  {"id":"23","name":"售卖房卡记录","parentId":"7","url":"home3.html","icon":"","order":"1","isHeader":"0","childMenus":""}
                                             ]}
                                ]},
                            
                            {"id":"2","name":"数据统计","parentId":"0","url":"","icon":"","order":"2","isHeader":"1",
                                "childMenus":[
                                    {"id":"9","name":"日登录人数","parentId":"2","url":"","icon":"","order":"1","isHeader":"0","childMenus":""},
                                    {"id":"10","name":"多级","parentId":"2","url":"","icon":"","order":"1","isHeader":"0",
                                        "childMenus":[
                                            {"id":"11","name":"一级","parentId":"10","url":"","icon":"","order":"1","isHeader":"0","childMenus":""},
                                            {"id":"12","name":"一级","parentId":"10","url":"","icon":"","order":"1","isHeader":"0","childMenus":
                                                [
                                                    {"id":"13","name":"二级","parentId":"12","url":"","icon":"","order":"1","isHeader":"0","childMenus":""},
                                                    {"id":"14","name":"二级","parentId":"12","url":"","icon":"","order":"1","isHeader":"0","childMenus":[
                                                            {"id":"15","name":"三级","parentId":"14","url":"","icon":"","order":"1","isHeader":"0",
                                                                "childMenus":""
                                                            },
                                                            {"id":"16","name":"三级","parentId":"14","url":"","icon":"","order":"1","isHeader":"0",
                                                                "childMenus":[
                                                                        {"id":"17","name":"四级","parentId":"16","url":"","icon":"","order":"1","isHeader":"0","childMenus":""},
                                                                        {"id":"18","name":"四级","parentId":"16","url":"","icon":"","order":"1","isHeader":"0","childMenus":""}
                                                                 ]}
                                                            ]}
                                                ]}
                                        ]}
                                ]}
            ];
                        
            initMenu(menu,$(".side-menu"));
            $(".side-menu > li").addClass("menu-item");
            
            /*获取菜单icon随机色*/
            //getMathColor();
        }); 
    </script>
  </body>
</html>
