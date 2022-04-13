
$(function () {
    $("#save-sysparameter-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#sysparameter-dialog");
        var webnameInput = $("input[name='webname']");
        var webtitleInput = $("input[name='webtitle']");
        var basic_wageInput = $("input[name='basic_wage']");
        var second_HI_rateInput = $("input[name='second_HI_rate']");
        var defresultcodeInput = $("input[name='defresultcode']");
        var defuniformnumInput = $("input[name='defuniformnum']");

        var webname = webnameInput.val();
        var webtitle = webtitleInput.val();
        var basic_wage = basic_wageInput.val();
        var second_HI_rate = second_HI_rateInput.val();
        var defresultcode = defresultcodeInput.val();
        var defuniformnum = defuniformnumInput.val();
        var submitType = self.attr('data-type');
        var sysparameterId = self.attr("data-id");

        if(!webname || !webtitle || !basic_wage || !second_HI_rate ||
            !defresultcode || !defuniformnum){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/mc/usysparameter/';
        }else{
            url = '/mc/asysparameter/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'webname':webname,
                'webtitle': webtitle,
                'basic_wage': basic_wage,
                'second_HI_rate':second_HI_rate,
                'defresultcode':defresultcode,
                'defuniformnum':defuniformnum,
                'sysparameter_id': sysparameterId
            },
            'success': function (data) {
                dialog.modal("hide");
                if(data['code'] == 200){
                    // 重新加载这个页面
                    window.location.reload();
                }else{
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail': function () {
                zlalert.alertNetworkError();
            }
        });
    });
});

$(function () {
    $(".edit-sysparameter-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#sysparameter-dialog");
        dialog.modal("show");

        var tr = self.parent().parent();
        var webname = tr.attr("data-webname");
        var webtitle = tr.attr("data-webtitle");
        var basic_wage = tr.attr("data-basic_wage");
        var second_HI_rate = tr.attr("data-second_HI_rate");
        var defresultcode = tr.attr("data-defresultcode");
        var defuniformnum = tr.attr("data-defuniformnum");

        var webnameInput = dialog.find("input[name='webname']");
        var webtitleInput = dialog.find("input[name='webtitle']");
        var basic_wageInput = dialog.find("input[name='basic_wage']");
        var second_HI_rateInput = dialog.find("input[name='second_HI_rate']");
        var defresultcodeInput = dialog.find("input[name='defresultcode']");
        var defuniformnumInput = dialog.find("input[name='defuniformnum']");

        var saveBtn = dialog.find("#save-sysparameter-btn");

        webnameInput.val(webname);
        webtitleInput.val(webtitle);
        basic_wageInput.val(basic_wage);
        second_HI_rateInput.val(second_HI_rate);
        defresultcodeInput.val(defresultcode);
        defuniformnumInput.val(defuniformnum);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-id',tr.attr('data-id'));
    });
});