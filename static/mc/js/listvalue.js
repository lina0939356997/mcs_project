$(function () {
    $("#save-listvalue-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#listvalue-dialog");

        var set_typeInput = $("input[name='set_type']");
        var value_codeInput = $("input[name='value_code']");
        var value_nameInput = $("input[name='value_name']");
        var value_descInput = $("input[name='value_desc']");
        var parent_valueInput = $("input[name='parent_value']");

        var set_type = set_typeInput.val();
        var value_code = value_codeInput.val();
        var value_name = value_nameInput.val();
        var value_desc = value_descInput.val();
        var parent_value = parent_valueInput.val();
        var submitType = self.attr('data-type');
        var set_value_id = self.attr("data-id");

        if(!set_type || !value_code || !value_name ||
            !value_desc || !parent_value){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/ulistvalue/';
        }else{
            url = '/alistvalue/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'set_type':set_type,
                'value_code': value_code,
                'value_name': value_name,
                'value_desc': value_desc,
                'parent_value':parent_value,
                'set_value_id':set_value_id
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
    $(".edit-listvalue-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#listvalue-dialog");
        dialog.modal('show');

        var tr = self.parent().parent();
        var set_type = tr.attr("data-set_type");
        var value_code = tr.attr("data-value_code");
        var value_name = tr.attr("data-value_name");
        var value_desc = tr.attr("data-value_desc");
        var parent_value = tr.attr("data-parent_value");

        var set_typeInput = dialog.find("input[name='set_type']");
        var value_codeInput = dialog.find("input[name='value_code']");
        var value_nameInput = dialog.find("input[name='value_name']");
        var value_descInput = dialog.find("input[name='value_desc']");
        var parent_valueInput = dialog.find("input[name='parent_value']");

        var saveBtn = dialog.find("#save-listvalue-btn");

        set_typeInput.val(set_type);
        value_codeInput.val(value_code);
        value_nameInput.val(value_name);
        value_descInput.val(value_desc);
        parent_valueInput.val(parent_value);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-id',tr.attr('data-id'));
    });
});

$(function () {
    $(".delete-listvalue-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var set_value_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg":"確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/dlistvalue/',
                    'data':{
                        'set_value_id': set_value_id
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