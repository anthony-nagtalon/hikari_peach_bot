import os

import hikari
import lightbulb

from peach_bot import TEST_GUILD_ID, OUTPUT_CHANNEL_ID

with open("./secrets/token") as f:
  _token = f.read().strip()

bot = lightbulb.BotApp(
  token=_token,
  prefix="!",
  intents=hikari.Intents.ALL,
  default_enabled_guilds=TEST_GUILD_ID,
)

bot.load_extensions_from("./testbot/extensions")

@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
  channel = await bot.rest.fetch_channel(OUTPUT_CHANNEL_ID)
  await channel.send("Hello!")

if __name__ == "__main__":
  if os.name != "nt":
    import uvloop
    uvloop.install()
  
  bot.run()