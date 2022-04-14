
$(function () {
    $("#save-incomedata-btn").click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dialog = $("#incomedata-dialog");
        var form_idInput = $("input[name='form_id']");
        var uniform_numInput = $("input[name='uniform_num']");
        var id_noInput = $("input[name='id_no']");
        var id_numInput = $("input[name='id_num']");
        var id_nameInput = $("input[name='id_name']");
        var income_yyyInput = $("input[name='income_yyy']");
        var income_mmInput = $("input[name='income_mm']");
        var income_formatInput = $("input[name='income_format']");
        var income_markInput = $("input[name='income_mark']");
        var income_amtInput = $("input[name='income_amt']");
        var tax_amtInput = $("input[name='tax_amt']");
        var net_amtInput = $("input[name='net_amt']");
        var exe_industryInput = $("input[name='exe_industry']");
        var other_incomeInput = $("input[name='other_income']");
        var royalties_expInput = $("input[name='royalties_exp']");
        var house_tax_numInput = $("input[name='house_tax_num']");
        var house_addressInput = $("input[name='house_address']");
        var declare_statusInput = $("input[name='declare_status']");
        var remarkInput = $("input[name='remark']");


        var form_id = form_idInput.val();
        var uniform_num = uniform_numInput.val();
        var id_no = id_noInput.val();
        var id_num = id_numInput.val();
        var id_name = id_nameInput.val();
        var income_yyy = income_yyyInput.val();
        var income_mm = income_mmInput.val();
        var income_format = income_formatInput.val();
        var income_mark = income_markInput.val();
        var income_amt = income_amtInput.val();
        var tax_amt = tax_amtInput.val();
        var net_amt = net_amtInput.val();
        var exe_industry = exe_industryInput.val();
        var other_income = other_incomeInput.val();
        var royalties_exp = royalties_expInput.val();
        var house_tax_num = house_tax_numInput.val();
        var house_address = house_addressInput.val();
        var declare_status = declare_statusInput.val();
        var remark = remarkInput.val();

        var submitType = self.attr('data-type');


        if (!form_id || !uniform_num || !id_no || !id_num || !id_name ||
            !income_yyy || !income_mm || !income_format ||
            !income_amt || !tax_amt || !net_amt || !declare_status) {
            zlalert.alertInfoToast('請輸入完整資訊！');
            return;
        }

        var url = '';
        if (submitType == 'update') {
            url = '/uincomedata/';
        } else {
            url = '/aincomedata/';
        }

        zlajax.post({
            "url": url,
            'data': {
                'form_id': form_id,
                'uniform_num': uniform_num,
                'id_no': id_no,
                'id_num': id_num,
                'id_name': id_name,
                'income_yyy': income_yyy,
                'income_mm': income_mm,
                'income_format': income_format,
                'income_mark': income_mark,
                'income_amt': income_amt,
                'tax_amt': tax_amt,
                'net_amt': net_amt,
                'exe_industry': exe_industry,
                'other_income': other_income,
                'royalties_exp': royalties_exp,
                'house_tax_num': house_tax_num,
                'house_address': house_address,
                'declare_status': declare_status,
                'remark': remark,
            },
            'success': function (data) {
                dialog.modal("hide");
                if (data['code'] === 200) {
                    // 重新加载这个页面
                    window.location.reload();
                } else {
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
    $(".edit-incomedata-btn").click(function (event) {
        var self = $(this);
        var dialog = $("#incomedata-dialog");
        var tr = self.parent().parent();
        var form_id = tr.attr("data-form_id");
        var uniform_num = tr.attr("data-uniform_num");
        var id_no = tr.attr("data-id_no");
        var id_num = tr.attr("data-id_num");
        var id_name = tr.attr("data-id_name");
        var income_yyy = tr.attr("data-income_yyy");
        var income_mm = tr.attr("data-income_mm");
        var income_format = tr.attr("data-income_format");
        var income_mark = tr.attr("data-income_mark");
        var income_amt = tr.attr("data-income_amt");
        var tax_amt = tr.attr("data-tax_amt");
        var net_amt = tr.attr("data-net_amt");
        var exe_industry = tr.attr("data-exe_industry");
        var other_income = tr.attr("data-other_income");
        var royalties_exp = tr.attr("data-royalties_exp");
        var house_tax_num = tr.attr("data-house_tax_num");
        var house_address = tr.attr("data-house_address");
        var declare_status = tr.attr("data-declare_status");
        var remark = tr.attr("data-remark");
        dialog.modal('show')

        var form_idInput = dialog.find("input[name='form_id']");
        var uniform_numInput = dialog.find("input[name='uniform_num']");
        var id_noInput = dialog.find("input[name='id_no']");
        var id_numInput = dialog.find("input[name='id_num']");
        var id_nameInput = dialog.find("input[name='id_name']");
        var income_yyyInput = dialog.find("input[name='income_yyy']");
        var income_mmInput = dialog.find("input[name='income_mm']");
        var income_formatInput = dialog.find("input[name='income_format']");
        var income_markInput = dialog.find("input[name='income_mark']");
        var income_amtInput = dialog.find("input[name='income_amt']");
        var tax_amtInput = dialog.find("input[name='tax_amt']");
        var net_amtInput = dialog.find("input[name='net_amt']");
        var exe_industryInput = dialog.find("input[name='exe_industry']");
        var other_incomeInput = dialog.find("input[name='other_income']");
        var royalties_expInput = dialog.find("input[name='royalties_exp']");
        var house_tax_numInput = dialog.find("input[name='house_tax_num']");
        var house_addressInput = dialog.find("input[name='house_address']");
        var declare_statusInput = dialog.find("input[name='declare_status']");
        var remarkInput = dialog.find("input[name='remark']");

        var saveBtn = dialog.find("#save-incomedata-btn");

        form_idInput.val(form_id);
        uniform_numInput.val(uniform_num);
        id_noInput.val(id_no);
        id_numInput.val(id_num);
        id_nameInput.val(id_name);
        income_yyyInput.val(income_yyy);
        income_mmInput.val(income_mm);
        income_formatInput.val(income_format);
        income_markInput.val(income_mark);
        income_amtInput.val(income_amt);
        tax_amtInput.val(tax_amt);
        net_amtInput.val(net_amt);
        exe_industryInput.val(exe_industry);
        other_incomeInput.val(other_income);
        royalties_expInput.val(royalties_exp);
        house_tax_numInput.val(house_tax_num);
        house_addressInput.val(house_address);
        declare_statusInput.val(declare_status);
        remarkInput.val(remark);
        saveBtn.attr("data-type", 'update');
    });
});

$(function () {
    $(".delete-incomedata-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var form_id = tr.attr('data-form_id');
        zlalert.alertConfirm({
            "msg": "確認刪除？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/dincomedata/',
                    'data': {
                        'form_id': form_id
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