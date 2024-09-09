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

    print (time.strftime("Rolling at %H:%M - %d/%m/%y",time.localtime()))
    i = 1
    x = 0
    claimed = '❤️'
    unclaimed = '🤍'
    kakera = '💎'
    emoji='👍'
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])
    continueRolling = True

    while continueRolling == True or x < 4:

        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data = rollCommand)
        time.sleep(1.8)
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
            cardPower = int((jsonCard[0]['embeds'][0]['description']).split('**')[1])
        except IndexError:
            cardName = 'null'
            cardSeries = 'null'
            cardPower = 0
        except KeyError:
            cardName = 'null'
            cardSeries = 'null'
            cardPower = 0
        except ValueError:
            cardPower = 0
        if not 'footer' in jsonCard[0]['embeds'][0] or not 'icon_url' in jsonCard[0]['embeds'][0]['footer']:
            print(i,' - '+unclaimed+' ---- ',cardPower,' - '+cardName+' - '+cardSeries)
            if cardSeries in Vars.desiredSeries:
                print('Trying to Claim '+ cardName)
                r= requests.put(f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/{emoji}/%40me',headers=auth)
        else: 
            print(i,' - '+claimed+' ---- ',cardPower,' - '+cardName+' - '+cardSeries)

        cardsKakera = (jsonCard[0]['components'][0]['components'][0]['emoji']['name'])
        components = jsonCard[0]["components"][0]['components']
        for index in range(len(components)):
            try:
                if cardsKakera in Vars.desiredKakeras:
                    x -= 1 
                    print(kakera+' - '+kakera+' - Trying to react to '+ cardsKakera+ ' of '+ cardName)
                    bot.click(jsonCard[0]['author']['id'], channelID =jsonCard[0]['channel_id'], guildID = Vars.serverId, messageID=jsonCard[0]['id'], messageFlags=jsonCard[0]['flags'], data={'component_type': 2, 'custom_id': components[index]['custom_id']})
                    time.sleep(0.5)

            except IndexError:
                cardsKakera = 'null'
                
        i += 1
    print('Rolling ended')

    if(Vars.pokeRoll):
        print('\nTrying to roll Pokeslot')
        requests.post(url=url , headers = auth, data = {'content' : '$p'})
