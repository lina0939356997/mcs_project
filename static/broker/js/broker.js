$(function () {
    $("#search-broker-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);

        var broker_idInput = $("input[name='broker_id']");

        var broker_id = broker_idInput.val();


        if(!broker_id){
            zlalert.alertInfoToast('請輸入ID！');
            return;
        }

        var url = '/broker/show_comms/';


        zlajax.post({
            "url": url,
            'data':{
                'broker_id':broker_id,
            }
        });
    });
});