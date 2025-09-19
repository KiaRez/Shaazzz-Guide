--- 
hide:
  - footer
comments: true
---

# LIS & LCS

## توضیحات
### LIS

#### مسئله

یک آرایه به طول $N$ $(1 \leq N \leq 10^{6})$ داریم $a_{1} , a_{2} , a_{3} , \dots , a_{N}$ که به ازای هر $i$ $(1 \leq i \leq N)$ شرط $1 \leq a_{i} \leq 10^{9}$ برقرار است طول بلندترین زیر دنباله صعودی اعداد آرایه چند است؟

زیر دنباله یک آرایه به آرایه هایی گفته می شود که از حذف تعدادی عضو و کنار هم قرار دادن باقی اعضای آرایه اولیه به همان ترتیب بدست آیند.
برای مثال برای آرایه اولیه [1 , 2 , 3] آرایه های [] , [1] , [1 , 3] , [1 , 2 , 3] زیر دنباله هستند ولی [2 , 1] , [4] نیستند

به دنباله $b_{1} , b_{2} , \dots , b_{K}$ صعودی می گوییم اگر: 

$$b_{1} < b_{2} < \dots < b_{K}$$ 

#### راه حل

آرایه $dp[N]$ می سازیم که تعریف آن بدین شکل است:

$min(a[j])$ بطوری که زیر دنباله صعودی به طول i مختوم به j وجود داشته باشد = $dp[i]$

در ابتدا همه عضو های این آرایه بجز $dp[0]$ را برابر بی نهایت قرار می دهیم و $dp[0] = 0$ قرار می دهیم (زیرا دنباله های بطول بیشتر از 0 اول کار وجود ندارند) و سعی می کنیم مرحله مرحله روی آرایه $a$ حرکت کنیم و آرایه $dp$ را آپدیت کنیم

اگر این آرایه را بسازیم جواب سوال ما برابر آخرین خانه نا بی نهایت آرایه خواهد بود زیرا اگر خانه ای بینهایت نباشید یعنی دنباله ای به آن طول در آرایه وجود دارد

پس اگر بتوانیم روشی ارائه دهیم که آرایه $dp$ را با اردر خوبی آپدیت کند سوال حل می شود

ابتدا ادعا می کنیم که آرایه $dp$ صعودی است

??? success "اثبات"
    فرض خلف می کنیم:
    
    $$ 
    \exists \quad j : dp[j] \leq dp[j-1]
    $$

    دنباله جواب $dp[j]$ را در نظر می گیریم و عضو آخر آن را حذف می کنیم حالا آرایه ای به طول $j-1$ داریم که انتهایش کمتر از $dp[j-1]$ است که با تعریف $dp$ متناقض است

    از تناقض حاصل درستی ادعا نتیجه می شود


فرض کنید به خانه $a[i]$ رسیدیم و می خواهیم $dp$ را آپدیت کنیم اولین خانه بزرگتر یا مساوی $a[i]$ در $dp$ را $j$ در نظر می گیریم

ادعا می کنیم تنها خانه در $dp$ که تغییر می کند خانه j ام است

??? success "اثبات"
    ابتدا اثبات می کنیم خانه $j$ تغییر می کند
    می دانیم $dp[j-1] < a[i]$ (طبق تعریف $j$)

    دنباله ی جواب $dp[j-1]$ را در نظر بگیرید و $a[i]$ را به انتهای آن اضافه کنید یک دنباله به طول $j$ خواهیم داشت

    چون همه $dp[0] , dp[1] , \dots , dp[j-1]$ کمتر از $a[i]$ هستند پس تغییر نمی کنند چون دنباله های مختوم به $i$ تنهای بیشتری دارند و طبق تعریف $dp$ تغییری انجام نمی شود

    از طرفی دنباله ای به طول $j , j+1 , \dots , N-1$ وجود ندارد که دارای انتهایی کمتر از $a[i]$ باشد و ما بتوانیم دنباله های به طول $j+1 , j+2 , \dots , N$ با انتهای $a[i]$ بسازیم چون تمام $dp[j] , dp[j+1] , \dots , dp[N-1]$ از $a[i]$ بزرگتر مساوی هستند

