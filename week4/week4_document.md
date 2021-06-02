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
- `open_file()`   
ファイルの内容を取得して返す  
- `find_start_end_id(pages)`  
スタートのページと見つけたいのページのidを返す  
- `list_of_connected(links, page_id)`  
page_idとつながっている(指している)ページのidをリストで全て返す  
- `visited_pages(visited, page_id)`  
既に調べたページのidを保持する  
※ ページ最後の[問題点](#問題点)参照  
- `find_connected_page(pages, links, start_id, end_id)`    
Q 内の要素を最後から順番にwhile文で繰り返す。  
探しているページが見つかった場合(page_idとend_idが一致した場合)：  
found!を表示してwhile文を抜ける。
探しているページではなかった場合：  
　　既にすべてのページを探している場合  
　　→　not found.....を表示して終了する  
　　まだ探していないページがある場合　　  
　　→　page_idが指しているページがすでに調べたページでなければ、pathに保存、Qの最初に追加。  
- `find_route(pages, path, page_id, start_id, end_id)`  
最短経路を見つける。  
pathには{key:[values]}が保持されている。  
end_idからstart_idに一致するまでpathをたどる。  
1つ前のvalueのkeyを、valueから見つけ、そのvalueのkeyをvalueの中から見つける...ということを繰り返す。  
最終的にstart_idが指しているidのいずれかにたどり着く。  
- `find_pagename(pages, pageid)`  
idからそのidのページのタイトルを返す。    
### 問題点  
・実行時間がとても長い（30分くらいかかりました）  
　想定している原因：  
　何度も探索している部分が多い  
　　・list_of_connectedが呼び出されるたびにlinksを探す  
　　・visited内に存在しているか、各ページのconnected1の回数分探している  
　　・routeを見つけるときにpathを探す -> 探し終えた分は消す、ソートしてから探索する？  
・pathにはend_idが見つかるまでのlinksの情報が入っているためメモリの消費量が多い  
・pagesに存在しないページ名を指定したときに起こるエラーをうまく処理できなかった    
・実行回によっては最短経路の表示が予想通りではない  
  (飛ばされている、被るなど。。。）  
  (関数`visited_pages`を`find_connected_page`に入れようとしたときにも最短経路がうまく表示されなくなった)  

