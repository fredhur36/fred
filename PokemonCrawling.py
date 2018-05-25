import requests
from sys import platform
from bs4 import BeautifulSoup

response=requests.get('http://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national')
html=response.text
soup=BeautifulSoup(html,'html.parser')
#soup_list=soup.select('div[class=infocard-tall-list]')
info_card_list=soup.find_all("span",{"class":"infocard-tall"})
a=[] # a is pokemon number
b=[]

for number in info_card_list:
    for num_tag in number.find_all('small'):
        a.append(num_tag.get_text())

for name in info_card_list:
    for name_tag in name.find_all("a",{"class" : "ent-name"}):
        b.append(name_tag.get_text())

pokemon_type=[]
for i in a[1::2]:
    pokemon_type.append(i)
total=len(pokemon_type)

f=open("pokemon.txt",'w',encoding='utf-8',newline="")
if(platform == "linux"):
    new_line="\n"
elif(platform=="win32"):
    new_line="\r\n"
for i in range(0,total):
   # b[i]=b[i].replace(u'\xe9','')
    f.write("(")
    f.write('"')
    f.write(b[i])
    f.write('"')
    f.write(',')
    f.write('"')
   # pokemon_type[i]=pokemon_type[i].replace(u'\xe9','')
    f.write(pokemon_type[i])
    f.write('"')
    f.write("),")
    f.write(new_line)

f.close()

