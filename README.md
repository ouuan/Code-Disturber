# Code Disturber

To generate "beautiful" codes.

## How to use?

`python disturb.py <sourcefile>`

e.g. `python disturb.py example.cpp`

## How to compile the generated codes?

Use Clang.

For example, [LOJ](https://loj.ac/) and [Codeforces](https://codeforces.com/) support Clang.

## An example

Source code:

```cpp
#include <iostream>

using namespace std;

int main()
{
    int a,b;

    cin>>a>>b;

    cout<<a+b;

    return 0;
}
```

The output:

```cpp
#define 娠 cin
#define 汦 std
#define 囍 cout
#define 潤 a
#define 鉑 namespace
#define 欘 using
#define 變 int
#define ‮ b
#define 踾 main
#define 嗤 return
#define 憪 0

#include <iostream>
欘 鉑 汦 ;變 踾 (){變 潤 ,‮ ;娠 >>潤 >>‮ ;囍 <<潤 +‮ ;嗤 憪 ;}
```

## Online examples

[LOJ](https://loj.ac/submission/393739)

[Codeforces](https://codeforces.com/contest/235/submission/52145456)

##### Why are your codes so ugly?

Because my python is totally based on baidu.