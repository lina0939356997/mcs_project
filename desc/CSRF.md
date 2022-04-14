#CSRF
簡單來說，CSRF 就是在使用者不知情的情況下，讓使用者的瀏覽器自動送出請求給目標網站，利用使用者當前的身份去做一些未經過授權的操作以達攻擊目的。

也因為 Server 不知道收到的 request 到底是從信任的來源發出的還是不信任的來源，所以如果能解決來源信任的問題，就可以避免掉 CSRF 的攻擊。

![avatar](https://miro.medium.com/max/1400/0*1dWDiri9HzeU19-e.)

#如何避免攻擊
##CSRF token
![avatar](https://www.maxlist.xyz/wp-content/uploads/2020/05/Flask_CSRF%E9%98%B2%E8%AD%B7.png)

由 Server 產生 token 存放在 session 中，並在前端頁面中所有表單加上一個 hidden 的欄位放 token，當 Server 接收到使用者發送的請求時，會驗證 session 中的 token 與請求中的 token 是否相同，來判斷請求來源是否是可信。


##Flask 實作 CSRF token
###安裝 flask-wtf
```
pip install flask-wtf
```
###從 flask_wtf 中載入 CSRFProtect，並設定 SECRET_KEY
```angular2html
import os
from flask_wtf.csrf import CSRFProtect

app.config['SECRET_KEY'] = os.urandom(24)

csrf = CSRFProtect(app)
```
###在所有表單中加入 hidden 欄位 csrf_token
```angular2html
<form method="post">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    <input type="text" name="email" class="form-control form-control-lg" placeholder="max@email.com">
</form>
```
###如果是使用 ajax 或 axios 可在 header 中加入 csrf-token
```angular2html
<script>
var csrf = "{{ csrf_token() }}";
axios.post('/auth/login', data, {
        headers: {'x-csrf-token': csrf}
        })
</script>
```

為什麼可以防禦 CSRF 攻擊呢？這個方法，之所以有用是因為 form 表單的 token 雖然可以隨便修改，但攻擊者並不知道正確的 csrf_token 值是什麼，也沒辦法猜到，兩者不可能匹配， request 就不被信任，所以自然就無法進行攻擊了。




