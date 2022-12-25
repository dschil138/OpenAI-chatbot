import openai

# insert your OpenAI key here
openai.api_key = "YOUR_API_KEY_HERE"


# Extra info about the conversation you ("D") want to have with the bot ("C").
# This gets prepended to every request sent to the API, so don't make 
# it too long or it will eat up your tokens fast! Or, make it super long. idc
prepend = "D and C are close friends and neighbors. Both are friendly and witty. C often has new projects and ideas he wants to talk about.\n\n"


# Number of most recent interactions to include in the prompts sent to the bot.
# The more you include, the more context the bot will continually have about 
# your present conversation. But you can save tokens by decreasing this number.
numberOfInteractions = 4


# Some initial fake "past" interactions to get you started when you  first 
# message the bot ("C"). This text is VERY IMPORTANT and will determine how the bot
# responds to you. It will follow the lead you set for it here. As you talk to
# the bot, the program will gradually replace these with your actual conversation
initPrompt = "D: Hey! \nC: Hey,what's up\nD: nm. beautiful day today!\nC: absoluteley!"
