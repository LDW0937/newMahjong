/**
  项目js入口,初始化所有插件

*/

layui.define(['layer','form'],function(exports){
    var layer = layui.layer,
        form  = layui.form();


    layer.msg('hello,world!');

    exports('index',{});

});