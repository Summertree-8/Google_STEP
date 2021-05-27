# STEP homework week3
電卓のプログラムを題材にして、プログラムをモジュール化することの重要性を考える。

## __Homework1、2__
#### Q.モジュール化されたプログラムを変更して「*」「/」に対応。テストケースの追加。

##### ・方針    
　　先に「*」「/」のみ計算し終えた後、「+」「−」の計算を行う。  

##### ・説明  

  
（例)  
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| fomula | 1 |+ | 2.5 | - | __3__ | __/__ | __1.0__ | + | 20 | * | 5 |
| fomula | 1 |+ | 2.5 | - | __3__ | + | 20 | * | 5 |  |  |  |
| fomula | 1 |+ | 2.5 | - | 3 | + | 100 |  |  |  |  |  |
| fomula |100.5 | 

## __Homework3__
#### Q.括弧に対応。テストケースの追加。
##### ・方針
　　1.より内側にあるかっこ内を計算。  
　　2.「*」「/」のみ計算し終えた後、「+」「−」を計算。  
  
  
##### ・説明  
　　”inbracket_evaluated”：最終的に括弧内を計算し終えた式が入る  
　　”inbracket”：括弧の内側にある式  
　　はじめて右括弧が見つかったとき  
　　対応する左括弧(リストを戻った時に最初に現れる左括弧）を見つける  
　　括弧内を計算

##### ・補足  
　　括弧内の計算をするときに、計算される部分の削除を同時に行う  

（例)  
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
3*((5+10)-10)
| fomula | 3 |* | ( | ( | 5 | + | 10 | ) | - | 10 | ) |
| inbracket | 5 | + | 10 |
| inbracket_evaluated | 3 |* | ( | 15 | - | 10 | ) |  | |  |  |
| inbracket | 15 | - | 10 |
| inbracket_evaluated | 3 |* | 5 | 
| inbracket_evaluated | 15 |  
  

