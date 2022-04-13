$(function () {
    $(".start-kanban-btn").click(function () {
        var url = "/startkanban/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('排程已開始！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".resume-mock_pos-btn").click(function () {
        var url = "/resumemock_pos/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('新增資料排程已繼續！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".pause-mock_pos-btn").click(function () {
        var url = "/pausemock_pos/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('新增資料排程已停止！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".resume-insert_comm-btn").click(function () {
        var url = "/resumeinsert_comm/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('抓資料排程已繼續！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});

$(function () {
    $(".pause-insert_comm-btn").click(function () {
        var url = "/pauseinsert_comm/";
        zlajax.post({
            'url': url,
            'success': function (data) {
                if (data['code'] == 200) {
                    zlalert.alertSuccessToast('抓資料排程已停止！');
                } else {
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});