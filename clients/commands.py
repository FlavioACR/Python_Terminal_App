# ------------- Agrupamiento de los comandos con el decorador @click.group() ------------- # 

# Librerías y modulos:
# 1. Importamos click, modulo desarrollado por los autores de Flask para crear rápidamente líneas de comando.
import click
# Importamos las clases ClientService del modúlo services.py y Client del modúlo models.py:
from clients.services import ClientService
from clients.models import Client
# Importamos la biblioteca tabulate:
from tabulate import tabulate


# 3. Para que las funciones se ejecuten como comandos se utilizan decoradores, el decorador @click.group()
#    convierte a la función donde se aplique en un decorador más y pasarlo como decorador a las funciones que 
#    se convertiran en parte del grupo 'clients': 
@click.group()
# 2. Definimos una función llamada clientas para crear un grupo de funciones que se ejecutarán dependiendo de los comandos:
def clients():
    '''Grupo de funciones que administra el ciclo de vida de los clientes'''
    pass

# ------------- Comando CREATE ------------- # 


# Utilizamos la función 'clients' ya convertida en decorador con @click.group(), usamos el método .command()
# que es parte de decrador group .commands()
@clients.command()
@click.option('-n','--name', # Asignamos un ShortName= 'n' y un LongName= '--name' a la opción.
                type=str, # Tipo de dato, en ese caso string.
                prompt=True, #En caso que no nos de el patron abreviado se solicitará al usuario.
                help='The client\'s name')# Comentario de apoyo de la propiedad.
@click.option('-c', '--company',type=str,prompt=True,help='The client\'s name')
@click.option('-e', '--email',type=str,prompt=True,help='The client\'s name')
@click.option('-p', '--position',type=str,prompt=True,help='The client\'s name')
@click.pass_context # Pasamos el contexto.
def create(ctx, name, company, email, position):
    """
    Crear y registro un nuevo cliente:
    name    : Nombre del cliente.
    company : Nombre de la compañia.  
    email   : Email de cliente.
    position: Posición en la compañía del cliente.
    
    """
    # Instanciamos las clase ClientService del modulo services.py y pasamos como parametro el objeto contexto
    # el cual hacer referencia a nuestro archivo tipo .csv:
    client_service = ClientService(ctx.obj['clients_table'])
    # Instanciamos las clase Client del modulo models.py y pasamos los argumentos opcionales,
    # creando un nuevo objeto de la clase Client:
    client = Client(name, company, email, position)

    # Instanciamos el metodo del modulo service.py, colo cual crearemos y 
    # guardaremos el cliente en nuestro archivo tipo .csv:
    client_service.create_client(client)


# ------------- Comando LIST ------------- #     
# Importamos el modulo tabulate, que permite imprimir en la salida estándar o escribir
# en un archivo de texto tablas con datos tabulados con varios formatos conocidos.  
from tabulate import tabulate
@clients.command()
@click.pass_context
def list(ctx):
    """Lista de todos los clientes"""
    # Instanciamos las clase ClientService del modulo services.py y pasamos como parametro el objeto contexto
    # el cual hacer referencia a nuestro archivo tipo .csv:
    client_service = ClientService(ctx.obj['clients_table'])
    
    # Despues dentro de una variable aplicamos el método list_clients() de la clase ClientService
    # para obtener la lista de los clientes dentro de nuestro archivos tipo .csv:
    clients_list = client_service.list_clients()
    
    # Para utilizar un formato del modulo tabulates;
    # Creamos las siguientes variables:
    #   headers : Aplica el método .capitalize() a nuestra clase Client() el método .schema(), que nos retorna los headers del schema.
    #   tables  : Guarda la iteración de los atributos de cada elemento de la variable client_list, después de la iteración.
    headers = [field.capitalize() for field in Client.schema()]
    table = []
    
    # Iteración y almacenaje de los datos de cada cliente en la variable tipo lista table:
    for client in clients_list:
        table.append(
            [client['name'],
             client['company'],
             client['email'],
             client['position'],
             client['uid']])
    
    # Por ultimo utilizamos el método tabulate del modulo tabulate para imprimir los datos:
    print(tabulate(table, headers))
    

# ------------- Comando UPDATE ------------- #    
@clients.command()
# Solicitamos posterior al comento UPDATE un cliens_uid para actualizarlo.
@click.argument('client_uid', type=str)

@click.pass_context
def update(ctx, client_uid):
    """Actualización de un unico cliente:
       Proporcione despues del UPDATE el client_uid, para actualizarlo.
       """
    # Guardamos en una variable el objeto ctx 'archivo.csv'
    client_service = ClientService(ctx.obj['clients_table'])

    # Instanciamos el método de la clase del modulo services.
    # Que nos regresa una lista del objeto:
    clients = client_service.list_clients()

    # Busca los datos de cliente usando un List comperhersion:
    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]

    if client:
        # Uso de la función auxiliar _update_client_flow():
        client = _update_client_flow(Client(**client[0]))
        # Uso del método update_client() de la clase ClientService():
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')

def _update_client_flow(client):
    '''
    Función auxiliar para la actualización de clientes, en caso de no queder actualizar un dato,
    unicamente dejar en blanco y continuar.
    '''
    #click.echo('Leave empty if you don\'t want to modify a value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


# ------------- Comando UPDATE ------------- #    
# COMANDO: DELETE
@clients.command()
# Solicitamos posterior al comento UPDATE un cliens_uid para actualizarlo (En este caso Borrarlo).
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Borra a clientes de nuestro archivo de almacenaje tipo .csv"""
    client_service = ClientService(ctx.obj['clients_table'])

    # Instanciamos el método de la clase del modulo services.
    # Que nos regresa una lista del objeto:
    clients = client_service.list_clients()

    # Genero una lista que actualizada sin el id del cliente a eliminar:
    clients_wd = [client for client in client_service.list_clients() if client['uid'] != client_uid]
    print(clients_wd)
    # Utilizamos el método privado _save_to_disk() de la clase ClientService():
    client_service._save_to_disk(clients_wd)
   #if click.confirm(f"Are you sure you want to delete the client with uid: {client_uid}"):
    #   client_service.update_client(client_uid)

all = clients
