#!/usr/bin/env python
# coding: utf-8

# # Uso del API MakeSens

# Instalar Librerias

# In[1]:


#!pip install APIMakeSens
#!pip install tk


# Cargar librería *MakeSens*

# In[2]:


# Makesens
from MakeSens import MakeSens
# Pandas 
import pandas as pd 
# datetime para manejo de fechas
import datetime
# pytz para manejo de zonas horarias
import pytz

import pylab as plt


# Definir token y cargar listado de estaciones

# In[3]:


#estaciones = pd.read_csv("evasLA-CoNGA.csv").set_index("id")


# Definir rango de fechas para descarga

# In[4]:


fechaFin = datetime.datetime.now(pytz.timezone('America/Bogota')).strftime('%Y-%m-%d %H:%M:%S')
fechaInicio = (datetime.datetime.now(pytz.timezone('America/Bogota'))-datetime.timedelta(hours=240)).strftime('%Y-%m-%d %H:%M:%S')


# In[5]:


data = MakeSens.download_data('E2_00021', fechaInicio, fechaFin, 'h')
  


# In[40]:


data.columns.values


# In[50]:


fig=plt.figure()

data.plot( y=["temperatura2","pm_temperatura"])

plt.xticks(rotation='vertical')

plt.show()


# In[52]:


fechaInicio = (datetime.datetime.now(pytz.timezone('America/Bogota'))-datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')


# In[53]:


MakeSens.weekly_profile('E2_00021', fechaInicio, fechaFin, 'PM2.5')


# In[ ]:





# In[ ]:




