--- 
hide:
  - footer
---
# باینری سرچ

## توضیحات 
### باینری سرچ

#### مسئله

بازی ای دو نفره داریم که دو فرد $A$ و $B$ در آن بازی میکنند. ابتدا $A$ یک عدد طبیعی از $1$ تا $10^{9}$ انتخاب میکند. سپس $B$ بایستی عدد انتخاب شده را حدس بزند. او حداکثر $40$ بار فرصت حدس زدن دارد. هربار که $B$ عددی را حدس بزند. $A$ به او میگوید که عدد حدس زده شده کوچکتر از عدد انتخاب شده هست یا نه؛ به عبارتی اگر $A$ عدد $k$ را انتخاب کرده باشد و $B$ عدد $x$ را حدس زده باشد. اگر $x < k$ باشد آنگاه نفر $A$ میگوید **بله** در غیر این صورت **خیر**.

همچنین $B$ یک فرصت برای حدس نهایی دارد که اگر حدس او با عدد انتخاب شده یکی باشد، برنده شده در غیر این صورت میبازد. حال ما بایستی به عنوان فرد $B$ برنده بازی بشویم.

#### راه حل

دو متغیر $L$ و $R$ را تعریف میکنیم. ابتدا 
$L = 0$
و 
$R = 10^{9}$
قرار میدهیم. میدانیم 
$L < k$
و
$k \leq R$
است. حال متغیر $mid$ را تعریف میکنیم و آنرا برابر با
$\lfloor \frac{L + R}{2} \rfloor$
قرار میدهیم. حال عدد $mid$ را از $A$ میپرسیم اگر گفت که عدد داده شده از $k$ کوچکتر است،
$L = mid$
قرار میدهیم در غیر این صورت
$R = mid$
قرار میدهیم. حال به ازای $L$ و $R$ جدید میدانیم 
$L < k$
و
$k \leq R$
است.

این روند را ادامه میدهیم تا زمانی که
$L+1 = R$
شود. سپس $R$ را به عنوان حدس نهایی خروجی میدهیم.

#### تعداد عملیات های راه حل

فرض کنیم
$len = R - L$
باشد. پس از هر بار پرسش و تغییر مقادیر $L$ و $R$ میتوان گفت اگر مقدار جدید $len$ را برابر با
$len^{\prime}$
در نظر بگیریم 
$len^{\prime} \leq \lceil \frac{len}{2} \rceil$
است.
??? success "اثبات"

    $mid = \lfloor \frac{L + R}{2} \rfloor = \lfloor \frac{2 * L + len}{2} \rfloor = L + \lfloor \frac{len}{2} \rfloor$
    
    اگر $R = mid$ شود:
    $len^{\prime} = L + \lfloor \frac{len}{2} \rfloor - L = \lfloor \frac{len}{2} \rfloor$
    
    اگر $L = mid$ شود:
    $len^{\prime} = L + len - (L + \lfloor \frac{len}{2} \rfloor) = len - \lfloor \frac{len}{2} \rfloor =  \lceil \frac{len}{2} \rceil$

حال چون هر بار مقدار $len$ به حداکثر 
$\lceil \frac{len}{2} \rceil$
تبدیل میشود و ما وقتی
$len = 1$
شود عملیات هارا تمام میکنیم، حداکثر
$\lceil log(10^{9}) \rceil$
پرسش انجام میدهیم (‌مقدار $len$ در ابتدا برابر با
$10^{9}$
است.) که برابر با $30$ پرسش میشود.

#### تعریف کلی

فرض کنیم تابع $f$ را داریم که عدد صحیح ورودی میگیرد. میدانیم عدد صحیح $y$ ای وجود دارد به طوری که به ازای هر عدد صحیح $x$:

- $f(x) = 0$ است اگر و تنها اگر $x < y$

- $f(x) = 1$ است اگر و تنها اگر $y \leq x$

همچنین میدانیم دو عدد صحیح $L$ و $R$ وجود دارند به طوری که 
$L < y$
و
$y <= R$
است.

میخواهیم عدد $y$ را پیدا کنیم. برای اینکار دقیقا مانند سوال بالا میتوان رفتار کرد و در
$O(log(R - L))$
عملیات مسئله را حل کرد.

#### کد
در این جا کدی مربوط به سوالی که حل کردیم را مشاهده میکنیم.

``` cpp linenums="1" 
int ask(int x){ // (1)!

	cout << "Ask: " << x << endl;

	int res;
	cin >> res;

	return res;
}

int main(){

	int L = 0, R = 1'000'000'000; // (2)!

	while(L + 1 < R){
		int mid = (L + R) >> 1; // (3)!		
		if (ask(mid) == 0) L = mid;
		else R = mid;
	}

	cout << "Hads nahaei: " << R << endl;
}
```

1.	تابع 
`#!cpp ask`
 معادل تابع $f(x)$ در حالت کلی مسئله است که به ازای مقادیر کوچکتر از عدد مورد نظر $0$ و در غیر اینصورت $1$ میدهد.

2.	مقدار $L$ و $R$ که میدانیم  قطعا عدد مورد نظر بزرگتر اکید از $0$ و کوچکتر مساوی $10^{9}$ است.

3.	در اینجا میتوان ثابت کرد این عملیات معادل کف تقسیم بر دو میباشد.

#### باینری سرچ پیوسته

میتوان در تمامی تعاریف گفته شده به جای عدد صحیح، عدد حقیقی قرار داد. مشکلی که پیش خواهد آمد این است که در این صورت الگوریتم شرط پایان ندارد‌ ($L + 1 = R$).

اما نکته ای که وجود دارد این است که در سوال های مربوطه همواره با تعدادی رقم اعشار قرار است جواب سوال را خروجی بدهیم (‌برای مثال با $6$ رقم اعشار).

پس میتوان شرط جدیدی برای پایان الگوریتم گذاشت‌ 
($R - L > 0.000001$)
. اما به خاطر خطا های محاسباتی در اعشار در ++C این روش زیاد مناسب نیست.

میتوان تا جایی باینری سرچ را ادامه داد تا مطمعن باشیم مقدار $L$ و $R$ تا $6$ رقم اعشار دقیق شده باشد. میتوان با استدلالی مشابه حالت گسسته باینری سرچ گفت تعداد این عملیات ها برابر با
$\lceil log(R - L * 10^{6}) \rceil$
میباشد

کد این دو روش به شکل زیر میباشد:

- روش اول:

``` cpp linenums="1" 

int ask(double x){

	cout << fixed << setprecision(6) << "Ask: " << x << endl; // (1)!

	int res;
	cin >> res;

	return res;
}

int main(){

	double L = 0, R = 1e9;
	double eps = 0.000001; // (2)!

	while(R - L > eps){
		double mid = (L + R) / 2; // (3)!
		if (ask(mid) == 0) L = mid;
		else R = mid;
	}

	cout << fixed << setprecision(6) << "Hads nahaei: " << R << endl; 
}
```

1.	به این شیوه عدد $x$ را با $6$ رقم اعشار خروجی میدهیم.

2.	دقت اعشاری که قرار است خروجی بدهیم.

3.	در اینجا چون با اعداد اعشاری سر و کار داریم دیگر از عملگر شیفت به راست (‌ << ) نمیتوانیم استفاده کنیم.

حال کد روش دوم را میبینیم.

روش دوم:

``` cpp linenums="1" 

int ask(double x){

	cout << fixed << setprecision(6) << "Ask: " << x << endl;

	int res;
	cin >> res;

	return res;
}

int main(){

	double L = 0, R = 1e9;

	for (int i = 1; i <= 60; i++){ // (1)!
		double mid = (L + R) / 2;
		if (ask(mid) == 0) L = mid;
		else R = mid;
	}

	cout << fixed << setprecision(6) << "Hads nahaei: " << R << endl;
}

```

1.	میدانیم
$\lceil log(10^{9} * 10^{6}) \rceil \leq 50$
میباشد پس با تعداد بار پرسیدن بیشتر مساوی $50$ بار از دقت جواب اطمینان خواهیم داشت.

### ترنری سرچ

#### تعریف کلی

تابعی به نام $f$ داریم. میدانیم دو عدد صحیح $y$ و $z$ وجود دارد که $y \leq z$ و به طوری که به ازای هر عدد صحیح $x$:


- $f(x) > f(x+1)$ است اگر و تنها اگر $x < y$

- $f(x) = f(x+1)$ است اگر و تنها اگر $y \leq x < z$

- $f(x) < f(x+1)$ است اگر و تنها اگر $z \leq x$

همچنین دو عدد $L$ و $R$ را داریم به طوری که  $L < y$ و $z \leq R$، میخواهیم عدد k را پیدا کنیم به طوری که 
$y \leq k \leq z$
باشد.

#### راه حل

تابع $g(x)$ را تعریف میکنیم به شکل زیر:

- $g(x) = 1$ اگر و تنها اگر $f(x) \leq f(x+1)$

- $g(x) = 0$ اگر و تنها اگر $f(x) > f(x+1)$

میتوان مشاهده کرد که تابع $g(x)$ باینری سرچ پذیر است و مقداری که به ما میدهد برابر با $y$ است که شرایط $k$ را دارد پس در $O(log(R-L))$ عملیات مسئله حل میشود.

#### ترنری سرچ پیوسته

باز میتوان به جای استفاده از اعداد صحیح مسئله را به اعداد حقیقی گسترش داد.

