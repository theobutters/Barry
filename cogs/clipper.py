import discord
from discord.ext import commands
from collections import defaultdict, deque
import io
import html
import asyncio
from playwright.sync_api import sync_playwright
import re

class Clipper(commands.Cog):
    def __init__(self, bot: commands.Bot, history_limit: int = 8):
        self.bot = bot
        self.history_limit = history_limit
        self.channel_logs = defaultdict(lambda: deque(maxlen=self.history_limit))

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        self.channel_logs[message.channel.id].append(message)

    def get_user_color(self, member: discord.Member) -> str:
        if member.color.value != 0:
            return f"#{member.color.value:06x}"
        return "#ffffff"

    def parse_markdown(self, text: str) -> str:
        text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
        text = re.sub(r"__(.+?)__", r"<u>\1</u>", text)
        return text

    async def replace_mentions(self, message: discord.Message) -> str:
        text = message.content

        for user in message.mentions:
            mention_html = f'<span class="mention user">@{html.escape(user.display_name)}</span>'
            text = text.replace(f"<@{user.id}>", mention_html)
            text = text.replace(f"<@!{user.id}>", mention_html)

        if isinstance(message.channel, discord.TextChannel):
            for role in message.role_mentions:
                role_color = f"#{role.color.value:06x}" if role.color.value else "#3ba55d"
                mention_html = f'<span class="mention role" style="background-color:{role_color}">@{html.escape(role.name)}</span>'
                text = text.replace(f"<@&{role.id}>", mention_html)

        return text

    @commands.command()
    async def clip(self, ctx: commands.Context, num: int = None):
        limit = num if (num is not None and num > 0) else self.history_limit
        messages = list(self.channel_logs[ctx.channel.id])[-limit:]
        if not messages:
            await ctx.send("No messages to clip yet.")
            return

        html_parts = []
        html_parts.append("""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>Transcript</title>
        <style>
            body { background:#36393f; color:#dcddde; font-family:'Segoe UI', sans-serif; padding:20px; }
            .message { display:flex; margin:10px 0; }
            .avatar { width:40px; height:40px; border-radius:50%; margin-right:10px; flex-shrink:0; }
            .content { max-width:600px; }
            .header { display:flex; align-items:baseline; margin-bottom:2px; flex-wrap:wrap; }
            .author { font-weight:600; margin-right:6px; }
            .timestamp { font-size:0.75em; color:#72767d; }
            .bubble { display:inline-block; background:#2f3136; padding:8px 12px; border-radius:8px; white-space:pre-wrap; word-wrap:break-word; }
            code { background:#202225; padding:2px 4px; border-radius:4px; font-family:monospace; }
            .mention.user { background-color:#00b0f4; color:#fff; padding:2px 4px; border-radius:3px; font-weight:600; display:inline-block; }
            .mention.role { color:#fff; padding:2px 4px; border-radius:3px; font-weight:600; display:inline-block; }
        </style>
        </head>
        <body>
        """)

        for m in messages:
            timestamp = m.created_at.strftime("%H:%M:%S")
            author_name = html.escape(m.author.display_name)
            avatar_url = m.author.display_avatar.url
            if isinstance(m.author, discord.Member):
                color = self.get_user_color(m.author)
            else:
                color = "#ffffff"

            content = await self.replace_mentions(m)
            content = self.parse_markdown(content)
            if not content.strip():
                content = "‎"

            html_parts.append(f"""
            <div class="message">
                <img class="avatar" src="{avatar_url}">
                <div class="content">
                    <div class="header">
                        <span class="author" style="color:{color}">{author_name}</span>
                        <span class="timestamp">{timestamp}</span>
                    </div>
                    <div class="bubble">{content}</div>
                </div>
            </div>
            """)

        html_parts.append("</body></html>")
        html_text = "\n".join(html_parts)

        def render():
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(viewport={"width":800, "height":600})
                page.set_content(html_text)
                screenshot_bytes = page.screenshot(full_page=True)
                browser.close()
            return screenshot_bytes

        screenshot_bytes = await asyncio.to_thread(render)
        await ctx.send(file=discord.File(io.BytesIO(screenshot_bytes), filename="clip.png"))

async def setup(bot: commands.Bot):
    await bot.add_cog(Clipper(bot))
