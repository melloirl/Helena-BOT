from discord.ext import commands, tasks

from datetime import datetime, time, timedelta 

import string

dict1 =  "aáâàeéêèiíîìoóôòuúûùAÁÂÀEÉÊÈIÍÎÌOÓÔÒUÚÛÙbcdfghjklmnpqrstvxwyzBCDFGHJKLMNPQRSTVXWYZ"
dict2 =  "uuuuooooiiiieeeeaaaaUUUUOOOOIIIIEEEEAAAAzywxvtsrqpnmlkjhgfdcbZYWXVTSRQPNMLKJHGFDCB"
table1 = str.maketrans(dict1,dict2)
table2 = str.maketrans(dict2,dict1)

def temduasletras(palavra):
    if (len(palavra) == 2):
        return True
    else:
        return False

def maiorpalavraadjacente(frase,x):
    if (len(frase[x+1]) > len(frase[x-1])):
        return x-1
    elif (len(frase[x-1]) > len(frase[x+1])):
        return x+1
    else:
        return x+1        


def portugues_para_anodicandriano(frase):
    retorno = ''
    frase = frase.translate(table1)
    frase = frase.split()
    for x in range(1,len(frase)):
        if ((temduasletras(frase[x]))):
            frase[maiorpalavraadjacente(frase,x)] += frase[x]
            frase[x] = ""
    for word in frase:
        retorno+=word
        retorno+=' '
    return retorno


TOKEN = 'INSIRA O TOKEN AQUI'

client = commands.Bot(command_prefix='h!')

print(type(client))

#Verifica se o bot conseguiu se conectar. Caso algo dê errado provavelmente o token tá errado.
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.command()
async def traduzir(ctx,*,args):
    await ctx.send(portugues_para_anodicandriano(args))

client.run(TOKEN)