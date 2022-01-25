import os
import logging
import hikari
import lightbulb

from peach_bot import peach_bot

def create_bot() -> lightbulb.BotApp:
  bot = lightbulb.BotApp(
    token=os.environ["TOKEN"],
    prefix="!",
    intents=hikari.Intents.ALL,
    default_enabled_guilds=int(os.environ["TEST_GUILD_ID"]),
    help_slash_command=True,
    logs="INFO"
  )  

  bot.load_extensions_from("./peach_bot/commands")

  return bot

if __name__ == "__main__":
  if os.name != "nt":
    import uvloop
    uvloop.install()
  
  create_bot().run()