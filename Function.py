import discum
import json
import time
import requests
import Vars
from discum.utils.slash import SlashCommander

botID = '432610292342587392' 
auth = {'authorization': Vars.token}
bot = discum.Client(token=Vars.token, log=False)
url = f'https://discord.com/api/v8/channels/{Vars.channelId}/messages'

def simpleRoll():
    print(time.strftime("Rolling at %H:%M - %d/%m/%y", time.localtime()))
    i = 1
    x = 0
    claimed = '❤️'
    unclaimed = '💫'
    kakera = '💎'
    emoji = '⭐'
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])
    continueRolling = True

    while continueRolling or x < 4:
        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data=rollCommand)
        time.sleep(1.8)
        r = requests.get(url, headers=auth)
        jsonCard = json.loads(r.text)

        if not jsonCard or len(jsonCard[0]['content']) != 0:
            x += 1  
            continueRolling = False
            continue

        idMessage = jsonCard[0]['id']
        try:
            cardName = jsonCard[0]['embeds'][0]['author']['name']
            cardSeries = jsonCard[0]['embeds'][0]['description'].replace('\n', '**').split('**')[0]
            cardPower = int(jsonCard[0]['embeds'][0]['description'].split('**')[1])
        except (IndexError, KeyError, ValueError):
            cardName, cardSeries, cardPower = 'null', 'null', 0

        if 'footer' not in jsonCard[0]['embeds'][0] or 'icon_url' not in jsonCard[0]['embeds'][0]['footer']:
            print(f"{i} - {unclaimed} ---- {cardPower} - {cardName} - {cardSeries}")
            if cardSeries in Vars.desiredSeries:
                print(f'Trying to Claim {cardName}')
                requests.put(f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/{emoji}/%40me', headers=auth)
        else: 
            print(f"{i} - {claimed} ---- {cardPower} - {cardName} - {cardSeries}")

        try:
            if 'components' in jsonCard[0] and jsonCard[0]['components']:
                components = jsonCard[0]["components"][0]['components']
                for index in range(len(components)):
                    if 'emoji' in components[index] and 'name' in components[index]['emoji']:
                        cardsKakera = components[index]['emoji']['name']
                        if cardsKakera in Vars.desiredKakeras:
                            x -= 1 
                            print(f"{kakera} - {kakera} - Trying to react to {cardsKakera} of {cardName}")
                            bot.click(jsonCard[0]['author']['id'], channelID=jsonCard[0]['channel_id'], guildID=Vars.serverId, messageID=jsonCard[0]['id'], messageFlags=jsonCard[0]['flags'], data={'component_type': 2, 'custom_id': components[index]['custom_id']})
                            time.sleep(0.5)
        except (IndexError, KeyError):
            pass

        i += 1
    print('Rolling ended')

    if Vars.pokeRoll:
        print('\nTrying to roll Pokeslot')
        requests.post(url=url, headers=auth, data={'content': '$p'})
        
