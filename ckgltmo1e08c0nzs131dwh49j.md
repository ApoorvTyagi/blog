## Having a go at common NLP tasks using TextBlob

# What is NLP 🤖
**NLP** is the subset if AI which enables computers to understand, interpret, and manipulate human natural languages. 

The history of NLP started in the early 1950s(although work can be found from earlier periods too) when Alan Turing published an article titled "Computer machinery and intelligence" which proposed a criterion of intelligence which is now known as the Turing test.

NLP contains many interesting libraries, the most basic one is NLTK, this library is pretty versatile but it’s also quite difficult to use. Most of the time, it’s rather slow and doesn’t match the demands of quick-paced production usage. The other famous libraries are:

- TextBlob
- CoreNLP
- polyglot
- spaCy
- Gensim 

Out of all these libraries i mentioned, TextBlob is my personal favorite. It basically provides beginners with an easy interface to help them learn most basic NLP tasks like sentiment analysis, POS-tagging, or noun phrase extraction.

Let's see some of them here.

![nlp.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603302739929/KLO6-o_qb.jpeg)

# 1. Correcting the spelling
Often people tend do a lot of typos. In this case the TextBlob library can come pretty handy let's take a look at a program to see how it works :
```
from textblob import TextBlob
incorrect_line = "Heello my naem is john and i lobe nathural langeguage procesing"
output = TextBlob(incorrect_line).correct()
print(output)
```
>Output: Hello my name is john and i love natural language processing

In the above program we have first imported the library then wrote a sentence having many incorrect words after which we have just called a correct() function of the library and finally get our output.

# 2. Extracting the Noun
Whenever we want to do some manipulation of a natural language using a computer we generally  have to extract a lot of things from a sentence out of which one important thing is extraction of nouns and TextBlob is a perfect for this task too:
```
from textblob import TextBlob
nouns = TextBlob("India is a country in the Asia. This is where Apoorv lives")
for noun in nouns.noun_phrases:
    print(noun)
```
>Output: india asia apoorv

# 3. Sentimental Analysis
It is the process of computationally identifying and categorizing opinions expressed in a piece of text, especially in order to determine whether the writer's attitude towards a particular topic, product, etc. is positive, negative, or neutral. This is used by all the companies all over the world to to get the review about their products
```
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
text = TextBlob("The movie was excellent!", analyzer=NaiveBayesAnalyzer())
print(text.sentiment)
text = TextBlob("The movie story pinch me a lot.", analyzer=NaiveBayesAnalyzer())
print(text.sentiment)  
```
>Output: Sentiment(classification='pos', p_pos=0.7318278242290406, p_neg=0.26817217577095936)
Sentiment(classification='neg', p_pos=0.258107501384339, p_neg=0.741892498764251609)


![sentimental.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603302782422/nhqSq8jKF.jpeg)

# 4. Antonyms of a word
Whenever we want to know the Antonym of a word we  either look up to that word in a dictionary(old school) or give the word a search on the internet but have you ever wonder how the online search is able to answer you queries, yes they also use the NLP for this and TextBlob again can help us do the same:
```
from textblob import Word
text_word = Word('danger')

if lemma.antonyms():
        antonyms.add(lemma.antonyms()[0].name())        
print(antonyms)  
```
>Output:{'safety'}

# 5. Synonyms of a word

![nlp2.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603302826355/1nccGyCZA.jpeg)

Just like we can find the antonym we can also find the synonym but let me tell you one more interesting aspect of this library which is, it can also define a word for you just by typing one extra statement
```
input_word='danger'
text_word = Word(input_word)

print(text_word.definitions)

synonyms = set()
for synset in text_word.synsets:
    for lemma in synset.lemmas():
        if(lemma.name()!=input_word):
            synonyms.add(lemma.name())  
print(synonyms)
```
>Output:  ['the condition of being susceptible to harm or injury', 'a venture undertaken without regard to possible loss        or injury', 'a cause of pain or injury or loss', 'a dangerous place'] 
{'peril', 'risk'}

# 6. Language detection and translation
This is by far the best part of this library and i have made my own language translator and detector application with the help of the textblob library.
```
blob = TextBlob("My name is Apoorv Tyagi")

print(blob.detect_language())

print(blob.translate(to='hi'))
print(blob.translate(to='fr'))
```
>To which we get output as: 
en  
मेरा नाम अपूर्व त्यागी है   
Je m'appelle Apoorv Tyagi

---

So that's it for now, i hope that you now have the idea of how powerful NLP libraries are.
Hopefully you learned something new today🤞! Happy Coding..

![giphy.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1603387799347/A-w4jg4SC.gif)

# Other articles you might like😊

- [Tail recursion in python 🐍](https://apoorvtyagi.tech/tail-recursion-in-python) - Learn about tail recursion & how to achieve it in python.
- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
- [Understanding Linear Regression](https://apoorvtyagi.tech/understanding-linear-regression) - One of the most popular algorithm in machine learning that every data scientist should know.
- [Bitcoin Mining](https://apoorvtyagi.tech/let-us-mine) -  Learn about what exactly happens in bitcoin mining.
- [Improving Time Complexity](https://apoorvtyagi.tech/improving-time-complexity) - Understanding how to improve the time complexity of your code