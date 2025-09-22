--- 
hide:
  - footer
comments: true
---
### استک (stack)

استک یک ساختمان داده خطی در ++C است که بر اساس اصل **LIFO (آخر وارد، اول خارج)** کار می‌کند. یعنی آخرین عنصری که وارد استک شده باشد، اولین عنصری است که خارج می‌شود.  
عملیات اصلی استک عبارت‌اند از:
- `push` برای اضافه کردن عنصر
- `pop` برای حذف عنصر
- `top` برای مشاهده عنصر بالای استک
- `empty` برای چک کردن خالی بودن استک

#### نمونه مسئله: بررسی پرانتزهای متعادل

در این مسئله یک رشته داده شده که شامل پرانتز باز `(` و پرانتز بسته `)` است.  
می‌خواهیم بررسی کنیم که آیا این پرانتزها به صورت درست و متعادل بسته شده‌اند یا خیر.

مثال‌ها:
- ورودی: `"()"` → معتبر ✅
- ورودی: `"(()"` → نامعتبر ❌
- ورودی: `"(())()"` → معتبر ✅

??? success "راه حل"
    برای حل این مسئله از استک استفاده می‌کنیم:
    - هرگاه پرانتز باز `'('` دیدیم آن را داخل استک قرار می‌دهیم.
    - هرگاه پرانتز بسته `')'` دیدیم، اگر استک خالی بود پاسخ غلط است وگرنه یک عنصر را از استک خارج می‌کنیم.
    - در انتها اگر استک خالی بود، رشته معتبر است.

    ```cpp linenums="1"
    #include <bits/stdc++.h>
    using namespace std;

    bool isValid(string s) {
        stack<char> st;
        for(char c : s){
            if(c == '(') st.push(c);
            else{
                if(st.empty()) return false;
                st.pop();
            }
        }
        return st.empty();
    }
    ```


---
### صف (queue)

صف یک ساختمان داده خطی در ++C است که بر اساس اصل **FIFO (اول وارد، اول خارج)** کار می‌کند.  
عملیات اصلی صف عبارت‌اند از:
- `push` برای اضافه کردن عنصر به انتها
- `pop` برای حذف عنصر از ابتدا
- `front` برای مشاهده اولین عنصر
- `empty` برای بررسی خالی بودن صف

```cpp linenums="1"
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    q.push(10);
    q.push(20);
    q.push(30);

    cout << "Front: " << q.front() << endl; // Front: 10
    cout << "Back: " << q.back() << endl;   // Back: 30
    q.pop();
    cout << "Front after pop: " << q.front() << endl; // Front after pop: 20

    cout << "Size: " << q.size() << endl; // Size: 2
    cout << "Is empty? " << q.empty() << endl; // Is empty? 0
}
```

!!! tip "نکته"
    صف در مسائل گراف (BFS)، شبیه‌سازی فرایندها و مدیریت وظایف در سیستم‌ها بسیار پرکاربرد است.


---
### وکتور (vector)

وکتور یک آرایه پویا در ++C است که اندازه‌اش می‌تواند در طول اجرا تغییر کند.  
عملیات اصلی وکتور عبارت‌اند از:
- `push_back` برای اضافه کردن عنصر به انتها
- `pop_back` برای حذف آخرین عنصر
- `[]` یا `at` برای دسترسی به عناصر
- `size` برای تعداد عناصر
- `clear` برای پاک کردن همه عناصر

```cpp linenums="1"
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3};

    v.push_back(4);
    cout << "Element at 2: " << v[2] << endl; // Element at 2: 3
    v.pop_back();
    cout << "Size after pop: " << v.size() << endl; // Size after pop: 3

    for(int x : v) cout << x << " "; // 1 2 3
    cout << endl;
}
```

!!! tip "نکته"
    وکتور در اکثر الگوریتم‌ها و مسائل جایگزین مناسب آرایه معمولی است و امکانات بیشتری دارد.

---
### دکیو (deque)

دکیو یا **double-ended queue** یک ساختمان داده در ++C است که امکان اضافه و حذف عناصر را هم از ابتدا و هم از انتها فراهم می‌کند.  
عملیات اصلی دکیو عبارت‌اند از:
- `push_back` و `push_front`
- `pop_back` و `pop_front`
- `front` و `back` برای مشاهده ابتدا و انتها
- دسترسی با `[]`

```cpp linenums="1"
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> d;

    d.push_back(10);
    d.push_front(20);
    d.push_back(30);

    cout << "Front: " << d.front() << endl; // Front: 20
    cout << "Back: " << d.back() << endl;   // Back: 30

    d.pop_front();
    d.pop_back();

    cout << "Front after pop: " << d.front() << endl; // Front after pop: 10
    cout << "Size: " << d.size() << endl; // Size: 1
}
```

### priority queue

`priority_queue` یک صف در ++C است که همواره عنصر بیشینه (یا کمینه با مقایسه‌گر سفارشی) در ابتدای صف قرار دارد.  
به طور پیش‌فرض یک **max-heap** است.  
عملیات اصلی:
- `push` برای اضافه کردن
- `pop` برای حذف بیشینه
- `top` برای مشاهده بیشینه
- `empty`

```cpp linenums="1"
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> pq;

    pq.push(10);
    pq.push(5);
    pq.push(20);

    cout << "Top: " << pq.top() << endl; // Top: 20
    pq.pop();
    cout << "Top after pop: " << pq.top() << endl; // Top after pop: 10

    cout << "Size: " << pq.size() << endl; // Size: 2
    cout << "Is empty? " << pq.empty() << endl; // Is empty? 0
}
```

!!! tip "نکته"
    `priority_queue` پیاده‌سازی پیش‌فرض هیپ در ++C است و در بسیاری از الگوریتم‌های مسیر کوتاه و مسائل انتخاب بهینه استفاده می‌شود.

---
### مجموعه (set)

`set` یک ساختمان داده در ++C است که عناصر یکتا را به صورت مرتب‌شده نگه می‌دارد (بر اساس BST).  
عملیات اصلی:
- `insert` برای افزودن عنصر
- `erase` برای حذف عنصر
- `find` برای جستجو
- پیمایش با iterator

```cpp linenums="1"
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;

    s.insert(10);
    s.insert(5);
    s.insert(20);
    s.insert(10); // Duplicate ignored

    cout << "Size: " << s.size() << endl; // Size: 3
    cout << "Contains 10? " << s.count(10) << endl; // Contains 10? 1
    cout << "Min element: " << *s.begin() << endl; // Min element: 5
    cout << "Max element: " << *s.rbegin() << endl; // Max element: 20

    s.erase(5);

    for(int x : s) cout << x << " "; // 10 20
    cout << endl;
}
```

!!! tip "نکته"
    `set` همیشه عناصر را مرتب نگه می‌دارد و عملیات آن  `O(log n)` است.

---
### map

`map` در ++C یک ساختار داده کلید-مقدار است که کلیدها یکتا و به ترتیب مرتب‌شده ذخیره می‌شوند.  
عملیات اصلی:
- `insert` یا `operator[]` برای افزودن
- `erase` برای حذف
- `find` برای جستجو
- پیمایش با iterator

```cpp linenums="1"
#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> mp;

    mp["apple"] = 10;
    mp["banana"] = 20;
    mp["orange"] = 15;

    cout << "apple count: " << mp["apple"] << endl; // apple count: 10
    cout << "Contains 'banana'? " << mp.count("banana") << endl; // Contains 'banana'? 1

    mp.erase("orange");

    for(auto &[key, val] : mp) cout << key << ": " << val << endl; 
    // apple: 10
    // banana: 20
}
```

!!! tip "نکته"
    `map` همیشه کلیدها را مرتب نگه می‌دارد و عملیاتش `O(log n)` است. برای سرعت بیشتر از `unordered_map` استفاده می‌شود.

### سوال ها 
<form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[stack](/Level1/stack){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Min Stack](https://leetcode.com/problems/min-stack/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[stack](/Level1/stack){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[stack](/Level1/stack){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/){:target="_blank"}|Hard|<details> <summary>Spoiler</summary> <ul><li>[stack](/Level1/stack){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[queue](/Level1/queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Design Circular Queue](https://leetcode.com/problems/design-circular-queue/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[queue](/Level1/queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[queue](/Level1/queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[queue](/Level1/queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[vector](/Level1/vector){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[vector](/Level1/vector){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[vector](/Level1/vector){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Insert Interval](https://leetcode.com/problems/insert-interval/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[vector](/Level1/vector){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/){:target="_blank"}|Hard|<details> <summary>Spoiler</summary> <ul><li>[deque](/Level1/deque){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Design Circular Deque](https://leetcode.com/problems/design-circular-deque/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[deque](/Level1/deque){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/){:target="_blank"}|Hard|<details> <summary>Spoiler</summary> <ul><li>[deque](/Level1/deque){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Dota2 Senate](https://leetcode.com/problems/dota2-senate/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[deque](/Level1/deque){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[priority_queue](/Level1/priority_queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[priority_queue](/Level1/priority_queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/){:target="_blank"}|Hard|<details> <summary>Spoiler</summary> <ul><li>[priority_queue](/Level1/priority_queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/){:target="_blank"}|Hard|<details> <summary>Spoiler</summary> <ul><li>[priority_queue](/Level1/priority_queue){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[set](/Level1/set){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[set](/Level1/set){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Third Maximum Number](https://leetcode.com/problems/third-maximum-number/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[set](/Level1/set){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[set](/Level1/set){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Two Sum](https://leetcode.com/problems/two-sum/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[map](/Level1/map){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Group Anagrams](https://leetcode.com/problems/group-anagrams/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[map](/Level1/map){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/){:target="_blank"}|Medium|<details> <summary>Spoiler</summary> <ul><li>[map](/Level1/map){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Word Pattern](https://leetcode.com/problems/word-pattern/){:target="_blank"}|Easy|<details> <summary>Spoiler</summary> <ul><li>[map](/Level1/map){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
