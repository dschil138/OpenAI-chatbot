import openai
import time
import random
from chatConfig import *


def randomSleep(num1, num2):
    randomNumber = random.uniform(num1, num2)
    time.sleep(randomNumber)


def addUserToPrompt(prevPromptV, userInputV):
    newPrompt = prevPromptV + "\nD: " + userInputV + "\nC: "
    if (newPrompt.count("D: ") > numberOfInteractions):
        index = newPrompt.find("D: ", newPrompt.find("D: ") + 1)
        strippedPrompt = newPrompt[index:]
    else:
        strippedPrompt = newPrompt
    return strippedPrompt


def addBotToPrompt(promptWithUserV, botResponse):
    newPrompt = promptWithUserV + botResponse
    return newPrompt


def sendToBot(prependV, myPrompt):
    fullPrompt = prependV + myPrompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=fullPrompt,
        temperature=1,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=1.0,
        presence_penalty=1.0,
        stop=["D:"]
    )
    time.sleep(1)
    latestResponse = response.choices[0].text.strip()
    print(f"\nC: {latestResponse}\n")
    return latestResponse

