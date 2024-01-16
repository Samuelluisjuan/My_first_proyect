#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Samuel!
# 
# Mi nombre es Carlos Enrique, soy code reviewer en Tripleten y tengo el gusto de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# ## Inicialización

# In[2]:


# Cargar todas las librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
from scipy import stats as st
from IPython.display import display


# ## Cargar datos

# In[3]:


# Carga los archivos de datos en diferentes DataFrames
df_calls = pd.read_csv('/datasets/megaline_calls.csv')
df_internet = pd.read_csv('/datasets/megaline_internet.csv')
df_messanges = pd.read_csv('/datasets/megaline_messages.csv')
df_plans = pd.read_csv('/datasets/megaline_plans.csv')
df_users = pd.read_csv('/datasets/megaline_users.csv')

display('Llamadas')
display(df_calls)
display('Internet')
display(df_internet)
display('Mensajes')
display(df_messanges)
display('Tarifas')
display(df_plans)
display('Usuarios')
display(df_users)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Buen trabajo con la importación de las librerias
# </div>
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# CORREGIDO Aca hay un error con la carga de datos debes utilizar la referencia relativa para que se direccione a los archivos del servidor
# </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Corregido tambien, es que hice el proyecto en visual studio code y yo uso windows hay tenia los archivos csv en tipo windows pero ya quedo :)

# ## Preparar los datos

# ## Tarifas

# In[4]:


# Imprime la información general/resumida sobre el DataFrame de las tarifas
display(df_plans.info())


# In[5]:


# Imprime una muestra de los datos para las tarifas
display(df_plans)


# °En la muestra de datos, vemos que los datos son válidos y consistentes. Todas las tarifas tienen un nombre, una tarifa mensual y una cantidad de datos incluidos. No hay datos faltantes ni valores anómalos.
# Sin embargo, podemos hacer un tipo de cambio en la columna plans_name a category; Esto nos permitiría utilizar funciones de Pandas específicas para trabajar con datos categóricos.

# ## Corregir datos

# In[6]:


df_plans = df_plans.rename(columns={'plan_name': 'category'})
display(df_plans)


# ## Enriquecer los datos

# In[ ]:





# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# HECHO Recuerda que nuestro cliente utiliza la medida en gb, transforma los mb a gb (recorda la correcta conversion).</div>
# 
# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# En esta seccion se sugiere completar este codigo agregando la formula de conversion de mb a gb, si el resultado no es un valor exacto se aconseja redondearlo o aproximarlo .</div>
# 
# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# La sugerencia es hacerlo en esta parte de enriquecimiento de datos para futuras referencias es una seccion apropiada.</div>
# 

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     esta parte tambien hice el cambio mas abajo, en el clculo total de mb y hay mismo hice la combercion a gb. :)

# In[ ]:





# ## Usuarios/as

# In[9]:


# Imprime la información general/resumida sobre el DataFrame de usuarios
display(df_users.info())
display(df_users.describe())


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# CORREGIDO Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen.
# Describi al respecto lo que ves. </div>

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Corregido

# In[11]:


# Imprime una muestra de datos para usuarios
display(df_users.head(50))
display(df_users.isnull().sum())


# °En la tabla de df_users podemos notar que hay dos tipos de problemas potenciales: 
# 
# Tipos de datos: las columnas city y reg_date están actualmente definidas como tipo object. Podríamos cambiar el tipo de datos de estas columnas a category para mejorar el rendimiento y la eficiencia de las operaciones.
# Datos ausentes: la columna churn_date tiene 34 valores ausentes. Podríamos intentar investigar las causas de estos valores ausentes y, si es posible, completarlos con datos válidos.
# 

# ### Corregir los datos

# In[12]:


# Rellenar los valores nulos con la fecha actual
df_users.fillna(0, inplace=True)


# ### Enriquecer los datos

# In[13]:



display(df_users)
display(df_users.info())


