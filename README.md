口增長推測
=====
[TOC]

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

-----

## feature 2
![](https://i.imgur.com/TsSpevF.png)
![](https://i.imgur.com/vfItoHH.png)
輸出
![](https://i.imgur.com/xTXom0C.png)
![](https://i.imgur.com/x5T4xaO.png)

-----

## feature 3
![](https://i.imgur.com/C55MKAE.png)
輸出結果
![](https://i.imgur.com/J5Cb1v5.png)

-----

## feature 4
![](https://i.imgur.com/7CPJWcR.png)
此模式下 **藍色為預測人口數量** 而 **黃色為實際人口數量**

-----

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


#完整程式碼

請到[github](https://github.com/loben-illimited/Calculus-project-using-python--1062)上下載


![qr code](data:image/png;base64,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)

