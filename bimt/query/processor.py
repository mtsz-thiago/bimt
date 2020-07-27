from bimt.query.cfg import config

import xml.etree.ElementTree as ET
import pandas as pd

class ProcessQuery:

    def __init__(self, xml_file):
        self.xml_file = xml_file

    def transform(self, raw_query):
        query = raw_query.strip(";")
        query = query.upper()
        return query

    def from_tag_to_consulta_json(self, tag):
        return {
            "QueryNumber": tag.find("QueryNumber").text,
            "QueryText": self.transform(tag.find("QueryText").text)
        }

    def write_consultas_file(self):
        consulta_file_path = config["DEFAULT"]["CONSULTAS"]

        queries_tags = self.xml_file.findall('QUERY')
        consulta_data = [ self.from_tag_to_consulta_json(tag) for tag in queries_tags ]
        consulta_df = pd.DataFrame(consulta_data)

        consulta_df.to_csv(consulta_file_path, sep=";")

    @staticmethod
    def get():
        query_xml_file_path = config["DEFAULT"]["LEIA"]
        queries_xml = ET.parse(query_xml_file_path ).getroot()

        return ProcessQuery(queries_xml)
