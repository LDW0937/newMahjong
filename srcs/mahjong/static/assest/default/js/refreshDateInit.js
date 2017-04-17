$().ready(function(){
    var now = new Date();                    //当前日期      
    var nowDayOfWeek = now.getDay();         //今天本周的第几天
    if (!nowDayOfWeek)
        nowDayOfWeek = 6
    else
        nowDayOfWeek -= 1
    var nowDay = now.getDate();              //当前日      
    var nowMonth = now.getMonth();           //当前月      
    var nowYear = now.getFullYear();             //当前年 
    var loadTable = false;

    $("#btn_lastMonth").click(function(){
        var firstDate = getLastMonthStartDate();
        var endDate = getLastMonthEndDate();
        refresh(firstDate, endDate);
    });

    $("#btn_thisMonth").click(function(){
        var firstDate = getMonthStartDate();
        var endDate = getMonthEndDate();
        refresh(firstDate, endDate);
    });

    $("#btn_lastWeek").click(function(){
        var firstDate = getLastWeekStartDate();
        var endDate = getLastWeekEndDate();
        refresh(firstDate, endDate);
    });

    $("#btn_thisWeek").click(function(){
        var firstDate = getWeekStartDate();
        var endDate = getWeekEndDate();
        refresh(firstDate, endDate);
    });

    $("#btn_yesterday").click(function(){
        var date=new Date();
        date.setDate(date.getDate()-1);
        var firstDate = date;
        var endDate = date;
        refresh(firstDate, endDate);
    });

    $("#btn_today").click(function(){
        var firstDate=new Date();
        var endDate = new Date();
        refresh(firstDate, endDate);
    });

    $("#btn_query").click(function(){
        if (!loadTable) {
            initTable();
            loadTable = true;
        }
        else {
            $("#dataTable").bootstrapTable('destroy');
            // $("#dataTable").bootstrapTable('refresh');
            initTable();
        }
    });

    function refresh(startDate, endDate){
        $('#pick-date-start').val(startDate.Format("yyyy-MM-dd"));
        $('#pick-date-end').val(endDate.Format("yyyy-MM-dd"));
        if (!loadTable) {
            initTable();
            loadTable = true;
        }
        else {
            $("#dataTable").bootstrapTable('destroy');
            initTable();
        }
    }

    //获得某月的天数      
    function getMonthDays(myMonth){      
        var monthStartDate = new Date(nowYear, myMonth, 1);       
        var monthEndDate = new Date(nowYear, myMonth + 1, 1);    
        var   days   =   (monthEndDate   -   monthStartDate)/(1000   *   60   *   60   *   24);     
        return   days;       
    }

    //获得本周的开始日期      
    function getWeekStartDate() {       
        var weekStartDate = new Date(nowYear, nowMonth, nowDay - nowDayOfWeek);
        return weekStartDate;      
    }

    //获得本周的结束日期      
    function getWeekEndDate() {
        var weekEndDate = new Date(nowYear, nowMonth, nowDay + (6 - nowDayOfWeek));     
        return weekEndDate;    
    }  

    //获得上周的开始日期      
    function getLastWeekStartDate() {       
        var weekStartDate = new Date(nowYear, nowMonth, nowDay - nowDayOfWeek);
        weekStartDate.setDate(weekStartDate.getDate()-7);     
        return weekStartDate;      
    }

    //获得上周的结束日期      
    function getLastWeekEndDate() {       
        var weekEndDate = new Date(nowYear, nowMonth, nowDay - nowDayOfWeek);       
        weekEndDate.setDate(weekEndDate.getDate()-1); 
        return weekEndDate;    
    }  

    //获得本月的开始日期      
    function getMonthStartDate(){      
        var monthStartDate = new Date(nowYear, nowMonth, 1);       
        return monthStartDate;      
    }

    //获得本月的结束日期      
    function getMonthEndDate(){      
        var monthEndDate = new Date(nowYear, nowMonth, getMonthDays(nowMonth));       
        return monthEndDate;      
    }

    //获得上月的开始日期      
    function getLastMonthStartDate(){      
        var monthStartDate = new Date(nowYear, nowMonth-1, 1);       
        return monthStartDate;      
    }

    //获得上月的结束日期      
    function getLastMonthEndDate(){  
        var monthEndDate = new Date(nowYear, nowMonth - 1, getMonthDays(nowMonth-1));      
        return monthEndDate;    
    }

});