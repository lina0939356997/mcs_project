$(function () {
    $("#save-userset-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#userset-dialog");
        var accountInput = $("input[name='account']");
        var passwordInput = $("input[name='password']");
        var nameInput = $("input[name='username']");
        var permissionInput = $("input[name='permission']:checked");


        var account = accountInput.val();
        var password = passwordInput.val();
        var name = nameInput.val();
        var permission = permissionInput.val();
        var submitType = self.attr('data-type');
        var user_id = self.attr("data-id");


        if(!account || !password || !name || !permission){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if(submitType == 'update'){
            url = '/uuserset/';
        }else{
            url = '/auserset/';
        }

        zlajax.post({
            "url": url,
            'data':{
                'account':account,
                'password': password,
                'name': name,
                'permission': permission,
                'user_id':user_id
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
    $(".edit-userset-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#userset-dialog");
        var tr = self.parent().parent();
        var account = tr.attr("data-account");
        var password = tr.attr("data-password");
        var name = tr.attr("data-name");
        var permission = tr.attr("data-permission");
        dialog.modal('show')

        var accountInput = dialog.find("input[name='account']").attr('readonly',true);
        var passwordInput = dialog.find("input[name='password']");
        var nameInput = dialog.find("input[name='username']");
        var permissionInput = dialog.find("input[name='permission']:checked");
        var saveBtn = dialog.find("#save-userset-btn");

        accountInput.val(account);
        nameInput.val(name);
        passwordInput.val(password);
        permissionInput.val(permission);
        saveBtn.attr("data-type",'update');
        saveBtn.attr('data-id',tr.attr('data-id'));
    });
});

$(function () {
    $(".delete-userset-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var user_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg":"確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/duserset/',
                    'data':{
                        'user_id': user_id
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