!!! danger "مهم"

	تعاریف در حالت حقیقی دستخوش تغییرات مهمی میشود ولی با نگاه کلی میتوان دید مشابه حالت قبل است.
    
   	به ازای تابع $f$ میدانیم دو عدد $y$ و $z$ که $y \leq z$ وجود دارند به طوری که به ازای هر دو عدد $a$ و $b$ که $a < b$ است:
   	
   	- اگر $b < y$ باشد، آنگاه $f(a) > f(b)$ است.
   	- اگر $y \leq a$ و $b \leq z$ باشد، آنگاه $f(a) = f(b)$ است.
   	- اگر $z \leq a$ باشد، آنگاه $f(a) < f(b)$ است.
   	
   	به عبارتی میتوان گفت تابع f محدب است. ([تابع محدب چیست؟](https://en.wikipedia.org/wiki/Convex_function))

باز فرض میکنیم با $6$ رقم اعشار جواب را میخواهیم محاسبه کنیم. یک روش این است که همان روش حالت گسسته مسئله را اجرا کنیم و مقدار $g(x)$ به جای اینکه به $f(x)$ و $f(x+1)$ وابسته باشد به $f(x)$ و $f(x+0.000001)$ باشد‌ (زیرا میخواهیم با این دقت جواب را محاسبه کنیم). پس باز با باینری سرچ مسئله را حل کنیم. در این وضعیت دوباره ممکن است به همان مشکل خطای محاسبه اعداد اعشاری در ++C برخورده میکنیم.

در این روش ابتدا دو متغیر $midl$ و $midr$ تعریف میکنیم به طوری که
$midl = \frac{2 * L + R}{3}$ و $midr = \frac{L + 2 * R}{3}$ باشد.
(میتوان ثابت کرد اگر بازه $L$ تا $R$ را به $3$ بازه مساوی تقسیم کنیم دو سر دیگر این سه بازه $midl$ و $midr$ خواهد بود. اثبات این موضوع با شما :) )

حال دو حالت خواهیم داشت:

- اگر $f(midl) \geq f(midr)$ آنگاه $L = midl$ قرار میدهیم.

- اگر $f(midl) < f(midr)$ آنگاه $R = midr$ قرار میدهیم.

فرض کنیم حالت اول رخ داده است. میخواهیم بگوییم با فرض اینکه قبل از انجام عملیات عدد $k$ ای میان $L$ و $R$ وجود داشت، بعد از عملیات نیز هنوز عددی میان $L$ و $R$ هست که خاصیت مورد نظر برای عدد $k$ را داشته باشد.

- اگر $f(midl) > f(midr)$: میتوان به راحتی گفت که $midl < y$ است پس اگر در بازه $[L , R]$ عدد $k$ وجود داشت در بازه $[midl , R]$ نیز وجود خواهد داشت.

- اگر $f(midl) = f(midr)$: میتوان باز به راحتی گفت که $midl < z$ است پس در بازه $[midl , R]$ قطعا عدد $k$ مورد نظر وجود خواهد داشت زیرا در بازه $[L, R]$ وجود داشته است.

اگر حالت دوم رخ داده باشد نیز میتوان با استدلال مشابه گفت که هنوز مقدار $k$ مناسب در بازه وجود خواهد داشت.

در این الگوریتیم اگر $len = R - L$ تعریف کنیم و $len^{\prime}$ را مقدار بعدی $len$ قرار دهیم، میتوان گفت که $len^{\prime} = \frac{2 * len}{3}$ است. و میتوان ثابت کرد که در حالت گسسته این الگوریتم از $O(log(R-L))$ است. در حالت پیوسته نیز ماننده حالت پیوسته باینری سرچ به تعدادی این کار را انجام میدهیم تا مطمعن باشیم تا $6$ رقم اعشار درست حساب شده است که تعداد این بار ها از $O(log((R-L)*10^{6}))$ است.

#### کد

``` cpp linenums="1" 

int ask(double x){ // (1)!

	cout << fixed << setprecision(6) << "Ask: " << x << endl;

	int res;
	cin >> res;

	return res;
}

int main(){

	double L = 0, R = 1e9; // (2)!

	for (int i = 1; i <= 100; i++){ // (4)!
		double midl = (2 * L + R) / 3;
		double midr = (L + 2 * R) / 3;

		if (ask(midl) <= ask(midr)) L = midl;
		else R = midr;
	}

	cout << fixed << setprecision(6) << "Hads nahaei: " << R << endl; // (3)!
}


```

1.	تابع 
`#!cpp ask`
در این جا نقش تابع $f(x)$ را برای ما ایفا میکند و میتواند به جای آن هر تابعی ای با خواص $f(x)$ باشد. همچنین میتواند خروجی $f(x)$ به جای عدد صحیح عدد اعشاری باشد که در الگوریتم ما اهمیتی ندارد.

2.	مقادیر $L$ و $R$ را چیزی قرار میدهیم که میدانیم شرایط گفته شده برقرار اند

3.	در این حالت $L$ با $R$ فرقی ندارد و هردو جواب مسئله هستند

4.	میتوان ثابت کرد که $100$ مرحله برای گرفتن دقت مورد نظر کافی است.

### توابع ++C

در ++C ما تابع
 `#!cpp lower_bound(a + l, a + r, x)` 
 را داریم که در یک آرایه سورت $a$ شده به ما پوینتر اولین خانه در یک بازه که بزرگتر مساوی یک عدد دلخواه است را به ما میدهد که قابل تبدیل به اندیس آن خانه و مقدار آن خانه است.

``` cpp linenums="1" 
int a[7] = {2, 3, 7, 7, 9, 10, 13};
int *x = lower_bound(a, a + 7, 5); // (1)!
int idx = lower_bound(a + 2, a + 7, 7) - a; // (2)!
int val = *lower_bound(a + 4, a + 6, 10); // (3)!
```

1.	پوینتر اولین خانه بزرگتر مساوی $5$ را در کل آرایه به ما میدهد (‌یعنی پوینتر خانه $2$ آرایه).

2.	اندیس اولین خانه بزرگتر مساوی $7$ را در خانه های اندیس $2$ تا اخر آرایه به ما میدهد (یعنی اندیس $2$ را خروجی میدهد).

3.	مقدار اولین خانه بزرگتر مساوی $10$ را در خانه های اندیس $4$ تا $5$ به ما میدهد ( یعنی مقدار خانه $5$ یعنی $10$).

همچنین ما تابع 
`#!cpp upper_bound(a + l, a + r, x)`
 را داریم که مشابه 
`#!cpp lower_bound`
عمل میکند ولی به جای مقدار بزرگتر مساوی دنبال مقدار بزرگتر اکید میگردد و پیاده سازی آن نیز مشابه است.

``` cpp linenums="1" 
int a[7] = {2, 3, 7, 7, 9, 10, 13};
int *x = upper_bound(a, a + 7, 5); // (1)!
int idx = upper_bound(a + 2, a + 7, 7) - a; // (2)!
int val = *upper_bound(a + 2, a + 6, 9); // (3)!
```

1.	پوینتر اولین خانه بزرگتر $5$ را در کل آرایه به ما میدهد (‌یعنی پوینتر خانه $2$ آرایه).

2.	اندیس اولین خانه بزرگتر $7$ را در خانه های اندیس $2$ تا اخر آرایه به ما میدهد (یعنی اندیس $4$ را خروجی میدهد).

3.	مقدار اولین خانه بزرگتر $9$ را در خانه های اندیس $2$ تا $5$ به ما میدهد ( یعنی مقدار خانه $5$ یعنی $10$).


همچنین میتوان توابع
`#!cpp upper_bound`
 و 
`#!cpp lower_bound`
  را روی وکتور استفاده کرد

``` cpp linenums="1" 
vector<int> a = {2, 3, 7, 7, 9, 10, 13};
vector<int> *x = upper_bound(a.begin(), a.end(), 5); // (1)!
int idx = lower_bound(a.begin() + 2, a.end(), 7) - a.begin(); // (2)!
int val = *upper_bound(a.begin() + 2, a.begin() + 6, 9); // (3)!
```

1.	پوینتر اولین خانه بزرگتر $5$ را در کل آرایه به ما میدهد (‌یعنی پوینتر خانه $2$ آرایه).

2.	اندیس اولین خانه بزرگتر  مساوی $7$ را در خانه های اندیس $2$ تا اخر آرایه به ما میدهد (یعنی اندیس $2$ را خروجی میدهد).

3.	مقدار اولین خانه بزرگتر $9$ را در خانه های اندیس $2$ تا $5$ به ما میدهد ( یعنی مقدار خانه $5$ یعنی $10$).

در نهایت میتوان به این دو تابع تابع
`#!cpp cmp`
داد تا برای مقایسه به شیوه دیگری استفاده شود.

!!! info "نکته"

	قبل از اینکه به توابع 
	`#!cpp upper_bound`
	و
    `#!cpp lower_bound`
	تابع 
	`#!cpp cmp`
	را بدهیم بایستی آرایه را بر اساس تابع
	`#!cpp cmp`
	سورت شده باشد.


``` cpp linenums="1" 

bool cmp(int x, int y){
	return x > y; // (1)!
}

int main(){
	vector<int> a = {2, 3, 7, 7, 9, 10, 13}; // (2)!
	
	sort(a.begin(), a.end(), cmp); // (3)!
	
	int idx = lower_bound(a.begin(), a.end(), 5, cmp) - a.begin() // (4)!
}

```

1.	قرار است این تابع از بزرگ به کوچک اعداد وکتور را سورت کند.

2.	اعداد آرایه که در ابتدا طبق تابع 
`#!cpp cmp`
مرتب نشده اند.

3.	اکنون اعداد آرایه به ترتیب مورد نظر سورت میشوند. بدین صورت که آرایه تبدیل به
`#!cpp a = {13, 10, 9, 7, 7, 3, 2}`
میشود.

4.	حال اندیس اولین خانه کوچکتر مساوی $5$ را به دست می آوریم که برابر با $5$ میباشد.

تعداد عملیات های این دو تابع نیز به ازای هربار استفاده برابر با $O(log(n))$ است که $n$ طول آرایه میباشد.
### منابع بیشتر

- [Binary search](https://cp-algorithms.com/num_methods/binary_search.html)

- [Ternary Search](https://cp-algorithms.com/num_methods/ternary_search.html)

- [Tutorial On Tof (Ternary Search)](https://codeforces.com/blog/entry/60702) (ایده ای برای اینکه توابعی که کاملا ترنری سرچ پذیر نیستند را ترنری سرچ پذیر کنیم)

## سوال ها 
??? warning "نیاز به عضویت در گروه شاززز!"

    برای حل برخی از سوالات باید ابتدا در [گروه شاززز](https://quera.org/course/add_to_course/course/12879/){:target="_blank"} عضو شوید.
| سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Guess The Number](https://oj.uz/problem/view/BOI20_guess){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-ojuz: [Oj.uz](https://oj.uz){:target="_blank"}|
|[فاصله گذاری اجتماعی](https://quera.org/course/assignments/48772/problems/168592){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[Number Game](https://codeforces.com/problemset/problem/1749/C){:target="_blank"}|1400|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Fixed Point Guessing](https://codeforces.com/problemset/problem/1698/D){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Magic Powder 2](https://codeforces.com/problemset/problem/670/D2){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Vasya and String](https://codeforces.com/contest/676/problem/C){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Mafia](https://codeforces.com/problemset/problem/348/A){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Hamburgers](https://codeforces.com/problemset/problem/371/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Tree Infectoin](https://codeforces.com/contest/1665/problem/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Keshi Is Throwing a Party](https://codeforces.com/problemset/problem/1610/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[String game](https://codeforces.com/problemset/problem/778/A){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Searching Local Minimum](https://codeforces.com/problemset/problem/1479/A){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Worm Worries - sub 1 - 2](https://oj.uz/problem/view/BOI18_worm){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>golden_ratio</li></ul> </details>|:judge-ojuz: [Oj.uz](https://oj.uz){:target="_blank"}|
|[Increasing by Modulo](https://codeforces.com/problemset/problem/1169/C){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Renting bikes](https://codeforces.com/problemset/problem/363/D){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Elevator](https://codeforces.com/problemsets/acmsguru/problem/99999/379){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Multiplication Table](https://codeforces.com/problemset/problem/448/D/){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Multiplication Table](https://codeforces.com/problemset/problem/448/D){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Read Time](https://codeforces.com/problemset/problem/343/C){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Memory for Arrays](https://codeforces.com/problemset/problem/309/C){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Guess The String](https://codeforces.com/problemset/problem/1697/D){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Castle Defense](https://codeforces.com/problemset/problem/954/G){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Minimizing Difference](https://codeforces.com/problemset/problem/1244/E){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Interacdive Problem](https://codeforces.com/problemset/problem/1624/F){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Project Planning](https://atcoder.jp/contests/abc227/tasks/abc227_d){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp){:target="_blank"}|
|[Characteristics of Rectangles](https://codeforces.com/problemset/problem/333/D){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>bitset</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Degenerate Matrix](https://codeforces.com/problemset/problem/549/H){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Guess The Maximums](https://codeforces.com/problemset/problem/1363/D){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[GukiZ hates boxes](https://codeforces.com/problemset/problem/551/C){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Professor GukiZ and Two Arrays](https://codeforces.com/problemset/problem/620/D){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Weakness and Poorness](https://codeforces.com/problemset/problem/578/C){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Restorer Distance](https://codeforces.com/problemset/problem/1355/E){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Median pyramid hard](https://atcoder.jp/contests/agc006/tasks/agc006_d){:target="_blank"}|2500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp){:target="_blank"}|
|[Joking (Easy Version)](https://codeforces.com/contest/1746/problem/E1){:target="_blank"}|2500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Worm Worries - sub 3 - 4](https://oj.uz/problem/view/BOI18_worm){:target="_blank"}|2700|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li></ul> </details>|:judge-ojuz: [Oj.uz](https://oj.uz){:target="_blank"}|
