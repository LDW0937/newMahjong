<script type="text/javascript" src="{{info['STATIC_ADMIN_PATH']}}/js/agent_create.js"></script>
<div class="definewidth" role="form">
    <div class='header definewidth'>
        <h3>
          <span class="">
              %if info.get('title',None):
                  {{info['title']}}
              %end
          </span>
        </h3>
    </div>
</div>

<form class='form-horizontal group-border-dashed' action="{{info['submitUrl']}}" method='POST' id='agentCreate'>
       <input type='hidden' name='parentAg' value="{{info['parentAg']}}" />
       <div class="form-group">
            <label class="col-sm-5 col-xs-10 control-label">代理账号:</label>
            <div class="col-sm-6 col-xs-12">
                  <input type='text' name='account' class='input' data-rules="{required:true}">
            </div>
       </div>

       <div class="form-group">
            <label class="col-sm-5 col-xs-10 control-label">密码:</label>
            <div class="col-sm-6 col-xs-12">
                  <input type='password' name='passwd' class='input' data-rules="{required:true}">
            </div>
       </div>

       <div class="form-group">
            <label class="col-sm-5 col-xs-10 control-label">确认密码:</label>
            <div class="col-sm-6 col-xs-12">
                  <input type='password' name='comfirPasswd' class='input' data-rules="{required:true}">
            </div>
       </div>       
       %if  info['aType'] == '0':
       <div class="form-group">
            <label class="col-sm-5 col-xs-10 control-label">是否允许创建下级代理:</label>
            <div class="col-sm-6 col-xs-10">
                  <input type='radio' name='isCreate' value='1' checked='' style='margin-left:20px;' class="">&nbsp;是
                  <input type='radio' name='isCreate' value='0' style='margin-left:20px;' class="">&nbsp;否
            </div>
       </div>
       %end

       <div class="modal-footer" style="text-align:center">
           <button type="submit" class="btn btn-sm btn-xs btn-primary btn-mobile">创建</button>
           <button type="button" class="btn btn-sm btn-xs btn-primary btn-mobile" name="backid" id="backid">返回</button>
       </div>
</form>
<script type="text/javascript">
    $('#backid').click(function(){
        window.location.href="{{info['backUrl']}}";
   });
</script>
%rebase admin_frame_base