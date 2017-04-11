
layui.use(['layer','element','util'], function(){
        var element = layui.element(),
            layer   = layui.layer,
            $       = layui.jquery,
            util    = layui.util; //导航的hover效果、二级菜单等功能，需要依赖element模块

        // 分辨率小于1024  使用内部工具组件
        if($(window).width() < 1024) {
            util.fixbar({
                bar1: '&#xe602;'
                ,css: {right:10, bottom:10}
                ,click: function(type){
                    if(type === 'bar1'){
                        //iframe层
                        layer.open({
                            type: 1,                        // 类型
                            title: false,                   // 标题
                            offset: 'l',                    // 定位 左边
                            closeBtn: 0,                    // 关闭按钮
                            anim: 0,                        // 动画
                            shadeClose: true,               // 点击遮罩关闭
                            shade: 0.8,                     // 半透明
                            area: ['150px', '100%'],        // 区域
                            skin: 'my-mobile',              // 样式
                            content: $('body .my-side').html() // 内容
                        });
                    }
                    element.init();
                }
            });
        }

        //监听导航(side)点击切换页面
        element.on('nav(side)', function(elem){
            var src = elem.children('a').attr('href-url');
            if(src != null && src != ''){
                $('#iframe').attr('src',src);
            }
            layer.msg(elem.text());
        });


});