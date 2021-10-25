#!/usr/bin/env python3
#This product cannot be changed code or skid
#Get Help: https://github.com/Sn8ow/Raspberry-SSH
#I like: https://github.com/Sn8ow/Its-Vichy
from colorama import Fore, Style, init
from discord.ext import commands
import paramiko, discord, os
init()

class ssh_controller():
    def __init__(self, host, username, password):
        self.client   = paramiko.SSHClient()
        self.password = password
        self.username = username
        self.host     = host
        self.ssh      = None

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname= self.host, username= self.username, password= self.password)

    def send_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return str(stdout.read()).split('b\'')[1].split("\\n'")[0].replace('\\n', '\n')

class discord_client():
    def __init__(self, prefix, token, host, username, password):
        self.client   = commands.Bot(command_prefix= prefix)
        self.password = password
        self.username = username
        self.token    = token
        self.host     = host

        self.ssh = ssh_controller(self.host, self.username, self.password)

        client = self.client
        client.remove_command("help")

        @client.event
        async def on_ready():
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system(f'title [RaspberryPI SSH] - Release V.1')
            await self.client.change_presence(activity=discord.Game(name=">ssh V.1| github.com/Sn8ow")) #Dont change it!
            print(f"""
    {Fore.GREEN}       .~~.   .~~.
    {Fore.GREEN}      \'. \ \' \' / .\'
    {Fore.RED}       .~ .~~~..~.
    {Fore.RED}      : .~.\'~\'.~. :  {Fore.GREEN}  __      __ __  __  __ __  __     
    {Fore.RED}     ~ (   ) (   ) ~ {Fore.GREEN} |__) /\ (_ |__)|__)|_ |__)|__)\_/_ . 
    {Fore.RED}    ( : \'~\'.~.\'~\' : ){Fore.GREEN} | \ /--\__)|   |__)|__| \ | \  ||_)| SSH V.1
    {Fore.RED}     ~ .~ (   ) ~. ~ {Fore.GREEN}                                 |
    {Fore.RED}      (  : \'~\' :  )       {Fore.WHITE}Made by github.com/{Fore.RED}Sn8ow
    {Fore.RED}       \'~ .~~~. ~\'        {Fore.WHITE}Help:{Fore.RED}https://github.com/Sn8ow/Raspberry-SSH       
    {Fore.RED}           \'~\'            


{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] RaspberrySSH was connected on {Fore.RED}{self.client.user.name}#{self.client.user.discriminator}""")
            self.ssh.connect()
            print(f'{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] RaspberrySSH was linked to raspberry ({Fore.RED}{self.username}{Fore.WHITE}@{Fore.GREEN}{self.host}{Fore.WHITE}:{Fore.RED}{self.password}{Fore.WHITE})')
            
        @client.command()
        async def ssh(ctx, *, command):
            await ctx.send(f'```{self.ssh.send_command(command)}```')
        
        client.run(self.token)

discord_client('your-prefix', 'your-token-bot', 'ip-addres-rpi', 'username-here', 'password-here') #Change only your informations

#This product cannot be changed code or skid
#your-prefix - ! ssh/ or more
#your-token-bot get token your bot (scrool up for help)
#ip-addres-rpi enter your IP Raspberry SSH
#enter username on your Rpi - (Default) Username: pi 
#enter your password SSH - (Default) Pass: raspberry
#You can compile .py to .exe using Pyinstaller or another program.
#Using Pyinstaller - (Install) pip install pyinstaller (Using) cd {Your path .py} (Compiling) pyinstaller -F {FileName.py} - {Add icon} pyinstaller -F {FileName.py} -i {IconPath.ico}