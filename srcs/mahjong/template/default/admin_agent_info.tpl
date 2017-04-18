<div class="definewidth" role="form">
    <div class='header definewidth'>
        <h3>
            %if info.get('title',None):
                {{info['title']}}
            %end
        </h3>
    </div>
</div>
<form class='form-horizontal group-border-dashed definewidth m10'>
        <div class="row">
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">代理账号:</span>
                <span class="form-control">{{info['account']}}</span> 
            </div>
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">代理Id:</span>
                <span class="form-control">{{info['aid']}}</span>
            </div>
        </div>  
        <div class="row">
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">代理名称:</span>
                <span class="form-control">{{info['name']}}</span>
            </div>
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">代理类型</span>
                <span class="form-control">{{info['aType']}}</span>
            </div>
            
        </div>
        <div class="row">
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">剩余房卡</span>
                <span class="form-control">{{info['roomCard']}}</span>
            </div>
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">注册时间:</span>
                <span class="form-control">{{info['regDate']}}</span>
            </div>
        </div>        
        <div class="row">
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">注册IP:</span>
                <span class="form-control">{{info['regIp']}}</span>
            </div>
            <div class="input-group col-lg-5 col-md-5 pull-left" style="padding:5px 0;margin-left:4.88%;">
                <span class="input-group-addon hint">账号状态:</span>
                <span class="form-control">{{info['valid']}}</span>
            </div>
        </div>
        <div class="modal-footer" style="text-align:center">
               <button type="button" class="btn btn-sm btn-primary" name="backid" id="backid">返回</button>
        </div>
</form>
<script type="text/javascript">
    $('#backid').click(function(){
        window.location.href="{{info['backUrl']}}";
   });
</script>
%rebase admin_frame_base