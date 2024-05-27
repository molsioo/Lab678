import sys
import os
import json
import xmltodict
import yaml

def convert_to_dict(content, input_format):
    if input_format == 'json':
        return json.loads(content)

def convert_from_dict(data_dict, output_format):
    if output_format == 'json':
        return json.dumps(data_dict, indent=4)

def main(input_file, output_file):
    pass


if __name__ == "__main__":


    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)