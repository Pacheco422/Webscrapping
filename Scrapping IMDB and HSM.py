#!/usr/bin/env python
# coding: utf-8


import requests 
from bs4 import BeautifulSoup
def extract(curso):
    headers = {'user Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url = f'https://www.hsmuniversity.com.br/{curso}'
    r = requests.get(url, headers) 
    return r.status_code

print(extract('pos-graduacao-em-gestao-de-pessoas/p'))
# essa é a primeira parte do scrapping. Nela a gente vai extrair os dados da página. Ao analisar o comportamento da página, observei que a variável final mudava quando eu clicava nas diferentes letras. Então, fiz uma def  com a variável letras e a coloquei a variável no final.
#precisava também saber se estava funcionando a url, então coloquei no return para retornar a url. 


# In[84]:


from urllib.request import urlopen 
from bs4 import BeautifulSoup

url = 'https://www.hsmuniversity.com.br/pos-graduacao-em-gestao-de-pessoas/p'

response = urlopen(url)
html = response.read()
html


# In[82]:


html = html.decode('utf-8')


# In[3]:


import requests

url = "https://www.hsmuniversity.com.br/api/dataentities/PP/search?_fields=titulo_sobre_o_curso,titulo_publico_alvo,descricao_media_src,publico_media_src,url_imagem,descricao,link,descricao_curso,descricao_publico&_where=id_produto=3002"

payload={}
headers = {
  'Cookie': 'VtexWorkspace=master%3A-'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
    


# In[4]:


hsm = response.text
print(hsm.index)


# In[25]:


import ast
lista_hsm = {"titulo_sobre_o_curso":"Sobre o Curso","titulo_publico_alvo":"Público-Alvo","descricao_media_src":"https://vtex-img.s3.amazonaws.com/hsmU_admin/gestaopessoasdesk.jpg","publico_media_src":"https://vtex-img.s3.amazonaws.com/hsmU_admin/publicoalvodesk.jpg","url_imagem":"null","descricao":"null","link":"null","descricao_curso":"Uma das mudanças fundamentais na gestão de negócios nos últimos anos é a valorização das pessoas nas organizações. Grande parte das vantagens competitivas das companhias hoje deriva da gestão de pessoas. Neste sentido, este curso visa preparar gestores para liderar e desenvolver equipes voltadas para resultados de alta performance, impulsionando negócios, retendo e valorizando talentos.","descricao_publico":"O curso de Pós-graduação em Gestão Estratégica de Pessoas é destinado a profissionais que objetivam desenvolver pessoas em organizações, aprendendo a reter talentos e conquistar melhores resultados de sua equipe."}
str(lista_hsm)
ast.literal_eval(str(lista_hsm))


# In[26]:


type(lista_hsm)


# In[27]:


lista_hsm


# In[29]:


descricao_curso = lista_hsm['descricao_curso']
print(descricao_curso)


# In[30]:


descricao_publico = lista_hsm['descricao_publico']
descricao_publico


# In[36]:


print("descrição do  Curso:",descricao_curso)
print("descrição do  publico:",descricao_publico)


# In[3]:


import requests

url = "https://www.imdb.com/chart/top/"

payload={}
headers = {
  'Cookie': 'VtexWorkspace=master%3A-'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# In[39]:


type(response.text)


# In[85]:


#webscrapping IMDB
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find('tbody', class_="lister-list").find_all('tr')

for movie in movies:
    name_movie = movie.find('td', class_="titleColumn").a.text
    Year_movie = movie.find('span', class_="secondaryInfo").text.strip('()')
    rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
    sheet.append([name_movie,Year_movie,rating])
    excel.save('IMDB Ratings')
    


# In[84]:

#importando para excel.
from bs4 import BeautifulSoup
import openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
#active sheet = sheet to load data 
sheet.title = 'Top Rated Movies'
sheet.append(['Name Movie, Year Movie, Rating'])


# In[3]:


import requests 
from bs4 import BeautifulSoup 

url = "https://www.imdb.com/chart/top/"

payload={}
headers = {
  'Cookie': 'VtexWorkspace=master%3A-'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find('tbody', class_="lister-list").find_all('tr')

for movie in movies:
    name_movie = movie.find('td', class_="titleColumn").a.text
    Year_movie = movie.find('span', class_="secondaryInfo").text.strip('()')
    rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
    print(name_movie, Year_movie, rating)


# In[89]:


print(sheet)
