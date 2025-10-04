import random, re
from asyncio import sleep
from discord.ext import commands
from discord.utils import get

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=["burn", "ridicule", "mock"])
  async def roast(self, ctx, *, tgt: str):
    guild = ctx.guild
    member = None

    print(f"\nRaw input target: {tgt}")

    mention_match = re.match(r"<@!?(\d+)>", tgt)
    if mention_match:
      user_id = int(mention_match.group(1))
      member = guild.get_member(user_id)
      print(f"Detected mention. User ID: {user_id}, Resolved member: {member}")

    if member is None and tgt.isdigit():
      user_id = int(tgt)
      member = guild.get_member(user_id)
      print(f"Trying ID lookup. User ID: {user_id}, Resolved member: {member}")

    if member is None:
      member = get(guild.members, name=tgt)
      print(f"Trying exact username. Member found: {member}")

    if member is None:
      member = get(guild.members, display_name=tgt)
      print(f"Trying exact nickname. Member found: {member}")

    if member is None and len(tgt) >= 5:
      member = next(
        (
          m for m in guild.members
          if any(
            tgt[i:i+5].lower() in m.name.lower() or tgt[i:i+5].lower() in m.display_name.lower()
            for i in range(len(tgt) - 4)
          )
        ),
        None
      )
      print(f"Trying partial match. Member found: {member}")

    target = member.mention if member else tgt
    print(f"Final target: {target}")

    responses = [
      f"{target} looks dehydrated.",
      f"{target} has something on their chin. No, the other chin.",
      f"{target} is so full of themselves, they could drown in a rainstorm.",
    ]
    responses2 = [
      f"\"{target}\" sounds like the name of a bean bag retailer.",
      f"Did you mean to roast someone else? Because \"{target}\" doesn't sound like a real person.",
      f"I'm sorry, I don't roast non-humans. \"{target}\" is not a valid target.",
      f"\"{target}\"? I've seen more intimidating houseplants.",
    ]
    responses3 = [
      "I'm not going to roast myself.",
      "Nope, not happening.",
      "Why would I roast myself?",
    ]

    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    
    if target == f"<@{self.bot.user.id}>":
      await ctx.reply(random.choice(responses3))

      print(f"\n{self.bot.user.name} refused to roast @{self.bot.user.name} (<@{self.bot.user.id}>) for {trail}.")

    else:
      if member:
        await ctx.reply(random.choice(responses))
        target_username = ctx.guild.get_member(int(target.strip("<@>"))).name

        print(f"\n{self.bot.user.name} roasted @{target_username} ({target}) for {trail}.")

      else:
        await ctx.reply(random.choice(responses2))

        print(f"\n{self.bot.user.name} roasted {target} for {trail}.")

  @commands.command(aliases=["kill", "murder", "eliminate", "destroy", "smite"])
  async def merc(self, ctx, *, tgt: str):
    guild = ctx.guild
    member = None

    print(f"Raw input target: {tgt}")

    mention_match = re.match(r"<@!?(\d+)>", tgt)
    if mention_match:
      user_id = int(mention_match.group(1))
      member = guild.get_member(user_id)
      print(f"Detected mention. User ID: {user_id}, Resolved member: {member}")

    if member is None and tgt.isdigit():
      user_id = int(tgt)
      member = guild.get_member(user_id)
      print(f"Trying ID lookup. User ID: {user_id}, Resolved member: {member}")

    if member is None:
      member = get(guild.members, name=tgt)
      print(f"Trying exact username. Member found: {member}")

    if member is None:
      member = get(guild.members, display_name=tgt)
      print(f"Trying exact nickname. Member found: {member}")

    if member is None and len(tgt) >= 5:
      member = next(
        (
          m for m in guild.members
          if any(
            tgt[i:i+5].lower() in m.name.lower() or tgt[i:i+5].lower() in m.display_name.lower()
            for i in range(len(tgt) - 4)
          )
        ),
        None
      )
      print(f"Trying partial match. Member found: {member}")

    target = member.mention if member else tgt
    print(f"Final target: {target}")

    responses = [
      f"**Bang**", f"{target} is dead.",
      f"On it.", f"{target} is down.",
      f"Yes sir.", f"{target} just got messed up.",
      f"Consider it done.", f"{target} has been merc'd.",
      f"Affirmative.", f"{target} is no more.",
      
    ]

    responses2 = [
      f"Nice try, <@{ctx.author.id}>. I'm not killing myself.",
      f"Don't be stupid, <@{ctx.author.id}>. I'm not mercing myself.",
      f"Why would I murder myself, <@{ctx.author.id}>? That's just stupid.",
    ]


    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    
    if target == f"<@{self.bot.user.id}>":
      await ctx.reply(random.choice(responses2))

      print(f"\n{self.bot.user.name} refused to merc @{self.bot.user.name} (<@{self.bot.user.id}>) for {trail}.")

    else:
      reply = await ctx.reply(random.choice(responses[0::2]))
      await sleep(1.5)
      await reply.reply(random.choice(responses[1::2]))
      if member:
        target_username = ctx.guild.get_member(int(target.strip("<@>"))).name
        print(f"\n{self.bot.user.name} merc'd @{target_username} ({target}) for {trail}.")
      else:
        print(f"\n{self.bot.user.name} merc'd {target} for {trail}.")

  @commands.command(aliases=["comfort", "pet", "cuddle"])
  async def hug(self, ctx, *, tgt: str):
    guild = ctx.guild
    member = None

    print(f"Raw input target: {tgt}")

    mention_match = re.match(r"<@!?(\d+)>", tgt)
    if mention_match:
      user_id = int(mention_match.group(1))
      member = guild.get_member(user_id)
      print(f"Detected mention. User ID: {user_id}, Resolved member: {member}")

    if member is None and tgt.isdigit():
      user_id = int(tgt)
      member = guild.get_member(user_id)
      print(f"Trying ID lookup. User ID: {user_id}, Resolved member: {member}")

    if member is None:
      member = get(guild.members, name=tgt)
      print(f"Trying exact username. Member found: {member}")

    if member is None:
      member = get(guild.members, display_name=tgt)
      print(f"Trying exact nickname. Member found: {member}")

    if member is None and len(tgt) >= 5:
      member = next(
        (
          m for m in guild.members
          if any(
            tgt[i:i+5].lower() in m.name.lower() or tgt[i:i+5].lower() in m.display_name.lower()
            for i in range(len(tgt) - 4)
          )
        ),
        None
      )
      print(f"Trying partial match. Member found: {member}")

    target = member.mention if member else tgt
    print(f"Final target: {target}")

    responses = [
      "Sure.", f"-# *Hugs {target}*", "Hey, this isn't so bad.",
      "Okay.", f"-# *Comforts {target}*", "Happy now?",
      "Alright.", f"-# *Cuddles {target}*", "That was nice.",
    ]

    responses2 = [
      "Myself? Okay.",
      "Me? Sure, why not.",
      "Why not? I could use a hug.",
      "Yeah, I guess I can hug myself.",
      "If I must.",
      "I suppose I can manage that.",
      "Fine, I'll hug myself."
    ]


    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"
    
    if target == f"<@{self.bot.user.id}>":
      await ctx.reply(random.choice(responses2))

      print(f"\n{self.bot.user.name} was told to hug themselves by @{self.bot.user.name} (<@{self.bot.user.id}>) for {trail}.")

    else:
      reply = await ctx.reply(random.choice(responses[0::3]))
      await sleep(1.5)
      reply2 = await reply.reply(random.choice(responses[1::3]))
      await sleep(1.5)
      await reply2.reply(random.choice(responses[2::3]))
      if member:
        target_username = ctx.guild.get_member(int(target.strip("<@>"))).name
        print(f"\n{self.bot.user.name} hugged @{target_username} ({target}) for {trail}.")
      else:
        print(f"\n{self.bot.user.name} hugged {target} for {trail}.")

async def setup(bot):
  await bot.add_cog(Fun(bot))