--- 
hide:
  - footer
comments: true
---
# توپول سورت

## تعریف 

فرض کنین یک گراف جهت دار $G$ با $n$ راس داریم و یک ترتیبی دادیم مثلا دنباله 
$v_1, v_2, \dots, v_n$

که این شرط رو داره:

اگر $v_i$ به $v_j$ یال داشت اون وقت $i < j$$

به این دنباله دنباله $sort$ $topological$ شده گراف $G$ میگن که البته برای بعضی گراف ها وجود نداره

## لم مهم

### صورت لم

دنبال $sort$ $tpoplogical$ برای گراف جهتدار $G$ وجود دارد اگر و تنها اگر گراف $G$ دور نداشته باشد یا به عبارت دیگر $DAG$ باشد

### اثبات لم

ابتدا اثبات می کنیم اگر توپول سورت وجود داشته باشد آنگاه گراف $G$ دور ندارد

فرض خلف می کنیم که اینطور نیست و با وجود توپول سورت دور هم در گراف وجود دارد 

سمت راست ترین راس دور در دنباله توپول سورت را در نظر می گیریم این راس حتما به سمت چپ یال دارد زیرا در دور است و هر راس در دور یک یال ورودی و خروجی دارد از آنجایی که این راس راست ترین راس در دور است پس خروجی آن به سمت چپ است و این با شرط توپول سورت تناقض دارد در نتیجه اگر توپول سورت وجود داشته باشد دور وجود ندارد

حال اثبات می کنیم اگر گرافی بدون دور داشته باشیم آنگاه حتما توپول سورتی وجود دارد

اینکار را با دادن یک الگوریتم برای ساخت توپول سورت توضیح میدهیم:

می دانیم در هر گراف جهتداری که دور ندارد یک راس وجود دارد که ورودی ندارد (اثبات این موضوع پایین تر آمده است) آن راس $source$ می نامیم این راس را پاک کرده و به دنباله ای که می سازیم اضافه می کنیم و سپس آن را از گراف حذف می کنیم چون گراف جدید زیر گرافی از گراف $G$ است پس در آن نیز دوری نیست (وگرنه در $G$ هم دور وجود داشت) و حال دوباره کل اینکار ها را با گراف جدید انجام میدهیم در نهایت دنباله ساخته شده توپول سورت است زیرا هر راسی ورودی نداشته را اضافه کردیم و کسی از جلوتر نمی تواند به آن یال داشته باشد و گرنه راس اضافه شده راس $source$ نبوده

??? success "اثبات"
    در اینجا اثبات می کنیم که در گراف جهتدار بدون دور حتما یک راس بدون ورودی وجود دارد

    فرض خلف می کنیم

    یک راس دلخواه مثلا $v$ رو در نظر بگیرید می دونیم این حداقل یک ورودی داره یکی از ورودی هارو به دلخواه انتخاب می کنیم مثلا باشه $p[v]$ باز برای این راس هم یک ورودی داریم مثلا باشه $p[p[v]]$ و همین کارو ادامه میدیم چون راس ها متناهی هستند پس در یک مرحله به راس تکراری می رسیم پس دوری در گراف وجود دارد و این مخالف فرض است 


## الگوریتم های پیدا کردن توپول سورت

### روش اول

از روشی که در اثبات استفاده کردیم استفاده می کنیم هر مرحله یک راس با درجه ورودی 0 رو به دنباله اضافه می کنیم و همینطور ادامه میدیم تا وقتی همه راس هارو توی دنباله بریزیم

برای اینکار یک $set$ میگیریم که توش درجه ورودی هر راس و خود راس رو ریختیم و هر مرحله اولین عضو $set$ رو حذف می کنیم (کمترین درجه ای که داریم که اثبات شد اگر دور نداشته باشیم همیشه 0 عه)

!!! info "نکته"
    میشه ازین کار برای فهمیدن اینکه دور داریم یا نه هم استفاده کرد اگر بجایی رسیدیم که کوچکترین درجه 0 نبود یعنی دور داریم

