
# OpenAI-Chatbot Documentation

This is a chatbot that you  can talk to in the command line, made with OpenAI's GPT3 API. This program offers a simple way to help define what type of "person" you want the chatbot to be.

There are 3 main files:

**1. chatConfig.py**
use this file to adjust how you want the bot to behave, and to input your OpenAI API key

**2. main.py**
this is the file you will run in the command line to run the bot

**3. chatFunctions.py**
you don't need to do anything this file

---

## understanding how it works and how to use it:

First, go to config.py and read the descriptions above the 3 main variables there.

each time you send a message to the bot, it will receive:
1. the "prepend" string
2. past N interactions
3. current message you just sent
 
so if you defined "prepend" like this:
```
prepend = "A and B are close friends and neighbors. Both are friendly and witty. B often has new projects and ideas he wants to talk about.\n"
```
and "initPrompt" as this:
```
initPrompt = "A: Hey
B: Heyooo. what up
A: nm. beautiful day today!
B: absoluteley!"
```
and you enter the following in the command line to send as a message to the bot:
```
So you got any plans for the weekend?
```
then this is what will get sent to the bot API:
```
A and B are close friends and neighbors. Both are friendly and witty. Ty often has new projects and ideas he wants to talk about.\n

A: Hey
B: Heyooo. what up
A: nm. Beautiful day out today!
B: Absolutely
A: So you got any plans for the weekend? 
B: 
```
*(the program handles adding all the A: B: stuff)*

The API needs all this info to create a good response! If you just sent "So you got any plans this weekend", the response would be wildly unpredictable. 

So what this program does is handle remembering and sending all the extra context for you, so that you can just interact with the bot as if it's a normal conversation

---
## Token Use (OpenAI's pricing)

Open AI  charges by the token (words, basically). You get charged for the tokens you send to the bot, and the tokens that the bot sends back.

So each time you send a message, you are charged for all the text in the prompt, plus for whatever text the bot generates and sends back.

That means the vast majority of the tokens you are charged are actually for the context you provide with each call. But the bot needs that context to be able to know what to say! That is the tradeoff: more context means better responses, but it's more expensive. Choose wisely.

---
## Running The Bot:

1. Set up your chatConfig.py file
2. install the openAI library
```bash
pip install openai
```
3. Run the program
```bash
python3 main.py
```