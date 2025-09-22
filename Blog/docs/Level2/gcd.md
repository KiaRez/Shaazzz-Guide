# الگوریتم اقلیدس

الگوریتم اقلیدس یکی از قدیمی‌ترین و ساده‌ترین روش‌ها برای پیدا کردن 
**بزرگ‌ترین مقسوم‌علیه مشترک (GCD)**
دو عدد است. این الگوریتم بر پایه اصل تقسیم استوار است و می‌توان آن را به صورت بازگشتی یا غیربازگشتی پیاده‌سازی کرد.

## توضیح الگوریتم

فرض کنید دو عدد $A$ و $B$ داده شده‌اند. بدون کاستن از عمومیت مسئله، می‌توان فرض کرد $A \geq B$. بزرگ‌ترین مقسوم‌علیه مشترک $A$ و $B$ برابر است با بزرگ‌ترین مقسوم‌علیه مشترک $B$ و باقیمانده تقسیم $A$ بر $B$:

\[
\text{GCD}(A, B) = \text{GCD}(B, A \% B)
\]

این فرایند را تا جایی ادامه می‌دهیم که یکی از مقادیر صفر شود. مقدار غیرصفر باقی‌مانده همان بزرگ‌ترین مقسوم‌علیه مشترک است.

## پیاده‌سازی الگوریتم

### روش بازگشتی

```cpp
int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
```

### روش غیربازگشتی

```cpp
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
```

## پیچیدگی زمانی

پیچیدگی زمانی این الگوریتم برابر با $O(\log(\min(A, B)))$ است. این پیچیدگی به دلیل کاهش سریع مقادیر $A$ و $B$ در هر مرحله از محاسبات است. ادعا می‌شود که هربار عدد بزرگتر، حداکثر نصف مقدار قبلی خود است.

فرض کنیم که $B \leq A$ (اگر اینگونه نباشد چون هر مرحله جای دو عدد عوض می‌شود در مرحله‌ی بعد این اتفاق می‌افتد) .

حال دو حالت داریم :

1. $A \geq 2*B$
    در این حالت حتما مقدار $A$ نصف خواهد شد چون باقی مانده به $B$ گرفته شده است.
2. $A < 2*B$
    در این حالت مقدار باقی مانده برابر $A - B$ است که چون $B$ حداقل نصف $A$ است پس $A - B$ کمتر مساوی نصف $A$ است.

و چون در همان مرحله‌ی اول $A$ کمتر از $B$ می‌شود از آن به بعد  الگوریتم ما از $O(\log(\min(A, B)))$ طول می‌کشد.

خود زبان $c++$ تابع استانداردی دارد که به محاسبه‌ی $\text{GCD}(A, B)$ کمک می‌کند. 

```cpp
int main() {
    int A, B;
    
    cin >> A >> B;

    cout << __gcd(A, B) << endl;

    return 0;
}
```

## کاربردها

1. **محاسبه ک.م.م (LCM)**: از رابطه زیر می‌توان ک.م.م دو عدد را محاسبه کرد:

   $\text{LCM}(A, B) = \frac{|A \times B|}{\text{GCD}(A, B)}$

2. **بهینه‌سازی کد**: در بسیاری از مسائل برنامه‌نویسی و بهینه‌سازی، الگوریتم اقلیدس به دلیل سادگی و کارایی بالا، کاربرد دارد.

## مثال‌ها

### مثال 1

محاسبه GCD برای $A = 48$ و $B = 18$:

1. $48 \% 18 = 12$
2. $18 \% 12 = 6$
3. $12 \% 6 = 0$

پاسخ: $\text{GCD}(48, 18) = 6$.

### مثال 2

محاسبه GCD برای $A = 101$ و $B = 103$:

1. $103 \% 101 = 2$
2. $101 \% 2 = 1$
3. $2 \% 1 = 0$

پاسخ: $\text{GCD}(101, 103) = 1$.


## سوال ها 
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Two Divisors](https://codeforces.com/contest/1916/problem/B){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[GCD](/Level2/GCD){:target="_blank"}</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
|[Big Vova](https://codeforces.com/contest/1407/problem/B){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[GCD](/Level2/GCD){:target="_blank"}</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
|[Modified GCD](https://codeforces.com/contest/75/problem/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[GCD](/Level2/GCD){:target="_blank"}</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
|[Enlarge GCD](https://codeforces.com/contest/1034/problem/A){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[GCD](/Level2/GCD){:target="_blank"}</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