پس یک خانه تغییر می کند و از آنجایی که آرایه $dp$ به ترتیب صعودی است پس می توان j را با یک باینری سرچ بدست آورد و آن را تغییر داد

#### تحلیل اردر

از آنجایی که ما برای برای هر $i$ $(1 \leq i \leq N)$ یک باینری سرچ انجام می دهیم و اردر باینری سرچ $log(N)$ است پس در کل سوال از $O(Nlog(N))$ حل شده

#### کد

```cpp linenums="1"

int main() {
    int n;
    cin >> n;

    int a[n+1];
    for(int i = 1 ; i <= n ; i++)
        cin >> a[i];

    int dp[n+1];
    dp[0] = 0;
    for(int i = 1 ; i <= n ; i++)
        dp[i] = 1e9 + 23;

    for(int i = 1 ; i <= n ; i++) {
        int j = lower_bound(dp , dp + n + 1 , a[i]);
        dp[j] = a[i];
    }

    for(int i = 1 ; i <= n ; i++) 
        if(dp[i] == 1e9 + 23) {
            cout << i-1 << "\n";
            return 0;
        }

    return 0;
}

```

همچنین اگر بخواهیم دنباله را خروجی بدهیم (بجای فقط طول آن) می توانیم به ازای هر dp

### LCS

#### مسئله

دو رشته $s , t$ داریم بلندترین زیردنباله برابر این دو رشته چه طولی دارد

$|s| , |t| \leq 10^{3}$

#### راه حل

$dp[i][j]$ می سازیم با تعریف زیر:

بلند ترین زیردنباله برابر در $i$ کاراکتر اول $s$ و $j$ کاراکتر اول $t$ چه طولی است

پایه $dp$:

برای همه $i$ ها از 0 تا |$t$| داریم $dp[0][i] = 0$ (زیرا یک رشته به طول 0 است)

مشابها برای همه $j$ ها از 0 تا |$s$| هم داریم $dp[j][0] = 0$

آپدیت $dp$:

یا کاراکتر $i$ ام $s$ با کاراکتر $j$ ام $t$ برابر است یا اینگونه نیست

اگر اینگونه نباشد آنگاه می توان نتیجه گرفت یکی از دو کاراکتر مورد نظر در بلندترین دنباله $i$ کاراکتر اول $s$ و $j$ کاراکتر اول $t$ نیستند (زیرا اگر هر دو باشند آنگاه کاراکتر $i$ ام $s$ با یک کاراکتر از $t$ مثل $k$ برابر بوده ولی $k < j$ و کاراکتری بعد $i$ در $s$ باقی نمی ماند برای همین کاراکتر $j$ ام $t$ در جواب $dp[i][j]$ نیست)

پس دو حالت داریم که کدام در جواب نباشد و از بین این دو بیشترین را انتخاب می کنیم

$dp[i][j] = max(dp[i-1][j] , dp[i][j-1]);$ 

حال اگر دو کاراکتر برابر بودند آنگاه یک حالت علاوه بر دو حالت بالا هم داریم که این دو هر دو در جواب باشند ولی طبق حرفی که در بالا زدیم اگر $i$ با کاراکتری قبل $j$ جفت شود خود $j$ در جواب نمیاید پس این دو با هم جفت شوند و حاصل برابر $dp[i-1][j-1] + 1$ بشود 

$dp[i][j] = max({dp[i-1][j-1] + 1 , dp[i-1][j] , dp[i][j-1]});$

جواب سوال طبق تعریف $dp$ برابر $dp[|s|][|t|]$ است

 تحلیل اردر:

ما داریم به ازای هر $i$ , $j$ ما $dp[i][j]$ را در $O(1)$ بدست می آوریم پس اردر کل راه حل $O(|s| * |t|)$ است

