# STEP homework week4  
課題：Wikipediaのリンク構造を使って面白いことを見つける!
  
    
## 概要
Google”から”渋谷”を（最短で）たどる経路を探す。

## 実行方法  
テスト環境：python3.9.5  
```
python3 wikipedia_findpath.py      
```
## 出力例
Google  
渋谷  

## 説明
グラフアルゴリズムはBFSを使用しました。
### 関数について
`open_file`   
ファイルの内容を取得して返す  
`find_page_id`  
スタートのページと見つけたいのページのidを返す  
`list_of_connected`  
page_idとつながっているページのidをリストで全て返す  
`find_connected_page`  
Q:BFSの実装で使用したキュー  
visited:1度調べたページのidを保持
path:{`key`にページxのid:`value`にページxが指しているすべてのページ}という組み合わせでたどったページについて保持
page_id:調べているページのid(Ｑの最後の要素)  
connected:page_idが指しているページ  


`show_path`  
経路を表示する
pathには{key:[values]}が保持されている。
end_idからstart_idに一致するまでvalue->keyをたどる。
`find_pagename`  
idからそのidのページのタイトルを返す  
### 計算量について


