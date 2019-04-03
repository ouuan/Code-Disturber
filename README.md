# Code Disturber

To generate "beautiful" codes.

## How to use?

`python xxx.py <sourcefile>`

e.g. `python chinese.py example.cpp`

## How to compile the generated codes?

**Use Clang.**

For example, [LOJ](https://loj.ac/) and [Codeforces](https://codeforces.com/) support Clang.

## Examples

### Source code

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

### Chinese

```cpp
#define 铤 std
#define 无 return
#define 曊 b
#define 洞 a
#define 抽 using
#define 乨 int
#define 砀 main
#define 埚 cout
#define ‮ namespace
#define 磸 cin
#define 孇 0

#include <iostream>
抽 ‮ 铤 ;乨 砀 (){乨 洞 ,曊 ;磸 >>洞 >>曊 ;埚 <<洞 +曊 ;无 孇 ;}
```

### Invisible

```cpp
#define ‭‬‫‬‮ 0
#define ‬‭‮‬‬ main
#define ‬‫‬‭‭ return
#define ‭‭‮‮‮ using
#define ‫‭‫‭‬ b
#define ‬‮‬‫‮ int
#define ‬‬‬‮‬ std
#define ‮ cin
#define ‮‮‫‭‭ a
#define ‮‮‫‮‮ namespace
#define ‫‬‫‭‭ cout

#include <iostream>
‭‭‮‮‮ ‮‮‫‮‮ ‬‬‬‮‬ ;‬‮‬‫‮ ‬‭‮‬‬ (){‬‮‬‫‮ ‮‮‫‭‭ ,‫‭‫‭‬ ;‮ >>‮‮‫‭‭ >>‫‭‫‭‬ ;‫‬‫‭‭ <<‮‮‫‭‭ +‫‭‫‭‬ ;‬‫‬‭‭ ‭‬‫‬‮ ;}
```

### Emoji

```cpp
#define 🔐 main
#define 🐸 namespace
#define 👚 std
#define 📚 0
#define 💎 a
#define 👎 using
#define 🐄 cin
#define ‮ cout
#define 💍 b
#define 🕨 int
#define 😊 return

#include <iostream>
👎 🐸 👚 ;🕨 🔐 (){🕨 💎 ,💍 ;🐄 >>💎 >>💍 ;‮ <<💎 +💍 ;😊 📚 ;}
```

## Online examples

[LOJ](https://loj.ac/submission/393739)

[Codeforces](https://codeforces.com/contest/235/submission/52145456)

## Customize

You can customize the disturber.

For example, you can delete the line `disturbname[keys[random.randint(0,len(keys)-1)]]="\u202E"` so that there will be no RLO in the generated codes.

You can change the function `getVar()` to generate codes in different character sets. However, some Unicode characters are not supported by Clang, please be careful with that.

## Contributor

[mcfx0](https://github.com/mcfx0)/[**Code-Disturber**](https://github.com/mcfx0/Code-Disturber).

