--- 
hide:
  - footer
comments: true
---
# DP range

درود در این بخش به یک ایده مهم و پر استفاده در مسائل برنامه نویسی پویا خواهیم پرداخت و اینکار رو با حل کردن چند مثال توضیح میدیم

## longest palindromic subsequence

### سوال

در این مسئله آرایه ای از اعداد به شما داده مبشه و ازتون طول بلند ترین زیر دنباله<sup>1</sup>
پالیندرومش<sup>2</sup>
رو می خوان

1: به دنباله ای که با حذف چند عوض از آرایه بدست میاد زیردنباله  اون دنباله میگن

2: به دنباله ای که از هر دو طرف به یک شکل خونده بشه پالیندروم میگن

### پاسخ

مثل باقی مسائل برنامه نویسی پویا اول تعریفی برای $dp$ ارائه میدیم

$dp[l][r]$: در بازه $l$ تا $r$ طول بلندترین زیردنباله پالینروم چقدره

حالا سعی می کنیم $dp$ رو آپدیت کنیم

برای یک بازه $l$ تا $r$ چندین حالت داریم:

حالت اول اینکه هر دو اندیس در زیردنباله باشن در این صورت این دو باید با هم برابر باشن چون یکیشون اولین عضو زیر دنباله و دیگری آخرین عضوه و پون زیردنباله ما پالیندرومه پس این دو با هم برابر باید باشن

در این حالت داریم:
$dp[l][r] = 2 + dp[l+1][r-1]$ 

در دوحالت دیگه یکی از دو سر بازه در زیردنباله نیومده بسته به اینکه کدوم سر نیومده باشه یکی از دوحالت زیر جواب $dp[l][r]$ میشه:

$dp[l+1][r]$ 

$dp[l][r-1]$

پس برای آپدیت دیپی همچین کدی داریم:

```cpp linenums="1"
dp[l][r] = max(dp[l+1][r] , dp[l][r-1]);
if(a[l] == a[r])
  dp[l][r] = max(dp[l][r] , dp[l+1][r-1] + 2);
```

برای پایه $dp$:

می دونیم هر بازه که طولش 1 عه یک زیردنباله پالیندروم به طول 1 داره و هر بازه ای که $l$ از $r$ بزرگتر باشه چون وجود نداره پس جواب $dp$ براش 0 عه

اگر دقت کنین طول بازه برای آپدیت یا یکدونه یا دوتا کم میشه پس همین 2 چیز برای پایه کافی هستن چون هم بازه های بطول 1 و هم به طول 0 رو حساب کردیم

### ترتیب آپدیت

یک نکته مهم دیگه که درمورد این نوع $dp$ وجود داره ترتیب آپدیت خونه های اونه.
دو مدل این $dp$ رو آپدیت می کنن

مدل اول بر اساس طوله چون اگر دقت کنین برای آپدیت ما از بازه های با طول کمتر استفاده می کنیم

یک $for$ روی طول بازه و یک $for$ برای خونه شروع بازه می زنن و با استفاده از این دو مقدار میشه $r$ رو هم در آورد

```cpp linenums="1"
for(int len = 1 ; len <= n ; len++) 
  for(int l = 1 ; l <= n-len+1 ; l++) {
    int r = l + len - 1;
    // dp update
  }
```


یک مدل دیگه اینکه اول $r$ رو از اول به آخر می برن و توی $for$ دوم مقدار $l$ رو از $r$ به سمت 1 می برن اگر به آپدیت نگاه کنین می بینین که در آپدیت هر مرحله یا $r$ کم میشه یا $r$ ثابته و $l$ زیاد میشه و در ترتیب آپدیت ما هم اول $r$ های کمتر و برای $r$ های برابر اول $l$ های بیشتر دیده میشن

```cpp linenums="1"
for(int r = 1 ; r <= n ; r++)
  for(int l = r ; l >= 1 ; l--) { 
    // dp update
  }
```

### اردر زمانی

اردر این $dp$ هم برابر مقدار زمانی که برای آپدیت هر خونه می گذاریم در $n^2$ عه مثلا در این سوال خاص ما هر خونه رو در اردر 1 آپدیت می کنیم پس در کل راه از اردر $O(n^2)$ عه

### شکل های دیگر در مسائل

در مسائل گاهی اوقات به بعد های بیشتری نیاز داریم که دیتای بیشتر رو داشته باشیم برای مثال امکان داره شما نیاز به نگه داشتن $dp[l][r][k]$ باشین و این نوع $dp$ همیشه به صورت خام نمیاد در بخش سوال ها چند سوال به این شکل هم هست تا با این نوع بیشتر آشنا بشین

## سوال ها

 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: |
|[Modern Art 3](https://usaco.org/index.php?page=viewproblem2&cpid=1114){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[DP range](/Level2/dp_range){:target="_blank"}</li></ul> </details>|:judge-usaco: [Usaco](https://usaco.org/){:target="_blank"}|
|[Reversed LCS](https://atcoder.jp/contests/agc021/tasks/agc021_d){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[DP range](/Level2/dp_range){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp){:target="_blank"}|
|[Zuma](https://codeforces.com/problemset/problem/607/B){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[DP range](/Level2/dp_range){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com){:target="_blank"}|
|[Greedy Pie Eaters](https://usaco.org/index.php?page=viewproblem2&cpid=972){:target="_blank"}|2300|<details> <summary>Spoiler</summary> <ul><li>[DP range](/Level2/dp_range){:target="_blank"}</li></ul> </details>|:judge-usaco: [Usaco](https://usaco.org/){:target="_blank"}|
|[Sailing Race](https://oj.uz/problem/view/CEOI12_race){:target="_blank"}|2700|<details> <summary>Spoiler</summary> <ul><li>[DP range](/Level2/dp_range){:target="_blank"}</li></ul> </details>|:judge-ojuz: [Oj.uz](https://oj.uz){:target="_blank"}|