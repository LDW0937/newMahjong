/**
  * 弹出层确认框
  * @author:ldw
  -----------------------------------------------
*/
function comfirmDialog(url,method,jsonStr){
    var comfirmTxt = '是否确定此操作';

      layer.open({
          title: [
             '麻将后台提醒你',
            'background-color:#204077; color:#fff;'
          ]
          ,anim: 'up'
          ,content:comfirmTxt
          ,btn: ['确认', '取消']
          ,yes:function(index){
            normalAjaxStrData(url,method,jsonStr);
            layer.close(index);
          }
      });
}

/**
  * 弹出层确认框
  * @author:ldw
  -----------------------------------------------
*/
function comfirmServer(url,method,jsonStr){
    var comfirmTxt = '是否确定关闭服务器';

      layer.open({
          title: [
             '麻将后台提醒你',
            'background-color:#204077; color:#fff;'
          ]
          ,anim: 'up'
          ,content:comfirmTxt
          ,btn: ['确认', '取消']
          ,yes:function(index){
            formAjax(url,method,jsonStr,'正在关闭服务器');
            layer.close(index);
          }
      });
}

/**
  * 订单确认弹出层
  * @author:ldw
  -----------------------------------------------
*/
function comfirmOrderDialog(url,method,jsonStr){
   var str = JSON.parse(jsonStr.replace(/\@/g, "\"")),
       orderUrl = '/admin/order/info';

   $.ajax({
        url : orderUrl,
        type : 'GET',
        data : {'isAjax':1,'orderNo':str['orderNo']},
        dataType: "json",//(可以不写,默认)

        success : function(data, statue) {
              var title = "订单号:"+data.orderNo+""
              var orderTxt = '  <p>充值房卡数     : '+data.cardNums+' </p>\
                                <p>申请充值账号   : '+data.rechargeAccount+'</p>\
                                <p>申请时间       : '+data.applyDate+'</p>\
                                <p>备注           : '+data.note+'</p>';
                                
              layer.open({
                  title: [
                     title,
                    'background-color:#204077; color:#fff;'
                  ]          
                  ,anim: 'up'
                  ,content : orderTxt
                  ,btn: ['确认', '取消']
                  ,yes:function(index){
                    normalAjaxStrData(url,method,jsonStr);
                    layer.close(index);
                  }
            });
        }
    });
}

/**
  * 后台首页消息提示框
  * @author:ldw
  -----------------------------------------------
*/
function tipsDialog(nums){

    var content = '<p style="font-size:14px;text-align:center;margin-top:8px">\
                   有<a href="/admin/order/saleOrderPending"><b>&nbsp;'+nums+'</b>&nbsp;</a>条待处理房卡订单</p>';

    layer.open({
          title: [
            '待处理订单消息',
            'background-color:#204077; color:#fff;'
          ]
          ,anim: 'up'
          ,content: content
    });
}

/**
  * 悬空提示操作框
  * @author:ldw
  -----------------------------------------------
*/
function timeTipsDialog(url,time,message){

    layer.open({
          title: [
             '系统提示',
            'background-color:#204077; color:#fff;'
          ]
          ,anim: 'up'
          ,content:message
          ,btn: ['确认', '取消']
          ,yes:function(index){
            location.href = url;
            layer.close(index);
          }
    });
}


function cancelDialog(url,orderNo){

      layer.open({
            content: '是否删除该订单'
            ,btn: ['删除', '取消']
            ,skin: 'footer'
            ,yes: function(index){
              $.ajax({
                  type  :   'POST',
                  url   :   url,//提交的URL
                  data  :   {'orderNo':orderNo}, // 要提交的表单,必须使用name属性
                  dataType:'JSON',

                  success: function (data,statue) {
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

                          default: //错误信息提示,不刷新页面
                              layer.open({
                                content: data.msg
                                ,skin: 'msg'
                                ,time: 2 //2秒后自动关闭
                              });
                      }
                  }
            });
       }
  });
}