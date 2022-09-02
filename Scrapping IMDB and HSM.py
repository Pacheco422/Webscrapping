#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup
import requests 
url = "https://www.amazon.com/s?bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&dc&qid=1653482808&rnid=16225007011&ref=lp_16225007011_nr_n_0"
payload={}
headers = {
  'Cookie': 'i18n-prefs=USD; session-id=134-2407235-9987527; session-id-time=2082787201l'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)


# In[11]:


import raw_response.json


# In[12]:


cat raw_response.har


# In[86]:


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


# In[28]:





# In[76]:


import requests 
from bs4 import BeautifulSoup
def extract(curso):
    headers = {'user Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url = f'https://www.hsmuniversity.com.br/{curso}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
def transform(soup):
            divs = soup.html
            divs_tratadas = divs.decode('utf-8')
            print(divs)
            return 
c = extract('pos-graduacao-em-gestao-de-pessoas/p')
transform(c) 


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


# In[153]:


ano = soup.find_all( "span", class_ = 'secondaryInfo', text = True)


# In[155]:


str(ano)


# In[161]:


str.replace.ano("2021", "texts")


# In[122]:


for item in soup.find_all("span", class_ = 'secondaryInfo'):
    print(item.get('txt'))


# In[81]:


soup.find_all("a", class_ = 'secondaryInfo')


# In[42]:


teste = dict['ntitle']
teste


# In[44]:


type(dict)


# In[157]:


import ast
dict = {"<span class="secondaryInfo">(1994)</span>, <span class="secondaryInfo">(1972)</span>, <span class="secondaryInfo">(2008)</span>, <span class="secondaryInfo">(1974)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(1993)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(1994)</span>, <span class="secondaryInfo">(2001)</span>, <span class="secondaryInfo">(1966)</span>, <span class="secondaryInfo">(1994)</span>, <span class="secondaryInfo">(1999)</span>, <span class="secondaryInfo">(2010)</span>, <span class="secondaryInfo">(2002)</span>, <span class="secondaryInfo">(1980)</span>, <span class="secondaryInfo">(1999)</span>, <span class="secondaryInfo">(1990)</span>, <span class="secondaryInfo">(1975)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(1954)</span>, <span class="secondaryInfo">(1946)</span>, <span class="secondaryInfo">(1991)</span>, <span class="secondaryInfo">(2002)</span>, <span class="secondaryInfo">(1998)</span>, <span class="secondaryInfo">(1997)</span>, <span class="secondaryInfo">(1999)</span>, <span class="secondaryInfo">(1977)</span>, <span class="secondaryInfo">(2014)</span>, <span class="secondaryInfo">(1991)</span>, <span class="secondaryInfo">(1985)</span>, <span class="secondaryInfo">(2001)</span>, <span class="secondaryInfo">(1960)</span>, <span class="secondaryInfo">(2002)</span>, <span class="secondaryInfo">(1994)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(1994)</span>, <span class="secondaryInfo">(2000)</span>, <span class="secondaryInfo">(1998)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(2006)</span>, <span class="secondaryInfo">(2006)</span>, <span class="secondaryInfo">(1942)</span>, <span class="secondaryInfo">(2014)</span>, <span class="secondaryInfo">(2011)</span>, <span class="secondaryInfo">(1936)</span>, <span class="secondaryInfo">(1962)</span>, <span class="secondaryInfo">(1968)</span>, <span class="secondaryInfo">(1988)</span>, <span class="secondaryInfo">(1954)</span>, <span class="secondaryInfo">(1979)</span>, <span class="secondaryInfo">(1931)</span>, <span class="secondaryInfo">(1988)</span>, <span class="secondaryInfo">(2000)</span>, <span class="secondaryInfo">(1979)</span>, <span class="secondaryInfo">(1981)</span>, <span class="secondaryInfo">(2012)</span>, <span class="secondaryInfo">(2008)</span>, <span class="secondaryInfo">(2006)</span>, <span class="secondaryInfo">(1950)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(1980)</span>, <span class="secondaryInfo">(1940)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(2018)</span>, <span class="secondaryInfo">(1986)</span>, <span class="secondaryInfo">(1999)</span>, <span class="secondaryInfo">(1964)</span>, <span class="secondaryInfo">(2012)</span>, <span class="secondaryInfo">(2018)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(1984)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(2017)</span>, <span class="secondaryInfo">(1981)</span>, <span class="secondaryInfo">(2022)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(1997)</span>, <span class="secondaryInfo">(1984)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(1997)</span>, <span class="secondaryInfo">(2000)</span>, <span class="secondaryInfo">(2010)</span>, <span class="secondaryInfo">(1952)</span>, <span class="secondaryInfo">(2016)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(1983)</span>, <span class="secondaryInfo">(1968)</span>, <span class="secondaryInfo">(1992)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1963)</span>, <span class="secondaryInfo">(1941)</span>, <span class="secondaryInfo">(2018)</span>, <span class="secondaryInfo">(1962)</span>, <span class="secondaryInfo">(2012)</span>, <span class="secondaryInfo">(1931)</span>, <span class="secondaryInfo">(1959)</span>, <span class="secondaryInfo">(1958)</span>, <span class="secondaryInfo">(2001)</span>, <span class="secondaryInfo">(1971)</span>, <span class="secondaryInfo">(1985)</span>, <span class="secondaryInfo">(1987)</span>, <span class="secondaryInfo">(1944)</span>, <span class="secondaryInfo">(1960)</span>, <span class="secondaryInfo">(1983)</span>, <span class="secondaryInfo">(1952)</span>, <span class="secondaryInfo">(1962)</span>, <span class="secondaryInfo">(1973)</span>, <span class="secondaryInfo">(1976)</span>, <span class="secondaryInfo">(2021)</span>, <span class="secondaryInfo">(1997)</span>, <span class="secondaryInfo">(2020)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(1927)</span>, <span class="secondaryInfo">(2000)</span>, <span class="secondaryInfo">(2011)</span>, <span class="secondaryInfo">(1988)</span>, <span class="secondaryInfo">(2010)</span>, <span class="secondaryInfo">(1989)</span>, <span class="secondaryInfo">(1948)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(2007)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1965)</span>, <span class="secondaryInfo">(2005)</span>, <span class="secondaryInfo">(2016)</span>, <span class="secondaryInfo">(1921)</span>, <span class="secondaryInfo">(1959)</span>, <span class="secondaryInfo">(2020)</span>, <span class="secondaryInfo">(1950)</span>, <span class="secondaryInfo">(2018)</span>, <span class="secondaryInfo">(2013)</span>, <span class="secondaryInfo">(1961)</span>, <span class="secondaryInfo">(1992)</span>, <span class="secondaryInfo">(2006)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(1985)</span>, <span class="secondaryInfo">(2007)</span>, <span class="secondaryInfo">(1999)</span>, <span class="secondaryInfo">(2001)</span>, <span class="secondaryInfo">(1975)</span>, <span class="secondaryInfo">(1998)</span>, <span class="secondaryInfo">(1961)</span>, <span class="secondaryInfo">(1948)</span>, <span class="secondaryInfo">(1950)</span>, <span class="secondaryInfo">(1963)</span>, <span class="secondaryInfo">(2010)</span>, <span class="secondaryInfo">(1993)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(2007)</span>, <span class="secondaryInfo">(1980)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(1980)</span>, <span class="secondaryInfo">(1974)</span>, <span class="secondaryInfo">(1939)</span>, <span class="secondaryInfo">(2005)</span>, <span class="secondaryInfo">(2015)</span>, <span class="secondaryInfo">(1982)</span>, <span class="secondaryInfo">(1998)</span>, <span class="secondaryInfo">(1954)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(2017)</span>, <span class="secondaryInfo">(1996)</span>, <span class="secondaryInfo">(2008)</span>, <span class="secondaryInfo">(2011)</span>, <span class="secondaryInfo">(1996)</span>, <span class="secondaryInfo">(1988)</span>, <span class="secondaryInfo">(2013)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1925)</span>, <span class="secondaryInfo">(1982)</span>, <span class="secondaryInfo">(2002)</span>, <span class="secondaryInfo">(1954)</span>, <span class="secondaryInfo">(1949)</span>, <span class="secondaryInfo">(1997)</span>, <span class="secondaryInfo">(1959)</span>, <span class="secondaryInfo">(1926)</span>, <span class="secondaryInfo">(2013)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(2014)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(1978)</span>, <span class="secondaryInfo">(2011)</span>, <span class="secondaryInfo">(1993)</span>, <span class="secondaryInfo">(2014)</span>, <span class="secondaryInfo">(1939)</span>, <span class="secondaryInfo">(1953)</span>, <span class="secondaryInfo">(1924)</span>, <span class="secondaryInfo">(1975)</span>, <span class="secondaryInfo">(2015)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(2016)</span>, <span class="secondaryInfo">(1957)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(2014)</span>, <span class="secondaryInfo">(1998)</span>, <span class="secondaryInfo">(2010)</span>, <span class="secondaryInfo">(2015)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(2001)</span>, <span class="secondaryInfo">(1975)</span>, <span class="secondaryInfo">(1928)</span>, <span class="secondaryInfo">(1955)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1953)</span>, <span class="secondaryInfo">(1989)</span>, <span class="secondaryInfo">(1986)</span>, <span class="secondaryInfo">(1976)</span>, <span class="secondaryInfo">(2019)</span>, <span class="secondaryInfo">(1986)</span>, <span class="secondaryInfo">(1984)</span>, <span class="secondaryInfo">(2013)</span>, <span class="secondaryInfo">(2015)</span>, <span class="secondaryInfo">(2007)</span>, <span class="secondaryInfo">(1976)</span>, <span class="secondaryInfo">(1939)</span>, <span class="secondaryInfo">(2017)</span>, <span class="secondaryInfo">(1993)</span>, <span class="secondaryInfo">(2007)</span>, <span class="secondaryInfo">(1973)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1946)</span>, <span class="secondaryInfo">(2004)</span>, <span class="secondaryInfo">(1942)</span>, <span class="secondaryInfo">(1966)</span>, <span class="secondaryInfo">(1940)</span>, <span class="secondaryInfo">(1940)</span>, <span class="secondaryInfo">(2009)</span>, <span class="secondaryInfo">(1967)</span>, <span class="secondaryInfo">(2000)</span>, <span class="secondaryInfo">(2003)</span>, <span class="secondaryInfo">(1975)</span>, <span class="secondaryInfo">(1959)</span>, <span class="secondaryInfo">(1966)</span>, <span class="secondaryInfo">(1995)</span>, <span class="secondaryInfo">(2005)</span>, <span class="secondaryInfo">(1979)</span>, <span class="secondaryInfo">(1965)</span>, <span class="secondaryInfo">(1934)</span>, <span class="secondaryInfo">(2016)</span>, <span class="secondaryInfo">(1982)</span>, <span class="secondaryInfo">(1992)</span>, <span class="secondaryInfo">(2011)</span>, <span class="secondaryInfo">(1991)</span>, <span class="secondaryInfo">(1990)</span>, <span class="secondaryInfo">(2021)</span>]"}
str(dict)
ast.literal_eval(str(dict))


# In[ ]:


x = int(input("how many candies do you want ?")) 
i = 1    
while i >= item: 
    print('candy')
    i = i+1


# In[2]:


nome = input('digite seu nome')     
print(f'Olá {nome} bem vinda ao Congo. Infelizmente tivemos alguns problemas de guerra, contamos com sua ajuda para soluciona-los')

print('Você aceita esse desafio ?')
desafio = input('Qual a sua decisão ?')
abertura = False
while desafio == desafio:
    pass
    if desafio == 'sim':
        abertura = True
        break
        print('beleza, vamos continuar.')
    else:
        abertura = False
        print('Todo mundo morreu, Buum')  
cipó = input(f'{nome}, escolha entre o cipó 1, 2 ou 3')
if cipó == '1' or cipó == '3':
    print('parabéns você morreu')
else:
    print(f'balança, caixão, balança você, {nome} está chegando pra ver o Tenente Menê')


# In[ ]:


mantra = []
conteudo = False
mantra.append(mantra(input('digite'))


# In[ ]:


mantra = []
conteudo = False
while conteudo == False:
    mantra.append(input('digite'))
    if mantra.append == 'pare':
        conteudo == True


# In[4]:





# In[ ]:




