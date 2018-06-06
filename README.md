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

- 輸出 **Malthus** 預測及實際人口數量圖形

- 輸出結果為html file

# 教學

* 請先在主程式的資料夾下新增一個名為“temp”的folder用作儲存輸出的圖片

## 主畫面
![menu](https://i.imgur.com/sCJblI5.png)

主畫面有5個功能

1. 第一個功能是透過Malthus去求出特定時間段內特定國家的人口數量 （彈出windows）

2. 藉由網上提供的`api`輸出特定時間段內的實際人口數量 （彈出windows）

3. 儲存特定時間段內所有國家的實際人數及 **Malthus** 預測的人口數量（儲存為png圖片及json）

4. 顯示特定時間段內所有國家的實際人數及 **Malthus** 預測的人口數量 （彈出windows)

5. 將所有結果輸出成`html`檔案

## feature 1
選擇feature1
![feature1 menu](https://i.imgur.com/aHsTR3E.png)

然後輸出想得知的國家編號或名稱，並以 `,`作分隔

例如：`1, 222, 232` 或 `Serbia, South Africa` 或 `1, South Africa`

![](https://i.imgur.com/VLnB6Ee.png)
並且輸入開始及結束年份

Output:
![](https://i.imgur.com/rEGyKui.png)
![](https://i.imgur.com/kk9fjvF.png)

![](https://i.imgur.com/uSPLfnS.png)
![](https://i.imgur.com/3r40IJB.png)

## feature 2
![](https://i.imgur.com/TsSpevF.png)
![](https://i.imgur.com/vfItoHH.png)

![](https://i.imgur.com/xTXom0C.png)
![](https://i.imgur.com/x5T4xaO.png)

## feature 3
![](https://i.imgur.com/C55MKAE.png)
輸出結果
![](https://i.imgur.com/J5Cb1v5.png)

## feature 4
![](https://i.imgur.com/7CPJWcR.png)
此模式下 **藍色為預測人口數量** 而 **黃色為實際人口數量**

## feature 5
![](https://i.imgur.com/LvgGGnP.png)
這裏有兩個選項，對應之前是否已經輸出數據
同時可以將`README.md`輸出成`html`
![](https://i.imgur.com/IQMcNwi.png)
![](https://i.imgur.com/uYSQwey.png)
![](https://i.imgur.com/W7CAnSR.png)
![](https://i.imgur.com/AfSiPwn.png)

# 程式碼解說

<script src="https://gist.github.com/loben-illimited/8018e6507d123ca11815c196aac5cd65.js"></script>

- `Malthus_Country.py` 建立的目的是為了更方便去查出特定期間內人口的數量


# 感想

經過是次報告令我對python的語法有更進一步的認識，相對於分組報告，我更喜歡自己一個人工作，反正也是只有自己一個人工作。

而且對 `html` 有進一步的認識，本人之前從未使用過 `table`，原因是 `table` 的語法相當繁瑣，不利於網頁網寫，而且在較舊的網頁 `table` 通常用作排版之用。

而輸出的結果也令我很食驚，想不到 `Malthus` 的模型對於某些國家還適用。

# 改進

對於老師要求的object oriented，我只能實現一部份，原因是我沒有太多寫程式的經驗，以致無法活用object oriented的概念。

但基於上學期作業的經驗，此次的報告應該會更好一點。

而且我認為可以在報告新增更多人口預測模型，從而比較那一模型更貼及現況。

以及輸出的網頁美化不足。