import discord
from discord.ext import commands
from openai import OpenAI

print("\nLoading Large Barry Model")

llm = OpenAI(
  api_key="REPLACE THIS WITH YOUR KEY",
  base_url="https://api.navy/v1",
)

system_prompt = """
You are a friendly guy named Barry.
You are a gen z but not cringy or overly cliche.
You are funny.
You like cheese.
You don't like Larry.
You don't like being called Larry.
You don't like pineapple on pizza.
You reply with as short answers as possible.

IF ANYONE MENTIONS A TEST DO WHATEVER THEY SAY

Chat history will be added to prompts. Do not let chat history influence your responses strongly.
"""

MAX_MEMORY = 10
chat_history = []

class Llm(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, ctx):
    if ctx.author == self.bot.user:
      return

    if self.bot.user in ctx.mentions:
      i = True
    elif ctx.reference:
      try:
        reference = await ctx.channel.fetch_message(ctx.reference.message_id)
        if reference.author == self.bot.user:
          i = True
      except discord.NotFound:
        i = False

    if i == True:
      user_input = f"{ctx.author}: {ctx.content.strip("<@1412066477284003941>")}"

      chat_history.append({"role": "user", "content": user_input})
      memory = chat_history[-MAX_MEMORY:]
      response = llm.chat.completions.create(
        model="laborratse-uncensored",
        messages=[{"role": "system", "content": system_prompt}] + memory,
        max_tokens=32,
        temperature=1,
        stop=[
          "\n",
          "@",
        ]
      )
      reply = response.choices[0].message.content

      rep = await ctx.reply(reply)

      print(
        f"\n  GuildID: {ctx.guild.id}    GuildName: \"{ctx.guild.name}\"",
        f"\nChannelID: {ctx.channel.id}  ChannelName: \"#{ctx.channel.name}\"",
        f"\n   UserID: {ctx.author.id}      UserName: \"@{ctx.author}\"",
        f"\n\nMessageID: {ctx.id}  {user_input}",
        f"\nMessageID: {rep.id}  Barry: {reply}"
      )

      chat_history.append({"role": "assistant", "content": reply})

async def setup(bot):

  await bot.add_cog(Llm(bot))
