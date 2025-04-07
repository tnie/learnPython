[Python 教程](https://docs.python.org/zh-cn/3/tutorial/index.html) 学习笔记，2020年基于 3.8 版本整理，2025年基于 3.13 版本更新。



[9.1. 名称和对象](https://docs.python.org/zh-cn/3/tutorial/classes.html#a-word-about-names-and-objects)

[9.2. Python 作用域和命名空间](https://docs.python.org/zh-cn/3/tutorial/classes.html#python-scopes-and-namespaces)，推荐先学习 [Python3 命名空间和作用域](https://www.runoob.com/python3/python3-namespace-scope.html) 再查看

—— 这两节都说了些啥乱七八糟的？

## REPL

交互式开发环境：“读取-求值-输出”循环（英语：Read-Eval-Print Loop，简称REPL）

> REPL 对于学习一门新的编程语言具有很大的帮助，因为它能立刻对初学者做出回应。

注意区分命令行模式和交互模式：后者不能够执行 xx.py 文件；后者无需使用 `print` 就会打印语句的执行结果。

以交互模式使用解释器，在输入多行指令时：需要**多敲一次回车**（在显示上是 `...` 开始的空行）以表示**函数定义**结束。

# 类-@todo 重新整理

## 命名空间

Python 的命名空间和 C++ 中的 `namespace` 是不一样的。 

Python 命名空间是一个 `dictionary`，是从名字到对象的映射（名字又是另一个命名空间）。

而 Python 一切皆对象，类自身、类实例化之后的对象、函数、模块、数值、字符串都是对象。

> A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries。

Python 的对象都是广义的 dictionary

~~基于此，Python 的命名空间就存在生命周期~~。纠结其生命周期对于开发似乎没有实际意义？

~~查看 python 的教程、手册，针对命名空间和作用域这一块，似乎都表达得乱七八糟。难道真和 C/C++/Java 等语言有区别？如果没有区别，自以为是换种方式描述，还没讲明白，自取其辱~~？

不要按照“范围”的概念理解 Python 的命名空间，它就是 dictionary，即对象自身（名称即对象实体的句柄）！所以才有这种奇葩的描述：

> 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。

### 作用域

> Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
>
> 其它的代码块（如 `if/elif/else/`、`try/except`、`for/while` 等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。

```python
name='wang'
def func():
    print(name)
    # name="panda"

print(name)
func()
```

如果放开注释，会报错 `UnboundLocalError: local variable 'name' referenced before assignment` 很奇葩吧，
—— python 搜索 `name` 这个命名空间，首先搜索 `func` 命名空间是否有定义，发现 `func` 命名空间中有定义（停止搜索），但是它是在 `print(name)` 被解释之后被定义的，因此这里报错。

python 解释器只是创建了一堆的命名空间（并列或嵌套），执行就是加载（/引用）命名空间中的代码片段。

## 类

类，基于命名空间的类

Python 语言中类的概念是狭义的。C++ 中类就是类型的概念，class is type.

Python 是将 class 和 type 分开看待的（不然讲不明白吧）。对象是第一等公民

>  Creating a new class creates a new **type of object**, allowing new instances of that type to be made.

> Classes introduce a little bit of new syntax, three new object types, and some new semantics.

> In Python, the term `method` is not unique to *class instances*: other *object types* can have methods as well. For example, *list objects* have methods called append, insert, remove, sort, and so on.

—— 对于第三条引用，C++ 程序员一脑袋问号，要么这是在说啥，要么这不是废话嘛。按照上下文理解，它似乎在说“列表对象不是类实例”

——对于第二条引用，哪三种对象类型？

C++ 中类定义是静态编译的，Python 中 `if` 分支中的类定义如果没有被执行是不会起作用的。

Python 中定义类，即创建一个类型对象。当我们按照“创建类型对象”理解时，就能够和 C++ 中的认知习惯区分开了。
—— C++ 中 ~~创建类对象（不存在这种表述方式），意思是~~ 创建某个类的实例；Python 中创建类型对象 object of type，用这个 *类对象* 进而创建 *实例对象*。

```python
# class X is an object of type
#       s is an object of X
class student():
    pass

s=student()
print(type(s))          # <class '__main__.student'>
print(type(student))    # <class 'type'>
```

> When a class definition is left normally (via the end), a *class object* is created. This is basically **a wrapper around the contents of the namespace** created by the class definition;

类的 *实例化* 使用函数表示法。因此我们可以把类型对象（例如 `class student`）视为函数：是返回该类的一个新实例的不带参数的函数。

Python 文档中使用“类对象”，大致等价于 C++ 中“类”，我在这里使用“类型对象”

# 内置类型

Python 和我理解的动态类型不太一样，它是强类型的。

它和 C++ 的类型系统相似，函数传参时（或使用运算符时）对参数类型有预期，类型不对就会报错，无法执行。

可这门语言它又不需要声明变量（及其类型），造成用户不知道自己传参类型对不对，运行试一把再说。

```python
payload : dict = {"name":"ZhangSan"}
def send(msg : str) -> bool:
    pass
# 以下写法执行报错
send(payload)
# 现在采用类型提示，那最初设计语言时为什么要省略类型声明呢
# 缺失类型声明，是不是缺陷？
```

https://docs.python.org/zh-cn/3/library/stdtypes.html

- 不可变类型：数字、字符串、元组（tuple）
- 可变类型：列表、字典、集合（set)
- 其他常量：True / False / 空对象（None）

# 控制流-第4章

## 基础类型

Python 的除法运算 (`/`) 永远返回浮点数类型。如果要像 C++ 那样做 floor division 得到一个整数结果（忽略小数部分）你可以使用 `//` 运算符。

### 字符串

> Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

单引号、双引号定义字符串并无区别，在某些场景中选择更合适的即可（不需要在单引号里转义双引号，反之亦然）：
```python
'it\'s a dog.'  # 需转义
"it's a dog."   # 更清晰
```

除了使用 `+` 对字符串进行连接，相邻的两个或多个 *字符串字面值* 将会自动连接到一起（变量不行哦）。

字符串使用下标访问时，*索引使用负数* 和 C++ 中意义不同，使用负数表示倒序方向。比如 `'World'[-1] == 'd'` 顺序方向索引由 0 开始，倒序方向索引由 -1 开始。

索引越界会报错，但切片中的的越界索引会被自动处理。

字符串是不可变类型，所以对字符串的 **某个索引位置** 赋值会报错（对整个字符串的赋值是另一回事）

Python 中字符串类名是 `str`，而这常在 C++ 中用作临时变量名称。

## 条件判断和控制语句

- Python 和 C 一样，任何非零整数都为真；零为假
- 针对序列（包括字符串或列表），长度非零就为真，空序列就为假

Python 没有 `switch/case` 语句；在 3.10 中新增了 `match/case` 语句，入参类型、匹配条件都更加开放。

Python 遍历很特殊的一点：只读
> 在遍历同一个集合时修改该集合的代码可能很难获得正确的结果。通常，更直接的做法是循环遍历该集合的副本或创建新集合。 [来源](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#for-statements)

Python 不像 C++ 使用了分号和大括号来组织语句，而是使用缩进，所以无法表达“空语句”的概念，新增了关键词 `pass` 表示空语句。

比较运算符 `in` 和 `not in` 用于容器，参考 SQL 的 `where` 子句。

比较运算符 `is` 和 `is not` 用于比较两个对象是否是同一对象。

## 函数

在 C++ 中函数定义没有 `return` 语句（或 `return;`）表示“没有返回值”，所以无法将 `void func();` 赋值给变量。

但 Python 中所有函数都是有返回值的，即使没有 `return` 语句的函数也会返回一个相当无聊的值 `None`。

因为 Python 中变量非值，都是引用。所以，`None` 近似 C++ 中 `nullptr` 空指针的概念，而非 `void` 关键词。

### 传参

这是与 C++ 语言差别非常大的一点。

Python 中的**变量存放的都是对象引用**，所以 Python 的参数传递**只有引用传递** —— 造成函数内操作影响外部变量 —— 通过“不可变对象”避免这种混乱。

C++ 中对象存在 `mutable` 或 `const` 修饰；~~但在 Python 中，是否可变是不相同的两个类型。~~

Python 对象赋值时，也只是创建了别名/引用。如果是“可变对象”，一改全改；如果是“不可变对象”，写时拷贝一份新的。

区分“不可变对象”和“可变对象”，是通过类型区分（e.g. `list` 和 `tuple`），而非类型之外的修饰符:

- 不可变对象：`int`，`string`，`float`，`tuple`
- 可变对象 ：`list`，`dictionary`

### 参数默认值

参数避免使用可变类型，坚持使用不可变类型能够减少出错的风险。记住，Python 的变量其实都是引用。

> 重要警告： 默认值只会执行一次。[引用来源](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#default-argument-values)

—— 这就很扯了。当默认值是不可变对象时，和 C++ 中表现一致；当默认值是可变对象（列表、字典或类实例等）时，违反 C++ 程序员的直觉。

所以，**默认参数必须指向不变对象**！！

> 定义默认参数要牢记一点：默认参数必须指向不变对象！

### 关键字传参

此特性针对 *使用* 函数的场景，与 *定义* 函数无关。

既可以像 C++ 那样按照位置传参 `foo(value1, value2)`，也可 `foo(形参名2=value2, 形参名1=value1)` 使用关键字，不再受限于位置传参。

在函数调用中的限制或规则：
- 关键字参数必须在位置参数的后面
- 传递的所有关键字参数必须与函数定义的某个参数匹配，顺序不重要
- 不能对同一个参数多次赋值

这种位置传参和关键字传参的组合形式非常灵活，有时反而不是我们想要的。限制方式通过 `/` 或 `*` 实现：
- 仅限位置传参时，在定义时参数列表末尾增加 `,/`， 举例 `def pos_only_arg(arg, /):`
- 仅限关键字传参时，定义时参数列表之前增加 `*,`， 举例 `def kwd_only_arg(*, arg):`

更灵活的组合方式，我不想说了。玩呢

到底应该怎么使用呢？参考 [指导](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#recap)
- 形参名称没有实际意义；希望形参名称用于 `**kw` 任意关键字参数中
- 形参名称有实际意义，使函数定义更易理解
- 如果使用关键字传参，之后修改函数定义时仅仅调整形参名称也会造成冲击

### 任意个参数

- 使用者传入列表或元组或字典
- 定义函数时使用 `*agrs` 形式的参数，接收任意个位置参数
- 定时函数时使用 `**kw` 形式的参数，接收任意个关键字参数（除了与已有形参相对应的关键字参数以外的）

### 变量赋值和作用域

C++ 中变量需要先声明再使用，如果函数内没有声明同名的局部变量，可以直接对全局变量进行赋值。

但 Python 中变量无需声明即可直接使用，因此 **全局变量和外层函数的变量无法在函数内部直接赋值**（可以被引用），语法上会被解释为新定义同名的局部变量。

- 当内部作用域想修改全局作用域的变量时，就要用到 `global` 关键字
- 当内部作用域想修改嵌套作用域（外层非全局）的变量时，就要用到 `nonlocal` 关键字

### 注释和说明

针对函数 `def func()` ，可以通过 `print(func.__doc__)`  查看 document strings（在定义函数时补充的自我说明）；

可以通过 `print(func.__annotations__)` 查看函数注解（函数参数类型、返回值类型）。

# 序列和集合-第5章

常用的几个容器类型：dic `{}`  list `[]`  tuple`()`：

- 使用 `{}` 就创建了一个 dic 对象，字典
- 使用 `[]` 就创建了一个 list 对象，列表
- 使用 `()` 就创建了一个 tuple 对象，元组

> 要创建一个 set，需要提供一个 list 作为输入集合：`s = set([1, 2, 3])`

`for..in..` 循环，可用于什么类型？

 `range()` 的结果不是 `list`，但其结果可以使用 `for..in..` 循环：`[x*x for x in range(10)]`

> 集合数据类型如 `list`、`dict`、`str` 等是 `Iterable` 但不是 `Iterator`，不过可以通过 `iter()` 函数获得一个 `Iterator` 对象。

`Iterator` 类型需要定义 `__next()__` 函数，以便 `next(it)`  返回下一个 `Iterator` 对象

初始的 `Iterator` 通过 `iter(obj)` 访问实现了 `__iter()__` 的类型获取：obj 即满足 `Iterable` 概念。obj 无需和 Iterator 类型相同。

- `type([])` is `list`;
- `type(iter([]))` is `list_iterator`;

列表作为栈，后进先出是推荐的；但不推荐将列表用作队列，`collections.deque` 被设计用于快速地从两端操作。

`list.copy()` 虽然被描述为浅拷贝，但此处的 shallow 是针对嵌套序列而言。对于简单的列表是新建了副本的。

> Return a shallow copy of the list.

```python
users=[]
students=users.copy()
users is students   #False
```

# 模块

模块是包含 Python 定义和语句的文件。模块名就是去掉 `.py` 后缀名的文件名。

在模块内部，通过全局变量 `__name__` 可以获取模块名。

以脚本形式执行模块时（而非使用 `import` 导入模块），会把 `__name__` 赋值为 `"__main__"` 。

内置函数 `dir()` 用于查找模块定义的名称。

# 错误和异常-第8章

异常方面，和 C++ 最大的不同之处在于 Python 存在 `else` 子句和 `finally` 子句，而且

> 如果在执行 try 语句时遇到一个 `break`, `continue` 或 `return` 语句，则 `finally` 子句将在执行 `break`, `continue` 或 `return` 语句之前被执行。

这也就意味着

> 如果 `finally` 子句中包含一个 `return` 语句，则返回值将来自 `finally` 子句的某个 `return` 语句的返回值，而非来自 `try` 子句的 `return` 语句的返回值。

—— 推测和存在 `finally` 子句关联的是缺失 C++ 中析构函数的类似机制 RAII

# 类和对象-第9章

## 访问限制

python 在模块、类内部资源的访问限制上，使用下划线形式约定俗成，防君子不防小人
> 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 `__`

## 实例属性和类属性

实例属性，即 C++ 中的普通成员变量；给实例绑定属性有两种方式：
- 在构造方法 `__init__` 中通过 `self` 变量绑定
- 直接通过实例变量（可以任意绑定属性的）


类属性，即 C++ 中的静态成员变量；
- 直接在 `class` 中定义

和强类型约束的 C++ 相比：
- 在类定义之后，可以通过类名**动态添加**类数据属性，新增的类属性也被类和所有实例共有
- 在实例生成后，还可以**动态添加**实例数据属性，但是这些实例数据属性只属于该实例

## 实例方法和类方法

- 实例方法：即 C++ 中普通成员函数， `foo(self, ...)`
- 类方法：即 C++ 中类的静态成员函数，需要使用 `@classmethod` 修饰， `fun(cls, ...)`
- 静态方法：即 C++ 中的自由函数（+约束在当前类名作用域中），需要使用 `@staticmethod ` 修饰

Python 有概念接近 C++ 中的构造函数，但没有析构函数的概念。

## 类也是对象

所以，访问类属性和类方法时也是通过 `类名.xx` 访问，而非 C++ 中 `类名::` 形式。

如果类的函数和属性可以动态增删，如果实例的方法和属性可以动态增删，如果实例的成员没有访问限制（依赖下划线约定）

—— Python 允许这些，足够灵活，也能随意写出非常非常糟糕的代码，没有人能够维护。

基于命名空间的面向对象，呵呵—— Python 的类和对象让我反胃 啊

## 方法对象和函数对象

文字游戏、文字术语而已。

- 方法对象是实例对象的，不带有 `self` 参数
- 函数对象是类对象的，一般带有 `self` 参数

## 装饰器

装饰器的概念 `@log` `@perproty` `@xx.setter`
- 内置的 `@property` 装饰器就是负责把一个方法变成属性调用的
- `@property` 本身又创建了另一个装饰器 `@xx.setter`，负责把一个 `setter` 方法变成属性赋值

我认为博主对于装饰器的定义有误：
> 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

刚开始学习 python 时，不要去了解 decorator 是如何实现的，掌握它用来做什么、怎么使用就可以了。

## 创建不可变对象

正常定义一个类它的属性是可以正常访问和修改的，所以那些类的实例都是可变对象。

我们只要定义一个类，不允许它修改属性，就可以创建一个不可变对象。

# 异步 IO 与协程

## generator 生成器

和迭代器的概念相关：本质上就是迭代器的语法糖。

> 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

> 如果一个函数定义中包含 `yield` 关键字，那么这个函数就不再是一个普通函数，而是一个 `generator`。而调用该函数就会生成一个 `generator` 对象。

不同于常见的通过定义 `class` 描述类的属性和行为，此处通过包含 `yield` 关键字的函数也描述了某种类型，定义了它的行为。（推测此处通过函数封装了某个类的实现细节：在这个场景中，引入 `yield` 后通过函数描述更加清晰，且简洁 —— 结合 C++ 中使用 `switch` 模拟协程来理解，能够重入且能保存状态的函数）

使用两者创建对象的形式一致：`obj=cls()` 或 `obj=fun()`

> 这时 `func()` 并不会真正调用函数体，而是以函数体生成了一个生成器对象实例。

## 协程

协程的价值，是不是只有结合异步 IO 才能实现呢？包括本地磁盘 io，网络 io

大多数讲解 python 协程时 [举例生产者-消费者][3]，除去讲解 `yield` 如何使用外，没有任何实际意义。生产-消费-生产-消费-.... 的单一线程内循环没有任何实用价值：

- 如果以下代码能够解决问题，为什么要写协程？
- 如果以下代码无法解决问题，那例子中的协程也解决不了

```python
while True:
    producer()
    consumer()
```

我认为协程根本就不适用于生产-消费模型。欢迎来辩。

协程既然是一个线程执行，那如何利用多核 CPU 呢？最简单的方法是多进程 + 协程

## asyncio


# 工具

visual code 中调试 python，使用 Terminal 和 Python Interactive 有什么区别？为什么后者使用的 2.7.x 的环境？怎么修改？
- 选择解释器，会用于终端，但不会用于交互环境。
- https://github.com/Microsoft/vscode-python/issues/3579#issue-388444915

### 查看模块和函数的帮助文档

在 Python 的交互窗口中，使用 `print(对象.__doc__)` 或者 `help(包名.对象)`

# 问题

python 为什么不能把描述符放到实例的层次？（参考 c++，即类的普通成员，而非静态成员）

[1]:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000
[3]:https://www.liaoxuefeng.com/wiki/1016959663602400/1017968846697824