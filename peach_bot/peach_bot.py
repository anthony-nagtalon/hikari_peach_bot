import os
import logging
import hikari
import lightbulb

bot = lightbulb.BotApp(
  token=os.environ["TOKEN"],
  prefix="!",
  intents=hikari.Intents.ALL,
  default_enabled_guilds=int(os.environ["TEST_GUILD_ID"]),
  help_slash_command=True,
  logs="INFO"
)

@bot.command()
@lightbulb.add_cooldown(15.0, 1, lightbulb.UserBucket)
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
  await ctx.respond(ctx.options.text)

@bot.command()
@lightbulb.command("hello", "Make the bot say hello.")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def hello(ctx: lightbulb.Context) -> None:
  await ctx.respond("Hello!")

@hello.child()
@lightbulb.command("ext", "Make the bot say an extended hello.")
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def bar(ctx: lightbulb.Context) -> None:
  await ctx.respond("```Hello, my name is PeachBot!```")

@bot.command()
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

def run() -> None:
  if os.name != "nt":
    import uvloop
    uvloop.install()
  
  bot.run()