$(function () {
    $("#save-reportinform-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#reportinform-dialog");

        var uniform_numInput = $("input[name='uniform_num']");
        var site_nameInput = $("input[name='site_name']");

        var uniform_num = uniform_numInput.val();
        var site_name = site_nameInput.val();

        var submitType = self.attr('data-type');
        var register_id = self.attr("data-id");

        if(!uniform_num || !site_name){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType === 'update'){
            url = '/declare/uregister/';
        }else{
            url = '/declare/aregister/';
        }


        zlajax.post({
            "url": url,
            'data':{
                'uniform_num':uniform_num,
                'site_name': site_name,
                'register_id':register_id
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
    $(".edit-reportinform-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#reportinform-dialog");
        var tr = self.parent().parent();
        var uniform_num = tr.attr("data-uniform_num");
        var site_name = tr.attr("data-site_name");
        dialog.modal('show')

        var uniform_numInput = dialog.find("input[name='uniform_num']");
        var site_nameInput = dialog.find("input[name='site_name']");
        var saveBtn = dialog.find("#save-reportinform-btn");

        uniform_numInput.val(uniform_num);
        site_nameInput.val(site_name);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-id',tr.attr('data-id'));
    });
});