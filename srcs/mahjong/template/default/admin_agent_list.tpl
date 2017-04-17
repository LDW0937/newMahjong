<div class="cl-mcont">
  <div class="block">
            <div class="header bordered-bottom bordered-themesecondary" id="crumb">
                %if info.get('title', None):
                <i class="widget-icon fa fa-tags themesecondary"></i>
                <span class="widget-caption themesecondary" id="subTitle">{{info['title']}}</span>
                %end
                % if info['createAccess'] == '1':
                <span style='float:right;margin-right:10px;'>
                    <a href="{{info['createUrl']}}" class='btn btn-sm btn-primary'>
                        <i class='glyphicon glyphicon-plus'></i> 添加直属代理</a>
                </span>
                %end
            </div>
            <div class="content">
                <table id="agentTable" class="table table-bordered table-hover"></table>
            </div>
  </div>
</div>

<script type="text/javascript">
  $("#agentTable").bootstrapTable({
            url: '{{info["listUrl"]}}',
            method: 'get',
            detailView: {{info['showPlus']}},//父子表

            //sidePagination: "server",
            pagination: true,
            pageSize: 48,
            sortOrder: 'desc',
            sortName: 'regDate',
            pageList: [48, 100],
            columns: [
            {
                field: 'parentAg',
                title: '代理账号',
                align: 'center',
                valign: 'middle',
                sortable: true,
            },{
                field: 'roomCard',
                sortable: true,
                title: '房卡数量'
                align: 'center',
                valign: 'middle',
            },{
                field: 'valid',
                title: '状态',
                align: 'center',
                valign: 'middle',
                sortable: true,
                formatter:status
            },{
                field: 'regDate',
                sortable: true,
                title: '创建时间'
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
        var parentAg = row.parentAg;
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
                    field: 'parentAg',
                    title: '代理名称'
                },{
                    field: 'roomCard',
                    title: '房卡数量'
                },{
                    field: 'valid',
                    title: '状态',
                    formatter:status
                },{
                    field: 'regDate',
                    title: '创建时间'
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

        //定义列操作
        function getSearchP(p){
              sendParameter = p;
              sendParameter['account'] = parentAg;
              return sendParameter;
        }
}

function getOp(value,row,index){
      eval('rowobj='+JSON.stringify(row))
      var opList = []
      for (var i = 0; i < rowobj['op'].length; ++i) {
          var op = rowobj['op'][i];
          var str = JSON.stringify({account : rowobj['parentAg']});
          var cStr = str.replace(/\"/g, "@");
          var param = rowobj['parentAg'] ;
          if(op['url'] == '/admin/ag/del' || op['url'] == '/admin/ag/freeze')
              opList.push(String.format("<a href=\"#\" class=\"btn btn-primary btn-sm btn-xs\" onclick=\"comfirmDialog(\'{0}\', \'{1}\', \'{2}\')\"><i class=\"glyphicon glyphicon-edit\"> {3} </i></a> ", op['url'], op['method'], cStr, op['txt']));
          else
              opList.push(String.format("<a href=\"{0}?account={1}\" class=\"btn btn-primary btn-sm btn-xs\"><i class=\"glyphicon glyphicon-edit\"> {2}</i></a> ", op['url'], param, op['txt']));
      }
      return opList.join('');
}


function status(value,row,index){
    eval('var rowobj='+JSON.stringify(row))
    var statusstr = '';
    if(rowobj['valid'] == '0'){
        statusstr = '<span class="label label-danger">冻结</span>';
    }else if(rowobj['valid'] == '1'){
        statusstr = '<span class="label label-success">有效</span>';
    }

    return [
        statusstr
    ].join('');
}

</script>
%rebase admin_frame_base
