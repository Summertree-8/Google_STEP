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



### Worst fit




## 実行結果
### Best fit
```
Challenge 1: simple malloc => my malloc
Time: 33 ms => 17 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 18 ms => 28 ms
Utilization: 40% => 39%
==================================
Challenge 3: simple malloc => my malloc
Time: 114 ms => 18 ms
Utilization: 7% => 4%
==================================
Challenge 4: simple malloc => my malloc
Time: 35138 ms => 68 ms
Utilization: 16% => 6%
==================================
Challenge 5: simple malloc => my malloc
Time: 25797 ms => 67 ms
Utilization: 15% => 6%
==================================
```
### Worstfit  

