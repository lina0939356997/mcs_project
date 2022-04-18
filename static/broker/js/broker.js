$(function () {
    $(".search-broker-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);

        var broker_idInput = $("input[name='broker_id']");

        var broker_id = broker_idInput.val();


        if (!broker_id) {
            zlalert.alertInfoToast('請輸入ID！');
            return;
        }

        var url = "/broker/show_comms/";


        zlajax.post({
            "url": url,
            'data': {
                'broker_id': broker_id,
            },
        });
    });
});

$(function () {
    $("#save-broker-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#broker-dialog");
        var dialog2 = $("#brokerchose-dialog");
        var namecallInput = $("input[name='namecall']");

        var namecall = namecallInput.val();



        if(!namecall){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '/broker/search/';

        zlajax.post({
            "url": url,
            'data':{
                'namecall':namecall,
            },
            'success': function (data) {
                dialog.modal("hide");
                if(data['code'] === 200){
                    // 重新加载这个页面
                    dialog2.modal("show")
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
    $("#save-brokerchose-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#brokerchose-dialog");
        var brokerchoseInput = $("input[name='brokerchose']");

        var brokerchose = brokerchoseInput.val();



        if(!brokerchose){
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = 'broker/brokerchose/';

        zlajax.post({
            "url": url,
            'data':{
                'brokerchose':brokerchose,
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

