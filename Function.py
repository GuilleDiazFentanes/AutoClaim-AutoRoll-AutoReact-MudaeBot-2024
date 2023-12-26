import discum
import json
import time
import requests
import Vars
from discum.utils.slash import SlashCommander

botID = '432610292342587392' 
auth = {'authorization' : Vars.token}
bot = discum.Client(token = Vars.token, log=False)
url = (f'https://discord.com/api/v8/channels/{Vars.channelId}/messages')

def simpleRoll():

    print('Starting to Roll')
    i = 1
    x = 0
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])
    continueRolling = True

    while continueRolling == True or x < 4:

        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data = rollCommand)
        time.sleep(1.2)
        r = requests.get(url , headers = auth )
        jsonCard = json.loads(r.text)

        if (len(jsonCard[0]['content']) != 0):
            x += 1  
            continueRolling = False
            continue
        idMessage = (jsonCard[0]['id'])
        try:
            cardName = (jsonCard[0]['embeds'][0]['author']['name'])
            cardSeries = (jsonCard[0]['embeds'][0]['description']).replace('\n', '**').split('**')[0]
            print(i,' ---- '+cardName+' - '+ cardSeries) 
        except IndexError:
            cardName = 'null'
            cardSeries = 'null'

        try:
            cardsKakera = (jsonCard[0]['components'][0]['components'][0]['emoji']['name'])
            print(cardsKakera)
            print(Vars.desiredKakeras)
            if cardsKakera in Vars.desiredKakeras:
                print('Trying to react to '+ cardsKakera)
                bot.click( jsonCard[0]['author']['id'], channelID =jsonCard[0]['channel_id'], guildID = Vars.serverId, messageID=jsonCard[0]['id'], messageFlags=jsonCard[0]['flags'], data={'component_type': 2, 'custom_id': jsonCard[0]['components'][0]['components'][0]['custom_id']},)

        except IndexError:
            cardsKakera = 'null'

        if cardSeries in Vars.desiredSeries:
            if not 'footer' in jsonCard[0]['embeds'][0] or not 'icon_url' in jsonCard[0]['embeds'][0]['footer']:
                print('Trying to Claim '+ cardName)
                r= requests.put(f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/🐿️/%40me',headers=auth)
                time.sleep(2.6)
        i += 1
    print('Rolling ended')

    if(Vars.pokeRoll):
        print('\nTrying to roll Pokeslot')
        requests.post(url=url , headers = auth, data = {'content' : '$p'})

