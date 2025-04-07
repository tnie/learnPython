# 迭代器和生成器

先介绍迭代器，再看生成器。

## 可迭代对象和迭代器

在 Python 中，可迭代对象和迭代器是相关但不同的概念。 

> 集合数据类型如 `list`、`dict`、`str` 等是 `Iterable` 但不是 `Iterator`，
>
> 它们可以通过 `iter()` 内置函数获得一个 `Iterator` 对象。

Iterator 迭代器对象，是实现了以下两个接口的对象：

- 返回迭代器对象自身 `iterator.__iter__()`
- 返回下一项元素 `iterator.__next__()` ，当没有更多元素时会引发 `StopIteration` 异常。 

可迭代对象（广义上的容器）通过定义 `container.__iter__()` 方法，返回迭代器对象来支持 `Iterable` 特性。

因为迭代器对象、可迭代对象的 `__iter__()` 方法同名，所以：迭代器肯定是可以迭代的。

```python
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        raise StopIteration

my_iter = MyIterator(5)
for num in my_iter:
    print(num)
```

需要强调的是：迭代器是 **有状态的**，它记住每次调用 `__next__()` 后遍历到的位置。

一旦迭代器遍历完所有元素，再调用 `__next__()` 就会抛出 `StopIteration` 异常，不能再次从头开始遍历，除非重新创建一个迭代器对象。 

下面是简单的示例代码，展示可迭代类型和迭代器的使用：

 ```python
 my_list = [1, 2, 3]  # 可迭代类型 
 # 将可迭代类型转换为迭代器 
 my_iterator = iter(my_list) 
 print(next(my_iterator))   
 print(next(my_iterator))   
 print(next(my_iterator))   
 # print(next(my_iterator))  # 这行会引发 StopIteration 异常 
 ```

上述代码中 `my_list` 是可迭代类型，`my_iterator` 是迭代器，通过 `iter()` 函数可以将可迭代类型转换为迭代器。 

[9.8 迭代器]( https://docs.python.org/zh-cn/3/tutorial/classes.html#iterators)

>  在幕后，`for` 语句会在容器对象上调用 `iter()` 内置函数。 该函数返回一个定义了 `__next__()` 方法的迭代器对象，此方法将逐一访问容器中的元素。 
>
> 当元素用尽时，`__next__()` 将引发 `StopIteration` 异常来通知终止 `for` 循环。 你可以使用 `next()` 内置函数来调用 `__next__()` 方法。

## 生成器

[9.9 生成器](https://docs.python.org/3.13/tutorial/classes.html#generators) ，也遵循迭代协议，理解成 **迭代器的语法糖** 即可。

> Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically.

> 生成器可以完成的任何功能都可以迭代器来完成。 生成器的写法更为紧凑，因为它会自动创建 `__iter__()` 和 `__next__()` 方法。

```python
def my_generator():
    num = 0
    while num < 5:
        yield num
        num += 1

gen = my_generator()
for i in gen:
    print(i)

# 调用生成器函数，返回的生成器对象也实现了 __iter__ 和 __next__ 方法
print(hasattr(gen, '__iter__'))  # True
print(hasattr(gen, '__next__'))  # True
```

[生成器类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#generator-types)

> Python 的 generator 提供了一种实现迭代器协议的便捷方式。

[6.2.9. yield 表达式](https://docs.python.org/zh-cn/3/reference/expressions.html#yieldexpr)

除了“产出”结果 ， `yield` 表达式也是可以获取输入的，就像常见的函数调用一样。

> When the execution is resumed by calling one of the generator’s methods,
>
> the function can proceed exactly as if the yield expression were just another external call. 