# 
# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# 
# En esta seccion te sugiero crear una nueva columna que es lo que regularmente se realiza y puedes aplicar la extraccion del area metropolitana.</div>

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Cree la columna mas abajo. No crei necesario cambiarla pero si para la siguiente revicion me lo pide con gusto la modifico :)

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del revisor:</b>
#    Esta bien Samuel, es un comentario para tomar en cuenta en tus proyectos futuros

# ## Llamadas

# In[14]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas
display(df_calls.info())
display(df_calls.describe())


# In[15]:


# Imprime una muestra de datos para las llamadas
display(df_calls.head())


# °No hay problemas potenciales obvios que podamos identificar en el DataFrame de llamadas. Los tipos de datos son apropiados, no hay datos ausentes y los datos parecen ser válidos. Mas que el cambio de la colunma 'call_date' a tipo de dato datetime para facilitar futuros análisis de series temporales y operaciones relacionadas con fechas.

# ### Corregir los datos

# In[16]:


# Cambiar el tipo de datos de la columna 'call_date' a 'datetime64[ns]'
df_calls['call_date'] = pd.to_datetime(df_calls['call_date'])

# Cambiar el tipo de datos de la columna 'duration' a 'float64'
df_calls['duration'] = pd.to_numeric(df_calls['duration'])
df_calls.fillna(0, inplace=True)


# ### Enriquecer los datos

# In[20]:


display(df_calls)
display(df_calls.info())
display(df_calls[df_calls['duration'] == 0.000000])


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Para confirmar tus conclusiones es importante que uses la funcion describe recuerda que esta funcion te brinda mucha información podrias verificar si existen minimos equivalentes a 0 para determinar si hay duraciones de llamada con 0 minutos o podrias utilizar este comando: display(df_calls[df_calls['duration'] == 0.000000]) te lo dejo como ejemplo en todo caso haciendo estas verificaciones entonces puedes proceder a comentar y afirmar tus conclusiones
# </div>
# 

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Listo tambien la verificasion

# ~no se amerita enriquecer los datos, dentro de mi punto de vista

# ## Mensajes

# In[18]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes
display(df_messanges.info())


# In[19]:


# Imprime una muestra de datos para los mensajes
display(df_messanges.head())


# °En esta parte veo todo en orden, solo lo mismo que el mismo detalle que los anteriores de cambiar el tipo de dato que es la colunma 'message_date' a un tipo de dato datetime  para facilitar futuros análisis de series temporales y operaciones relacionadas con fechas.

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[21]:


# Cambiar el tipo de datos de la columna 'message_time' a 'datetime64[ns]'
df_messanges['message_date'] = pd.to_datetime(df_messanges['message_date'])
df_messanges.fillna(0, inplace=True)


# ### Enriquecer los datos

# In[26]:


display(df_messanges)
display(df_messanges.info())
display(df_messanges.describe())


# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Listo el describe()

# ## Internet

# In[ ]:


# Imprime la información general/resumida sobre el DataFrame de internet
describe(df_internet.info())


# In[28]:


# Imprime una muestra de datos para el tráfico de internet
display(df_internet.head())

display(df_internet.describe())


# °Vamos a cambiar el tipo de formato que es la columna 'session_date' a tipo de dato datetime para facilitar futuros análisis de series temporales y operaciones relacionadas con fechas.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# CORREGIDO Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen. </div>

# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     Listo

# ### Corregir los datos

# In[29]:


# Cambiar el tipo de datos de la columna 'date' a 'datetime64[ns]'
df_internet['session_date'] = pd.to_datetime(df_internet['session_date'])
df_internet.fillna(0, inplace=True)


# ### Enriquecer los datos

# In[30]:


display(df_internet)
display(df_internet.info())


# ## Estudiar las condiciones de las tarifas

# In[31]:


# Imprime las condiciones de la tarifa y asegúrate de que te queden claras
display(df_plans)


