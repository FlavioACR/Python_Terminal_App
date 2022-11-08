# ------------- Modulo de instalación ------------- # 

# Librerías y modulos:
from setuptools import setup
    
setup(
    name='pv', # Nombre
    version='0.1', # Versión de desarrollo
    description="Aplicación CRUD a un .csv en linea de comandos",  # Descripción del funcionamiento
    author="Flavio Carrola + Platzi",  # Nombre del autor
    author_email='flavioabatcarrolar@gmail.com',  # Email del autor
    py_modules=['pv'], # Modúlos a instalar
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)