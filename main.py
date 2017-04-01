from chatterBotApi.python.chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()

#bot1 = factory.create(ChatterBotType.CLEVERBOT)
#bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

inputText = raw_input('Say something to Bot: ')
while (1):
	
    #print 'bot1> ' + s
	botReply = bot2session.think(inputText)
	print "bot> " + botReply
	inputText = raw_input("You> ")
    #s = bot1session.think(s);