# In[32]:


### Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado. df_calls Llamadas de los 12 meses
# Crear una nueva columna 'month' basada en la fecha de la llamada
df_calls['month'] = df_calls['call_date'].dt.month
# Agrupar por 'user_id' y 'month', y contar la cantidad de llamadas
df_count_month_nm_call = df_calls.groupby(['user_id', 'month'])['id'].count().reset_index()
# Renombrar la columna 'id' a 'total_calls'
df_count_month_nm_call = df_count_month_nm_call.rename(columns={'id': 'total_calls'})
# Mostrar las primeras filas del DataFrame resultante
display(df_count_month_nm_call.head(100))


# In[33]:


### Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.  df_calls Minutos de los 12 mese

# Agrupar por 'user_id' y 'month', y sumar la duración de las llamadas en minutos
#hacer redondeo 
df_calls['duration'] = np.ceil(df_calls['duration'])
df_count_calls_for_min = df_calls.groupby(['user_id', 'month'])['duration'].sum().reset_index()
# Renombrar la columna 'duration' a 'total_minutes'
df_count_calls_for_min = df_count_calls_for_min.rename(columns={'duration': 'total_minutes'})
# Mostrar las primeras filas del DataFrame resultante
display(df_count_calls_for_min.head())


# In[34]:


### Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado. df_messanges Mensajes de los 12 meses
# Crear una nueva columna 'month' basada en la fecha del mensaje
df_messanges['month'] = df_messanges['message_date'].dt.month
# Agrupar por 'user_id' y 'month', y contar la cantidad de mensajes
df_mess_count_month = df_messanges.groupby(['user_id', 'month'])['id'].count().reset_index()
# Renombrar la columna 'id' a 'total_messages'
df_mess_count_month = df_mess_count_month.rename(columns={'id': 'total_messages'})
# Mostrar las primeras filas del DataFrame resultante
display(df_mess_count_month.head(100))


# In[35]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado. df_internet Internet de los 12 meses
df_internet['month'] = df_internet['session_date'].dt.month
# Agrupar por 'user_id' y 'month', y sumar el volumen de datos
df_inter_by_month = df_internet.groupby(['user_id', 'month'])['mb_used'].sum().reset_index()
# Renombrar la columna 'mb_used' a 'total_mb_used'
df_inter_by_month = df_inter_by_month.rename(columns={'mb_used': 'total_mb_used'})
df_inter_by_month['total_mb_used'] = np.ceil(df_inter_by_month['total_mb_used'] / 1024)
df_inter_by_month = df_inter_by_month.rename(columns={'total_mb_used': 'total_gb_used'})
# Mostrar las primeras filas del DataFrame resultante
display(df_inter_by_month.head(100))


# <div class="alert alert-block alert-info">
# <b>Comentario</b> <a class="tocSkip"></a>
# 
# <b>Comentario del estudiante:</b>
#     hola que tal, aqui tengo la convercion de mb a gb para poder hacer las manupulaciones requeridas

# In[36]:


# Combina los DataFrames de llamadas, mensajes y tráfico de internet
df_group_data_by_month = pd.merge(df_count_month_nm_call, df_count_calls_for_min, on=['user_id', 'month'], how='outer')
df_group_data_by_month = pd.merge(df_group_data_by_month, df_mess_count_month, on=['user_id', 'month'], how='outer')
df_group_data_by_month = pd.merge(df_group_data_by_month, df_inter_by_month, on=['user_id', 'month'], how='outer')
df_group_data_by_month = pd.merge(df_group_data_by_month, df_users[['user_id', 'plan']], on='user_id', how='left')
# Reemplazar NaN con 0 en el DataFrame df_group_data_by_month
df_group_data_by_month = df_group_data_by_month.fillna(0)

# Mostrar las primeras filas del DataFrame resultante
display(df_group_data_by_month.head())


# In[37]:


