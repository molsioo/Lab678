import xmltodict
import yaml C:

xml_string="""<?xml version="1.0"?>
<employee>
  <name>John Doe</name>
  <age>35</age>
  <job>
    <title>Software Engineer</title>
    <department>IT</department>
    <years_of_experience>10</years_of_experience>
  </job>
  <address>
    <street>123 Main St.</street>
    <city>San Francisco</city>
    <state>CA</state>
    <zip>94102</zip>
  </address>
</employee>"""
print("The XML string is:")
print(xml_string)
python_dict=xmltodict.parse(xml_string)
yaml_string=yaml.dump(python_dict)
print("The YAML string is:")
print(yaml_string)