譜面定数表の更新の仕方
========

## 移行先のDBに接続

`sqlite3 db.sqlite3`

## 移行元のDBをアタッチ（接続）

`attach database "../../ongeki-net/my_ongeki.db" AS _from;`

`.databases`

2つのDBが見えることを確認。

## 移行先のDBから移行対象のテーブルを削除

`DELETE FROM baseratelist_music;`

## データコピー

`INSERT INTO main.baseratelist_music SELECT * FROM _from.base_rate;`

