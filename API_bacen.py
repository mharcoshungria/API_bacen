#!/usr/bin/env python
# coding: utf-8

# ## Importando Bibliotecas:

# In[1]:


import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)


# ## Função para obter dados através da API do Banco Central:

# In[2]:


def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df


# #### ICPA:

# In[3]:


ipca = consulta_bc(433) 


# In[4]:


ipca.head(10) # Exibindo os 10 primeiros registros


# In[5]:


ipca.tail(10) # Exibindo os 10 últimos registros


# In[6]:


ipca.shape # Exibindo o tamanho do DataFrame (Linhas x Colunas)


# In[7]:


ipca.plot()


# #### IGPM:

# In[8]:


igpm = consulta_bc(189)
igpm.plot()


# #### SELIC Meta:

# In[9]:


selic_meta = consulta_bc(432)
selic_meta.plot()


# #### Reserva internacional:

# In[10]:


reservas_internacionais = consulta_bc(13621)
reservas_internacionais.plot()

