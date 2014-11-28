!/usr/bin/python3

#-*-coding: utf-8 -*-

 

print( 'Coordenadas: {latitud}, {longitud}' .format( latitud='37.24N', longitud='-115.81W' ) )

 

coord = { 'latitud': '37.24N', 'longitud': '-115.81W' }

 

print( 'Coordenadas: {latitud}, {longitud}' .format( **coord ) )
