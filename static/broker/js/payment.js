$(function () {
    $(".add-payment-btn").click(function () {
        var url = "/broker/ashow_count/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('新增完成！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});


$(function () {
    $(".edit-payment-btn").click(function () {
        var url = "/broker/ushow_count/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('編輯完成！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".delete-payment-btn").click(function () {
        var url = "/broker/dshow_count/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('刪除成功！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});