# Calcula el ingreso mensual para cada usuario
# Combina los DataFrames df_group_data_by_month y df_plans basándote en las columnas 'plan' y 'category'
df_combined = pd.merge(df_group_data_by_month, df_plans, left_on='plan', right_on='category', how='left')
display(df_combined.head(100))


# In[38]:


df_combined['gb_per_month_included'] = np.ceil(df_combined['mb_per_month_included'] / 1024)

df_combined['minutes_charge'] = np.where(df_combined['total_minutes'] - df_combined['minutes_included'] < 0, 0, df_combined['total_minutes'] - df_combined['minutes_included']) * df_combined['usd_per_minute']
df_combined['message_charge'] = np.where(df_combined['total_messages'] - df_combined['messages_included'] < 0, 0, df_combined['total_messages'] - df_combined['messages_included']) * df_combined['usd_per_message']
df_combined['internet_charge'] = np.where(df_combined['total_gb_used'] - df_combined['gb_per_month_included'] < 0, 0, df_combined['total_gb_used'] - df_combined['gb_per_month_included']) * df_combined['usd_per_gb']

df_combined['income_per_used'] = df_combined['minutes_charge'] + df_combined['message_charge'] + df_combined['internet_charge'] + df_combined['usd_monthly_pay']
df_combined = pd.merge(df_combined, df_users[['user_id', 'city']], on='user_id', how='left')
display(df_combined)


# ## Estudia el comportamiento de usuario

# ### Llamadas

# In[39]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.
sns.histplot(x = "total_minutes", hue = "plan", multiple='stack', data =df_combined)
plt.yscale('linear') 
plt.ylabel('Frecuency')
plt.title('Minutos usados')
plt.xlabel('minutes_used')
plt.show()


# In[40]:


# Calcula la media y la varianza de la duración mensual de llamadas.

varianza_total_minutes = np.var(df_combined['total_minutes'])
media_total_minutes = df_combined['total_minutes'].mean()
mediana_total_minutes = df_combined['total_minutes'].median()
display("media total de minutos:", media_total_minutes)
display("varianza total de minutos:",varianza_total_minutes)
display('mediana total de minutos:', mediana_total_minutes)


# In[41]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_combined['total_minutes'])
plt.title('Distribución de la duración mensual de llamadas')
plt.ylabel('Frecuency')
plt.xlabel('minuted_used')
plt.show()


# Se puede observar que los datos exhiben un sesgo hacia la derecha, ya que la mayor concentración de información se encuentra en ese lado pero con una distribucion normal ya que tiene forma de campana. Además, podemos concluir que este comportamiento es independiente del plan, ya que ambos presentan un comportamiento similar, por lo cual no varía en función al plan

# ### Mensajes

# In[42]:


# Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan

sns.histplot(x = "total_messages", hue = "plan", multiple='stack', data =df_combined)
plt.yscale('linear') 
plt.ylabel('Frecuency')
plt.title('Mensajes usados')
plt.xlabel('messages_used')
plt.show()


# In[43]:


# Calcula la media y la varianza de la duración de mensajes.
varianza_total_messages = np.var(df_combined['total_messages'])
media_total_messages = df_combined['total_messages'].mean()
mediana_total_messages = df_combined['total_messages'].median()
display("media total de mensajes:", media_total_messages)
display("varianza total de mensajes:",varianza_total_messages)
display('mediana total de mensajes:', mediana_total_messages)


# In[44]:


# Traza un diagrama de caja para visualizar la mensual de mensajes
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_combined['total_messages'])
plt.title('Distribución mensual de mensajes')
plt.xlabel('Duración total de mensajes')
plt.ylabel('Frecuency')
plt.show()


# Como podemos apreciar, existe un sesgo en el lado derecho, mientras que en el lado izquierdo es donde encontramos la mayor concentración de datos, especialmente entre 0 y 50. Esto indica que hay un comportamiento que  no varía en función del plan, ya que tienen un comportamiento similar pero muy independientes.

