import random, discord
from discord.ext import commands

class Secret(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def secret(self, ctx):
    embed = discord.Embed(
      title="__Secret Commands__",
      description=f"""
        `Larry, larry`
        \n`Larry, barry`
        \n\n<@{self.bot.user.id}> is a bot created by \@figure.one (<@805126418152685568>).
      """,
      color=discord.Color.blurple()
    )
    await ctx.send(embed=embed)
    
    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} provided secrets to {trail}.")

  @commands.command()
  async def larry(self, ctx):
    responses = [
      "Thats not me, I'm Barry.",
      "No, I'm Barry.",
      "That's not my name, I'm Barry.",
      "Larry? That's not me.",
      "I'm not Larry.",
      "Larry isn't here.",
    ]
    await ctx.reply(random.choice(responses))

    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} was called Larry by {trail}")

  @commands.command()
  async def barry(self, ctx):
    responses = [
      "Hi, I'm Barry.",
      "Yep, I'm Barry.",
      "That's my name.",
      "Whats up?",
      "I'm Barry.",
      "I'm here.",
    ]
    await ctx.reply(random.choice(responses))

    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    print(f"\n{self.bot.user.name} was irritated by {trail}")

async def setup(bot):
  await bot.add_cog(Secret(bot))
