import discord

# create client
client = discord.Client()

# print bot name when logged in
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

# do not let the bot print its own messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# when user responds with "$count from"
    if message.content.startswith('$count from'):
        # get the content of the message
        word = message.content
        # print the content of the message
        print("{0.author} says: " + word)
        # create an array that holds the range specified by user
        res = [int(i) for i in word.split() if i.isdigit()]
        # start position of range
        start = res[0]
        # end position of range
        stop = res[1]
        # increment by one each time the bot sends a message
        step = 1
        stop += step

        # send confirmation message
        await message.channel.send('aight vro')

        # send messages containing the numbers from the specified range(inclusive)
        for x in range(start, stop, step):
            await message.channel.send(x)

# run the client using the token
client.run('insert token here')
