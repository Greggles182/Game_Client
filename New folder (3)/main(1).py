import discord
from discord import DMChannel
import subprocess
from keep_alive import keep_alive
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged On")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        categoryID = message.channel.category.id
        category = message.channel.category
    except AttributeError:
        print("channel not in category")
        category = "Not in category"
        categoryID = 000
    chID = message.channel.id
    channel = message.channel
    authID = message.author.id
    auth = message.author
    messageID = message.id
    content = message.content
    if (categoryID == 1089463556749144096):
        return
    #debug
    print(categoryID) #ID of category
    print(chID)       #ID of channel
    print(authID)     #ID of author
    print(messageID)  #ID of message
    print(category)   #Category
    print(channel)    #Channel
    print(auth)       #Author
    print(content)    #Message Content
    await message.channel.send("Registering...")
    if (content == "help"):
        await message.channel.send("Sent to yo DM's")
        #await DMChannel.send(auth, "Hello there!")
        embed=discord.Embed(title="Commands below:", url="https://cog-creators.github.io/discord-embed-sandbox/", description="It's very simple", color=0xff0000)
        embed.add_field(name="help", value="Sends this message", inline=False)
        embed.add_field(name="Program {Number}", value="Note number and space. Runs program specified.", inline=False)
        embed.set_footer(text="End of universe is imminent...")
        await DMChannel.send(auth, embed=embed)
    elif message.content.startswith ("Program"):
        length = len(content)
        for i in range(8, length):
            print(i)
            print("Char")
            char = content[i]
            if (i == 8):
                full = char
            else:
                full += char
        await message.channel.send("Loading Program: " + full)
        print(full)
        subprocess.Popen(["python3", full + ".py"])
    else:
        await message.channel.send("""This is not a command. Try "help".""")
        
    #print("Success")
    
keep_alive()
client.run("OTY4NjU0ODMzMDkzNTc0Njc2.YmiAHA.VqcC6YV2oM8XkqWvQiQI9oqs73I")