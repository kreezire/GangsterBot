from chatterBotApi.python.chatterbotapi import ChatterBotFactory, ChatterBotType
from gizoogleTranslateApi.GizoogleTranslator import GizoogleTranslator
factory = ChatterBotFactory()

#bot1 = factory.create(ChatterBotType.CLEVERBOT)
#bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()
gizoogleTranslator = GizoogleTranslator()

inputText = raw_input('Say something to Bot: ')
while (1):
	
    #print 'bot1> ' + s
	botReply = bot2session.think(inputText)
	print "bot> " + gizoogleTranslator.translate(botReply)
	inputText = raw_input("You> ")
    #s = bot1session.think(s);




#print gizoogleTranslator.translate(translateInput)

#print(response.text)