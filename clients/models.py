# ------------- OBJETO MODELO CLASE PRINCIPAL ------------- #

# Importamos el módulo uuid implementa identificadores universalmente únicos:
import uuid

# Nuestro modelo se basara en un objeto de clase Client:
class Client:
  '''
  Clase principal de las entidades a registrar.
  '''

  def __init__(self, name, company, email, position, uid=None):
    '''
    Método constructor solcita los siguientes parametros para poder generar una instancia de la clase:
    name    : Nombre del cliente.
    company : Nombre de la compañia.  
    email   : Email de cliente.
    position: Posición en la compañía del cliente.
    uid     : Si no se entraga este parametro se generá por default, un id unico.
    '''
    self.name = name
    self.company = company
    self.email = email
    self.position = position
    # Si lo tenemos bien si no usamos el modulo uid de python:
    self.uid = uid or uuid.uuid4()

  # Permite acceder a una representación del diccionario como objeto:
  def to_dict(self):
    return vars(self)

  # Permite declarar metodos estaticos dentro de una clase:
  #   Método Estacico : Es un método que se puede ejecutar sin instanciar la clase, no requiere self como parametro.
  @staticmethod
  def schema():
    '''
    Esquema de la base de datos, que retorna la lista de variables dentro del objeto.
    '''
    return ['name', 'company', 'email', 'position', 'uid']
