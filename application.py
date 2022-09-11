from naff import Extension, listen, Button, ButtonStyles, PartialEmoji, Modal, ShortText, ParagraphText, InteractionContext


class Application(Extension):

    # @listen()
    # async def on_ready(self):
    #     await self.bot.get_channel(1018356884962553967).send("To apply for the season, press this button and fill out the form.", components=Button(style=ButtonStyles.GREEN, label="Apply", custom_id="apply"))

    @listen()
    async def on_component(self, event):
        ctx = event.context
        if ctx.custom_id == "apply":
            my_modal = Modal(
                title="Laytonvivor: Monte d'Or Application",
                components=[
                    ShortText(label="Name, Age, Pronouns, Timezone", custom_id="info"),
                    ShortText(label="Discord Username and Tag", custom_id="username", placeholder="e.g. Jehan#0018"),
                    ShortText(label="Do you have computer, phone/tablet, or both?", custom_id="devices"),
                    ShortText(label="Who won't you play with, if anyone?", custom_id="wontplay"),
                    ShortText(label="Where did you find out about Laytonvivor?", custom_id="where", placeholder="If from a Discord or subreddit, specify which one.")
                ],
                custom_id="app"
            )
            await ctx.send_modal(modal=my_modal)
    @listen()
    async def on_modal_response(self, event):
        ctx = event.context
        if ctx.custom_id == "app":
            resp = ctx.responses
            await self.bot.get_channel(1018364913103675413).send("New application!\n\n**Info**: {}\n**Username**: {}\n**Devices**: {}\n**Won't Play With**: {}\n**Where They Found**: {}".format(*resp.values()))
            await ctx.send("Your application has been submitted.", ephemeral=True)


def setup(bot):
    Application(bot)
