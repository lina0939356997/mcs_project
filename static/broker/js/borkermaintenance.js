$(function () {
    $(".add-broker-btn").click(function () {
        var url = "ashow_count/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('結算完成！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});


$(function () {
    $(".edit-broker-btn").click(function () {
        var url = "ushow_count/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('結算完成！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".delete-broker-btn").click(function () {
        var url = "dshow_count/";
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