# قضیه کوچک فرما
[قضیه کوچک فرما](https://fa.wikipedia.org/wiki/%D9%82%D8%B6%DB%8C%D9%87_%DA%A9%D9%88%DA%86%DA%A9_%D9%81%D8%B1%D9%85%D8%A7) بیان میکند که اگر $p$ عددی اول باشد و $a$ عددی صحیح باشد که بر $p$ بخشپذیر نیست.

$$ a^p \equiv a \pmod{p} $$

این قضیه را به صورت $a^{p-1} \equiv 1 \pmod{p}$ نیز بیان میکنند.

## اثبات قضیه کوچک فرما
??? اثبات
    یک گراف $p-1$ راسی میسازیم که راس های آن اعداد $1,...,p-1$ هستند و از راس $v$ به راس $v*a$ یک یال جهت دار میدهیم.
    
    درجه خروجی هر راس این گراف $1$ است٬ اثبات میکنیم درجه ورودی هر راس هم $1$ است.
    ??? اثبات
        از برهان خلف استفاده میکنیم. فرض کنید راس $z$ وجود دارد که درجه ورودی آن حداقل $2$ است. یعنی دو راس متفاوت $x$ و $y$ وجود دارد که:
        
        $$x*a \equiv z \pmod{p} , y*a \equiv z \pmod{p}$$
        
        اگر این دو عبارت را از هم تفریق کنیم به عبارت زیر میرسیم:
        
        $$x*a-y*a \equiv 0 \pmod{p} => a(x-y) \equiv 0 \pmod{p}$$
        
        میدانیم که $a$ بر $p$ بخشپذیر نیست. پس $x-y$ باید بر $p$ بخشپذیر باشد.
        
        $$x-y \equiv 0 \pmod{p} => x \equiv y \pmod{p}$$
        
        که این با متفاوت بودن $x$ و $y$ در تناقض است.
    میدانیم گرافی که درجه ورودی و خروجی هر راس برابر با $1$ است اجتماع تعدادی دور مجزا است. (به این گراف گراف جایگشت میگویند)
    
    فرض کنید کوتاه ترین دور این گراف $C$ است و $v$ یکی از راس های $C$ است.
    
    میدانیم اگر از $v$٬ $|C|$ بار به جلو حرکت کنیم به $v$ میرسیم. پس:
    
    $$ v*a^{|C|} \equiv v \pmod{p} => a^{|C|} \equiv 1 \pmod{p} $$

    حال اثبات میکنیم طول تمام  دور های گراف $|C|$ است.
    ??? اثبات
        از برهان خلف استفاده میکنیم. فرض کنید یک دور $D$ داریم که $|D|>|C|$ و $u$ یکی از راس های $D$ است.
        
        چون $a^{|C|} \equiv 1 \pmod{p}$ است٬ اگر از $u$٬ $|C|$ بار به جلو حرکت کنیم باید به $u$ برسیم. اما چون $|D|>|C|$ است به راسی غیر $u$ میرسیم.
    اگر گراف $t$ دور داشته باشد $t*|C|=p-1$ است. یعنی‌ $p-1$ مضربی از طول دور ها است. پس اگر از راس $v$ شروع کنیم و $p-1$ بار به جلو حرکت کنیم دوباره به راس $v$ میرسیم. پس:
    
    $$ v*a^{p-1} \equiv v \pmod{p} => a^{p-1} \equiv 1 \pmod{p} $$ 
## وارون ضربی

وارون ضربی عدد $a$ به پیمانه $p$ که آن را با $a^{-1}$ نشان میدهند٬ عددی است که اگر آن را در $a$ ضرب کنیم. حاصل به پیمانه $p$ برابر $1$ شود.

$$a*a^{-1} \equiv 1 \pmod{p}$$

- اثبات میشود که اگر $a$ و $p$ نسبت به هم اول باشند٬ $a$ وارون ضربی دارد.

طبق قضیه کوچک فرما $a^{p-1} \equiv 1 \pmod{p}$ برقرار است. همچنین میدانیم $a^{p-1} = a*a^{p-2}$. پس:

$$ a*a^{p-2} \equiv 1 \pmod{p} $$

پس وارون ضربی $a$ به پیمانه $p$ برابر با $a^{p-2}$ است.

### محاسبه وارون ضربی
برای محاسبه وارون ضربی میتوانیم از توان دودویی  استفاده کنیم که این کار را در $O(log(p))$ استفاده کنیم.

### پیاده‌سازی

#### روش بازگشتی

```cpp
long long power(long long a, long long b, long long p) {
    if(b==0) return 1;
    long long res = power(a*a%p, b/2, p);
    if(b%2) res = res*a%p;
    return res;
}

long long inverse(long long a, long long p) {
    return power(a, p-2, p);
}
```

#### روش غیربازگشتی

```cpp
long long inverse(long long a, long long p) {
    long long res=1, b=p-2;
    while(b) {
        if(b%2) res = res*a%p;
        a = a*a%p;
        b /= 2;
    }
    return res;
}
```

## تقسیم به پیمانه $p$
برای محاسبه $x/y$ به پیمانه $p$ میتوان $x$ را در وارون ضربی $y$ ضرب کرد:

$$ x/y \equiv x*y^{-1} \equiv x*y^{p-2} \pmod{p} $$

??? مثال
    $$ 10/2 \equiv 10*2^5 \equiv 320 \equiv 5 \pmod{7} $$

## سوال ها
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Modular Inverse](https://www.geeksforgeeks.org/problems/modular-multiplicative-inverse-1587115620/1){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[Fermat](/Level2/fermat){:target="_blank"}</li></ul> </details>| [GFG](https://www.geeksforgeeks.org/explore?page=1&sortBy=submissions){:target="_blank"}|
|[Two Arrays](https://codeforces.com/problemset/problem/1288/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[Fermat](/Level2/fermat){:target="_blank"}</li></ul> <ul><li>Combinatorics</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
|[Beautiful Numbers](https://codeforces.com/problemset/problem/300/C){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[Fermat](/Level2/fermat){:target="_blank"}</li></ul> <ul><li>Combinatorics</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
|[Inversion Expectation](https://codeforces.com/problemset/problem/1096/F){:target="_blank"}|2300|<details> <summary>Spoiler</summary> <ul><li>[Fermat](/Level2/fermat){:target="_blank"}</li></ul> <ul><li>Expected Value</li></ul> <ul><li>Data Structures</li></ul> </details>|:judge-codeforces: [CF](https://codeforces.com/problemsets){:target="_blank"}|