```cpp linenums="1"

int main() {
    string s , t;
    cin >> s >> t;

    int n = s.size();
    int m = t.size();

    int dp[n+1][m+1];
    for(int i = 0 ; i <= m ; i++)
        dp[0][i] = 0;
    for(int i = 0 ; i <= n ; i++)
        dp[i][0] = 0;

    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= m ; j++) {
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1]);
            if(s[i-1] == t[j-1]) 
                dp[i][j] = max(dp[i][j] , dp[i-1][j-1] + 1);
        }

    cout << dp[n][m];

    return 0;
}

```

برای بدست آوردن خود دنباله هم می توان برای هر $dp[i][j]$ نگه داریم که از کدام یک از $dp[i-1][j-1] , dp[i][j-1] , dp[i-1][j]$ آپدیت شده و آنگاه فقط کافیست از $dp[|s|][|t|]$ شروع به حرکت کنیم اگر $dp[i][j]$ از $dp[i-1][j-1]$ آپدیت شده بود آنگاه این را به دنباله جواب اضافه می کنیم و بعد از هر مرحله هم به کسی که $dp$ راآپدیت کرده برویم و هیمنطوری تا وقتی که کل دنباله ساخته شود

```cpp linenums="1"

int main() {
    string s , t;
    cin >> s >> t;

    int n = s.size();
    int m = t.size();

    int dp[n+1][m+1];
    pair<int , int> par[n+1][m+1]; // (1)!
    for(int i = 0 ; i <= m ; i++)
        dp[0][i] = 0;
    for(int i = 0 ; i <= n ; i++)
        dp[i][0] = 0;

    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= m ; j++) {
            if(dp[i-1][j] < dp[i][j-1]) {
                dp[i][j] = dp[i][j-1];
                par[i][j] = {i , j-1};
            }
            else {
                dp[i][j] = dp[i-1][j];
                par[i][j] = {i-1 , j};
            }
            if(s[i-1] == t[j-1]) 
                if(dp[i][j] < dp[i-1][j-1] + 1) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    par[i][j] = {i-1 , j-1};
                }
        }

    vector<int> a; // (2)!
    vector<int> b; // (3)!

    int x = n;
    int y = m;

    while(x != 0 && y != 0) {
        int i = par[x][y].first;
        int j = par[x][y].second;
        if(x-1 == i && y-1 == j) {
            a.push_back(x);
            b.push_back(y);
        }
        x = i;
        y = j;
    }

    reverse(a.begin() , a.end());
    reverse(b.begin() , b.end());

    for(auto id : a) 
        cout << id << " ";
    cout << "\n";
    for(auto id : b) 
        cout << id << " ";
    cout << "\n";

    return 0;
}

```

1. اینکه $dp[i][j]$ از روی کدام آپدیت می شود را در $par[i][j]$ نگه می داریم
2. اعضای $s$ در دنباله جواب را در این نگه می داریم
3. اعضای $t$ در دنباله جواب را در این نگه می داریم

## سوال ها 

 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">

</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: |
|[Towers](https://cses.fi/problemset/task/1073){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi/){:target="_blank"}| 
|["North-East"](https://codeforces.com/problemsets/acmsguru/problem/99999/521){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Consecutive Subsequence](https://codeforces.com/contest/977/problem/F){:target="_blank"}|1400|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}| 
|[LCS on Permutations](https://codeforces.com/gym/102951/problem/C){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Gym](https://codeforces.com/gyms){:target="_blank"}| 
|[Cow Jog](https://usaco.org/index.php?page=viewproblem2&cpid=496){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-usaco: [Usaco](https://usaco.org/){:target="_blank"}| 
|[ Korney Korneevich and XOR (easy version)](https://codeforces.com/contest/1582/problem/F1){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}| 
|[LCIS](https://codeforces.com/contest/10/problem/D){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li><li>[LCS](/Level2/LIS_LCS/#lcs){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Tourist](https://codeforces.com/contest/76/problem/F){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Global Warming](https://oj.uz/problem/view/CEOI18_glo){:target="_blank"}|2400|<details> <summary>Spoiler</summary> <ul><li>[LIS](/Level2/LIS_LCS/#lis){:target="_blank"}</li></ul> </details>|:judge-ojuz: [OJ](https://oj.uz/){:target="_blank"}|
