from discord.ext import commands

from hooks.discord.use_discord import make_embed, make_file
from const import (
    GENERAL_COMMANDS,
    OWNER_COMMANDS,
    BOT_COLOR,
    BOT_VERSION,
    XNONXTE_USER_ID,
)


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help", description="Shows the available commands you can use."
    )
    async def help(self, ctx: commands.Context):
        xnonxte_mention = (await self.bot.fetch_user(XNONXTE_USER_ID)).mention
        general_commands_entry = [
            f"`{key}` - {GENERAL_COMMANDS[key]}" for key in GENERAL_COMMANDS
        ]
        owner_commands_entry = [
            f"`{key}` - {OWNER_COMMANDS[key]}" for key in OWNER_COMMANDS
        ]

        embed = make_embed(
            "PortalGuessr Help",
            f"PortalGuessr is a quiz for guessing the map in Portal, made by {xnonxte_mention} - Constructive feedbacks are appreciated!",
            BOT_COLOR,
        )
        embed.add_field(
            name="General Commands",
            value="\n".join(general_commands_entry),
            inline=False,
        )
        embed.add_field(
            name="Owner Only Commands",
            value="\n".join(owner_commands_entry),
            inline=False,
        )
        embed.set_footer(
            text=f"PortalGuessr 2 {BOT_VERSION}", icon_url="attachment://icon.png"
        )

        await ctx.send(embed=embed, file=make_file("./src/assets/icon.png", "icon.png"))


async def setup(bot):
    await bot.add_cog(Help(bot))