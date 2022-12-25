
each time you send a message to the bot, it will receive:

prepend

past N interactions

current message you just sent

so if you have:

```py
prepend = "A and B are close friends and neighbors. Both are friendly and witty. Ty often has new projects and ideas he wants to talk about.\n"
```
and:
```py
initPrompt = "A: Hey
B: Heyooo. what up
A: nm. exciting day today!
B: you know it! things have been going great lately. Had to pinch myself yesterday lol"

```
and you enter the following as a message to send to the bot:

```
So you got any plans for the weekend? 
```

then this is what will get sent to the bot API:
```
A and B are close friends and neighbors. Both are friendly and witty. Ty often has new projects and ideas he wants to talk about.\n

A: Hey
B: Heyooo. what up
A: nm. exciting day today!
B: you know it! things have been going great lately. Had to pinch myself yesterday lol
```

# TOKEN USE

Each time you send a message, you are charged tokens for all the above text you are sending, plus for whatever text the bot generates and sends back. So the vast majority of the tokens you are charged are actually for the context you provide with each call. But the bot needs that context to be able to know what to say! That is the tradeoff: more context means better responses, but it's more expensive.