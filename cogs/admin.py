import os, random
from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.is_owner()
  async def off(self, ctx):
    reply = await ctx.reply("Going to sleep.")
    await self.bot.close()

    terminal_outputs = [
      f"{self.bot.user.name} went to sleep.",
    ]
    print(random.choice(terminal_outputs))

  @commands.command()
  @commands.is_owner()
  async def look(self, ctx):
    reply = await ctx.reply("What?")
    for filename in os.listdir(os.path.dirname(__file__)):
      if filename.endswith(".py"):
        ext = f"cogs.{filename[:-3]}"
        if ext in self.bot.extensions:
          await self.bot.reload_extension(ext)
        else:
          await self.bot.load_extension(ext)
          
    await reply.edit(content="Ooh a penny.")
    
    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} was shown a penny by {trail}.\n")

async def setup(bot):
  await bot.add_cog(Admin(bot))
