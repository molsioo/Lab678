import sys
import os
import json
import xmltodict
import yaml

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def convert_to_dict(content, input_format):
    if input_format == 'json':
        return json.loads(content)
    elif input_format in ['yml', 'yaml']:
        return yaml.safe_load(content)
    elif input_format == 'xml':
        return xmltodict.parse(content)
    else:
        raise ValueError(f"Unsupported output format: {input_format}")

def convert_from_dict(data_dict, output_format):
    if output_format == 'json':
        return json.dumps(data_dict, indent=4)
    elif output_format in ['yml', 'yaml']:
        return yaml.dump(data_dict, default_flow_style=False)
    elif output_format == 'xml':
        return xmltodict.unparse(data_dict, pretty=True)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

def main(input_file, output_file):

    input_format = os.path.splitext(input_file)[1][1:]

    output_format = os.path.splitext(output_file)[1][1:]

    content = read_file(input_file)

    data_dict = convert_to_dict(content, input_format)
    converted_content = convert_from_dict(data_dict, output_format)

    write_file(output_file, converted_content)

if __name__ == "__main__":


    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)