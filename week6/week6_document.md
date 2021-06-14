# STEP homework week6  
課題：freelist mallocの、メモリ使用率と速度をUpさせる
    
## 概要
simple_malloc.cのFirst fitのlinked listの実装をもとに、best fitにする。  
First fitが一番最初に見つかった十分なサイズのメモリをとるのに対して、best fitでは要求されたサイズを満たすもののうち最も小さいメモリを選択する。また、比較としてWorst fitも試してみました。  
b_malloc.c -> best fit  
w_malloc.c -> worst fit  
simple_malloc -> first fit(sample code)  

## 方針  
### Best fit
1.もし


### Worst fit




## 実行結果
### Best fit
```
Challenge 1: simple malloc => my malloc
Time: 50 ms => 1431 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 42 ms => 812 ms
Utilization: 40% => 39%
==================================
Challenge 3: simple malloc => my malloc
Time: 524 ms => 950 ms
Utilization: 7% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 45095 ms => 11411 ms
Utilization: 16% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 33455 ms => 6014 ms
Utilization: 15% => 71%
==================================
```
### Worstfit  
```
Challenge 1: simple malloc => my malloc
Time: 39 ms => 818 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 21 ms => 515 ms
Utilization: 40% => 39%
==================================
Challenge 3: simple malloc => my malloc
Time: 334 ms => 199974 ms
Utilization: 7% => 3%
==================================
Challenge 4: simple malloc => my malloc
Time: 41172 ms => 983290 ms
Utilization: 16% => 6%
==================================
Challenge 5: simple malloc => my malloc
Time: 24462 ms => 785198 ms
Utilization: 15% => 6%
==================================
```
## 改善できそうなところ
・二分木を使うことで探索時間を短縮できそう    
・
```
my_metadata_t *min_slot = NULL;
    my_metadata_t *prev_min_slot = NULL;
```
を`metadata`で初期化するとコアダンプや無限ループぽくなる
