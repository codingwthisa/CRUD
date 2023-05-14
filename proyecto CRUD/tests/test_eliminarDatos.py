import sys
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
import unittest
from modelo.claseCliente import Cliente
from CRUD.eliminarDatos import eliminar_cliente

class TestEliminarCliente(unittest.TestCase):

    def test_eliminar_cliente_existente(self):
        # Crear clientes de prueba
        cliente1 = Cliente(nombre="Juan Perez", cedula="1234567", fecha_pedido="14052023")
        cliente2 = Cliente(nombre="Maria Garcia", cedula="7654321", fecha_pedido="14052023")
        clientes = [cliente1, cliente2]

        eliminar_cliente(clientes, "1234567")

        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0].cedula, "7654321")

if __name__ == "__main__":
    unittest.main()