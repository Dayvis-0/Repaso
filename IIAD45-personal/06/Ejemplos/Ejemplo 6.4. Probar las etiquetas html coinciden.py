# Funcion para probar si las etiquetas HTML coinciden

from ArrayStack import ArrayStack

def empareja_html(raw):
    """Devuelve True si las etiquetas HTML se emparejan"""
    
    S = ArrayStack()
    
    j = raw.find('<')
    
    while j != -1:
        k = raw.find('>', j+1)
        
        if k == -1:
            return False  
        
        etiqueta = raw[j+1:k]
        
        if not etiqueta.startswith('/'):
            S.push(etiqueta)
        else:
            if S.is_empty():
                return False
            if etiqueta[1:] != S.pop():
                return False
            
        j = raw.find('<', k+1)
        
    return S.is_empty()

if empareja_html('<h1>Hola</h1>'):
    print('Las etiquetas coinciden')
    
else:
    print('Las etiquetas no coinciden')