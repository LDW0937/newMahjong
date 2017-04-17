<div class="cl-mcont">
<div class="block">
          <div class="header">
                %if info.get('title', None):
                    <i class="widget-icon fa fa-tags themesecondary"></i>
                    <span class="widget-caption themesecondary">{{info['title']}}</span>
                %end
          </div>
          <div class="content">
             %if message:
              <div class='errorMsg' style='position:relative;left:25%;color:red;'>
                      {{message}}
              </div>
             %end
             <form class="form-horizontal group-border-dashed" id='changeSelfPwdForm' action="{{info['submitUrls']}}" method="post" style="border-radius: 0px;">
              <div class="form-group">
                <label class="col-sm-3 control-label">{{lang.INPUT_LABEL_OLD_PASSWD_TXT}}</label>
                <div class="col-sm-6">
                  <input type="password" style='width:450px;float:left'id="selfPwd" name="selfPwd" class="form-control">
                  <label for='selfPwd' class='hitLabel'>*</label>
                </div>
              </div>

              <div class="form-group">
                <label class="col-sm-3 control-label">{{lang.INPUT_LABEL_PASSWD1_TXT}}</label>
                <div class="col-sm-6">
                  <input type="password" style='width:450px;float:left'id="newPwd" name="newPwd" class="form-control">
                  <label for='newPwd' class='hitLabel'>*</label>
                </div>
              </div>

              <div class="form-group">
                <label class="col-sm-3 control-label">{{lang.INPUT_LABEL_PASSWD2_TXT}}</label>
                <div class="col-sm-6">
                  <input type="password" style='width:450px;float:left'id="comfirmPwd" name="comfirmPwd" class="form-control" />
                  <label for='comfirmPwd' class='hitLabel'>*</label>
                </div>
              </div>

              <div class="modal-footer" style="text-align:center">
                   <button type="submit" class="btn btn-primary">{{lang.BTN_SUBMIT_TXT}}</button>
              </div>
            </form>
          </div>
</div>
</div>
%rebase admin_frame_base
