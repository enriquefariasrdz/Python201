    #!/usr/bin/python3

    #-*-coding: utf-8 -*-

     

    print( '{0}, {1}, {2}' .format( 'a', 'b', 'c' ) )

     

    print( '{}, {}, {}' .format( 'a', 'b', 'c' ) ) # 3.1+ only

     

    print( '{2}, {1}, {0}' .format( 'a', 'b', 'c' ) )

     

    print( '{2}, {1}, {0}' .format( *'abc' ) ) # Cambiar un string en sus elementos 

     

    print( '{0}{1}{0}' .format( 'abra', 'cad' ) ) # Puedes repetir argumentos
