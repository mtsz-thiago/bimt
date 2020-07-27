import unittest
from bimt.query.processor import ProcessQuery


class TestQuery(unittest.TestCase):

    def test_default_cfg_paths(self):
        from bimt.query.cfg import config
        self.assertEqual(config["DEFAULT"]["LEIA"], 'data/cfquery.xml')
        self.assertEqual(config["DEFAULT"]["CONSULTAS"], 'output/consultas.csv')
        self.assertEqual(config["DEFAULT"]["ESPERADOS"], 'output/esperados.csv')

    def test_write_consulta_file(self):
        query_processor = ProcessQuery.get()
        query_processor.write_consultas_file()
        
if __name__ == '__main__':
    unittest.main()