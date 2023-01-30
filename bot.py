import discord
global scores
scores = []
intents = discord.Intents.default()
intents.message_content = True
global client
client = discord.Client(intents=intents)
class Leaderboard:
    def init(self):
        client.run("MTA2Nzc1NjYxMDEwMzAyNTY4NA.GAyBFT.7e7ifFnVL425Lshwac1DYSKVsUFXHpvxZc02g4")
        
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message : discord.Message):
        if message.author == client.user:
            return
        int_list = "0123456789"
        nu = -1 
        strnum = ""
        for char in message.content:
            nu += 1
            if char in int_list:
                for i in range(nu, nu+3):
                    if message.content[i] in int_list:
                        strnum = strnum+message.content[i]
                        continue
        lis = [int(strnum)]
        num = -1
        st = ""
        for char in message.content:
            num += 1
            if char == "$":
                for i in range(1, len(char)-num):
                    st = st+message.content[i+num]
                break
        lis.append(st)
        scores.append(lis)
        print(scores)
        return
Leaderboard = Leaderboard()
Leaderboard.init()