# ### Internet

# In[45]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan
# Compara el número de gb mensuales que necesitan los usuarios de cada plan. Traza un histograma.
sns.histplot(x = "total_gb_used", hue = "plan", multiple='stack', data =df_combined)
plt.yscale('linear') 
plt.ylabel('Frecuency')
plt.title('Internet usados')
plt.xlabel('gb_used')
plt.show()


# In[46]:


# Calcula la media y la varianza de la duración de gb usados.
varianza_total_gb_used = np.var(df_combined['total_gb_used'])
media_total_gb_used = df_combined['total_gb_used'].mean()
mediana_total_gb_used = df_combined['total_gb_used'].median()
display("media total de gb usados:", media_total_gb_used)
display("varianza total de gb usados:",varianza_total_gb_used)
display('mediana total de gb usados:', mediana_total_gb_used)


# In[47]:


# Traza un diagrama de caja para visualizar la distribución de gb usados
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_combined['total_gb_used'])
plt.title('Distribución mensual de gb usados')
plt.xlabel('Duración total de gb usados')
plt.ylabel('Frecuency')
plt.show()


# Aquí podemos observar una diferencia con respecto a los otros datos, ya que este presenta una distribución más normal en forma de campana. Se puede apreciar y concluir que la distribución de cada plan es similar entre sí, pero con un comportamiento independiente

# ## Ingreso

# In[48]:



sns.histplot(x = "income_per_used", hue = "plan", multiple='stack', data =df_combined)
plt.yscale('linear') 
plt.ylabel('Frecuency')
plt.title('Ingresos por los planes')
plt.xlabel('income_per_used')
plt.show()


# In[49]:


# Calcula la media y la varianza de la duración mensual de gb usados.
varianza_income_per_used = np.var(df_combined['income_per_used'])
media_income_per_used = df_combined['income_per_used'].mean()
mediana_income_per_used = df_combined['income_per_used'].median()
display("media total de ingresos por usuario:", media_income_per_used)
display("varianza total de ingresos por usuario:",varianza_income_per_used)
display('mediana total de ingresos por usuario:', mediana_income_per_used)


# In[50]:


# Traza un diagrama de caja para visualizar la distribuciónde gb usados
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_combined['income_per_used'])
plt.title('Distribución mensual de ingresos por usuario')
plt.xlabel('Duración total de ingresos por usuario')
plt.ylabel('Frecuency')
plt.show()


# Como podemos observar en el histograma de ingresos, notamos un comportamiento que varía según el plan. Se destaca una barra muy alta que sobrepasa los 700 en el caso del plan 'ultimate', y ligeramente a la izquierda, una barra que supera los 600 en el plan 'surf'. A diferencia de los histogramas de otros dataframes, como mensajes, internet o llamadas, este dataframe muestra una distribución que depende del plan. En el diagrama de caja, observamos que la mayoría de los valores se encuentran cargados hacia el lado derecho. Sin embargo, en el histograma se aprecian aún valores que disminuyen gradualmente hasta llegar a la mitad del rango de 200 a 300, donde prácticamente desaparecen. Aquí podemos concluir que existen comportamientos muy variables, indicando que los ingresos de los usuarios varían significativamente según el plan.

# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>   
# Esta parte es muy importante debido que es aqui donde tambien esta nuestro valor, ya que muchos podran no entender el codigo pero si el analisis o la descripcion, por tal razón te recomiendo validar y comentar mas al respecto</div>

# ## Prueba las hipótesis estadísticas

# In[51]:


df_only_surf = df_combined[df_combined['plan'] == 'surf'].copy()
df_only_ultimate = df_combined[df_combined['plan'] == 'ultimate'].copy()
#df_only_users_ultimate = 


# In[52]:


# Prueba las hipótesis

alpha = 0.05

