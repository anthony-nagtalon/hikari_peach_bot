import os
import hikari
import lightbulb

bot = lightbulb.BotApp(
  token=os.environ["TOKEN"],
  prefix="!",
  intents=hikari.Intents.ALL,
  default_enabled_guilds=int(os.environ["TEST_GUILD_ID"]),
  help_slash_command=True
)

@bot.command()
@lightbulb.add_cooldown(15.0, 1, lightbulb.UserBucket)
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
  await ctx.respond(ctx.options.text)

def run() -> None:
  if os.name != "nt":
    import uvloop
    uvloop.install()
  
  bot.run()