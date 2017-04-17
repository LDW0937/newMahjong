<script type="text/javascript">
    var uploadUrl = "{{info['uploadUrl']}}";
</script>
<style type="text/css">
    .config-table td.table-title{text-align:center;font-size:13px;vertical-align:middle}
</style>
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
             <form class="form-horizontal group-border-dashed" id='gameForm' action="{{info['submitUrl']}}" method="post" style="border-radius: 0px;" enctype="multipart/form-data">
               <table class='table config-table'>
                        <tr>
                          <td width='20%' class='table-title'>游戏创建</td>
                        </tr>
                        <tr>
                              <td class='table-title'>基本设置</td>
                              <td>
                                <table class='table config-table' border='1'>
                                    <tr>
                                         <td class='table-title'>游戏名称</td>
                                         <td>
                                             <input type="text" style='width:250px;float:left' id="name" name="name" class="form-control">
                                             <label for='name' class='hitLabel' style='float:left;line-height:30px'>*</label>
                                         </td>
                                    </tr>                                
                                    <tr>
                                         <td class='table-title'>游戏图标</td>
                                         <td>
                                             <input type="file" style='width:250px;float:left' id="icon_path" name="icon_path" class="form-control">
                                              <br/><br/>
                                              <img src="{{info['icon_path']}}" style='margin:10px;' id='icon_preview' width='160' height='120' />
                                             <input type='hidden' name='file_name' id='file_name' />
                                         </td>
                                    </tr>                                                      
                                </table>
                              </td>
                        </tr>                           
                        <tr>
                              <td class='table-title'>
                                      更新下载配置<br/>
                                      <small>用于接口提示更新,非专业人员勿动此配置</small>
                              </td>
                              <td>
                                <table class='table config-table' border='1'>
                                    <tr>
                                         <td class='table-title'>
                                                  资源文件名<br/>
                                                  <small>更新的资源文件包名,入fishing.zip</small>
                                         </td>
                                         <td>
                                             <input type="text" style='width:250px;float:left' id="downloadUrl" name="downloadUrl" class="form-control">
                                         </td>
                                    </tr>                                     
                                    <tr>
                                         <td class='table-title'>
                                                  APKSIZE<br/>
                                                  <small>APK大小</small>
                                         </td>
                                         <td>
                                             <input type="text" style='width:250px;float:left' id="apksize" name="apksize" class="form-control">
                                         </td>
                                    </tr>                                     
                                    <tr>
                                         <td class='table-title'>
                                                  APKMD5<br/>
                                                  <small>apk对应的md5</small>
                                         </td>
                                         <td>
                                             <input type="text" style='width:250px;float:left' id="apkmd5" name="apkmd5" class="form-control">
                                         </td>
                                    </tr>                                                      
                                </table>
                              </td>
                        </tr>                         
                        <tr>
                              <td class='table-title'>游戏路径配置</td>
                              <td>
                                <table class='table config-table' border='1'>
                                    <tr>
                                         <td class='table-title'>
                                                Web启动tag<br/>
                                                <small>WEB启动游戏的TAG(第三方游戏需填完整的URL)</small>
                                         </td>
                                         <td>
                                                <input type="text" style='width:250px;float:left' id="web_tag" name="web_tag" class="form-control">
                                                <label for='web_tag' class='hitLabel'>*</label>
                                         </td>
                                    </tr>                          
                                    <tr>
                                         <td class='table-title'>
                                                APK启动tag<br/>
                                                <small>Android启动Tag</small>
                                         </td>
                                         <td>
                                                <input type="text" style='width:250px;margin-right:10px;float:left' id="apk_tag" name="apk_tag" class="form-control">
                                                <label for='apk_tag' class='hitLabel'>*</label>
                                         </td>
                                    </tr>                                
                                    <tr>
                                         <td class='table-title'>
                                                IPA下载tag<br/>
                                                <small>IOS下载链接</small>
                                         </td>
                                         <td>
                                                <input type="text" style='width:250px;float:left' id="ipa_tag" name="ipa_tag" class="form-control">
                                                <label for='ipa_tag' class='hitLabel'>*</label>
                                         </td>
                                    </tr>                                   
                                    <tr>
                                         <td class='table-title'>
                                                PC下载tag<br/>
                                                <small>PC下载链接</small>
                                         </td>
                                         <td>
                                              <input type="text" style='width:250px;float:left' id="pc_tag" name="pc_tag" class="form-control">
                                              <label for='pc_tag' class='hitLabel'>*</label>
                                         </td>
                                    </tr>                                                      
                                </table>
                              </td>
                        </tr>
              </table>
              <div class="modal-footer" style="text-align:center">
                   <button type="submit" class="btn btn-primary">{{lang.BTN_SUBMIT_TXT}}</button>
                  <button type="button" class="btn btn-primary" onclick='normalAjax("{{info["back_pre"]}}/backLastUrl", "GET", {})'>{{lang.BTN_BACK_TXT}}</button>
              </div>
            </form>
          </div>
</div>
</div>
%rebase admin_frame_base