# STEP homework week4  
課題：Wikipediaのリンク構造を使って面白いことを見つける:)
    
## 概要
Google”から”渋谷”を（最短で）たどる経路を探す。

## 実行方法  
テスト環境：python3.9.5  
```
python3 wikipedia_findpath.py      
```

## 出力例
```
found!!  
Google  
スターバックス
渋谷
```
```
not found.....
```

## 説明
今回は最短でたどる経路を見つけるため、グラフアルゴリズムはBFSを使用しました。  
もし、探しているページにたどり着くまでの経路が複数ある場合、BFSでは1番短いものが最初に見つかる。  
### 関数について
`open_file`   
ファイルの内容を取得して返す  
`find_page_id`  
スタートのページと見つけたいのページのidを返す  
`list_of_connected`  
page_idとつながっているページのidをリストで全て返す  
`find_connected_page`  
| Q |:　BFSの実装で使用したキュー  
| visited |:　1度調べたページのidを保持  
| path |:　{`key`にページxのid:`value`にページxが指しているすべてのページ}という組み合わせでたどったページについて保持  
| page_id |:　調べているページのid(Ｑの最後の要素)  
| connected |:　page_idが指しているページ  
  
Q 内の要素を最後から順番にwhile文で繰り返す。  
探しているページが見つかった場合(page_idとend_idが一致した場合)：  
foundを表示してwhile文を抜ける。
探しているページではなかった場合：  
　　既にすべてのページを探している場合  
　　→　not found.....を表示して終了する  
　　まだ探していないページがある場合　　  
　　→　page_idが指しているページがすでに調べたページでなければ、pathに保存、Qの最初に追加。  



`show_path`  
経路を表示する  
pathには{key:[values]}が保持されている。  
end_idからstart_idに一致するまでvalue->keyをたどる。  
1つ前のvalueのkeyを、valueから見つけるということを繰り返す。
`find_pagename`  
idからそのidのページのタイトルを返す。    
### 計算量について


