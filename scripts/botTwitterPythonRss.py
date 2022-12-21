#!/usr/bin/env python
# -*- coding: utf-8 -*-


# script que lee el feed rss de un blog y publica un articulo
# de forma aleatoria en twitter y mastodon

# Tienes que tener instaladas las librerias feedparser,
# Twython, Mastodon

# Autor: Carlos M.
# https://elblogdelazaro.org

# Llama a los modulos Python
import feedparser
import random
from twython import Twython


# Llamando a las llaves del Diccionario
CUSTOMER_KEY = 'i95qIEYpi9WwQkRRhNr6dQyIj'
CUSTOMER_SECRET = 'QvyV34L5JVNlntNnuIfyiJj4PYJpwX3iRXpVYX9CQco8Vovf76'
ACCESS_TOKEN = '1006427191-LSufe6sgu9kWb6e99A9fBanDFPa2f8a5FpQyJXq'
ACCESS_TOKEN_SECRET = 'c5YDhblhlqrd3QgoVUtCPXsSYNZUyXX2tVLwXDBgGFgXh'
# Seleccionamos el Feed
feed = 'https://vctrsnts.github.io/feed.xml'

# Parseamos el Feed
d = feedparser.parse(feed)

# Extrae la longitud del Feed y aleatoreamente selecciona un articulo
feedlen = len(d['entries'])
num = random.randint(0, feedlen)

# Inicializa la API de Twitter, escribe el nuevo estado y salimos
api = Twython(CUSTOMER_KEY, CUSTOMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
status_text = d['entries'][num]['title'] + '\n' + d['entries'][num]['link']
articulo = ("Recordando artículos publicados:" + '\n' + status_text)

api.update_status(status=articulo)
