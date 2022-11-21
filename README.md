#Documentacion
este es una aplicacion web utilizando el franework flask y bootstrap. su proposito es ejemplificar un crud utilizando el recurso mensaje. los datos se guardan en la base de datos postgres utilizando migraciones.

las dependencias se gestionan con pipenv

##Dependencias
para correr este proyecto usted necesita tener instalado python 3 y su herramienta pip.
para revisar si las tiene instalado debe ejecutar los siguientes comando:

'''
python -v
pip -v
'''

el resultado debe indicar un numero superior a 3 
para instalar las dependencias debe ejecutar 'pipenv install'

##Migraciones 
para ejecutar las migraciones el comando es el siguiente:

'''

flask db upgrade
'''

en caso de modificar un modelo agragando a notificacion un atributo, debemos generar una nueva migracion con el comando

'''
flask db migrate .m"mensaje de la migracion"

**nota**:los comandos anteriores se deben ejecutar dentro de 'pipenv shell'

'''

flask --app app --debug run
'''