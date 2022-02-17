import os
import discord
import names
import random
import os
client=discord.Client()
@client.event
async def on_ready(): 
  print('you are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/help'):
    await message.channel.send('hello soldier type roll to roll dice')

  if message.content.startswith('/roll'):
    n = random.randint(1,6)
    await message.channel.send(n)
    
  if message.content.startswith('/flip'):
    n = random.randint(0,1)
    coin=["heads","tails"]
    await message.channel.send(coin[n])
      
  if message.content.startswith('/name '):
    print('enter male or female')
    if message.content.startswith('male'):
        await message.channel.send(names.get_full_name(gender='male'))
    else: message.channel.send(names.get_full_name(gender='female'))
       
   
    

  
  
my_secret = os.environ['token']
client.run(my_secret)

                                
    







