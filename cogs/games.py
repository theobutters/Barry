import random
from discord.ext import commands

class Games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def rps(self, ctx, choice: str):
    invalid_response = [
      f"You cant play with \"{choice}\". Choose rock, paper, or scissors.",
      f"\"{choice}\" is not a valid option. Pick rock, paper, or scissors.",
      f"\"{choice}\"? Really? Just pick rock, paper, or scissors.",
      f"\"{choice}\" is not an option. Pick rock, paper, or scissors.",
      f"\"{choice}\"? Pick rock, paper, or scissors.",
      f"What? How do I play against \"{choice}\"?",
    ]
    bot_loses = [
      "You win.", 
      "How'd you do that?", 
      "Thought I had you, you win.", 
      "I hate this game.",
      "Every time I think I'm gonna win, I lose.",
      "Mods ban them, they're hacking.",
    ]
    bot_wins = [
      "I win.",
      "Woo, I win.",
      "Woo, you lose.",
      "You lost.",
      "Oh yeah, I knew I'd win.",
      "You lose.",
      "Somebody clip this.",
    ]
    bot_draws = [
      "Well, that was unexpected.",
      "Pick something different.",
      "Did u read my mind?",
      "Breh.",
      "Okay, stop looking at my cards.",
      "Are you casting some crazy magic? How've you done that?",
      "What? How?",
      "I swear I was gonna win that.",
    ]

    choices = ["rock", "paper", "scissors"]
    if choice.lower() == "r":
      choice = "rock"
    elif choice.lower() == "p":
      choice = "paper"
    elif choice.lower() == "s":
      choice = "scissors"

    bot_choice = random.choice(choices)

    if choice.lower() not in choices:
      await ctx.send(random.choice(invalid_response))
      return

    trail = f"@{ctx.author} (<@{ctx.author.id}>) in #{ctx.channel} of {ctx.guild} ({ctx.guild.id})"

    if choice.lower() == bot_choice:
      result = f"{bot_choice.title()}.\n{random.choice(bot_draws)}"

      print(f"{self.bot.user.name} drew in a game of rock, paper, scissors against {trail}.")

    elif (choice.lower() == "rock" and bot_choice == "scissors") or \
      (choice.lower() == "paper" and bot_choice == "rock") or \
      (choice.lower() == "scissors" and bot_choice == "paper"):
      result = f"{bot_choice.title()}.\n{random.choice(bot_loses)}"

      print(f"{self.bot.user.name} lost in a game of rock, paper, scissors against {trail}.")

    elif (choice.lower() == "rock" and bot_choice == "paper") or \
      (choice.lower() == "paper" and bot_choice == "scissors") or \
      (choice.lower() == "scissors" and bot_choice == "rock"):
      result = f"{bot_choice.title()}.\n{random.choice(bot_wins)}"

      print(f"{self.bot.user.name} won in a game of rock, paper, scissors against {trail}.")

    await ctx.reply(result)

async def setup(bot):
  await bot.add_cog(Games(bot))
