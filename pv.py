# ------------- Punto de Entrada de la aplicación ------------- # 

# Librerías y modulos:
# Módulo desarrollado por los autores de Flask para crear rápidamente líneas de comando.
import click
# Importa todos los comandos generados en la clase 'clients' con el alias 'clients_commands'.
from clients import commands as clients_commands

# Variable constante y global es el nombre del archivo .csv
# donde guardaremos los datos de los clientes:
CLIENTS_TABLE = 'clients.csv'

@click.group() # Decorador que confirma que la función 'cli' es el punto de entrada.
@click.pass_context # Decorador que nos da un objeto contexto 'ctx'.
def cli(ctx):
  '''Una aplicación para Crear, Leer, Actualizar & Borrar un archivo .csv de clientes'''
  ctx.obj = {} # Objeto 'ctx' vacio.
  # Asignación de valores al diccionario ctx.obj, se aginá:
  #   Llave = 'clients_table' Es el nombre de la tabla
  #   Valor = Constante con el nombre del archivo .csv
  ctx.obj['clients_table'] = CLIENTS_TABLE 
  
# Agrega los comandos de la clase 'clients' usando la variable all.
cli.add_command(clients_commands.all) 
