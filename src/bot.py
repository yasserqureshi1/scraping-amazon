import discord
from amazon import search
from config import TOKEN, CHANNEL_ID


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if message.content.split(' ')[0] == '!amazon':
        try:
            query = message.content.replace('!amazon ', '')

            item = search(query)

            embed = discord.Embed(
                title=item['title'],
                url='https://www.amazon.co.uk/' + item['url']
            )
            embed.set_thumbnail(
                url=item['img']
            )
            embed.add_field(
                name='Price',
                value=item['price']
            )
            embed.add_field(
                name='Rating',
                value=item['rating']
            )
            embed.add_field(
                name='Number of Ratings',
                value=item['number_of_ratings']
            )
            await message.channel.send(embed=embed)
        except:
            response = 'An error occurred with your request.'
            await message.channel.send(response)

client.run(TOKEN)

    