# LOGICA DE NEGOCIO
# Cada función representa un comando en la terminal:

import csv 
import os

from clients.models import Client #Importamos el modelo de la fnción

class ClientService:
    # Recibe el nombre del archivo donde se guardará
    # Metodo constructor:
    def __init__(self, table_name): 
        self.table_name = table_name

    def create_client(self, client):
        '''Crea un cliente y bla bla bla'''
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_client):
        # Usamos a la función de arriba, la cual nos regresa una lista del archivo.
        clients = self.list_clients()

        # Creamos una lista vacia:
        updated_clients = []

        # Creamos un ciclo para iterar en el contenido del archivo csv.    
        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)    

    # Para guardar la lista actualizada en el disco utilizamos 
    # el método privado _save_to_disk()
    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)     

    