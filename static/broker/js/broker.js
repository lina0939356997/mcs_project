$(function () {
    $(".search-broker-btn").click(function (event) {
        var self = $(this);

        var broker_idInput = $("input[name='broker_id']");

        var broker_id = broker_idInput.val();


        if (!broker_id) {
            zlalert.alertInfoToast('請輸入ID！');
            return;
        }

        var url = "/borker/show_comms/";


        zlajax.post({
            "url": url,
            'data': {
                'broker_id': broker_id,
            },
        });
    });
});

$(function () {
    $(".update-userset-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var user_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg": "確認編輯？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/duserset/',
                    'data': {
                        'user_id': user_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            window.location.reload();
                        } else {
                            zlalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});


$(function () {
    $(".delete-userset-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var user_id = tr.attr('data-id');
        zlalert.alertConfirm({
            "msg": "確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/duserset/',
                    'data': {
                        'user_id': user_id
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            window.location.reload();
                        } else {
                            zlalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});