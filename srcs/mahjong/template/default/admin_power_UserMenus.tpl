<div class="cl-mcont">
  <div class="block">
            <div class="header bordered-bottom bordered-themesecondary" id="crumb">
                %if info.get('title', None):
                <i class="widget-icon fa fa-tags themesecondary"></i>
                <span class="widget-caption themesecondary" id="subTitle">{{info['title']}}</span>
                %end
            </div>
            <div class="content">
                %if info['createAccess']:
                 <a href="{{info['createUrl']}}" class='btn btn-sm btn-primary '>
                            <i class='glyphicon glyphicon-plus'></i> 创建顶级菜单</a>
                 </a>
                 %end
                <table id="table" class="table table-bordered table-hover"></table>
            </div>
  </div>
</div>

<script type="text/javascript">
  $("#table").bootstrapTable({
            url: '{{info["listUrl"]}}',
            method: 'get',
            detailView: {{info['showPlus']}},//父子表
            //sidePagination: "server",
            pagination: true,
            pageSize: 48,
            sortOrder: 'desc',
            sortName: 'regDate',
            pageList: [48, 100],
            columns: [{
                field: 'menu_id',
                title: '菜单ID',
                align: 'center',
                valign: 'middle'
            },{

                field: 'menu_name',
                title: '菜单名称',
                align: 'center',
                valign: 'middle'
            },{

                field: 'menu_child_count',
                title: '子菜单个数',
                align: 'center',
                valign: 'middle'
            },{

                field: 'menu_type',
                title: '是否可见',
                align: 'center',
                valign: 'middle',
                // formatter:isMenus
            },{
                field: 'menu_url',
                title: '菜单URL',
                align: 'center',
                valign: 'middle',
            },{
                field: 'menu_sort',
                title: '菜单排序',
                align: 'center',
                valign: 'middle',
            },{
                field: 'op',
                title: '操作',
                align: 'center',
                valign: 'middle',
                formatter:getOp
            }],

            //注册加载子表的事件。注意下这里的三个参数！
            onExpandRow: function (index, row, $detail) {
                console.log(index,row,$detail);
                InitSubTable(index, row, $detail);
            }
  });


//初始化子表格(无线循环)
function InitSubTable(index, row, $detail) {
        var parentId = row.menu_id;
        var cur_table = $detail.html('<table table-bordered table-hover definewidth></table>').find('table');
        $(cur_table).bootstrapTable({
                url: '{{info["listUrl"]}}',
                method: 'get',
                detailView: {{info['showPlus']}},
                contentType: "application/json",
                datatype: "json",
                cache: false,
                queryParams:getSearchP,
                sortOrder: 'desc',
                sortName: 'regDate',
                pageSize: 15,
                pageList: [15, 25],
                columns: [{
                field: 'menu_id',
                title: '菜单ID',
                align: 'center',
                valign: 'middle'
            },{

                field: 'menu_name',
                title: '菜单名称',
                align: 'center',
                valign: 'middle',
            },{
                field: 'menu_child_count',
                title: '子菜单个数',
                align: 'center',
                valign: 'middle'
            },{

                field: 'menu_type',
                title: '是否可见',
                align: 'center',
                valign: 'middle',
                // formatter:isMenus
            },{
                field: 'menu_url',
                title: '菜单URL',
                align: 'center',
                valign: 'middle',
            },{
                field: 'menu_sort',
                title: '菜单排序',
                align: 'center',
                valign: 'middle',
            },{
                field: 'op',
                title: '操作',
                align: 'center',
                valign: 'middle',
                // formatter:getOp
            }],
                //注册加载子表的事件。注意下这里的三个参数！
                onExpandRow: function (index, row, $detail) {
                    console.log(index,row,$detail);
                    InitSubTable(index, row, $detail);
                }

        });
                //定义列操作
        function getSearchP(p){
              sendParameter = p;
              sendParameter['pid'] = parentId;
              return sendParameter;
        }

}

function isMenus(value,row,index){
    eval('var rowobj='+JSON.stringify(row))
    var statusstr = '';
    if(rowobj['menu_type'] == '0'){
        statusstr = '<span class="label label-success">菜单</span>';
    }else{
        statusstr = '<span class="label label-danger">非菜单</span>';
    }

    return [
        statusstr
    ].join('');
}

function getOp(value,row,index){
    eval('rowobj='+JSON.stringify(row))
    var opList = []
    for (var i = 0; i < rowobj['op'].length; ++i) {
        var op = rowobj['op'][i];
        var str = JSON.stringify({id : rowobj['menu_id']});
        var cStr = str.replace(/\"/g, "@");
        if (op['txt'] == '删除')
            opList.push(String.format("<a href=\"#\" class=\"btn btn-info\" onclick=\"comfirmDialog(\'{0}\', \'{1}\', \'{2}\')\"><i class=\"fa fa-edit\"> {3} </i></a> ", op['url'], op['method'], cStr, op['txt']));
        else
            opList.push(String.format("<a href=\"#\" class=\"btn btn-info\" onclick=\"normalAjaxStrData(\'{0}\', \'{1}\', \'{2}\')\"><i class=\"fa fa-edit\"> {3} </i></a> ", op['url'], op['method'], cStr, op['txt'])); 
    }
    return opList.join('');
}


</script>
%rebase admin_frame_base
