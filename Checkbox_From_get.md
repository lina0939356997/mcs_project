# 佣金計算頁面

## 資料導入後端步驟

1.使用checkbox選取要計算的資料

```
{% for broker in brokers %}
    <tr>
        <td>
            <label class="checkbox">
                <input type="checkbox" name="broker_id" value="{{ broker.broker_id }}"/>
            </label>
        </td>
    </tr>
{% endfor %}
```

2.搭配From，將選取資料代入後端
```
<form action="{{ url_for('func') }}" method="post" name="broker_id_list">
    <button class="button is-danger">計算</button>
</form>
```

3.後端使用request.form.getlist取得前端傳輸的資料

```angular2html
form_broker_id = request.form.getlist("broker_id")
```

- [ ] 取得checkbox資料並傳送
- [ ] Form將資料傳送進後端
- [ ] request.form.getlist取得前端傳送資料
##難題、缺點
無法將資料使用dict方式傳送，只能使用list

只能傳送單一類型list



