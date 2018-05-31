人口增長推測
=====
[toc]

# 前言

在現今人口增長迅速、糧食不足、土地缺乏、老年化的情況下，人口數量已成為一個大問題。
故此本人選擇以人口作為今次微積分python報告的題目，希望能藉此對人口、python及數學有進一步的認識。

# 人口增長推測

本人參考了[人口成長模型](http://episte.math.ntu.edu.tw/applications/ap_population/index.html)這篇文章的數學模型去編寫`Malthus`及`Logistic`這兩個class。

## 利用Malthus推測人口增長
Malthus數學模組是由英國經濟學家Malthus在1798年匿名發表的《人口原理》中用來描述人口成長的數學模組。

$$P(t)=P_0 \cdot e^{\lambda(t-t_0)}$$

> $t$ 為當前所求人口的時間
> $P(t)$ 為求出的人口
> $t_0$ 為任意時間點
> $P_0$ 為任意時間點的人口
> $\lambda$ 為一常數（需由計算求得）

而本人利用上式推導以求出$\lambda$：
$$\lambda = \frac{ln(\frac{P(t)}{P_0})}{t-t_0}$$

# 功能

- 藉由 **Malthus** 及 [api.population.io](http://api.population.io/) 所取得的資料去推算某一（數個）地區的人口數量。

- 可以藉由輸入人數去推算某一（數個）地區增長到特定人數的時間點。

- 藉由實際人數及計算出來的結果進行比較，從而得知那些地區仍適合利用 **Malthus** 去估算人口增長。

