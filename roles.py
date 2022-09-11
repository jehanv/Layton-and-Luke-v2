from naff import Extension, listen, Button, ButtonStyles, PartialEmoji, Modal, ShortText, ParagraphText, InteractionContext, ActionRow, ComponentContext


class Roles(Extension):

    # @listen()
    # async def on_ready(self):
    #     await self.bot.get_channel(1018584057333940295).send("React accordingly to get your pronouns, so we can use proper pronouns when referring to you! Remember to respect everyone's pronouns!", components=[ActionRow(Button(style=ButtonStyles.BLUE, label="He/Him", custom_id="he"), Button(style=ButtonStyles.BLUE, label="She/Her", custom_id="she"), Button(style=ButtonStyles.BLUE, label="They/Them", custom_id="they"), Button(style=ButtonStyles.BLUE, label="Other Pronouns", custom_id="other"))])

    @listen()
    async def on_component(self, event):
        ctx: ComponentContext = event.context
        if ctx.custom_id == "he":
            he = ctx.guild.get_role(1018584292038803507)
            if ctx.author.has_role(he):
                await ctx.author.remove_role(he)
                await ctx.send("Removed He/Him role.", ephemeral=True)
            else:
                await ctx.author.add_role(he)
                await ctx.send("Added He/Him role.", ephemeral=True)
        if ctx.custom_id == "she":
            she = ctx.guild.get_role(1018584321734488074)
            if ctx.author.has_role(she):
                await ctx.author.remove_role(she)
                await ctx.send("Removed She/Her role.", ephemeral=True)
            else:
                await ctx.author.add_role(she)
                await ctx.send("Added She/Her role.", ephemeral=True)
        if ctx.custom_id == "they":
            they = ctx.guild.get_role(1018584350910070784)
            if ctx.author.has_role(they):
                await ctx.author.remove_role(they)
                await ctx.send("Removed They/Them role.", ephemeral=True)
            else:
                await ctx.author.add_role(they)
                await ctx.send("Added They/Them role.", ephemeral=True)
        if ctx.custom_id == "other":
            other = ctx.guild.get_role(1018584378412114133)
            if ctx.author.has_role(other):
                await ctx.author.remove_role(other)
                await ctx.send("Removed Other Pronouns role.", ephemeral=True)
            else:
                await ctx.author.add_role(other)
                await ctx.send("Added Other Pronouns role.", ephemeral=True)

def setup(bot):
    Roles(bot)