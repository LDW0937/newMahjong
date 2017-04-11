<div class="cl-mcont">
  <div class="block">
            <div class="header">              
              <h3>
                %if info.get('title',None):
                  {{info['title']}}
                %end
              </h3>
            </div>
            <div class="content">
                <table id="memberOLtable" class="table table-bordered table-hover"></table>
                <span id='refresh_time' style='position:relative;top:10px;left:5px'>
                         距离刷新时间:<i class='countTime' style='color:red'></i>
                </span>
            </div>
  </div>
</div>
<script type="text/javascript">
  $('#memberOLtable').bootstrapTable({
            method: 'get',
            url: '{{info["listUrl"]}}',
            contentType: "application/json",
            datatype: "json",
            cache: false,
            checkboxHeader: true,
            striped: true,
            pagination: true,
            pageSize: 24,
            pageList: [24, 48, 100, 'All'],
            search: true,
            showColumns: true,
            showRefresh: true,
            minimumCountColumns: 2,
            clickToSelect: true,
            smartDisplay: true,
            //sidePagination : "server",
            queryParams:getSearchP,
            responseHandler:responseFun,
            //onLoadError:responseError,
            showExport:true,
            exportTypes:['excel', 'csv', 'pdf', 'json'],
            //exportOptions:{fileName: "{{info['title']}}"+"_"+ new Date().Format("yyyy-MM-dd")},
            columns: [
            {
                field: 'memberAccount',
                title: '会员账号',
                align: 'center',
                valign: 'middle'
            },{
                field: 'id',
                title: '会员ID',
                align: 'center',
                valign: 'middle',
            },{

                field: 'credit',
                title: '信用余额',
                align: 'center',
                valign: 'middle'
            },{
                field: 'channel_name',
                title: "所在游戏",
                align: 'center',
                valign: 'middle'
            },{
                field: 'server_tag',
                title: '服务器标识',
                align: 'center',
                valign: 'middle',
            },{
                field: 'client_type',
                title: '客户端类型',
                align: 'center',
                valign: 'middle',
            },{
                field: 'login_date',
                title: '登录时间',
                align: 'center',
                valign: 'middle',
            },{
                field: 'login_ip',
                title: '登录IP',
                align: 'center',
                valign: 'middle'
            },{
                field: 'op',
                title: '操作',
                align: 'center',
                valign: 'middle',
            }]
});

//获得返回的json 数据
function responseFun(res){
    //刷新表格
    timerTick = setTimeout('refreshTable();', 1000);
    return res;
}

//定义列操作
function getSearchP(p){
    gameSelect = $("#gameSelect").val();
    channelSelect   = $("#channelSelect").val();
    userId = $("#userId").val();
    curOnlineType = $("#curOnlineType").val();

    sendParameter = p;

    sendParameter['gameId'] = gameSelect;
    sendParameter['channelId']  = channelSelect;
    sendParameter['userId'] = userId;
    sendParameter['curOnlineType'] = curOnlineType;

    return sendParameter;

}

</script>
%rebase admin_frame_base