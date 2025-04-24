import json
import xml.etree.ElementTree as ET

class Parser:
    def parse(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

class JSONParser(Parser):
    def parse(self, data):
        return json.loads(data)

class XMLParser(Parser):
    def parse(self, data):
        return ET.fromstring(data)

def parser_factory(data_format):
    parsers = {
        "json": JSONParser(),
        "xml": XMLParser()
    }
    parser = parsers.get(data_format)
    if not parser:
        raise ValueError(f"Unknown format: {data_format}")
    return parser

# Example usage
if __name__ == "__main__":
    # JSON Example
    json_data = '{"name": "Alice", "age": 30}'
    json_parser = parser_factory("json")
    parsed_json = json_parser.parse(json_data)
    print("Parsed JSON:", parsed_json)
    # Output: Parsed JSON: {'name': 'Alice', 'age': 30}

    # XML Example
    xml_data = "<person><name>Alice</name><age>30</age></person>"
    xml_parser = parser_factory("xml")
    parsed_xml = xml_parser.parse(xml_data)
    print("Parsed XML:", parsed_xml.tag, [child.tag + "=" + child.text for child in parsed_xml])
    # Output: Parsed XML: person ['name=Alice', 'age=30']
