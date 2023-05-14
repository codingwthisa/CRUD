import sys
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
import unittest
from modelo.claseCliente import Cliente
from ui.menu_actualizar import mostrar_menu_actualizar
from CRUD.actualizarDatos import actualizar_factura
from unittest.mock import patch

class TestActualizarFactura(unittest.TestCase):
    
    def test_actualizar_factura(self):
        cliente = Cliente("Juan", "1111", "20210510")
        clientes = [cliente]
        with patch('builtins.input', side_effect=['1111','3', '14052023']):
            actualizar_factura(clientes)
        self.assertEqual(cliente.fecha_pedido, '14052023')


if __name__ == "__main__":
    unittest.main()
