<div class="table-toolbar" style="float:left;width:100%;position:relative;top:2.5em">
          <div class='col-sm-12' style='margin-left:1em;'>
                  <div style='float:left;margin-left:1em;' class="input-group date datetime col-md-1 col-xs-1"data-min-view="2" data-date-format="yyyy-mm-dd">
                    <input class="form-control" size="18" type="text" style='width:140px;' id='pick-date-start' name="startdate" value="{{lang.INPUT_LABEL_START_DATE_TXT}}" readonly>
                    <span class="input-group-addon btn btn-primary"><span class="glyphicon glyphicon-th"></span>
                  </div>

                  <div style='float:left;margin-left:1em;' class="input-group date datetime col-md-1 col-xs-1"  data-min-view="2" data-date-format="yyyy-mm-dd">
                    <input class="form-control" style='width:140px;'id='pick-date-end' name="enddate" size="18" type="text" value="{{lang.INPUT_LABEL_END_DATE_TXT}}" readonly>
                    <span class="input-group-addon btn btn-primary"><span class="glyphicon glyphicon-th"></span></span>
                  </div>
                  <div style='float:left;margin-left:1em;'>
                          <button id="btn_query" class='btn btn-primary btn-sm'><i class='fa fa-search'></i>{{lang.INPUT_LABEL_QUERY}}</button>
                          <button id="btn_lastMonth" class='btn btn-sm'>{{lang.INPUT_LABEL_PREV_MONTH}}</button>
                          <button id="btn_thisMonth" class='btn btn-sm '>{{lang.INPUT_LABEL_CURR_MONTH}}</button>
                          <button id="btn_lastWeek" class='btn btn-sm '>{{lang.INPUT_LABEL_PREV_WEEK}}</button>
                          <button id="btn_thisWeek" class='btn btn-sm'>{{lang.INPUT_LABEL_CURR_WEEK}}</button>
                          <button id="btn_yesterday" class='btn btn-sm'>{{lang.INPUT_LABEL_PREV_DAY}}</button>
                          <button id="btn_today" class='btn btn-sm'>{{lang.INPUT_LABEL_CURR_DAY}}</button>
                         <div class='clearfix'></div>
                  </div>
          </div>
</div>