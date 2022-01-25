import hikari
import lightbulb
from lightbulb import commands

@lightbulb.command("valo", "Request a group for valorant.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def valo(ctx: lightbulb.Context) -> None:
  embed = (
    hikari.Embed(
      title=f"Valorant (Unrated)",
      colour=0x3B9DFF,
    )
    .set_footer(
      text=f"Requested by {ctx.member.display_name}",
      icon=ctx.member.avatar_url or ctx.member.default_avatar_url
    )
  )

  await ctx.respond(embed)

def load(bot: lightbulb.BotApp) -> None:
  bot.command(valo)

def unload(bot: lightbulb.BotApp) -> None:
  bot.remove_command(bot.get_prefix_command("valo"))