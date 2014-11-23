#!/usr/bin/python3

#-*-coding: utf-8 -*-

     

ArchivoALeer = open( 'C:/NuevoArchivo.txt', 'r', encoding='utf-8' )

     

print( ArchivoALeer.read() )

ArchivoALeer.close()
