import discord
from discord.ext import commands

class testCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")
		
		
		
		
		async def punch(self, user : discord.Member):
			"""I will puch anyone! >.<"""
			#Your code will go here
			await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")
			
			embed=discord.Embed(description=" ")
		embed.set_author(name= ")
		embed.set_thumbnail(url="https://i.imgur.com/gRyvWkD.png")
		embed.add_field(name= , value= , inline=False)
		await self.bot.say(embed=embed)
		
		
		
		

def setup(bot):
    bot.add_cog(testCog(bot))
