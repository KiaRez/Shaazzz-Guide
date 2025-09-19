# کوله پشتی (‌‌knapsack)

## مسئله‌ی کوله پشتی

در مسئله‌ی کوله پشتی (‌‌knapsack) شما یک کوله پشتی دارید که حجم مشخصی دارد. علاوه بر کوله پشتی یک سری وسیله هم دارید و حجم هرکدام نیز به شما داده شده است. شما می‌خواهید طوری تعدادی از این وسیله‌ها را در کوله پشتی قرار دهید که بیشترین فضای ممکن از کوله پشتی اشغال شود. (فرض کنید شکل وسیله‌ها طوری است که فضای خالی میان آن‌ها نمی‌ماند.)

## الگوریتم

بیایید $n$ را برابر تعداد وسایل و $w$ را برابر حجم کوله پشتی قرار دهیم و حجم وسیله‌ی $i$ ام را برابر $a_i$ قرار دهیم. حال می‌خواهیم مسئله را با راهی از $O(n.w)$ حل کنیم. 

آرایه‌ی دوبعدی $dp$ را به ابعاد $(n+1) \times (w+1)$ تعریف می‌کنیم.

سپس می‌گوییم مقدار $dp_{i, j}$ برابر یک است اگر بتوان با استفاده‌ از $i$ وسیله‌ی اول حجم $j$ را پر کرد. یعنی زیرمجموعه‌ای از $i$ وسیله‌ی اول وجود داشته باشد که مجموع حجمشان دقیقا $j$ باشد. در غیر این صورت مقدار $dp_{i, j}$ برابر صفر است. 

حال جواب مسئله‌ی ما بزرگترین اندیس $j$ است که $dp_{n, j}$ برابر یک باشد. 

پایه: با استفاده از صفر وسیله‌ی اول فقط می‌توان حجم صفر را ساخت، پس تمام خانه‌های $dp_{0, j}$ برابر صفر است به جز خانه‌ی $dp_{0,0}$ که برابر یک است. 

به روزرسانی: برای به دست آوردن مقدار $dp_{i, j}$ دو حالت وجود دارد: 

1. یا از وسیله‌ی $i$ ام برای پر کردن حجم $j$ استفاده نشده است، که در آن حالت باید بتوان با $i-1$ وسیله‌ی اول حجم $j$ را پر کرد پس باید $dp_{i-1, j}$ برابر یک باشد. 

2. یا از وسیله‌ی $i$ ام برای پر کردن حجم $j$ استفاده شده است، در این صورت $a_i \le j$ باید باشد و علاوه بر آن باید با $i-1$ وسیله‌ی اول بتوان حجم $j-a_i$ را پر کرد پس باید $dp_{i-1, j-a_i}$ برابر یک باشد. 

اگر یکی از حالات بالا برقرار بود می‌توان با $i$ وسیله‌ی اول حجم $j$ را پر کرد و بنابرین مقدار $dp_{i, j}$ برابر یک است. در غیر این صورت نمی‌توان با $i$ وسیله‌ی اول حجم $j$ را پر کرد و بنابرین مقدار $dp_{i, j}$ برابر صفر است.

### کد

```cpp

bool dp[N][W];

int a[N]; 

int main()

{

    int n, w; cin>>n>>w; 

    for (int i=1; i<=n; i++) cin>>a[i]; 

    dp[0][0]=1;

    for (int j=1; j<=w; j++) dp[0][j]=0; 

    for (int i=1; i<=n; i++){

        for (int j=0; j<=w; j++){

            if(dp[i-1][j]==1) dp[i][j]=1; 

            else if(j>=a[i] && dp[i-1][j-a[i]]==1) dp[i][j]=1; 

            else dp[i][j]=0; 

        }

    }

    int ans=0; 

    for (int j=1; j<=w; j++) if(dp[n][j]==1) ans=j; 

    cout<<ans<<endl;

}

```


### پیچیدگی الگوریتم

پیچیدگی زمانی از $O(n \times w)$ و مقدار حافظه مورد نیاز هم از $O(n \times w)$ است.

### بهینه‌سازی حافظه

اگر کمی دقت کنید متوجه می‌شوید که برای به روزرسانی سطر $i$ ام آرایه فقط به سطر $i-1$ ام آرایه نیاز داریم، پس اگر ما به روزرسانی‌هایمان را به ترتیب سطر به سطر انجام دهیم برای به روزرسانی هر سطر فقط به مقدار $dp$ خانه‌های سطر قبل نیاز داریم، پس نگه داشتن تمام دو بعد آرایه بی فایده است و نگه داشتن دو سطر آرایه کافی است و آن وقت مقدار حافظه مورد نیاز از $O(n+w)$ می‌شود.

#### کد

