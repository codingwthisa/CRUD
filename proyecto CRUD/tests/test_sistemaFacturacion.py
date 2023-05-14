import sys
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
import unittest
from modelo.claseAntibiotico import Antibiotico
from modelo.claseCliente import Cliente
from modelo.clasePlagas import ControlPlagas
from modelo.claseFertilizantes import ControlFertilizantes


class TestCrearSistemaFacturacion(unittest.TestCase):

    def test_creacion_sistema_facturacion(self):
        cliente1 = Cliente(nombre="Juan Perez", cedula="1234567", fecha_pedido="14052023")
        cliente2 = Cliente(nombre="Maria Garcia", cedula="7654321", fecha_pedido="14052023")
        control_plagas = ControlPlagas(nombre="Control de Plagas", frecuencia_aplicacion = "Cada 7 dias", periodo_carencia= "20 dias", valor=50.0)
        control_fertilizantes = ControlFertilizantes(nombre="Control de Fertilizantes",frecuencia_aplicacion="Cada 2 dias", fecha_ultima_aplicacion="Hace 15 dias", valor=30.0)
        antibiotico = Antibiotico(nombre="Antibiotico 1", dosis=1, tipo_animal="Bovino", precio=300, dosis_recomendada=2)

        clientes = [cliente1, cliente2]
        productos_control = [control_plagas, control_fertilizantes]
        antibioticos = [antibiotico]

        self.assertEqual(len(productos_control), 2)
        self.assertIsInstance(productos_control[0], ControlPlagas)
        self.assertIsInstance(productos_control[1], ControlFertilizantes)
        self.assertEqual(len(antibioticos), 1)
        self.assertIsInstance(antibioticos[0], Antibiotico)

        self.assertEqual(len(clientes), 2)
        self.assertIsInstance(clientes[0], Cliente)
        self.assertIsInstance(clientes[1], Cliente)

if __name__ == '__main__':
    unittest.main()


    
