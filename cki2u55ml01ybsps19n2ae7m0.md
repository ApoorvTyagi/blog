## How i automated my WhatsApp chats

# Introduction

In this tutorial we are going to build an exciting project on Chatbot. We will be implementing a chatbot which will reply to the messages to a group or person from your WhatsApp account without your intervention (because some conversation don't need you to be there😉) 

Here's what is included in this tutorial & how we will proceed :- 
- [How chatbots are Categorized](#category)
- [Limitations of chatbots](#limits)
- [Chatterbot library & installing dependencies](#chatterbot) 
- [Coding the bot ](#code) 
- [Decoding the code ](#DEcode) 
- [Vote for next article ](#vote)  

(In case you are not interested in theory & have all the required libraries installed, feel free to jump directly to the [coding section 👨‍💻](#code))

I hope it sounds interesting so let's begin.✨

![gilfoyle AI.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1605252672744/gZcovNjsq.jpeg)

<a id="category"></a>
# Categories of Chatbots

When it comes to the working of chatbots, it is categorized into two -

- Self-learning approach
- Rule-based approach

### Self-learning approach

In this category, the bots follow the machine-learning approach and it is further categorized into 2 types :

**Retrieval-based Models**
According to the user’s inputs, the bots retrieve the best suitable response for the user from the list of responses.

**Generative Models**
Rather than searching from a set of answers, these models come up with a new response, which makes them intelligent

![the-future-is-5b7f1f.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1606590824794/P76DgP6QD.jpeg)

<a id="limits"></a>
# Limitations of a Chatbot

With increasing advancements, there also comes a point where it becomes fairly difficult to work with the chatbots. Following are a few limitations we face with the chatbots.

**Domain Knowledge** – Since true artificial intelligence is still out of reach, it becomes difficult for any chatbot to completely work out the conversational boundaries when it comes to conversing with a human.

**Personality **– Not being able to respond correctly and fairly poor comprehension skills has been more than frequent errors of any chatbot, adding a personality to a chatbot is still a benchmark that seems far far away.

<a id="chatterbot"></a>
# Chatterbot library

Chatterbot is a python library specifically designed to generate chatbots.

Chatterbot makes it easier to develop chatbots that can engage in conversations. It starts by creating an untrained chatterbot that has no prior experience or knowledge regarding how to communicate. 

As the users enter statements, the library saves the request made by the user as well as it also saves the responses that are sent back to the users. As the number of instances increases in chatterbot, the accuracy of the responses made by chatterbot also increases by every use.

The USP of chatterbot is that it is language independent. The library is designed in a way that makes it possible to train your bot in multiple programming languages, it even enables developers to create their own dataset.

An example of typical input would be something like this:

> user: Good morning! How are you doing?

> bot: I am doing very well, thank you for asking.

> user: You're welcome.

> bot: Do you like hats?

![chatterbot2.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1605427319221/AAsLn-dL5.png)

Before we begin just make sure you install this library by typing

>pip install chatterbot

in your terminal and also don't forget to install

>pip install chatterbot_corpus

because that's what will help us in training our bot.

<a id="code"></a>
# Let's Code our bot 🤖

<iframe src="https://giphy.com/embed/PiQejEf31116URju4V" width="480" height="288" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/memecandy-PiQejEf31116URju4V"></a></p>

I know you all are waiting for this part ;)

Before diving into the code, let's first try to understand what approach are we going with.

So when we receive a message from a particular chat or a group we will simply send it to the chatterbot instance which will return us the most appropriate response against that text. This part is simple. Now the question is how do we pick the last message received?

For that we will be maintaining a text file which will store the last message that was sent by us. 

To explain it more simply let's say the last message that was sent by us was 'xyz'. So we will store this 'xyz' in our text file & our script will keep on checking for any messages that will come after this. This will be done by comparing the picked message with the message in the text file.

After our program receives the new message, i.e the message it picked was different from the one in the text file. The message in the text file will be replaced with the response of the the new received message (which is again the last message sent by us)

This will get more clearer when you see the code(The code is written in Python and using [Selenium](https://pypi.org/project/selenium/)) 👇
```
# importing required modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from selenium import webdriver

# creating chatterbot instance & training
chatbot = ChatBot('chatBot_Name')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Function to make a connection with web whatsapp
def whatsappWebConnection():

     driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
     driver.get('https://web.whatsapp.com')
     driver.implicitly_wait(15) 


# Fetching the last message received
def getLastMessageFromChat(targetName):
        target = driver.find_element_by_xpath('//span[@title= "{}"]'.format(targetName))
        target.click()

        messages = None

        while(1):
            try:
                messages = driver.find_elements_by_class_name("_3zb-j")
                newMessage = messages[-1].text
                return newMessage
            except (NoSuchElementException, StaleElementReferenceException) as e:
                pass

# Function to send the response message back
def sendMessage(targetName, msg):
        target = driver.find_element_by_xpath('//span[@title= "{}"]'.format(targetName))
        target.click()

        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6').click()

# Function to call utilities & updating the text file
def startBot():
    msg=getLastMessage("chatName")
    f = open("WhatsappMessages.txt",encoding="utf8")
    oldMessage=f.readline()
    if(msg!=oldMessage):
        response = chatbot.get_response(msg)
        sendMessage("ME", str(response))#name of your contact with whom you want to talk
        f.write(str(response))
        f.close()
```

And that's all you need.

Don’t let the structure of the code intimidate you, if you already are familiar with python, just by going through the code once i am sure most of it would be easy to comprehend but still we will be doing a walk through of some of the important pieces of the code.

<a id="DEcode"></a>
# Code decoded

- **Library imports**

>from selenium import webdriver

Here, we’re importing “webdriver”, which is something that allows your code to interact with a browser like a human does.

> from chatterbot import ChatBot

> from chatterbot.trainers import ChatterBotCorpusTrainer

We are importing chatterbot library & it's corpus to train out bot

- **Creating & Training bot**

After this we have created out chatterbot instance which only requires one parameter that is the ChatBot name. This can be anything you want. 
```
chatbot = ChatBot('chatBot_Name')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
```
Now that we have created our ChatterBot instance, it is also possible to train the bot. 

Training is a good way to ensure that the bot starts off with knowledge about specific responses. Since we have already have library imported we can use it to quickly train ChatterBot to respond to various inputs in different languages. In this case we have trained it in english language only (there are over dozens of other languages available).

- **whatsappWebConnection()**

Now coming inside our first function "whatsappWebConnection"

>driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

This line is specifying where we’re getting our “driver” from. This driver is a file that contains instructions that let you interact with the browser, specifically Chrome browser in this case, and you can get it from anywhere on the internet. For example, you’ll find the chrome webdriver [here](https://chromedriver.chromium.org/downloads).

>driver.get('https://web.whatsapp.com')

This line of code simply starts a new instance of our browser through our driver. This is where we’ll mess with Whatsapp. Make sure to start your links with “http” (and “https” where available).

>driver.implicitly_wait(15)

This line tells our driver to wait for 15 seconds. What does that mean?

When we ask Selenium to get an element from a page for us, if the element is not found on the page, an exception is thrown. But an element can be missing from a page for many reasons. The page could still be loading, for example.

With this line of code, we’re telling our driver to look for an element for at least 15 seconds before reporting it rogue to us. That’s all. You can increase this timer if you have an even slower internet connection.

Next up, we need to start looking for identifiers for elements on our web page. We need a way of uniquely identifying each element, so we can tell our code to look for it. How do we do that? Visit the page, right click on the element that you want to single out, and hit “inspect element” 

If you opened the console , you’ll need to manually find your element. For the purpose of this tutorial, all of this is unnecessary, as I’ve already found the required information, and at the time of writing this post, these paths work just fine.

- **getLastMessageFromChat()**

Next in our "getLastMessageFromChat" function we are using those identifiers & elements to extract the last message sent/received from the chat. It just takes one parameter as a function argument which is the name of the Person or Group name in case it is the group

- **sendMessage()**

Similarly in "sendMessage" we again take the Person/Group name & also the message to be sent as the 2 argument & again with the help of certain identifiers & elements we are placing the text in message textbox & pressing the send button

>msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

In this line we ask our driver to locate the little text field where we generally type our messages (based on its XPath). Once it finds that field, it will send text to it.

>msg_box.send_keys(msg)

>button = driver.find_element_by_class_name('_35EW6').click()

Once the text is sent to the textbox in the chat, we are ready to hit the send button. This line does that for us, it locates the send button, and clicks on it using the click() method.

- **startBot()**

Now comes the last function which is the "startBot" function. It simply just calls all our utility functions & updates our text file with every new response message that we send.

> Note that we have to keep on calling this function at a particular interval for example every one min. This way every minute our script will pick the last message from the chat, compare with the message in text file & if found different, it will call other required functions to get a response which will be sent back.


*The full code is available on my* [Github](https://github.com/ApoorvTyagi/Anton/blob/master/Anton_v2.0.ipynb)

That’s it! That’s all there is to it! You’ve successfully written your very own WhatsApp bot. Let me know if you run into any issues in the comments, and I’ll try my best to help you out.

<a id="vote"></a>
# Voting Time 🗳

A. **C++ tips & tricks for competitive programming** - [🗳vote](https://iwanttoreadmore.com/vote/apoorv/Whatsapp_Chatbot/cpp_tricks)

B. **Top 10 useful Python tricks** - [🗳vote](https://iwanttoreadmore.com/vote/apoorv/Whatsapp_Chatbot/Python_Tricks)

C. **Explaining Knuth-Morris-Pratt (KMP) Algorithm** - [🗳vote](https://iwanttoreadmore.com/vote/apoorv/Whatsapp_Chatbot/KMP_Algo)


D. ** Build a phone number tracker app in Python** - [🗳vote](https://iwanttoreadmore.com/vote/apoorv/Whatsapp_Chatbot/PY_Phone_Tracker)

👆 These are some of the topics i have in my mind on which i will be writing an article & **YOU** get to decide the priority of them.

Just vote for any one of the topic that you want to read next :)

---

# Other articles you might like😊

- [Containerize your web application & deploy it on Kubernetes](https://apoorvtyagi.tech/containerize-your-web-application-and-deploy-it-on-kubernetes) - In this i have demonstrated how you can containerize an application and get it running in Kubernetes.
- [Having a go at common NLP tasks using Textblob library](https://apoorvtyagi.tech/nlp-textblob) - Know about some of the basic operations to do in Natural language processing using textblob library
- [Tail recursion in python 🐍](https://apoorvtyagi.tech/tail-recursion-in-python) - Learn what tail recursion is & how we can achieve it in python.
- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code 
- [Understanding Linear Regression ](https://apoorvtyagi.tech/understanding-linear-regression) - One of the most popular algorithm in machine learning that every data scientist should know.

---

### Whatsapp Policy 🚨
*Please note that Whatsapp does not encourage bots on their messaging service. Any mass advertising or spamming will lead to your account being banned. This is only for fun and educational purposes. Use it at your own risk*




