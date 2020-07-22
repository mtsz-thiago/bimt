import unittest

class TestQuery(unittest.TestCase):

    def test_default_cfg(self):
        from bimt.query.cfg import config
        self.assertEqual(config["DEFAULT"]["LEIA"], 'data/cfquery.xml')
        self.assertEqual(config["DEFAULT"]["CONSULTAS"], 'output/consultas')
        self.assertEqual(config["DEFAULT"]["ESPERADOS"], 'output/esperados')

if __name__ == '__main__':
    unittest.main()