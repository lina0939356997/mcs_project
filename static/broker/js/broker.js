$(function () {
    $("#count-car-btn").click(function (event) {
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