'''
Created on Apr 8, 2017

@author: ameya
'''
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot_corpus import corpus


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    # storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        # "chatterbot.comparisons.levenshtein_distance",
        # "chatterbot.response_selection.get_first_response",
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    output_format="text",
    trainer='chatterbot.trainers.UbuntuCorpusTrainer',
    database="../database.json"
    # database="chatbot"
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english"
#     "chatterbot.trainers.UbuntuCorpusTrainer"
)

print("Type something to begin...")
bot.train()
# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break