# Documentacion
este es una aplicacion web utilizando el franework flask y bootstrap. su proposito es ejemplificar un crud utilizando el recurso mensaje. los datos se guardan en la base de datos postgres utilizando migraciones.

las dependencias se gestionan con pipenv

## Dependencias

para correr este proyecto usted necesita tener instalado python 3 y su herramienta pip.
para revisar si las tiene instalado debe ejecutar los siguientes comando:

´´´

python -v
pip -v
´´´


el resultado debe indicar un numero superior a 3 o algo asi.
para instalar las dependencias debe ejecutar el comando 'pipenv install'

## Migraciones 
para ejecutar las migraciones el comando es el siguiente:

para ejecutar hacia adelante
´´´


flask db upgrade
´´´
para ejecutar hacia atras
´´´
flask db dowgradre
´´´

en caso de modificar un modelo agragando a notificacion un atributo, debemos generar una nueva migracion con el comando

´´´

flask db migrate .m"mensaje de la migracion"

**nota**:los comandos anteriores se deben ejecutar dentro de 'pipenv shell'

´´´


flask --app app --debug run
´´´
## Blueprint

Los blueprint permiten componer aplicaciones desde componentes pequeños. Cada componente es com una mini aplicacion. Permiten crear aplicaciones grandes manteniendolas simples.

## Modulos
para que los blueprint esten bien organizados, es mejor trabajarlos como mudulos, es decir, que esten dentro de una carpeta. Los modulos se pueden anidar, de hecho nosotros hicimos el modulo ´app´ con su respectivo ´__init__.py´ y dentro tenemos otros modulos como el modulo ´messages´ que es ademas un blueprint.



