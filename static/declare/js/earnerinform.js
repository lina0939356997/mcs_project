$(function () {
    $("#save-earner-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#earner-dialog");

        var id_noInput = $("input[name='id_no']");
        var id_numInput = $("input[name='id_num']");
        var id_nameInput = $("input[name='id_name']");
        var phone_numInput = $("input[name='phone_num']");
        var id_typeInput = $("input[name='id_type']:checked");
        var id_value_codeInput = $("input[name='id_value_code']");
        var id_value_nameInput = $("input[name='id_value_name']");
        var addressInput = $("input[name='address']");
        var telInput = $("input[name='tel']");
        var id_markInput = $("input[name='id_mark']");
        var remarkInput = $("input[name='remark']");
        var statusInput = $("input[name='status']");

        var id_no = id_noInput.val();
        var id_num = id_numInput.val();
        var id_name = id_nameInput.val();
        var phone_num = phone_numInput.val();
        var id_type = id_typeInput.val();
        var id_value_code = id_value_codeInput.val();
        var id_value_name = id_value_nameInput.val();
        var address = addressInput.val();
        var tel = telInput.val();
        var id_mark = id_markInput.val();
        var remark = remarkInput.val();
        var status = statusInput.val();

        var submitType = self.attr('data-type');

        if(!id_no || !id_num || !id_name || !phone_num ||
            !id_type || !id_value_code || !id_value_name||
            !address || !tel || !id_mark || !remark || !status){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/uearnerinform/';
        }else{
            url = '/aearnerinform/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'id_no':id_no,
                'id_num':id_num,
                'id_name': id_name,
                'phone_num': phone_num,
                'id_type': id_type,
                'id_value_code':id_value_code,
                'id_value_name':id_value_name,
                'address': address,
                'tel': tel,
                'id_mark': id_mark,
                'remark': remark,
                'status': status
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
    $(".edit-earner-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#earner-dialog");

        dialog.modal('show');

        var tr = self.parent().parent();
        var id_no = tr.attr("data-id_no");
        var id_num = tr.attr("data-id_num");
        var id_name = tr.attr("data-id_name");
        var phone_num = tr.attr("data-phone_num");
        var id_type = tr.attr("data-id_type");
        var id_value_code = tr.attr("data-id_value_code");
        var id_value_name = tr.attr("data-id_value_name");
        var address = tr.attr("data-address");
        var tel = tr.attr("data-tel");
        var id_mark = tr.attr("data-id_mark");
        var remark = tr.attr("data-remark");
        var status = tr.attr("data-status");

        var id_noInput = dialog.find("input[name='id_no']");
        var id_numInput = dialog.find("input[name='id_num']");
        var id_nameInput = dialog.find("input[name='id_name']");
        var phone_numInput = dialog.find("input[name='phone_num']");
        var id_typeInput = dialog.find("input[name='id_type']:checked");
        var id_value_codeInput = dialog.find("input[name='id_value_code']");
        var id_value_nameInput = dialog.find("input[name='id_value_name']");
        var addressInput = dialog.find("input[name='address']");
        var telInput = dialog.find("input[name='tel']");
        var id_markInput = dialog.find("input[name='id_mark']");
        var remarkInput = dialog.find("input[name='remark']");
        var statusInput = dialog.find("input[name='status']");

        var saveBtn = dialog.find("#save-earner-btn");

        id_noInput.val(id_no);
        id_numInput.val(id_num);
        id_nameInput.val(id_name);
        phone_numInput.val(phone_num);
        id_typeInput.val(id_type);
        id_value_codeInput.val(id_value_code);
        id_value_nameInput.val(id_value_name);
        addressInput.val(address);
        telInput.val(tel);
        id_markInput.val(id_mark);
        remarkInput.val(remark);
        statusInput.val(status);
        saveBtn.attr("data-type",'update');

    });
});

$(function () {
    $(".change-earner-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var id_no = tr.attr("data-id_no");
        var status = Boolean(parseInt(tr.attr("data-status")));
        var url = "/searnerinform/";
        zlajax.post({
            'url': url,
            'data': {
                'id_no': id_no,
                'status': status
            },
            'success': function (data) {
                if(data['code'] == 200){
                    zlalert.alertSuccessToast('操作成功！');
                    setTimeout(function () {
                        window.location.reload();
                    },500);
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});