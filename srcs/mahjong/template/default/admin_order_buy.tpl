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
              <form class='form-horizontal group-border-dashed' action="{{info['submitUrl']}}" method='POST' id='J_Form' onSubmit='return false'>
                     <div class="form-group">
                          <label class="col-sm-5 control-label">卖卡方:</label>
                          <div class="col-sm-6">
                                <input type="text" style='width:250px;float:left' id="parentAccount" name="parentAg" value="{{info['parentAccount']}}" class="form-control">
                          </div>
                     </div>  

                     <div class="form-group">
                          <label class="col-sm-5 control-label">备注信息:</label>
                          <div class="col-sm-6">
                                <textarea name='note' style='width:350px;height:100px;resize:none' class='form-control'></textarea>
                          </div>
                     </div>           

                     <div class="form-group">
                          <label class="col-sm-5 control-label">密码:</label>
                          <div class="col-sm-6">
                                <input type='password' name='passwd' style='width:250px;float:left' data-rules="{required:true}" class='form-control' />
                          </div>
                     </div>

                     <div class="modal-footer" style="text-align:center">
                         <button type="submit" class="btn btn-sm btn-primary">申请充值</button>
                         <button type="button" class="btn btn-sm btn-primary" name="backid" id="backid">返回</button>
                     </div>
              </form>
         </div>
    </div>
</div>
<script type="text/javascript">
    $('#J_Form').submit(function(){
          formAjax($(this).attr("action"), $(this).attr("method"), $(this).serialize(),'正在提交订单...');
    });

    $('#backid').click(function(){
        window.location.href="{{info['backUrl']}}";
   });
</script>
%rebase admin_frame_base