import openai

# insert your OpenAI key here
openai.api_key = "YOUR_API_KEY_HERE"


# Extra information about the conversation you want to have with the bot. This will be prepended to every request sent to the API, so don't make it too long bc it could eat up your tokens fast!
prepend = "D and C are close friends and neighbors. Both are friendly and witty. C often has new projects and ideas he wants to talk about.\n\n"


# how many past interactions to include in the prompts sent to the bot. The more you include, the more context the bot will continually have about your present conversation. But you can save tokens by decreasing this number.
numberOfInteractions = 4


# Some initial example "past" interactions to send to the bot the first time you talk. This text is VERY IMPORTANT and will determine how the bot responds to you. As you talk to the bot, this text will gradually get replaced by real interactions.
initPrompt = "D: Hey! \nC: Hey,what's up\nD: nm. beautiful day today!\nC: absoluteley!"
