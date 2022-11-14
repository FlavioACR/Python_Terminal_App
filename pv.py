# ------------- Punto de Entrada de la aplicación ------------- # 

# Librerías y modulos:
# 1. Importamos click, modulo desarrollado por los autores de Flask para crear rápidamente líneas de comando.
import click
# Importa todos los comandos generados en la clase 'clients' con el alias 'clients_commands'.
from clients import commands as clients_commands

# 7. Variable constante y global es el nombre del archivo .csv donde guardaremos los datos de los clientes:
CLIENTS_TABLE = 'clients.csv'

@click.group() # 3. Decorador que indica que la función 'cli' es el punto de entrada.
@click.pass_context # 4. Decorador que nos da un objeto contexto 'ctx' y los pasa como parametro a la función 'cli'.
# 2. Definimos la función "cli", que será nuestro punto de entrada.
def cli(ctx):
  '''
  Una aplicación para Crear, Leer, Actualizar & Borrar un archivo .csv de clientes.
  Parametros : 
    ctx      : Objeto contexto, que guardara nuestro objeto de trabajo en este caso un archivo .csv.
  '''
  # 5. Inicializamos el objeto contexto como un diccionario vacio:
  ctx.obj = {}
  # 6. Asignación de valores al diccionario ctx.obj, se aginá: 
  #   Llave = 'clients_table' Es el nombre de la tabla
  #   Valor = Constante con el nombre del archivo .csv
  ctx.obj['clients_table'] = CLIENTS_TABLE 
  
# 8. Utilizamos el metodo add_command() para agregar los comandos de la clase 'clients' importada del modulo commands
#    a la función 'cli' usando la variable all:
cli.add_command(clients_commands.all) 
