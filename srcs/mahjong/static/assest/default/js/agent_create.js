$(function(){
    $('#agentCreate').bootstrapValidator({
         message: '无效值',

         fields: {/*验证：规则*/
             account: {//验证input项：验证规则
                 message: '代理账号无效',
                
                 validators: {
                     notEmpty: {//非空验证：提示消息
                         message: '代理账号不能为空'
                     },
                     stringLength: {
                         min: 6,
                         max: 16,
                         message: '代理账号长度必须在6到16之间'
                     },
                     regexp: {
                         regexp: /^[a-zA-Z0-9_]+$/,
                         message: '代理账号由数字字母下划线组成'
                     }
                 }
             },
             passwd: {
                 message:'密码无效',
                 validators: {
                     notEmpty: {
                         message: '密码不能为空'
                     },
                     stringLength: {
                         min: 6,
                         max: 16,
                         message: '密码长度必须在6到16之间'
                     },
                 }
             },             

             comfirPasswd: {
                 message:'确认密码无效',
                 validators: {
                     notEmpty: {
                         message: '确认密码不能为空'
                     },
                     
                     stringLength: {
                         min: 6,
                         max: 16,
                         message: '密码长度必须在6到16之间'
                     },
                     identical: {//相同
                         field: 'passwd', //需要进行比较的input name值
                         message: '两次密码不一致'
                     },
                 }
             },
         }
     }).on('success.form.bv', function(e) {//点击提交之后
         e.preventDefault();

         var $form = $(e.target);

         var bv = $form.data('bootstrapValidator');

         var logTxt = '正在创建...';
         formAjax($(this).attr("action"), $(this).attr("method"), $(this).serialize(),logTxt);
     });
});