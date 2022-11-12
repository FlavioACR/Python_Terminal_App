# OBJETO 'MODELO'
# models.py
import uuid

# Modelo:
# 
class Client:

  def __init__(self, name, company, email, position, uid=None):
    self.name = name
    self.company = company
    self.email = email
    self.position = position
    # si lo tenemos bien si no usamos el modulo uid de python
    # uuid4 es estandar de la industria para ids unicos.
    self.uid = uid or uuid.uuid4()

  # permite accesder a una representación del diccionario como objeto:
  def to_dict(self):
    return vars(self)

  # Permite declarar metodos estaticos dentro de un a clase:
  # un mstati es un metodo que se puede ejecutar sin instanciar la clase
  # declararemos el esquemda de la base de datos: no recive el self por que no necesita una istantacia
  @staticmethod
  def schema():
    # Retorna lista de variables dentro del objeto
    return ['name', 'company', 'email', 'position', 'uid']
