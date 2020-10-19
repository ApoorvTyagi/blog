## Tail recursion in python 🐍

![tailrecursion.jpeg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603041848648/rDbWSro7E.jpeg)
A recursive function is **tail recursive** when recursive call is the last thing executed by the function i.e the function returns a call to itself.

# Why to care about tail-recursion?🤔
The tail recursive functions considered better than naive functions as tail-recursion can be optimized by compiler. 
The idea is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use hence discard everything saved so far in the memory stack.

Most programming languages are tail-recursive, which means that they're able to make optimizations to functions that return the result of calling themselves

Almost all recursive functions can be transformed into the tail-call form. Here's an example of a function :

First in the original form, then transformed into the tail-call form.

```
# Original Function
def function(n):
    if n == 0: 
        return 1
    return factorial(n-1) * n

# Tail recursive function
def function(n, var=1):
    if n == 0: 
        return var
    return factorial(n-1, var * n)
``` 

🧐They both look similar, and in fact the original even looks more simple & seems like it's also in the tail call form, but if you observe it you'll see there's a multiplication which is outside of the recursive call which can't be optimized away. 

🔑The key difference between the two is that in the non-tail function, the CPU needs to keep track of the number we're going to multiply, whereas in the tail-call function the CPU knows that only work left to do is another function call and it can just clear all of the variables and state used in the current function

This sounds great but still there's a problem, **"Python does not support tail-call optimization"**.🤷‍♀️

It is believed that tail recursion is considered a bad practice in Python. There are few reasons for this, the simplest of which is just that python is built more around the idea of iteration than recursion.

But the real question is **can we make it happen?**🤔

In short the answer is NO (since Guido van Rossum prefers to be able to have proper tracebacks). But we can manually eliminate the recursion with a transformation which we will see in the next section.

# Making python tail-recursive🤯

Recursive tail calls can be replaced by jumps. This is known as **"tail call elimination"** and is a transformation that can help limit the maximum stack depth used by a recursive function, with the benefit of reducing memory by not having to allocate stack frames.
 
Sometimes, recursive functions which aren't able to run due to stack overflow are transformed into function which can work infinitely without facing the same problem.

```
# factorial.py
from tail_recursion import tail_recursive, recurse

# Normal recursion depth maxes out at ~1000, this one works indefinitely
@tail_recursive
def factorial(n, var=1):
    if n == 0:
        return var
    recurse(n-1, var=var*n)
```

When a function is decorated by @tail_recursive, it returns an object implementing the tail_call method. This object also overrides the ```__call__``` method, which means we can call it like the original function (e.g. factorial(x)).

If you don't know what are decorators you should definitely read about them now [here](https://www.geeksforgeeks.org/decorators-in-python/), basically they're functions which are called on other functions and change the behavior in some way.

>*Note -  decorators != annotations*

Decorated functions test whether they return a call to tail_call(). If so then the return value is pushed on a call stack which is just a simple implementation of a list.

tail_call returns an object storing the function it was called on (e.g. factorial) and the (keyword) arguments (e.g. n - 1) it was called with. If the arguments contain a nested call to tail_call then this call is also pushed onto the call stack. 

On the other hand if tail_call is passed no nested tail_calls then the function that it stores is called with the stored (keyword) arguments. The return value of this lazy call then 
- Replaces the argument it was passed as or 
- Returns another tail_call which is pushed to the stack or (c) is the final return value of the call to the decorated function (e.g. factorial(x)).

# Conclusion⛳

![tailrecursion1.jpeg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603041948043/85-ZuWcqb.jpeg)

Here we have seen what is tail recursion & how to let Python eliminate tail calls by using the tail_recursive decorator to simply define tail recursive functions.

Python has a small limit to how many recursive calls can be made (typically ~1000). The reason for this limit is doing recursive calls takes a lot of memory and resources because each frame in the call stack must be persisted until the call is complete. 

The decorator gets around that problem by entering and exiting a single call, so technically our function isn't actually recursive anymore and hence we avoid the limits.

Also we have seen the benefits of tail recursion - If you are encountering maximum recursion depth errors or out-of-memory crashes tail recursion can be a helpful strategy.

Hopefully you learned something 🤞! Happy Coding

# Other articles you might like😊

- [scp command in Linux 💻](https://apoorvtyagi.tech/scp-command-in-linux) - Know about the ways to securely copy files and directories between two locations.
- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
- [Understanding Linear Regression](https://apoorvtyagi.tech/understanding-linear-regression) - One of the most popular algorithm in machine learning that every data scientist should know.
- [Bitcoin Mining](https://apoorvtyagi.tech/let-us-mine) -  Learn about what exactly happens in bitcoin mining.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code
