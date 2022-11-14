# ------------- LOGICA DE NEGOCIO ------------- #
# Cada función representa un comando en la terminal:

# Librerías y modulos:
# El módulo csv implementa clases para leer y escribir datos tabulares en formato CSV
import csv 
# El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo.
import os
# Importamos de nuestro modulo models.py nuestra clase Client() que es el objeto sobre el cual se trabajará:
from clients.models import Client


class ClientService:
    '''
    Declara como el funcionará los comandos 
    '''
    def __init__(self, table_name):
        '''
        Método constructor.
        Parametros:
            table_name : Nombre de la Tabla o archivo de almacenaje
         '''
        self.table_name = table_name

    def create_client(self, client):
        '''
        Crea un nuevo cliente dentro de la tabla de trabajo.
        Parametros:
            client : Es una instanción de la clase Client() para crear dentro de la tabla de trabajo, table_name:
        '''
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
            
    def list_clients(self):
        '''
        Retorna una lista de los clientes dentro de la tabla de trabajo table_name.
        '''
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_client):
        '''
        Actualiza determinado cliente.
        Parametros:
            updated_client : ID del usuario a actualizar
        
        Variables:
            clients         : Lista de los clientes usando el método, list_clienst().
            updated_clienst : Lista vacia, el la cual se guardaran los clientes una vez actualizados.
        '''
        clients = self.list_clients()
        updated_clients = []

        # Creamos un ciclo para iterar en el contenido del archivo .csv:    
        for client in clients:
            # Si el client['uid'] es igual a id del cliente que se pretende actualzar:
            if client['uid'] == updated_client.uid:
                # Utiliza el método .to_dict() agregando los nuevos datos del cliente:
                updated_clients.append(updated_client.to_dict())
            else:
            # Si el cliente no es igual al clente que se pretende simplemente agregarlo a la lista updated_clients:
                updated_clients.append(client)
        # Guardar información:
        self._save_to_disk(updated_clients)    

    # Para guardar la lista actualizada en el disco utilizamos 
    # el método privado _save_to_disk()
    def _save_to_disk(self, clients):
        '''
        Método privado, función auxiliar del método update_client, crea una tabla temporal 
        y escribe remplaza el contenido de la tabla de trabajo table_name y modifica el archivo de almacenaje
        clients.csv.
        
        Parametros:
            clients         : Lista de clientes:
        Variables:
            tmp_table_name : Tabla temporal de clientes            
        '''
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)     

    
