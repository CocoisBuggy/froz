import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import bot
import sys
import json
import os

botToken = open('token.txt', 'r', encoding='utf8')
Token = botToken.read()

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

class FrozStats: 
    message_count = ""  
    level = ""

#  Get the last used msg-level values
with open('message_count.txt', 'r', encoding='utf8') as f:
        message_count=f.read()

with open('level.txt', 'r', encoding='utf8') as f:
        level=f.read()

class write:

    def read_stats():
        with open('level.txt', 'r', encoding='utf8') as levelR:
            hel = levelR.read()
            FrozStats.level = hel

        with open('message_count.txt', 'r', encoding='utf8') as msgc:
            hel = msgc.read()
            FrozStats.message_count = hel

        print("msg count: ", FrozStats.message_count)
        print("level: ", FrozStats.level)

write.read_stats()
print("got new stats")
print("msg count: ", FrozStats.message_count)
print("level: ", FrozStats.level)
print("Token: ", Token)
print("------------")


class MyClient(discord.Client):


    async def on_ready(self):
        activity = discord.Game(name="Hmm")
        await client.change_presence(status=discord.Status.online, activity=activity)

        print('Logged on as {0}!'.format(self.user))
        print('We go now!')


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        cont=message.content.lower()
        print(cont)
        print(message.author.id)
        

        #IF Alex sends message
        if message.author.id == 185790487569891328:

            print("MESSAGE FROM THE FREEZED! HE IS ON MESSAGE {}".format(FrozStats.message_count))
            ##  Increment the msgcount
            ## Also Augment Level when needed

            with open('message_count.txt', 'w', encoding='utf8') as msgc:
                FrozStats.message_count = int(FrozStats.message_count) + 1
                msgc.write(str(FrozStats.message_count)) 

            print("msg count: ", FrozStats.message_count)
    
            int_check = int(FrozStats.message_count) / 10
            if int_check.is_integer():
                print(int_check, "Level uP!")

                with open('level.txt', 'w', encoding='utf8') as msgc:
                    FrozStats.level = int(FrozStats.level) + 1
                    msgc.write(str(FrozStats.level)) 
                print("level: ", FrozStats.level)
                await message.channel.send("Congratulations FreeZed!!! You just leveled up!!! **You are now level {}**, Well done!!!".format(FrozStats.level))
            
client = MyClient()
client.run(Token)
