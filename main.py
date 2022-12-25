from chatConfig import *
from chatFunctions import *

while True:
    userInput = input("D: ")
    promptWithUser = addUserToPrompt(initPrompt, userInput)
    randomSleep(0.8, 3.8)
    botResponse = sendToBot(prepend, promptWithUser)
    initPrompt = addBotToPrompt(promptWithUser, botResponse)
    
