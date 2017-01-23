import discord
import asyncio
import requests

token = "TKN"

#adds a prefix to the trigger for testing
trigPref = ""

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in')

#SCPBotCode

@client.event
async def on_message(message):
    trigMessage = message.content.lower()
    
    if trigMessage.startswith(trigPref + 'scp-'):
        await client.send_typing(message.channel)
        msg = message.content.split('-', 1)[1]
        
        if len(msg) <= 4 and len(msg) >= 3 and msg.isdigit():
            tmp_msg = await client.send_message(message.channel, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Checking for existence...*')
            scp = requests.get('http://www.scp-wiki.net/scp-' + msg)
            if scp.status_code == 200:
#                await client.send_typing(message.channel)
                await client.edit_message(tmp_msg, '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *SCP exists!*')

#               Someday images may get sent. Not today.
#                tree = BeautifulSoup(scp.text, "lxml")  
#                img_link = tree.find_all('div', class_="scp-image-block")[0].img.get('src')
#                await client.send_file(message.channel, img_link, filename='SCP-' + msg + '_img', content=None, tts=False)
                
            elif scp.status_code == 404:
                await client.edit_message(tmp_msg, '~~**Link:** http://www.scp-wiki.net/scp-' + msg + '~~ *SCP does not exist.*')
            else:
                await client.edit_message(tmp_msg,  '**Link:** http://www.scp-wiki.net/scp-' + msg + ' *Unable to determine if this SCP exists.*')

        else:
            await client.send_message(message.channel, 'SCP must be a 3 or 4 digit number. Example: `SCP-1175`')
#SarcasmBotCode
    elif trigMessage.startswith(trigPref + 'haha'):
        await client.send_message(message.channel, '^ sarcasm tbh')
#AyyLmaoBotCode
    elif trigMessage.startswith(trigPref + 'ayy'):
        await client.send_message(message.channel, 'lmao')
#StarWarsTitle
    elif trigMessage.startswith(trigPref + 'sw'):
        msg = message.content.split(' ', 1)[1]
        if len(msg) == 1 and msg.isdigit() and int(msg) >= 0 and int(msg) <= 9:
            titles =  {
                1: 'The Phantom Menace',
                2: 'Attack of the Clones',
                3: 'Revenge of the Sith',
                4: 'A New Hope',
                5: 'The Empire Strikes Back',
                6: 'Return of the Jedi',
                7: 'The Force Awakens',
                8: 'The Last Jedi',
                9: '[TBA]'
            }
            await client.send_message(message.channel, 'That Star Wars movie is called *' + titles[int(msg)] + '*')
#LoadingBar
    elif trigMessage.startswith(trigPref + 'load'):
        progress = 0
        loading = await client.send_message(message.channel, str(progress) + '% ----------------------------- 100%')
        i=0
        while i <= 100:
            progress = progress-1
            await client.edit_message(loading, '`10%  ||------------------ 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`20%  ||||---------------- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`30%  ||||||-------------- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`40%  ||||||||------------ 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`50%  ||||||||||---------- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`60%  ||||||||||||-------- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`70%  ||||||||||||||------ 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`80%  ||||||||||||||||---- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`90%  ||||||||||||||||||-- 100%`')
            await asyncio.sleep(0.5)
            await client.edit_message(loading, '`100% |||||||||||||||||||| 100%`')
            i = i+1
#LoadingBar
    elif trigMessage.startswith(trigPref + '`sudo order pizza`'):
        await client.send_message(message.channel,':pizza:')

client.run(token)