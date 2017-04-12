from django.shortcuts import render
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

#Chatter bot api and traslation api
from chatterBotApi.python.chatterbotapi import ChatterBotFactory, ChatterBotType
from gizoogleTranslateApi.GizoogleTranslator import GizoogleTranslator
factory = ChatterBotFactory()

#FB Messenger Page Token
FB_MESSENGER_ACCESS_TOKEN = 'EAAGwyoQV2LUBAOdoDTeRQszgIXwih0DoZAh2Cr4sTXrvZBO8vDP4pvVabZCHFbZB1DyA3pidPmaPeq18enk6axVWoouLw2Ekd0ZAaJIBDzr0WVomkmZB0t2c7kMsp27jXdUlSiRTpHDDP6xnk1Cr6ZBQ742uEO03oT29ph8OnjsSgZDZD'

def changeNameInString(inputText):
    return inputText.replace("Chomsky", "Vito (a.k.a The Little Finger)")
    
def respond_FB(sender_id, text):
    try:
        bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
        bot2session = bot2.create_session()
        bot2session.vars['custid']= "gangsterbot"+sender_id
        gizoogleTranslator = GizoogleTranslator()
        botReply = bot2session.think(text)
        json_data = {
            "recipient": {"id": sender_id},
            "message": {"text": changeNameInString(gizoogleTranslator.translate(botReply))}
        }
    except:
        json_data = {
            "recipient": {"id": sender_id},
            "message": {"text": "I don't know what you mean. Try with different text"}
        }
    params = {
        "access_token": FB_MESSENGER_ACCESS_TOKEN
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)
    #print(r, r.status_code, r.text)


@csrf_exempt
def index(request):
    #print request
    #req=json.loads(request.body)
    if request.method == 'POST':
        try:
            body = request.body
            #print("BODY", body)
            messaging_events = json.loads(body.decode("utf-8"))
            #print("JSON BODY", body)
            sender_id = messaging_events["entry"][0]["messaging"][0]["sender"]["id"]
            message = messaging_events["entry"][0]["messaging"][0]["message"]["text"]
            respond_FB(sender_id, message)
            return HttpResponse('Received.')
        except:
            return HttpResponse('')
    else:
        if request.GET.get('hub.verify_token') == 'make_me_an_offer_i_can_not_refuse':
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
           return HttpResponse("Hello, world. This is Faacebook Messenger API.")