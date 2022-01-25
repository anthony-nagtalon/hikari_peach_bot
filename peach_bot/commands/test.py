import lightbulb

@lightbulb.add_cooldown(15.0, 1, lightbulb.UserBucket)
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
  await ctx.respond(ctx.options.text)

@lightbulb.command("hello", "Make the bot say hello.")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def hello(ctx: lightbulb.Context) -> None:
  await ctx.respond("Hello!")

def load(bot: lightbulb.BotApp) -> None:
  bot.command(cmd_say)
  bot.command(hello)

def unload(bot: lightbulb.BotApp) -> None:
  bot.remove_command(bot.get_prefix_command("cmd_say"))
  bot.remove_command(bot.get_prefix_command("hello"))