results = st.levene(df_only_surf['income_per_used'], df_only_ultimate['income_per_used'])

print('valor p: ', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")


# In[53]:


alpha = 0.05

results = st.ttest_ind(df_only_surf['income_per_used'], df_only_ultimate['income_per_used'])

print('valor p: ', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")


# In[54]:


df_city_ny_nj = df_combined[df_combined['city'].str.contains('NY-NJ', case=False, na=False)].copy()

df_city_others = df_combined[~df_combined['city'].str.contains('NY-NJ', case=False, na=False)].copy()


# In[55]:


# Prueba las hipótesis
alpha = 0.05

results = st.levene(df_city_ny_nj['income_per_used'], df_city_others['income_per_used'])

print('valor p: ', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")


# In[56]:


# Prueba las hipótesis
alpha = 0.05

results = st.ttest_ind(df_city_ny_nj['income_per_used'], df_city_others['income_per_used'])

print('valor p: ', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")


# ## Conclusión general
# 
# [En esta sección final, enumera tus conclusiones importantes. Asegúrate de que estas abarquen todas las decisiones (suposiciones) importantes que adoptaste y que determinaron la forma elegida para procesar y analizar los datos.]

# <div class="alert alert-block alert-info">
# <b>Comentario del Final</b> <a class="tocSkip"></a>
# 
# <b>Comentario del Final estudiante:</b>
# 
# <b>Conclusiones :</b>
# Las conclusiones generales derivadas de nuestras pruebas de hipótesis estadísticas indican que podemos rechazar la hipótesis nula que afirmaba que los ingresos promedio de los usuarios de los planes 'ultimate' y 'surf' son iguales. La prueba de hipótesis arrojó un valor de probabilidad del 2.8%. Para validar este resultado, realizamos una prueba de Levene como corroboración adicional.
# 
# En la segunda hipótesis, que analiza la diferencia en los ingresos promedio entre los usuarios del área NY-NJ y los usuarios de otras regiones, la prueba de Levene sugiere que no podemos rechazar la hipótesis nula, mientras que la prueba t nos lleva a rechazarla.
# 
# Los gráficos presentados en los códigos anteriores, relacionados con el uso de Internet, mensajes y minutos de llamadas, indican que no hay diferencias significativas en el comportamiento entre un plan y otro. Estos patrones de comportamiento son bastante similares, sugiriendo que no varían dependiendo del plan, con la excepción de los ingresos. En esta sección, podemos confirmar que los ingresos varían según el plan
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# 
# Me parece bien tu conclusión, pero es importante que tomes algunas correcciones que se plantearon durante la revisión.
#     
# Vamos bien con el proyecto, espero que puedas completar los pendientes
# </div><div class="alert alert-block alert-success">
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# Excelente el proyecto esta aprobado.
# </div><div class="alert alert-block alert-warning">
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# Te sugiero que siempre valides las medidas estadisticas de dispersion antes de la prueba de hipotesis para una proxima, es importante por los parametros de la funcion.
# </div>

# <div class="alert alert-block alert-info">
# <b>Comentario del Final</b> <a class="tocSkip"></a>
# 
# <b>Comentario del Final estudiante:</b>
#     He realizado las modificaciones que usted me sugirió. Sin embargo, como podra notar, hay algunos códigos que ya había generado más abajo, con los datos un poco más manipulados. Opté por no modificarlos, ya que deshacer parte del código para colocarlo más arriba sería más laborioso. No obstante, si lo prefiere, estaré encantado de realizar los ajustes necesarios en la próxima revisión. Por ahora, he dejado el código como está.
#     

# <div class="alert alert-block alert-info">
# <b>Comentario del Final</b> <a class="tocSkip"></a>
# 
# <b>Comentario del Final REVISOR:</b>
#     He visto las mejoras al codigo en base a los comentarios y me parece que estamos bien con la forma de trabajo

# In[ ]:




