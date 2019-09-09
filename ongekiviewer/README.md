オンゲキ
=======

## 運用メモ

`nginx<->uwsgi<->django` の構成  
基本的に設定変更とかをしたら、uwsgiをリロードすればOK。  


### 起動
`uwsgi --ini uwsgi.ini`

### 停止
`uwsgi --stop uwsgi.ini`

### リロード
`uwsgi --reload uwsgi.ini`
