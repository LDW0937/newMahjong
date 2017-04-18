function normalAjax(url, method, dataJson){
  
  $.ajax({
        url : url,
        type : method,
        data : dataJson,
        dataType: "html",//(可以不写,默认)

        success : function(data, statue) {

            $("#mainContent").html(data);
        },

        complete:function(){
            layer.closeAll();
        },

        error : function(XMLHttpRequest, textStatus, errorThrown) {
            // handle the error. 
            var strError = "error:\n" + "XMLHttpRequest.status: " + XMLHttpRequest.status + "\n"+
                            "XMLHttpRequest.readyState: " + XMLHttpRequest.readyState + "\n"+
                            "textStatus: " + textStatus;
            alert(strError);
        }
    });
};


/**
  * normalAjaxStrData
  * @params:
       url :  请求的url地址
           method : 请求方法
           jsonStr : 携带的参数,json格式
           message : 请求等待时的文字信息
  *
*/
function normalAjaxStrData(url, method, jsonStr, message){
    var str = jsonStr.replace(/\@/g, "\"");
    var message = message || '正在加载...';

    formAjax(url, method, JSON.parse(str),message);
};

/**
  * formAjax
  * @params:
        url :  请求的url地址
        method : 请求方法
        jsonStr : 携带的参数,json格式
        message : 请求等待时的文字信息
  *
*/
function formAjax(url, method, dataJson, message){
    var message = message || '正在加载...';

    $.ajax({
            type: method,
            url: url,//提交的URL
            data: dataJson, // 要提交的表单,必须使用name属性
            dataType:'JSON',

            beforeSend: function () {
                  layer.open({ type: 2,content:message});
            },

            success: function (data,statue) {
                layer.closeAll();
                reCode = parseInt(data.code);
                switch(reCode){
                    case 0: 
                        //信息框
                        layer.open({
                            content: data.msg
                            ,btn: '确认'
                            ,yes:function(index){
                                 location.href=data.jumpUrl;
                                 layer.close(index);
                            }
                        });
                        break;
                    
                    case 2://渲染内容模版
                        $('#mainContent').html(data.content);
                        layer.closeAll();
                        break;
                    
                    case 3: //网页直接跳转
                        location.href=data.jumpUrl;
                        break;

                    case 4: //弹框停留页
                        timeTipsDialog(data.jumpUrl,5,data.msg);
                        break;
                        
                    default: //错误信息提示,不刷新页面
                        layer.open({
                          content: data.msg
                          ,skin: 'footer'
                          ,time: 2 //2秒后自动关闭
                        });
                }
            },

            error : function(XMLHttpRequest, textStatus, errorThrown) {
                var strError = "error:\n" + "XMLHttpRequest.status: " + XMLHttpRequest.status + "\n"+
                              "XMLHttpRequest.readyState: " + XMLHttpRequest.readyState + "\n"+
                              "textStatus: " + textStatus;
                alert(strError);
            }
     });
};

String.format = function() {
    if( arguments.length == 0 ) {
    return null; 
    }
    var str = arguments[0];
    for(var i=1;i<arguments.length;i++) {
    var re = new RegExp('\\{' + (i-1) + '\\}','gm');
    str = str.replace(re, arguments[i]);
    }
    return str;
}

Date.prototype.Format = function(fmt)
{ //author: meizz
  var o = {
    "M+" : this.getMonth()+1,                 //月份
    "d+" : this.getDate(),                    //日
    "h+" : this.getHours(),                   //小时
    "m+" : this.getMinutes(),                 //分
    "s+" : this.getSeconds(),                 //秒
    "q+" : Math.floor((this.getMonth()+3)/3), //季度
    "S"  : this.getMilliseconds()             //毫秒
  };   
  if(/(y+)/.test(fmt))
    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
  for(var k in o)
    if(new RegExp("("+ k +")").test(fmt))
  fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
  return fmt;
}