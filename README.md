# Big_Data
codereview for Bigdata

## Server
這邊是純後端code, 另外需要前端 以及 DB 對接

## 使用說明
首先進入 backend/settings.py 設定 db

如果透過本機啟動,則需要先使用
    python manage.py createsuperuser
新增使用者之後
    python manage.py migrate 在db建立 table

## urls
*主頁
    articles/',views.article_cover)
*顯示指定文章內容
    article/<id:int>,
*新增文章
    article/create/<id:int>
*刪除文章
    article/delete_<id:int>
*修改文章
    article/update_<id:int>

