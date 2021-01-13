## Five++ cool Python snippets that will blow your mind🤯

# Introduction

Python is one of the world’s most popular and in-demand programming languages. This is for many reasons:

- Easy to learn
- Versatile
- Huge range of modules and libraries

I almost use Python daily. Along the way, I’ve picked up a few clever yet useful tricks and tips that will surely make you think hard.

Here, I’ve shared 5++ of them 😉

# 1. Careful with chained operations

```
>>> (False == False) in [False] # makes sense
False
>>> False == (False in [False]) # makes sense
False
>>> False == False in [False] # now what?
```
The first two makes sense but what do think the third one will print?
Even if you give '==' precedence over 'in' or do it otherwise in both cases you'll get the answer as 'False' but it is wrong. Why?

This is because all comparison operations in Python have the same priority when they're chained together (i.e when you don't use brackets). What this means is :
> If a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators, then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z.

So the third expression will evaluate as ```(False == False) and (False in [False])```
Which comes out to be **True**.

To learn more about it, head over to this [LINK](https://docs.python.org/3/reference/expressions.html#comparisons)

# 2. Leakage of Loop variables

```
for x in range(7):
    if x == 6:
        print(x)
print(x)
```
The first print statement seems pretty easy, right? It will simply print 6 because of the if condition that we have put. But what about the second print statement? 

Should it not throw an error as variable 'x' is now out of scope & x was never defined outside the scope of for loop...

But actually it will print '6' again. This is because in Python, for-loops use the scope they exist in and leave their defined loop-variable behind. 

This also applies if we explicitly defined the for-loop variable in the global namespace before. In this case, it will rebind the existing variable.

In simple words python does not have blocks, unlike C/C++ or Java. The only scoping unit in Python is a **function**. If you declare a variable in a function, you can use it anywhere inside it without having any problem.


*If you are a **Javascript **enthusiast then there is something more for you*😉

If you translate that code to javascript, it would first print '6' and then '7'.
The reason for this is the way we iterate in python. The set of values that variable 'x' will take is explicitly determined before starting the 'for loop'. Which is not the case with javascript.

# 3. Default mutable arguments

```
def func(default_arg=[]):
    default_arg.append("python")
    return default_arg

print(func())
print(func())
print(func())
```

What do you think will be the output of the above code? It's very intuitive to think that we will get :
```
['python']
['python']
['python']
```

But again this is not the case. The default argument is a mutable object like 'list' in our case, Python creates it when you define the function, and not every time you invoke it. 

Instead, the recently assigned value to them is used as the default value every time they're invoked. 

So the correct output will be :
```
['Python']
['python', 'python']
['python', 'python', 'python']
```

>NOTE: When we explicitly pass [] to "func" as the argument, the default value of the default_arg variable will not be used, so the function will returned as expected i.e ['python'] ['python'] ['python'].

To learn more about mutable/immutable objects in python, check out this [LINK](https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/)

# 4. Keep trying

```
def func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'

print(func()) #What will get printed?
```

If you look at the above code carefully, you'll see a return statement inside the 'try' block. According to that, it should print "from_try" as the output. 

But [Python docs](http://docs.python.org/reference/compound_stmts.html#the-try-statement) state:

>When a **return**, **break ** or **continue **statement is executed in the try suite of a try…finally statement, the finally clause is also executed ‘on the way out.’

The return value of a function is determined by the last return statement executed. Since the finally clause always executes, a return statement executed in the finally clause will always be the last one executed. Hence the correct output will be ```from_finally```.

# 5. What is wrong with "is"

```
>>> a = 256
>>> b = 256
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
>>> ?
```

Since the first one is True, the second one should also be True. isn't it?

Well no. The correct answer is **False**. Reason being 256 is an existing object but 257 isn't.

What I mean by this statement is When you start up python the numbers from -5 to 256 will be allocated. These numbers are used a lot, so it makes sense just to have them ready.

According to the python docs:

> The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you just get back a reference to the existing object.

This is why when you assigned a & b to 257, two different references are generated & "is" operator checks if both the operands refer to the same object which is not true in this case.

---

So those were the 5 cool quirks of python. I hope you liked them & hopefully leant something new. But since the title contains "**Five++**  python snippets", I have one extra piece for you all which I am sure you will like 👇

# 5++. Emojis in Python 🐍
Do you know you can use Emojis in your Python code?

Yes, [It's true](https://pypi.org/project/emoji/)

```
>>import emoji
>>print(emoji.emojize('Python is amazing :thumbs_up:'))
Python is amazing 👍
```
Here's your whole [emoji cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/). Go on & try it out…

> If you enjoyed these tips & tricks consider following me on [Twitter](https://twitter.com/apoorv__tyagi) because that's where I most actively share such Python tricks along with other topics like Docker, kubernetes, Data structure & Algorithms

%[https://twitter.com/apoorv__tyagi/status/1339852383103320064]

---

# Other articles you might like😊

- [How I automated my WhatsApp chats](https://apoorvtyagi.tech/how-i-automated-my-whatsapp-chats) - Implement a chatbot which will reply to the messages to a group or person from your WhatsApp account without your intervention.
- [Containerize your web application & deploy it on Kubernetes](https://apoorvtyagi.tech/containerize-your-web-application-and-deploy-it-on-kubernetes) - In this i have demonstrated how you can containerize an application and get it running in Kubernetes.
- [Tail recursion in python](https://apoorvtyagi.tech/tail-recursion-in-python) - Learn what tail recursion is & how we can achieve it in python.
- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