```cpp

bool dp[2][W];

int a[N]; 

int main()

{

    int n, w; cin>>n>>w; 

    for (int i=1; i<=n; i++) cin>>a[i]; 

    dp[0][0]=1;

    for (int j=1; j<=w; j++) dp[0][j]=0; 

    for (int i=1; i<=n; i++){

        for (int j=0; j<=w; j++){

            if(dp[(i-1)%2][j]==1) dp[i%2][j]=1; 

            else if(j>=a[i] && dp[(i-1)%2][j-a[i]]==1) dp[i%2][j]=1; 

            else dp[i%2][j]=0; 

        }

    }

    int ans=0; 

    for (int j=1; j<=w; j++) if(dp[n%2][j]==1) ans=j; 

    cout<<ans<<endl;

}

```


## صورت‌ دیگر سؤال

فرض کنید وسایل شما علاوه بر حجم ارزش هم دارند. شما می‌خواهید طوری وسایل را در کوله پشتی خود جا دهید که وسایل برداشته شده بیشترین ارزش ممکن را داشته باشند. سعی کنید سؤال را با الگوریتمی از $O(n \times w)$ حل کنید.

### الگوریتم

بیایید ارزش وسیله‌ی $i$ ام را با $b_i$ نشان دهیم. حل کردن این حالت مشابه حالت قبل است. 

آرایه‌ی دوبعدی $dp$ را به ابعاد $(n+1) \times (w+1)$ تعریف می‌کنیم.

سپس می‌گوییم مقدار $dp_{i, j}$ برابر بیشترین ارزشی است که می‌توان با استفاده از $i$ وسیله‌ی اول برداشت به طوری که بتوان آن‌ها را در کوله پشتی‌ای به حجم $j$ قرار داد. 

حال جواب مسئله‌ی ما  $dp_{n, w}$  است. 

پایه: با استفاده از صفر وسیله‌ی اول هیچ چیزی نمی‌توان برداشت پس ارزش برابر صفر است، پس تمام خانه‌های $dp_{0, j}$ برابر صفر است.

به روزرسانی: برای به دست آوردن مقدار $dp_{i, j}$ دو حالت وجود دارد: 

1. یا از وسیله‌ی $i$ ام ستفاده نشده است، که در آن حالت باید کوله‌ای به حجم $j$ با استفاده از $i-1$ وسیله اول طوری پر کرد که بیشترین ارزش ممکن را داشته باشد، این مقدار برابر $dp_{i-1, j}$ است. 

2. یا از وسیله‌ی $i$ ام برای پر کردن حجم $j$ استفاده شده است، در این صورت $a_i \le j$ باید باشد و باید بقیه‌ی حجم $j-a_i$ باقی مانده را با استفاده از $i-1$ وسیله‌ی اول طوری پر کرد که بیشترین ارزش ممکن را داشته باشد، پس مقدار این حالت برابر $b_i + dp_{i-1, j-a_i}$ است.

برای پیدا کردن مقدار $dp_{i, j}$ کافی است بیشترین مقدار از دو حالت بالا را برابر $dp_{i, j}$ قرار دهید. 

مشابه حالت قبلی می‌توان مشاهده کرد که نیاز به نگه داشتن کامل آرایه‌ی دوبعدی نداریم و نگه داشتن دو سطر از آن هم کافی است. 

#### کد

```cpp

int dp[2][W];

int a[N], b[N]; 

int main()

{

    int n, w; cin>>n>>w; 

    for (int i=1; i<=n; i++) cin>>a[i]; 

    for (int i=1; i<=n; i++) cin>>b[i];

    for (int j=0; j<=w; j++) dp[0][j]=0; 

    for (int i=1; i<=n; i++){

        for (int j=0; j<=w; j++){

            dp[i%2][j]=dp[(i-1)%2][j];

            if(j>=a[i]) dp[i%2][j]=max(dp[(i-1)%2][j], b[i]+dp[(i-1)%2][j-a[i]]);

        }

    }

    cout<<dp[n][w]<<endl;

}

```

#### پیچیدگی الگوریتم

پیچیدگی زمانی این الگوریتم از $O(n \times w)$ است و مقدار حافظه مورد نیاز از $O(n+w)$ است.

## منابع بیشتر

+ [knapsack](https://cp-algorithms.com/dynamic_programming/knapsack.html)

## سوال ها 
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[ کوله پشتی ](/Level2/knapsack){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp/){:target="_blank"}|
|[Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[ کوله پشتی ](/Level2/knapsack){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp/){:target="_blank"}|
|[Colored Balls](https://codeforces.com/contest/1954/problem/D){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[ کوله پشتی ](/Level2/knapsack){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Fire](https://codeforces.com/problemset/problem/864/E){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[ کوله پشتی ](/Level2/knapsack){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Antimatter](https://codeforces.com/problemset/problem/383/D){:target="_blank"}|2300|<details> <summary>Spoiler</summary> <ul><li>[ کوله پشتی ](/Level2/knapsack){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
