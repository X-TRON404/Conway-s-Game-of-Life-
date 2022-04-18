import unittest
from cell import Cell

class TestCell(unittest.TestCase):
    def test_types_is_ON(self):
        '''This test will fail if the value is not a boolean'''
        tcell = Cell()
        self.assertTrue(type(tcell.is_ON()) is bool)

    def test_status_value(self):
        '''This test will fail if the status value is not the exact boolean value passed'''
        tcell = Cell(False)
        self.assertEqual(tcell.status, False)
        tcell = Cell(True)
        self.assertEqual(tcell.status, True)

if __name__ == '__main__':
    unittest.main()