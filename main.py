
"""
by: mohamed fares

This code defines a chatbot using the NLTK (Natural Language Toolkit) library in Python. The chatbot is initialized with a set of patterns and responses that allow it to engage in a conversational dialogue with a user.

The `pairs` list contains the patterns and corresponding responses that the chatbot will use to respond to user input. Each pattern is a regular expression that matches a user's input, and the corresponding response is a list of possible responses that the chatbot can provide.

The `reflections` dictionary is used to map certain words in the user's input to their corresponding "reflections" (e.g. "I am" -> "you are"). This helps the chatbot provide more natural and contextual responses.

The `my_dummy_reflections` dictionary is an example of additional reflections that can be defined and used by the chatbot.

The chatbot is then created using the `Chat` class from the `nltk.chat.util` module, and the `converse()` method is called to start the conversation.
"""
#
from nltk.chat.util import Chat, reflections


#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["mohamed fares created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Cairo, egypt',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of football",]
    ],
    [
        r"who (.*) (footballer)?",
        ["Cristiano Ronaldo"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


print(reflections)

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()