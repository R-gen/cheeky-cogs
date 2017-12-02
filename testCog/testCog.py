import discord
from discord.ext import commands

class testCog:


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):

        #Your code will go here
	await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

def setup(bot):
    bot.add_cog(testCog(bot))

	
