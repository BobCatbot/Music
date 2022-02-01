import discord, asyncio

async def chpr(client):
    await client.wait_until_ready()

    while not client.is_closed():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"my code"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="help"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="www.youtube.com"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my commands"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"www.bobcatbot.xyz"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over my devs"))
        await asyncio.sleep(10)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{str(len(client.guilds))} servers"))
        await asyncio.sleep(10)


#OWNER CMDS
red = 0xed5757
green = 0x57f287
owner = 0x5865f2