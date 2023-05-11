#coded with ❤ by Hermione
import json
import os
import random
import traceback
import sys
import discord
from colorama import Fore
import time
import fade
import requests
from discord import Embed, Permissions
from discord.ext import commands
from pystyle import Center, Colorate, Colors, Cursor, System
os.system('cls')
banner = """

            ─────────────────────────────────────────────────────────────────────────────────────────────────────
                ─██████████████─██████████─████████████████───██████████████─██████████████─██████████████─
                ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
                ─██░░██████░░██─████░░████─██░░████████░░██───██░░██████░░██─██████░░██████─██░░██████████─
                ─██░░██──██░░██───██░░██───██░░██────██░░██───██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██████░░██───██░░██───██░░████████░░██───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░░░░░░░░░██───██░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─
                ─██░░██████████───██░░██───██░░██████░░████───██░░██████░░██─────██░░██─────██░░██████████─
                ─██░░██───────────██░░██───██░░██──██░░██─────██░░██──██░░██─────██░░██─────██░░██─────────
                ─██░░██─────────████░░████─██░░██──██░░██████─██░░██──██░░██─────██░░██─────██░░██████████─
                ─██░░██─────────██░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─────██░░██─────██░░░░░░░░░░██─
                ─██████─────────██████████─██████──██████████─██████──██████─────██████─────██████████████─
            ──────────────────────────────────────────────────────────────────────────────────────────────────────
""" 
faded_banner = fade.pinkred(banner)
for o in faded_banner:
    time.sleep(0.0001)
    sys.stdout.write(o)
    sys.stdout.flush()
time.sleep(1)
print(f'\n{Fore.GREEN}hey{Fore.YELLOW} :)')
time.sleep(2)
TOKEN = "MTA4NjM4NzI2MzE5OTUyMzAyOA.GFS_3k.u9QmeexjTfJHlA86k6GABC81NSYSUPv2W9af4E"
discord_bot = commands.Bot (command_prefix = "!" , intents = discord.Intents.all() ,activity=discord.Activity(type=discord.ActivityType.listening, name="Hermione is here"))
discord_bot.remove_command('help')
print(f'\n{Fore.GREEN} Type {Fore.YELLOW}!rename{Fore.GREEN} to start the process{Fore.RESET} \n')
@discord_bot.command(name='rename')
async def ctx(ctx):
 time.sleep(1)
 await ctx.send(f'Please Enter the NickName in the console')
 name = input(f'{Fore.CYAN}Enter the name that you want to be for all members{Fore.YELLOW} :)\n{Fore.BLACK}')
 time.sleep(1)
 await ctx.reply(f'changing "{ctx.guild.member_count}" members nickname to "{name}"')
 time.sleep(2)
 try:
         for member in list(ctx.guild.members):
             payload = {
                "nick": name
             }
             headers = {
                "Authorization": f"Bot {TOKEN}",
                "Content-Type": "application/json",
             }
             r = requests.patch(
                 f'https://discord.com/api/v9/guilds/{ctx.guild.id}/members/{member.id}', data=json.dumps(payload), headers=headers)
             await ctx.send(f'{member.name} has been renamed')
             print(f"{Fore.GREEN}{member.name} was renamed.")
             time.sleep(2)
 except:
        print(f"{Fore.RED}{member.name} was not renamed")
        await ctx.send(f'{member.name} was not renamed')
 print(f'finished')
discord_bot.run(TOKEN)
