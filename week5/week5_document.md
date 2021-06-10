# STEP homework week5  
課題：Write a program, solving each TSP by designing and implementing an algorithm.
    
## 概要
貪欲法で経路を出した後に、交差している部分を見つけ、交差を解消する方針で実装しました。

## 出力
- 貪欲法による経路  
- 改善した方法の経路  
- 距離の合計  
を順番に出力します

### 関数について
- `read_input(filename)`   
- `format_tour(tour)`
- `print_tour(tour)`  
- `visited_pages(visited, page_id)`  
- `distance(city1, city2)`    
- `greedy(cities)`  
※上記の関数は[https://github.com/hayatoito/google-step-tsp] を参考に同じものを実装しました
