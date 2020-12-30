from chatterbot import ChatBot

bot = ChatBot('Norman',
    logic_adapters=[
            "chatterbot.logic.BestMatch"
    ],
      preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ]

)
