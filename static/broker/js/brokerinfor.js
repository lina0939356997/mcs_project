$(function () {
    $("#save-brokerinfor-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#brokerinfor-dialog");
        var borker_nameInput = $("input[name='borker_name']");
        var borker_numInput = $("input[name='borker_num']");
        var travelInput = $("input[name='travel']");
        var phoneInput = $("input[name='phone']");
        var addressInput = $("input[name='address']");


        var borker_name = borker_nameInput.val();
        var borker_num = borker_numInput.val();
        var travel = travelInput.val();
        var phone = phoneInput.val();
        var address = addressInput.val();
        var submitType = self.attr('data-type');
        var borker_id = self.attr("data-borker_id");


        if(!borker_name || !borker_num || !travel || !phone){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/ubrokerinfor/';
        }else{
            url = '/abrokerinfor/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'borker_name':borker_name,
                'borker_num': borker_num,
                'travel': travel,
                'phone': phone,
                'address':address,
                'borker_id':borker_id
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
        var borker_name = tr.attr("data-borker_name");
        var borker_num = tr.attr("data-borker_num");
        var travel = tr.attr("data-travel");
        var phone = tr.attr("data-phone");
        var address = tr.attr("data-address");
        dialog.modal('show')

        var borker_nameInput = dialog.find("input[name='borker_name']");
        var borker_numInput = dialog.find("input[name='borker_num']");
        var travelInput = dialog.find("input[name='travel']");
        var phoneInput = dialog.find("input[name='phone']");
        var addressInput = dialog.find("input[name='address']");
        var saveBtn = dialog.find("#save-brokerinfor-btn");

        borker_nameInput.val(borker_name);
        borker_numInput.val(borker_num);
        travelInput.val(travel);
        phoneInput.val(phone);
        addressInput.val(address);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-borker_id',tr.attr('data-borker_id'));
    });
});

$(function () {
    $(".delete-brokerinfor-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var borker_id = tr.attr('data-borker_id');
        zlalert.alertConfirm({
            "msg":"確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/dbrokerinfor/',
                    'data':{
                        'borker_id': borker_id
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