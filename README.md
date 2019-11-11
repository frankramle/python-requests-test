### Instrucciones para instalar el proyecto local:

- Disponer de una terminal con SO (Windows 10 / Ubuntu 18.04)
- Tener instalado python 3.6 
- Mediante GIT hacer un git clone del proyecto
- Ir a la raíz del proyecto y ejecutar:
 
        pip install . 
        si no es admin: pip install --user .

### Instrucciones run test con pytest:

- Desde la raíz del proyecto ejecutar: 
        
        pytest -s

### Instrucciones run test con @click:

- Desde la raíz del proyecto ejecutar (ejecutara la suite de test):
    
        beonit test 


*** Aclaración: la api tomado para realizar el flow son del siguiente repo: https://github.com/frankramle/api-rest-node-express