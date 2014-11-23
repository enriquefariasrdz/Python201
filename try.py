#!/usr/bin/python3

#-*-coding: utf-8 -*-



try:

  fh = open( "ArchivoDePrueba.txt", "w" )

  fh.write( "Eso es mi archivo a probar try/except/else!!\n" )
  fh.write( "prueba append","a")

except IOError:

  print( "Error: No puedo abrir el archivo: ArchivoDePrueba.txt" )

else:

  print( "Se escribió con exito el archivo ArchivoDePrueba.txt" )

  fh.close()
