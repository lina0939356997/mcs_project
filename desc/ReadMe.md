# 建置步驟__指令集
## -Docker安裝postgres
1. 下載docker desktop
>https://www.docker.com/get-started/
> 
>https://www.netapp.com/zh-hant/devops-solutions/what-are-containers/
2. 拉至最新版image
```angular2html
docker pull postgres
```
3. 建立container，設定port、postgres最高權限的登入密碼
>一定要指定port對應，官網上的說明沒有指定，但實際上可能會導致連不上
```angular2html
docker create --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 postgres
```
4. 執行container
```angular2html
docker start my-postgres
```
## -生成requirements環境
1. 安裝requirements的環境規格:
```angular2html
pip install -r requirements.txt
```
## -建立資料表(先確定config.py中已指向目標資料庫)
1. 依據Model的結構產生初始化設定並自動生成migrations資料夾來保存。
```angular2html
flask db init
```
2. 產生資料庫內容，而不用去寫SQL語法建立Table以及設定DB Schema。
```angular2html
flask db migrate
```
3. 當Model的結構有異動時要自動更新資料庫的話則執行此指令，會將versions中的最新版本套用到資料庫。
```angular2html
flask db upgrade
```
## -寫入資料
1. 將seeds資料夾中的.csv檔寫入Table中
```angular2html
python seed.py
```
## -進行test(只做後端資料拋接、指向的測試)
```angular2html
pytest
```

-----------------------------------
# 補充_指令集
## -生成requirements.txt 檔
```angular2html
pip freeze >requirements.txt
```
## -查詢插件版本檔
```angular2html
插件名稱 -v
```
## -用coverage生成.html形式的測試結果報告
1. 做測試
```angular2html
coverage run -m pytest
```
2. 生成報告
```angular2html
coverage report -m 
```
3. 將報告轉為一個index.html檔案(存在htmlcov檔案夾中)
```angular2html
coverage html 
```
