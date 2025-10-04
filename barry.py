import os, asyncio, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("token.env")
# Create a token.env file with "DISCORD_TOKEN=your_token_here" inside it (no inverted commas)

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
  raise ValueError("DISCORD_TOKEN not found")

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
intents.presences = True

bot = commands.Bot(
  command_prefix=("barry, ", "barry ", "Barry, ", "Barry "),
  intents=intents,
  help_command=None
)

@bot.event
async def on_ready():
  print(f"\n{bot.user.name} just woke up and is ready to go.\n")

async def main():
  for file in os.listdir("./cogs"):
    if file.endswith(".py"):
      await bot.load_extension(f"cogs.{file[:-3]}")
  await bot.start(TOKEN)

if __name__ == "__main__":
  asyncio.run(main())
 