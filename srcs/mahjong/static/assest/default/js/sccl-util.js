/*设置cookie*/
function setCookie(name, value, days){
	if(days == null || days == ''){
		days = 300;
	}
	var exp  = new Date();
	exp.setTime(exp.getTime() + days*24*60*60*1000);
	document.cookie = name + "="+ escape (value) + "; path=/;expires=" + exp.toGMTString();
}

/*获取cookie*/
function getCookie(name) {
	var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
	if(arr = document.cookie.match(reg))
		return unescape(arr[2]); 
	else 
		return null; 
}

/*ajax请求*/
function ajax(url, param, datat, callback) {  
	$.ajax({  
		type: "post",  
		url: url,  
		data: param,  
		dataType: datat,  
		success: function(data){
			callback;
		},  
		error: function () {  
			alert("失败.."); 
		}
	});  
}


function logout(message){
	var message = message || '正在登出..';

  //询问框
  layer.open({
    content: '是否退出系统'
    ,btn: ['确定', '取消']
    ,yes: function(index){
      location.href="/admin/logout";
      layer.close(index);
    }
  });
}


function formAjax(url, method, dataJson, message){
    var message = message || '正在加载...';

    $.ajax({
            type: method,
            url: url,//提交的URL
            data: dataJson, // 要提交的表单,必须使用name属性
            dataType:'JSON',

            beforeSend: function () {
                  layer.open({
                    type: 2
                    ,content: message
                  });
            },

            success: function (data,statue) {
                layer.closeAll();
                reCode = parseInt(data.code);
                switch(reCode){
                    case 0: 
                     layer.open({
                            content: data.msg
                            ,skin:'msg'
                            ,time:4
                            ,function(){
                                location.href = data.jumpUrl
                            }
                     });
                    default: //错误信息提示,不刷新页面
                         layer.open({
                            content: data.msg
                            ,skin: 'msg'
                            ,time: 3 //2秒后自动关闭
                         });
                }
            },

            error : function(){
                 layer.open({
                            content: XMLHttpRequest.status
                            ,skin: 'msg'
                            ,time: 3 //2秒后自动关闭
                  });
                  layer.closeAll();
            }
     });
};