# Code Disturber

To generate "beautiful" codes.

## How to use?

`disturb.py <sourcefile> <characterset> [repeat=1 [RLO=1]]`

- sourcefile : sourcefile path
- characterset : a json file contains Unicode codes
- repeat : the length of a name
- RLO（`0x202E`） : this ‮  is RLO

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

`python disturb.py example.cpp Chinese.json`

```cpp
#define 眠 int
#define 酵 namespace
#define 鸻 return
#define 饫 b
#define 费 main
#define ‮ using
#define 阇 std
#define 唐 a
#define 澘 0
#define 扺 cout
#define 怚 cin

#include <iostream>
‮ 酵 阇 ;眠 费 (){眠 唐 ,饫 ;怚 >>唐 >>饫 ;扺 <<唐 +饫 ;鸻 澘 ;}
```

### Invisible

`python disturb.py example.cpp invisible.json 5`

```cpp
#define ‫‭‫‬‪ cin
#define ‬‬‫‪‬ return
#define ‮‬‭‬‭ int
#define ‭‫‪‮‮ std
#define ‭‮‪‫‫ cout
#define ‪‪‮‪‮ namespace
#define ‮‮‬‬‭ using
#define ‪‭‫‫‪ a
#define ‮ b
#define ‬‭‭‬‪ 0
#define ‬‪‮‪‮ main

#include <iostream>
‮‮‬‬‭ ‪‪‮‪‮ ‭‫‪‮‮ ;‮‬‭‬‭ ‬‪‮‪‮ (){‮‬‭‬‭ ‪‭‫‫‪ ,‮ ;‫‭‫‬‪ >>‪‭‫‫‪ >>‮ ;‭‮‪‫‫ <<‪‭‫‫‪ +‮ ;‬‬‫‪‬ ‬‭‭‬‪ ;}
```

## Emoji

The emoji codes are based on [the wiki](https://en.wikipedia.org/wiki/Emoji#Unicode_blocks), so if there are "?"s in the generated code, it is your system that doesn't support the certain emoji.

`python disturb.py example.cpp emoji.json 2 0`

```cpp
#define 🆘🔖 namespace
#define 🐥🆑 0
#define 🍏🐧 using
#define 🎲🌳 return
#define 🎬🐌 b
#define 📙🀄 cin
#define 📗💄 std
#define 🎨🐢 a
#define 📗🌶 main
#define 🌛😃 cout
#define 🙎🐀 int

#include <iostream>
🍏🐧 🆘🔖 📗💄 ;🙎🐀 📗🌶 (){🙎🐀 🎨🐢 ,🎬🐌 ;📙🀄 >>🎨🐢 >>🎬🐌 ;🌛😃 <<🎨🐢 +🎬🐌 ;🎲🌳 🐥🆑 ;}
```

## Online examples

[LOJ](https://loj.ac/submission/393739)

[Codeforces](https://codeforces.com/contest/235/submission/52145456)

## Contributor

[mcfx0](https://github.com/mcfx0)/[**Code-Disturber**](https://github.com/mcfx0/Code-Disturber).

