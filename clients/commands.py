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
    Crear y registr un nuevo cliente:
    name    : Nombre del cliente.
    company : Nombre de la compañia.  
    email   : Email de cliente.
    position: Posición en la compañía del cliente.
    
    """
    client_service = ClientService(ctx.obj['clients_table'])
    client = Client(name, company, email, position)

    # Instanciamos el metodo del modulo service.py:
    client_service.create_client(client)

'''
from tabulate import tabulate

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in clients_list:
        table.append(
            [client['name'],
             client['company'],
             client['email'],
             client['position'],
             client['uid']])

    print(tabulate(table, headers))
'''
# COMANDO: LIST
@clients.command()
@click.pass_context
def list(ctx):
    """List all clients
    Mejorar despues la interfaz."""
    # Guardamos en una variable el objeto ctx 'archivo.csv'
    client_service = ClientService(ctx.obj['clients_table'])

    # Instanciamos el método de la clase del modulo services.
    # Que nos regresa una lista del objeto: PENSAR EN CAMBIAR EL NOMBRE A > CLIENTS_LIST
    clients = client_service.list_clients()

    # click.echo('ID  |  Name  |  Company  |  Email  |  Position')
    # click.echo('-' * 100)
    #for client in clients:
    #    click.echo(f"{client['uid']} | {client['name']} | {client['email']} | {client['position']}")

   
    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in clients:
        table.append(
            [client['name'],
             client['company'],
             client['email'],
             client['position'],
             client['uid']])

    print(tabulate(table, headers))

    

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""

    # Guardamos en una variable el objeto ctx 'archivo.csv'
    client_service = ClientService(ctx.obj['clients_table'])

    # Instanciamos el método de la clase del modulo services.
    # Que nos regresa una lista del objeto:
    clients = client_service.list_clients()

    # Busca los datos de cliente List comperhersion:
    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')

def _update_client_flow(client):
    #click.echo('Leave empty if you don\'t want to modify a value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client

# COMANDO: DELETE
@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    # Instanciamos el método de la clase del modulo services.
    # Que nos regresa una lista del objeto:
    clients = client_service.list_clients()

    # Genero una lista que actualizada sin el id del cliente a eliminar:
    clients_wd = [client for client in client_service.list_clients() if client['uid'] != client_uid]
    print(clients_wd)
    client_service._save_to_disk(clients_wd)


    #if click.confirm(f"Are you sure you want to delete the client with uid: {client_uid}"):
    #   client_service.update_client(client_uid)

all = clients