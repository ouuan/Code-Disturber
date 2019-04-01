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
#define 枢 using
#define 翩 a
#define 咊 0
#define 駾 cout
#define 邇 main
#define 荠 namespace
#define 满 cin
#define ‮ int
#define 樚 b
#define 喹 std
#define 鷴 return

#include <iostream>
枢 荠 喹 ;‮ 邇 (){‮ 翩 ,樚 ;满 >>翩 >>樚 ;駾 <<翩 +樚 ;鷴 咊 ;}
```

## Online examples

[LOJ](https://loj.ac/submission/393739)

[Codeforces](https://codeforces.com/contest/235/submission/52145456)

##### Why are your codes so ugly?

Because my python is totally based on baidu.