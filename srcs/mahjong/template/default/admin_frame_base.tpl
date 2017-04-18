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
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/css/style.css">
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/css/bootstrap.css">
    <link rel="stylesheet" href="{{info['STATIC_ADMIN_PATH']}}/js/table/bootstrap-table.min.css" />
    <link rel="stylesheet" type="text/css" href="{{info['STATIC_ADMIN_PATH']}}/skin/qingxin/skin.css" id="layout-skin"/>
    <link rel="stylesheet" type="text/css" href="{{info['STATIC_ADMIN_PATH']}}/js/bootstrap.datetimepicker/css/bootstrap-datetimepicker.min.css" />
    <link rel="stylesheet" type="text/css" href="{{info['STATIC_ADMIN_PATH']}}/js/validate/css/bootstrapValidator.min.css" />
    <link rel="stylesheet" type="text/css" href="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.css" />
        <!-- 弹出层组件 -->
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/layerMobile/layer.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/lib/jquery-1.9.0.min.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/sccl.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/sccl-util.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/table/bootstrap-table.min.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/table/bootstrap-table-zh-CN.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/table/bootstrap-table-export.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/table/tableExport.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/bootstrap.datetimepicker/js/bootstrap-datetimepicker.min.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/bootstrap.datetimepicker/js/bootstrap-datetimepicker.zh-CN.js"></script>
    <script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/validate/js/bootstrapValidator.min.js"></script>
    </head>
    <script type="text/javascript">
        /*
          初始化加载
        */
        $(function(){
                    $('body').on('focus','#pick-date-start',function(){
                            $(".datetime").datetimepicker({
                                    autoclose   : true
                            });
                    });
                    $('body').on('focus','.pickdate',function(){
                        $(".datetime").datetimepicker({
                                autoclose               : true,
                                format                  : 'yyyy-mm-dd hh:ii:ss',
                                todayHighlight          : true,
                                startView               : 2,
                                language                : 'zh-CN'
                        });
                    });

                }); 
    </script>
    <body>
    %include
    </body>
</html>