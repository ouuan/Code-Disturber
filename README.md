# Code Disturber

To generate "beautiful" codes.

## How to use?

`disturb.py <sourcefile> <characterset> [length=1 [RLO=1 [newline=0]]]`

- sourcefile : sourcefile path
- characterset : a json file contains Unicode codes
- length : the length of a macro name
- RLO（`0x202E`） : this ‮  is RLO
- newline : to have newlines in the codes besides `#include` and `#define`

## How to compile the generated codes?

**Use Clang.**

For example, [LOJ](https://loj.ac/) and [Codeforces](https://codeforces.com/) support Clang.

## Demos

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

### Japanese

` python disturb.py example.cpp Japanese.json`

```cpp
#define ヱ a
#define メ std
#define レ int
#define ヂ using
#define ぷ return
#define ‮ cout
#define バ namespace
#define カ 0
#define ふ cin
#define じ b
#define ウ main

#include <iostream>
ヂ バ メ ;レ ウ (){レ ヱ ,じ ;ふ >>ヱ >>じ ;‮ <<ヱ +じ ;ぷ カ ;}
```

### gua

`python disturb.py example.cpp gua.json`

```cpp
#define ‮ std
#define ䷞ cout
#define ䷑ main
#define ䷼ cin
#define ䷳ 0
#define ䷦ namespace
#define ䷋ int
#define ䷚ b
#define ䷙ using
#define ䷫ return
#define ䷠ a

#include <iostream>
䷙ ䷦ ‮ ;䷋ ䷑ (){䷋ ䷠ ,䷚ ;䷼ >>䷠ >>䷚ ;䷞ <<䷠ +䷚ ;䷫ ䷳ ;}
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

### Emoji

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

`python disturb.py example.cpp emoji.json 1 1 1`

```cpp
#define 🎀 int
#define 🎎 main
#define 🌉 using
#define 📢 return
#define 🌟 std
#define 💤 namespace
#define 🧓 a
#define 💡 cin
#define 🔽 0
#define ‮ cout
#define 🚡 b

#include <iostream>

🌉 💤 🌟 ;

🎀 🎎 ()
{
🎀 🧓 ,🚡 ;
💡 >>🧓 >>🚡 ;
‮ <<🧓 +🚡 ;
📢 🔽 ;
}

```

### Online demos

[LOJ](https://loj.ac/submission/393739)

[Codeforces](https://codeforces.com/contest/235/submission/52145456)

## Create characterset by yourself

You can use `gen.py` to help you.

[This blog](https://www.cnblogs.com/chris-oil/p/8677309.html) may be useful.

[This website](https://www.sojson.com/unicode.html) may be useful.

## Hints

1. The generated codes may look strange due to the RLO.
2. If it runs for a long time, try to increase the parameter `length`.

## ~~Known bugs~~ Some features

1. Only support variable name in this format : `[0-9a-z_]+`.
2. Doesn't work on `1e-9` —— `1e` + `-` + `9` instead.

## Contributor

[mcfx0](https://github.com/mcfx0)/[**Code-Disturber**](https://github.com/mcfx0/Code-Disturber), for the idea of having more than one character in the macro name and invisible characters.