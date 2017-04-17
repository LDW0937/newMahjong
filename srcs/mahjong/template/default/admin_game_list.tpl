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
          <div class="table-toolbar" style="float:left">
              <a id="add" href='{{info["createUrl"]}}' class="btn btn-primary">
                  <i class="btn-label fa fa-plus"></i>{{info['addTitle']}}
              </a>
          </div>
          <table id='loadDataTable' class="table table-bordered table-hover table-striped" ></table>
         </div>
    </div>
</div>
<script type="text/javascript">
    /**
      *表格数据
    */
    var editId;        //定义全局操作数据变量
    var isEdit;
    var startDate;
    var endDate;
    $('#loadDataTable').bootstrapTable({
          method: 'get',
          url: "{{info['tableUrl']}}",
          contentType: "application/json",
          datatype: "json",
          cache: false,
          checkboxHeader: true,
          striped: true,
          pagination: true,
          pageSize: 24,
          pageList: [24, 48, 100,'All'],
          search: true,
          showRefresh: true,
          minimumCountColumns: 2,
          clickToSelect: true,
          smartDisplay: true,
          //sidePagination : "server",
          sortOrder: 'desc',
          sortName: 'datetime',
          queryParams:getSearchP,
          responseHandler:responseFunc,
          //onLoadError:responseError,
          showExport:true,
          exportTypes:['excel', 'csv', 'pdf', 'json'],
          //exportOptions:{fileName: "{{info['title']}}"+"_"+ new Date().Format("yyyy-MM-dd")},
          columns: [
          {
              field: 'id',
              title: '游戏ID',
              align: 'center',
              valign: 'middle'
          },{

              field: 'name',
              title: '游戏名称',
              align: 'center',
              valign: 'middle'
          },{
              field: 'web_tag',
              title: 'WEB_TAG',
              align: 'center',
              valign: 'middle'
          },{
              field: 'apk_tag',
              title: 'APK_TAG',
              align: 'center',
              valign: 'middle',
          },{
              field: 'ipa_tag',
              title: 'IPA_TAG',
              align: 'center',
              valign: 'middle',
          }]
      });

        //定义列操作
        function getSearchP(p){
          sendParameter = p;

          sendParameter['startDate'] = startDate;
          sendParameter['endDate']  = endDate;

          startDate = $("#data-pick-start").val();
          endDate   = $("data-pick-end").val();

          return sendParameter;
        }

        function getOp(value,row,index){
            eval('rowobj='+JSON.stringify(row))
            var opList = []
            for (var i = 0; i < rowobj['op'].length; ++i) {
                var op = rowobj['op'][i];
                var str = JSON.stringify({id : rowobj['id']});
                var cStr = str.replace(/\"/g, "@");
                if(op['txt'] == '删除')
                    opList.push(String.format("<a href=\"#\" class=\"btn btn-info\" onclick=\"comfirmDialog(\'{0}\', \'{1}\', \'{2}\')\"><i class=\"fa fa-edit\"> {3} </i></a> ", op['url'], op['method'], cStr, op['txt']));
                else
                    opList.push(String.format("<a href=\"#\" class=\"btn btn-info\" onclick=\"normalAjaxStrData(\'{0}\', \'{1}\', \'{2}\')\"><i class=\"fa fa-edit\"> {3} </i></a> ", op['url'], op['method'], cStr, op['txt']));
            }
            return opList.join('');
        }

        function responseFunc(res){
            if (res.length && res[0].op.length)
                $("#dataTable").bootstrapTable('showColumn', 'op');
            else
                $("#dataTable").bootstrapTable('hideColumn', 'op');

            return res;
        }

        function responseError(status) {
            location.reload();
        }
</script>
%rebase admin_frame_base