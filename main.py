import discord
import asyncio
import random 
from bot_logic import genpass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Conectado como {self.user} (ID: {self.user.id})')

    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('hello'):
            await message.channel.send("Hi!")
        if message.content.startswith('bye'):
            await message.channel.send("\\\U0001f642")
        if message.content.startswith('me das una contraseña'):
            await message.channel.send("tu contraseña es: " +genpass(10))
        def flipcoin():
            flip = random.randint(0,2)
            if flip == 0:
                return "Head"
            else: 
                return "Tails"
        if message.content.startswith("coin"):
            await message.channel.send(flipcoin())
        if message.content.startswith('guess'):
            await message.channel.send('Adivina un numero entre el 1 y 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                 guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'losiento, tomo mucho tiempor pero la respuesta era {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('La has acertado!!!!!')
            else:
                await message.channel.send(f'Oops. Era {answer}.')
     
client = MyClient(intents=intents)
client.run("MTI0MDExMDQ4MDk2NjgxNTg2NQ.Gm5Mlz.VUm8Jx3WZwN1WbXOucb7B5tPd9IqXc8LQ4P6AA") 


