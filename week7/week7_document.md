# STEP homework week7  
## 課題1：  
行列積のループ順序としては6種類(i-j-k, i-k-j, j-i-k, j-k-i, k-i-j, k-j-i)の組合せがある。  
この6種類を実行速度が速いと思う方から順に並べる。実際に実験してその予想が正しいかどうか確かめる。
    
### 予想
メモリアクセスが連続または不変であれば、キャッシュヒット率が上がることより高速になる。  
`c[i][j] += a[i][k] * b[k][j];`  
の計算を行うとき、メモリアクセスが連続または不変であるものを示すと、
| ループ順序 | 連続または不変の行列 | 
| :-------------: | :-------------: | 
| i-j-k | c, a | 
| i-k-j | c, a, b | 
| j-i-k | c, a | 
| j-k-i | b | 
| k-i-j | c, a, b | 
| k-j-i | b | 

であるから、  
i-k-j, k-i-j ＜ i-j-k, j-i-k ＜ j-k-i,k-j-i 
と予想した。

### 実行結果  
| ループ順序 | 実行時間(sec) | 順番 |
| :-------------: | :-------------: | :-------------: |
| i-j-k | 0.149000 | 4 |
| i-k-j | 0.067000 | 1 |
| j-i-k | 0.142000 | 3 |
| j-k-i | 0.275000 | 6 |
| k-i-j | 0.071000 | 2 |
| k-j-i | 0.272000 | 5 |


## 課題2：  
C/C++/Java/Goで行列積を書くと、i-k-jループのほうがi-j-kループよりもずっと速かった。
でも、実はPythonで書くと、ループ順序を入れ替えても速度差はほとんどない理由を考える。

### 回答
pythonはインタプリタ言語であることから、実行時に与えられたプログラムの字句解析と構文解析を行い、作成した構文木を辿って評価を行う。
そのため、コンパイラのように最適化される過程がなく、実行が遅くなる。また、コンパイラではループ順序を入れ替えると連続したメモリアクセスが可能になるため実行速度が上がったが、インタプリタ言語の場合連続したメモリアクセスが行われる構文木を作成するとは限らないため、速度差がほとんどない。

## 課題3：  
TSP Challenge

### 方針
greedy法によって得られた経路において2-opt法を行う。また、スタートの位置を変えて一番短くなる場所を探す。

### 実行結果


### 改善できそうなところ