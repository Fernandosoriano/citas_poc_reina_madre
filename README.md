Este es un proyecto que sirve para gestionar por medio de un CRUD (rdesarrollado en Django) las citas que se pueden tener en establecimientos que se dedican al ámbito de la salud.

Instrucciones a seguir para levantar y probar el proyecto:

#1 
Clone el repositorio
git clone https://github.com/Fernandosoriano/citas_poc_reina_madre.git



#2
Instale virtualenvwrapper (solo si no está instalado, esto servirá para  las instalaciones de este proyecto
no interfieran con sus demás proyectos, teniendo un espacio aislado para la correcta instalación).

pip install virtualenvwrapper-win  # Para Windows
pip install virtualenvwrapper      # Para Mac/Linux


#3
Crear y activar entorno virtual
mkvirtualenv env   (con esto crea el entorno)
workon env  # En Windows (Para este paso asegúrese de estar en un cmd de windows)


Una vez que esté dentro del entorno virtual  instale las dependencias necesarias:


#4
Instalar dependencias
pip install -r requirements.txt


#5 
Genere migraciones iniciales
python manage.py makemigrations


#6
Aplique las migraciones
python manage.py migrate


#7
Inicie el servidor
python manage.py runserver y acceda a la ruta que le aparece en la terminal, vera algo como esto:

Starting development server at http://127.0.0.1:8000/
