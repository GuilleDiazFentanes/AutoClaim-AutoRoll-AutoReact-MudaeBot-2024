# Mudae AutoRoll AutoClaim AutoReact 2023
### by GDiazFentanes

## Introduction
Auto Rolling, Auto Claiming and Auto Reacting, in order to claim mudae's waifus, kakeras or husbandos every hour automatically. Slash rolling with given parameters for a better botting experience.
These files make it possible to use the Mudae Discord Bot 24/7 without any human input. It is supported by the Discord Api to send and receive messages from any account. After extensive research into the existing bots in late 2023, I realized that none of them are actually working/supported. In order to use it you only need basic knowledge about Discord and Python (If you don't have it, read this document completely and you will easily achieve it).

## Features
- **Auto roll** every hour with the command you want
- **Auto Claim** cards that belong to the series you like
- **Auto React** only to the kakera you prefer
- **Repeat** all the functionalities above each hour the minute you prefer
- **BONUS** - Uses always slash commands in order to benefit from the native slash boosts (10% extra Kakera)

## Files
This repository contains 3 different files:
| File Name | File Purpose | File Purpose |
| ------ | ------ |------ |
| Vars.py | Where the variables that you need to change are stored | Edit it!
| Bot.py | The bot is launched from here | Execute it!
| Function.py | Contains the function and code for the bot to work | Nothing!

## Requirements
This bot requires the following libraries in order to work correctly. Make sure you have them all installed.
[Discum](https://pypi.org/project/discum/) for message management.
[Schedule](https://nodejs.org/) in order to be permanently executed at an exact minute of an hour.

```python
pip install discum
pip install schedule
```

## How to set up /use
##### Pakages
To use this bot you just need to set up a few things. Make sure python 3 is installed along with the 2 required libraries (Discum and Schedule).
If you don't know how to do it, read here → [How to install a Python package](https://packaging.python.org/en/latest/tutorials/installing-packages/)

##### Variables (Vars)
Time to open Vars.py. Here you decide what settings the bot will have. In this section we will see what each variable does and what are the possibilities to fill them out. 
You also choose what Discord account you want to execute the code in and on what guild channel you want the bot to execute the Mudae commands. These two decision will be reflected in these two variables.

**Mandatory variables** : You will have to fill them in if you want the bot to work
+ `token` - The discord Token of the account you want to bot with → [How to get a Discord Token](https://www.androidauthority.com/get-discord-token-3149920/)
+ `channelId` - ID of the channel you want to roll in → [How to get a channel ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  
+ `serverId` - ID of the server/guild you want to roll in → [How to get a server/guild ID](https://docs.statbot.net/docs/faq/general/how-find-id/)  

**Optional variables** : They are already filled by default, but you can change them if you want (specialy the desiredSeries one)

+ `rollCommand` - Choose what command (only one) will the bot use to roll (mx, ma, mg, wx, wg, wa, hx, ha or hg)
+ `desiredKakeras` - **Case-sensitive** - Array of kakera types between single quotes separated by comas (see example below)
+ `desiredSeries` - **Case-sensitive** - Array of series between single quotes separated by comas (see example below)
+ `pokeRoll` - If you want to also roll the Mudae´s Pokeslot (True or False)
+ `repeatMinute` - You can choose what exact minute of the hour will the Bot roll (value between 00 and 59, will be set to 25 by default)

##### Example of correctly filled variables
Depending on the variable type (boolean, string, int or array), the data might be between quotes or not. Please pay attention to it.
In the example, the token, channelId and serverdId are invented fields.
```python
token = 'MTE4MDIyNzU4NTUzNjQzNDMxNw.GDXjNH.YqGhIq7GwyVHSk9sf9zod3AACAffJeZiynTexc' 
channelId = '1182144443902599230'                 
serverId = '816317249082097684'                  
rollCommand= 'wa'
desiredKakeras= ['kakeraP','kakeraY','kakeraO','kakeraR','kakeraW','kakeraL']
desiredSeries = ['One Piece','Dragon Ball Z','Death Note']
pokeRoll = True
repeatMinute = '25'
```
##### Execution
![image](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2023/assets/152492889/b39973db-35b7-4de4-a111-95c40de5c04d)
Once you have completed all the previous steps, you will be able to safely execute Bot.py
This will open the file and start the Bot, logging all the rolls and actions made. The console should look like the image
(note that if you set the minute to 25, the bot won't roll until it's that time every hour)
- Red heart -> already claimed cards
- White heart -> not claimed yet cards

## Possible Errors
- Mudae has no access/write/read permission to the channel you decided
- Your Discord Token may have changed
- Your Mudae settings always have a button on each character roll
- Series and Characters are case-sensitive
- Your account must have a DM (at any time) with the mudae bot (try $help to make sure)

## Advanced Bot

An advanced Bot comes with advanced features!! Let me know if you want me to post it!
These are the advanced Bot features:

- **ALL** the previous features
- **Desired Characters**: AutoClaim the exact characters when they appear with priority over all!
- **Optimized Kakera react**: The bot will use an algorithm to prioritize higher Kakera values without losing any efficiency
- **Optimized $dk use**: The bot will perfectly use and take into account the DK command to get even more effective kakera reactions
- **Optimized $rt use**: In case of not having an available claim, the Bot will use the $rt command to be able to claim
- **Optimized $daily use**: Use the daily command each time it is available
- **Optimized $rolls use**: Use the rolls command to get better claims or kakera reactions
- **Multi-Bot**: Add as many Discord Accounts as you want to do everything menctioned above to multiply your profits


