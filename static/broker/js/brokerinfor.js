$(function () {
    $("#save-brokerinfor-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#brokerinfor-dialog");
        var broker_nameInput = $("input[name='broker_name']");
        var broker_numInput = $("input[name='broker_num']");
        var travelInput = $("input[name='travel']");
        var phoneInput = $("input[name='phone']");
        var addressInput = $("input[name='address']");


        var broker_name = broker_nameInput.val();
        var broker_num = broker_numInput.val();
        var travel = travelInput.val();
        var phone = phoneInput.val();
        var address = addressInput.val();
        var submitType = self.attr('data-type');
        var broker_id = self.attr("data-broker_id");


        if(!broker_name || !broker_num || !travel || !phone){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/broker/ubrokerinfor/';
        }else{
            url = '/broker/abrokerinfor/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'broker_name':broker_name,
                'broker_num': broker_num,
                'travel': travel,
                'phone': phone,
                'address':address,
                'broker_id':broker_id
            },
            'success': function (data) {
                dialog.modal("hide");
                if(data['code'] === 200){
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
    $(".edit-brokerinfor-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#brokerinfor-dialog");
        var tr = self.parent().parent();
        var broker_name = tr.attr("data-broker_name");
        var broker_num = tr.attr("data-broker_num");
        var travel = tr.attr("data-travel");
        var phone = tr.attr("data-phone");
        var address = tr.attr("data-address");
        dialog.modal('show')

        var broker_nameInput = dialog.find("input[name='broker_name']");
        var broker_numInput = dialog.find("input[name='broker_num']");
        var travelInput = dialog.find("input[name='travel']");
        var phoneInput = dialog.find("input[name='phone']");
        var addressInput = dialog.find("input[name='address']");
        var saveBtn = dialog.find("#save-brokerinfor-btn");

        broker_nameInput.val(broker_name);
        broker_numInput.val(broker_num);
        travelInput.val(travel);
        phoneInput.val(phone);
        addressInput.val(address);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-broker_id',tr.attr('data-broker_id'));
    });
});

$(function () {
    $(".delete-brokerinfor-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var broker_id = tr.attr('data-broker_id');
        zlalert.alertConfirm({
            "msg":"確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/broker/dbrokerinfor/',
                    'data':{
                        'broker_id': broker_id
                    },
                    'success': function (data) {
                        if(data['code'] === 200){
                            window.location.reload();
                        }else{
                            zlalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});