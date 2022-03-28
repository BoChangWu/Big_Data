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
* 主頁
```python
    articles/
```
* 顯示指定文章內容
```python
article/(id:int)
```
* 新增文章
```python
article/create/(id:int)
```
* 刪除文章
```python
article/delete_(id:int)
```
* 修改文章
```python
article/update_(id:int)
```
以上四個功能中只有 POST, PUT 需要額外data:

```python
    data:{
        #標題
        'title': str,
        # 封面照片網址
        'cover': str,
        # 內文
        'content': str,
        # 內文圖片網址
        'img': List[str],
        # 相關文章網址
        'related': List[str]
    }
```
