<script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/refreshDateInit.js"></script>
<div class="cl-mcont">
  <div class="block">
            <div class="header bordered-bottom bordered-themesecondary" id="crumb">
                %if info.get('title', None):
                <i class="widget-icon fa fa-tags themesecondary"></i>
                <span class="widget-caption themesecondary" id="subTitle">{{info['title']}}</span>
                %end
            </div>
            <div class="content">
                %include original_search_bar
                <table id="dataTable" class="table table-bordered table-hover"></table>
            </div>
  </div>
</div>

<script type="text/javascript">

var firstDate=new Date();
firstDate.setDate(firstDate.getDate()-6);
$('#pick-date-start').val(firstDate.Format("yyyy-MM-dd"));
$('#pick-date-end').val(new Date().Format("yyyy-MM-dd"));

function initTable(){
    /**
      *表格数据
    */
    var editId;        //定义全局操作数据变量
    var isEdit;
    startDate = $("#pick-date-start").val();
    endDate   = $("#pick-date-end").val();
    $('#dataTable').bootstrapTable({
          method: 'get',
          url: '{{info["listUrl"]}}',
          contentType: "application/json",
          datatype: "json",
          cache: true,
          checkboxHeader: true,
          striped: true,
          pagination: true,
          pageSize: 24,
          pageList: [24, 48, 100,'All'],
          queryParamsType:'',
          sidePagination:"server",
          showColumns: true,
          minimumCountColumns: 2,
          clickToSelect: true,
          //smartDisplay: true,
          responseHandler:responseFun,
          //onLoadError:responseError,
          queryParams:getSearchP,
          //sortOrder: 'asc',
          //sortable: true,                     //是否启用排序
          showExport:true,
          exportTypes:['excel', 'csv', 'pdf', 'json'],
          // exportOptions:{fileName: "{{info['title']}}"+"_"+ new Date().Format("yyyy-MM-dd")},
          columns: [
          {
              field: 'date',
              title: '日期',
              align: 'center',
              valign: 'middle',
              sortable: true,
          },{
              field: 'login',
              title: '登陆人数(去重)',
              align: 'center',
              valign: 'middle',
              sortable: true,
          },{
              field: 'op',
              title: '操作',
              align: 'center',
              valign: 'middle',
              sortable: true
          }]
    });


        function getColorCredit(value,row,index) {
            if( parseInt(value) > 0)
                infoStr = String.format("<span style=\"color:red;\">+{0}</span>", value);
            else
                infoStr = String.format("<span style=\"color:green;\">{0}</span>", value);
            return [
                infoStr
            ].join('');
        }

        function getColorWithDraw(value,row,index) {
            infoStr = String.format("<span style=\"color: #6600FF;\">{0}</span>", value);
            return [
                infoStr
            ].join('');
        }


          //前台查询参数
        
        function getSearchP(p){
            // account = $("#account").val();
            // member_level = $('#member_level').val();
            // member_status = $("#member_status").val();
            // userId = $("#userId").val();
            startDate = $("#pick-date-start").val();
            endDate   = $("#pick-date-end").val();

            sendParameter = p;
            sendParameter['startDate'] = startDate;
            sendParameter['endDate']  = endDate;
            // sendParameter['member_level'] = member_level;
            // sendParameter['member_status']  = member_status;
            // sendParameter['account']  =account;
            // sendParameter['userId'] = userId;

            return sendParameter;
          }

        //获得返回的json 数据
        function responseFun(res){
            return {"rows": res.result,
                "total": res.total};
        }

        function responseError(status) {
            location.reload();
        }
}

</script>
%rebase admin_frame_base

