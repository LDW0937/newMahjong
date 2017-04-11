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
    <title>首页</title>
    
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/layui/css/layui.css">
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.css">
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/css/sccl.css">
    
  </head>
  
  <body class="login-bg">
    <div class="login-box">
        <header>
            <h1>{{lang.MAHJONG_LOGIN_TITLE_TXT}}</h1>
        </header>
        <div class="login-main">
            <form action="/manage/login" class="layui-form" method="post">
                <input name="__RequestVerificationToken" type="hidden" value="">                
                <div class="layui-form-item">
                    <label class="login-icon">
                        <i class="layui-icon"></i>
                    </label>
                    <input type="text" name="userName" lay-verify="userName" autocomplete="off" placeholder="这里输入登录名" class="layui-input">
                </div>
                <div class="layui-form-item">
                    <label class="login-icon">
                        <i class="layui-icon"></i>
                    </label>
                    <input type="password" name="password" lay-verify="password" autocomplete="off" placeholder="这里输入密码" class="layui-input">
                </div>
                <div class="layui-form-item">
                    <div class="login-code-box">
                        <input type="text" class="layui-input" id="code" />
                        <img id="valiCode" src="{{info['vcodeUrl']}}" alt="验证码" />
                    </div>
<!--                     <div class="pull-left login-remember">
                        <label>记住帐号？</label>

                        <input type="checkbox" name="rememberMe" value="true" lay-skin="switch" title="记住帐号"><div class="layui-unselect layui-form-switch"><i></i></div>
                    </div> -->
                    <div class="clear"></div>
                </div>
                <div class="login-code-box" style='text-align:center'>
                    <button class="layui-btn layui-btn-primary" lay-submit="" lay-filter="login">
                        <i class="layui-icon"></i> 登录
                    </button>
                </div>
            </form>        
        </div>
        <footer style='margin-top:10px;'>
            <p>{{lang.COPY_RIGHT_TXT}}</p>
        </footer>
    </div>
    <script src="{{info['STATIC_ADMIN_PATH']}}/layui/layui.js"></script>
    <script src="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.js"></script>
    <script type="text/javascript">
          layer.open({
                    content  : '移动版和PC版不能同时存在同一页面',
                    btn      : '我知道了'
          });
    </script>
  </body>
</html>
