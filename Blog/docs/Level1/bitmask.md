--- 
hide:
  - footer
---
# عملیات های بیتی

## توضیحات: 
### مبنای ۲ اعداد
در دنیای کامپیوتر، [مبنای ۲](https://fa.wikipedia.org/wiki/%D8%B1%D9%82%D9%85_%D8%AF%D9%88%D8%AF%D9%88%DB%8C%DB%8C) اعداد، مثل مبنای ۱۰ از اهمیت زیادی برخوردار هستند، به صورت کلی، در دنیای کامپیوتر هر چیزی به دنباله از ۰ و ۱ ها مدل میشوند. همچنین هر رقم در مبنای ۲ اعداد که میتواند مقدار ۰ یا ۱ داشته باشد بیت نامیده میشود.

به طور کلی، متغیر از جنس unsigned int در سی پلاس پلاس، از ۳۲ بیت تشکیل شده، برای همین یک متغیر از جنس unsigned int میتواند مقادیر ۰ تا $2^{32} - 1$ را به خود بگیرد. این موضوع برای متغیر از جنس int کمی پیچیده تر است چرا که میتوان اعداد منفی را در int ذخیره کرد(در صورت علاقه، برای مطالعه بیشتر به [این لینک](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjE8N-o-t38AhUUcfEDHcffCdoQFnoECAkQAQ&url=https://www.geeksforgeeks.org/how-the-negative-numbers-are-stored-in-memory/&usg=AOvVaw12olVbdS2FmPWHDqiHGHRt) مراجعه کنید).

همچنین برای تعریف یک متغیر از جنس ۰ یا ۱ در سی پلاس پلاس، میتوان از bool استفاده کرد.

### عملیات های بیتی
برای ۲ بیت مانند $a$ و $b$ (که تنها مقادیر ۰ یا ۱ را به خود میگیرند) چند عملگر معروف(مانند ضرب و جمع برای اعداد صحیح) تعریف میشود:

+ عملگر not: این عملگر یک بیت مانند $a$ را گرفته، و برعکس آن را خروجی میدهد(اگر ۰ بود ۱ و در غیر این صورت ۰ را خروجی میدهد).
+ عملگر and: این عملگر ۲ بیت $a$ و $b$ را گرفته و اگر **هر دوی آنها** برابر ۱ بودند، ۱ را خروجی میدهد(در غیر اینصورت حاصل عملگر and صفر است).
+ عملگر or: این این عملگر ۲ بیت $a$ و $b$ را گرفته و اگر **حداقل** یکی از آنها برابر ۱ بود، ۱ را خروجی میدهد(در غیر اینصورت حاصل عملگر or صفر است).
+ عملگر xor:  این این عملگر ۲ بیت $a$ و $b$ را گرفته و اگر **دقیقا** یکی از آنها برابر ۱ بود، ۱ را خروجی میدهد(در غیر اینصورت حاصل عملگر xor صفر است).

این ۴ عملیات، در سی پلاس پلاس از قبل تعریف شده و قابل استفاده هستند:

```cpp
bool a = true;
bool b = false;

bool c = !a; // not
bool d = a & b; // and
bool e = a | b; // or
bool f = a ^ b; // xor
```
همچنین به سادگی، میتوان این ۴ عملیات را روی ۲ متغیر از جنس int نیز تعریف کرد، برای مثال، اگر $a$ و $b$ تو متغیر از جنس int باشند، بیت $i$ام $a \& b$ را برابر با and بیت $i$ام $a$ و بیت $i$ام $b$ قرار میدهیم، بدین صورت، حاصل and دو متغیر $a$ و $b$ نیز یک عدد ۳۲ بیتی خواهد بود.

برای همین، این ۴ عملیات با تعریف ذکر شده، در سی پلاس پلاس برای متغیر های عددی نیز تعریف شده اند(همچنین خروجی هر یک برای درک بهتر شما داده شده):
```cpp
unsigned int a = 12, b = 5; // a = 000...01100, b = 000...00101

unsigned int c = ~a; // not, c = 111...10011
unsigned int d = a & b; // and, d = 000...00100
unsigned int e = a | b; // or, e = 000...01101
unsigned int f = a ^ b; // xor, f = 000...01001
```
در سی پلاس پلاس، روی ۲ عدد $a$ و $k$ دو عملگر پرکاربرد دیگر نیز تعریف میشوند:
+ شیفت چپ: $k$ رقم ابتدایی(از سمت راست) در نمایش دودویی عدد $a$ را حذف کرده و $k$ رقم ۰ به انتهای $a$ در نمایش دودویی اش اضافه میکند.
+ شیفت راست: $k$ رقم انتهایی در نمایش دودویی عدد $a$ را حذف کرده و $k$ رقم ۰ به ابتدای $a$ در نمایش دودویی اش اضافه میکند.

```cpp
int a = 7; // a = 000...00101
int b = (a << 2); // left shift, b = 000...0010100
int c = (a >> 2); // right shift, c = 000...0001
```

#### گرفتن $i$امین بیت یک عدد
از ترکیب ۶ عملیات پایه ای ذکر شده، میتوان عملیات های پیچیده تری ساخت، برای مثال میتوان به راحتی اثبات کرد که کد زیر، $k$امین بیت عدد $n$ را به عنوان خروجی بر میگرداند.(همچنین از شبه کد زیر در ادامه استفاده زیادی شده، برای همین توصیه میشود به خوبی آن را درک کنید).

```cpp
int n, k;
cin >> n >> k;
cout << ((n >> k) & 1) << endl;
```
### نمایش زیرمجموعه های یک مجموعه
یکی از کاربرد مبنای ۲ اعداد در دنیای الگوریتم، نمایش زیرمجموعه های یک مجموعه است، به طور کلی، میتوان تناظری یک به یک بین تمام اعداد $k$ بیتی و تمام زیرمجموعه های یک مجموعه $k$ عضوی به صورت زیر برقرار کرد:

اگر عضو $i$ام مجموعه(از ۰ تا $k - 1$) در زیرمجموعه دلخواه حضور داشت، بیت $i$ام عدد ذکر شده را ۱ گذاشته و در غیر این صورت بیت متناظر را ۰ میگذاریم.

به طور عامیانه، به عدد نمایانگر یک زیرمجموعه از مجموعه $k$ عضوی، **مسک(mask)** آن مجموعه گفته میشود.

حال با استفاده از تناظر ذکر شده، میتوان کدی زد که یک مجموعه $n$ عضوی را از ورودی بگیرد و تمام زیرمجموعه های آن را چاپ کند.

برای این کار کافیست روی تمام مقادیر ۰ تا $2^k$ فور زده و به ازای هر بیت ۱، عضو متناظر با آن بیت را در زیرمجموعه قرار دهیم.($O(2^n.n)$)

```cpp
vector<int> vec;
int n;
cin >> n;
for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    vec.push_back(x);
}

for (int mask = 0; mask < (1 << n); mask++) {
    for (int b = 0; b < n; b++)
            if (((mask >> b) & 1))
                cout << vec[b] << ' ';
    cout << endl;
}

// ((mask >> b) & 1) = b_omin bit mask
```

دقت کنید میتوان ثابت کرد که مقدار $1 << n$ برابر ۲ به توان $n$ است.	

!!! تمرین
    سعی کنید با گرفتن دو مسک متناظر با دو زیرمجموعه، بفهمید آیا اولی زیرمجموعه دومی است یا خیر.


#### نمایش زیرمجموعه های هر زیرمجموعه
در برخی از سوالات، نیاز میشود به ازای هر زیرمجموعه، روی تمام زیرمجموعه های آن زیرمجموعه فور بزنیم.به صورت کلی، به تمام دوتایی مرتب های ($B, C$) به شکل $C \subset B \subset A$ نیاز داریم.(میتوان ثابت کرد که تعداد این دوتایی مرتب ها، برابر $3^n$ است)، یک راه ساده برای اینکار، این است که به ازای هر زیرمجموعه، تمام زیرمجموعه های آن را پیدا کنیم، اما کد ساده تری نیز برای اینکار وجود دارد(اثبات به خواننده واگذار میشود.)

```cpp
for (int mask_B = 0; mask_B < (1 << n); mask_B++) {
    for (int mask_C = mask_B; mask_C > 0; mask_C = (mask_C - 1) & mask_B) {
        // کد دلخواه
    }

    // دقت کنید در این کد زیرمجموعه تهی به عنوان مجموعه دوم چک نمیشود و در صورت نیاز، در پایان آن را چک کنید
}
```
### چند تابع کاربردی در GCC:

+ تعداد بیت های عدد $x$ در نمایش دودویی: **__builtin_popcount(x)**
+ تعداد بیت های ۰ بعد آخرین بیت ۱ عدد $x$ در نمایش دودویی:  **__builtin_ctz(x)**
+ تعداد بیت های ۰ قبل اولین بیت ۱ عدد $x$ در نمایش دودویی:  **__builtin_clz(x)**
+ کف لاگ در مبنای ۲ $x$(بدون خطای اعشاری): **__lg(x)**

!!! warning ""
    برای استفاده توابع فوق برای متغیر های از جنس long long، به انتهای آنها عبارت ll را اضافه کنید.


### منابع بیشتر

+ [Bitwise operations for beginners](https://codeforces.com/blog/entry/73490)
+ [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html)


## سوال ها 
| سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Fedor and new game](https://codeforces.com/problemset/problem/467/B){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Petr and a Combination Lock](https://codeforces.com/contest/1097/problem/B){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[New Year's Eve](https://codeforces.com/problemset/problem/912/B){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Preparing Olympiad](https://codeforces.com/contest/550/problem/B){:target="_blank"}|1400|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Xor Guessing](https://codeforces.com/problemset/problem/1207/E){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[AND, OR and square sum](https://codeforces.com/contest/1368/problem/D){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Apollo versus Pan](https://codeforces.com/contest/1466/problem/E){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Bitwise Queries (Hard Version)](https://codeforces.com/problemset/problem/1451/E2){:target="_blank"}|2300|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Anton and School](https://codeforces.com/contest/734/problem/f){:target="_blank"}|2500|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Keep Xor Low](https://codeforces.com/problemset/problem/1616/H){:target="_blank"}|2900|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li> <li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li> <li>divide</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
