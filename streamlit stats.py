import streamlit as st, discord, asyncio

st.title("PossiblyAxolotl's Backpack Server Stats")

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    guild = client.get_guild(765639308207325226)
    online_members = []
    total_members = []
    for member in guild.members:
        if member.status is not discord.Status.offline:
            online_members.append(member.name)
            total_members.append(member.name)
        else:
            total_members.append(member.name)
    
    st.write(f"The server ID is: {guild.id}\n\nThe server is owned by {guild.owner}\n\nThere are currently {len(online_members)} members online and {len(total_members)} members total")
    exit()

client.run(st.secrets["bot_id"])
