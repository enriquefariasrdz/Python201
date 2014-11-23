#!/usr/bin/python3

#-*-coding: utf-8 -*-

     

MiArchivo = open( "NuevoArchivo.txt", "w", encoding='utf-8' )

     

MiArchivo.write( "Es mi primer archivo\n")

     

MiArchivo.write("creado en Python\n")

     

MiArchivo.close()
