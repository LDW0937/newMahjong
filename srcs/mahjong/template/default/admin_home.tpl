<div class="cl-mcont">
  <div class="block">
            <div class="header bordered-bottom bordered-themesecondary" id="crumb">
                %if info.get('title', None):
                <i class="widget-icon fa fa-tags themesecondary"></i>
                <span class="widget-caption themesecondary" id="subTitle">{{info['title']}}</span>
                %end
            </div>
            <div class="content">
                <table id="dataTable" class="table table-bordered table-hover"></table>
            </div>
  </div>
</div>
%rebase admin_frame_base