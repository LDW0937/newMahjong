<script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/refreshDateInit.js"></script>
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
  
  /**------------------------------------------------
    *  代理操作日志
    *
    -------------------------------------------------
  */
  function initTable() {
    startDate = $("#pick-date-start").val();
    endDate   = $("#pick-date-end").val();
    $('#dataTable').bootstrapTable({
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
          clickToSelect: true,
          //sidePagination : "server",
          sortOrder: 'desc',
          sortName: 'datetime',
          queryParams:getSearchP,
          responseHandler:responseFun,
          //onLoadError:responseError,
          showExport:true,
          exportTypes:['excel', 'csv', 'pdf', 'json'],
          // exportOptions:{fileName: "{{info['title']}}"+"_"+ new Date().Format("yyyy-MM-dd")},
          columns: [
            {
              field: 'date',
              title: '日期',
              align: 'center',
              valign: 'middle'
          },{
              field: 'cardNums',
              title: '售卡总数',
              align: 'center',
              valign: 'middle'
          },{
              field: 'price',
              title: '售卡单价',
              align: 'center',
              valign: 'middle',
             formatter:status,
          },{
              field: 'total',
              title: '总销售额',
              align: 'center',
              valign: 'middle'
          },{

              field: 'giveParent',
              title: '上线占成',
              align: 'center',
              valign: 'middle',
          }]
      });

       function status(value,row,index){
            eval('var rowobj='+JSON.stringify(row))
            var statusstr = '';

            switch(rowobj['loginDesc']){
                case 1:
                   statusstr = '<span class="label label-success">正常</span>';
                   break;
                case 2:
                   statusstr = '<span class="label label-danger">密码错误</span>';
                   break;
                case 3:
                   statusstr = '<span class="label label-danger">证书错误</span>';
                   break;
                case 4:
                   statusstr = '<span class="label label-danger">IP受限制</span>';
                   break;
            }

            return [
                statusstr
            ].join('');
        }
        //定义列操作
        function getSearchP(p){
          startDate = $("#pick-date-start").val();
          endDate   = $("#pick-date-end").val();

          sendParameter = p;

          sendParameter['startDate'] = startDate;
          sendParameter['endDate']  = endDate;

          return sendParameter;
        }

        //获得返回的json 数据
        function responseFun(res){
            data = res
            return data;
        }
}
</script>
%rebase admin_frame_base