بعد از اینکه این عضو رو به دنباله اضافه کردیم حالا اون رو حذف می کنیم و ورودی تمام راس هایی که این بهشون یال داشت رو یکدونه کم می کنیم

#### کد

```cpp linenums="1"

int n; //(1)!
vector<int> G[N]; //(2)!
int in[N]; //(3)!
set<pair<int , int>> s;

vector topol_sort() {
    for(int i - 1 ; i <= n ; i++)
        s.insert({in[i] , i});

    vector<int> ans;

    while(s.size()) { //(4)!
        int v = s.begin()->second;
        ans.push_back(v);
        s.erase(s.begin());

        for(auto u : G[v]) { //(5)!
            s.erase({in[u] , u});
            in[u]--;
            s.insert({in[u] , u});
        }
    }

    return ans;
}
```

1. تعداد راس های گراف
2. نگهدارنده یال های هر راس
3. درجه ورودی هر راس 
4. در هر مرحله یک راس از داخل $s$ حذف  شده و به وکتور جواب اضافه می شود پس اگر اینکار را تا وقتی $s$ خالی شود انجام دهیم همه راس ها به وکتور اضافه می شوند
5. در این فور درجه راس هایی که $v$ به آنها یال دارد را کم می کنیم و در $set$ آپدیت می کنیم

بخاطر اینکه $N + M$ بار داریم از $set$ عضو تغییر می دهیم این روش از اردر $O((N + M)lg(N))$ است

### روش دوم

یک روش دیگر این است که راس ها را بر اساس تایم پایان در $dfs$ یا به عباری $finishing time$ اضافه کنیم و در انتها دنباله را برعکس کنیم

با اینکار ما هر راس را بعد از اینکه تمام کسانی که آنها یال دارد اضافه می کنیم در نتیجه تمام یال های ما به یک طرف است

#### کد

```cpp linenums="1"

int n; //(1)!
vector<int> G[N]; //(2)!
int mark[N]; 
vector<int> ans;

void dfs(int v) {
    mark[v] = 1;
    for(auto u : G[v]) 
        dfs(u);
    ans.push_back(v);
}

vector topol_sort() {
    for(int i = 1 ; i <= n ; i++) //(3)!
        if(!mark[i])
            dfs(i);

    reverse(ans.begin() , ans.end());
    return ans;
}
```

1. تعداد راس های گراف
2. نگهدارنده یال های هر راس
3. از هر راسی که مارک نشده یک بار $dfs$ می زنیم اینکار برای اینه امکان داره راسی که ازش $dfs$ می زنیم به همه راس ها مسیر نداشته باشه البته این کار مشکلی بوجود نمیاره زیرا اگر راسی دیده نشه حتما یالی به باقی نداشته و بعد از برعکس کردن اونا قبلش میان

## منابع بیشتر

+ [topological-sort](https://cp-algorithms.com/graph/topological-sort.html)

## سوال ها 
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Topological Sorting](https://www.spoj.com/problems/TOPOSORT/){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-spoj: [Spoj](https://www.spoj.com/){:target="_blank"}|
|[Game Routes](https://cses.fi/problemset/task/1681){:target="_blank"}|1400|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topol_sort){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi/){:target="_blank"}|
|[Quantum Superposition](https://open.kattis.com/problems/quantumsuperposition){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|[Kattis](https://open.kattis.com/){:target="_blank"}|
|[Fox And Names](https://codeforces.com/problemset/problem/510/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Game Routes](https://cses.fi/problemset/task/1679){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi/){:target="_blank"}|
|[Milking Order](https://usaco.org/index.php?page=viewproblem2&cpid=838){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-usaco: [Usaco](https://usaco.org/){:target="_blank"}|
|[Pattern Matching](https://codeforces.com/problemset/problem/1476/E){:target="_blank"}|2300|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Course Schedule II](https://cses.fi/problemset/task/1757){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi/){:target="_blank"}|
|[Ex - Constrained Topological Sort](https://atcoder.jp/contests/abc304/tasks/abc304_h){:target="_blank"}|2500|<details> <summary>Spoiler</summary> <ul><li>[توپول سورت](/Level2/topolsort){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp/){:target="_blank"}|
