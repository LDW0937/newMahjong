<div class="cl-mcont">
    <div class='block'>
         <div class='header'>
             <h3>
             %if info.get('title',None):
               {{info['title']}}
             %end
           </h3>
         </div>
         <div class='content'>
                <form class="form-horizontal group-border-dashed" action="{{info['searchUrl']}}" method="get">  
                    <input type='text' name='startDate' id='startPick' value="{{info['startDate']}}" placeholder="开始日期" style='width:150px;height:28px'/>&nbsp;&nbsp;
                    <input type='text' name='endDate' id='endPick' placeholder="结束日期" value="{{info['endDate']}}" style='width:150px;height:28px'>&nbsp;&nbsp;
                    <button type="submit" class="btn btn-sm btn-primary">
                        <i class='glyphicon glyphicon-search'></i> 查询</button>&nbsp;&nbsp;
                    <!-- 统计数据 -->
                    <span style='margin-left:50px;' class='totalRoomCard'></span>
                </form>
            <table id='roomCardTable' class="table table-bordered table-hover definewidth m10" ></table>
        </div>
    </div>
</div>
<script type="text/javascript">
  $("#roomCardTable").bootstrapTable({
            url: "{{info['tableUrl']}}",
            method: 'get',
            pagination: true,
            pageSize: 15,
            search: true,
            showRefresh: true,
            pageList: [15, 25],
            responseHandler:responseFun,
            columns: [{
                field: 'cardNums',
                sortable: true,
                title: '售卡数(张)'
            },{
                field: 'applyAccount',
                title: '买卡方'
            },{
                field: 'saleAccount',
                title: '卖卡方'
            }, {
                field: 'status',
                title: '订单状态',
                formatter:status
            },{
                field: 'finishDate',
                sortable: true,
                title: '系统确认时间'
            },{
                field: 'op',
                title: '操作',
                formatter:getOp
            }],

            //注册加载子表的事件。注意下这里的三个参数！
            onExpandRow: function (index, row, $detail) {
                console.log(index,row,$detail);
                InitSubTable(index, row, $detail);
            }
  });

function status(value,row,index){
    eval('var rowobj='+JSON.stringify(row))
    var statusstr = '';
    if(rowobj['status'] == '0'){
        statusstr = '<span class="label label-danger">卖卡方未确认</span>';
    }else if(rowobj['status'] == '1'){
        statusstr = '<span class="label label-success">卖卡方已确认</span>';
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
          var str = JSON.stringify({orderNo : rowobj['orderNo']});
          var cStr = str.replace(/\"/g, "@");
          var param = rowobj['orderNo'] ;
          if(op['url'] == '/admin/roomCard/info')
          {     
                var contentUrl = op['url']+'?orderNo='+param
                opList.push(String.format("<a href=\"#\" class=\"btn btn-primary btn-sm\" onclick=\"orderDialog(\'{0}\')\"><i class=\"glyphicon glyphicon-edit\"> {1} </i></a> ",contentUrl, op['txt']));
          }
      }
      return opList.join('');
}

//获得返回的json 数据
function responseFun(res){
    return res
}
</script>
%rebase admin_frame_base