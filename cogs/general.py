import discord
from discord.ext import commands


class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    print(f"\n{self.bot.user.name} was called for in #{ctx.channel} by @{ctx.author.name} (<@{ctx.author.id}>).")
    latency_ms = round(self.bot.latency * 1000)
    await ctx.reply(f"Okay?\n-# It took Barry {latency_ms} ms to be pinged.")

    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} was successfully pinged in {latency_ms} ms for {trail}.")

  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(
      title="__Commands__",
      description=f"""
        Barry's prefix is `barry, `, `barry `, `Barry, `, or `Barry `. The space at the end is important.
        Here are the currently available interactions:
        \n\n__**General**__
        `Barry, help` - Show this help message.
        `Barry, ping` - Find out how fast Barry can be pinged.
        \n\n__**Fun**__
        `Barry, roast/burn/mock/ridicule <target>` - Make Barry talk shit about someone or something.
        `Barry, merc/kill/murder/destroy/eliminate <target>` - Make Barry kill someone or something.
        `Barry, hug/cuddle/comfort/pet <target>` - Make Barry hug someone or something.
        \n\n__**Games**__
        `Barry, rps <choice>` - Play Rock, Paper, Scissors. Choices: `rock`, `paper`, `scissors` or `r`, `p`, `s` respectively.
        \n\n__**Other**__
        
        \n\n__**Secret**__
        There's a number of unlisted commands that you can try to find out.
        \n\n<@{self.bot.user.id}> is a bot created by \@figure.one (<@805126418152685568>).
      """,
      color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    
    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} provided help to {trail}.")

async def setup(bot):
  await bot.add_cog(General(bot))