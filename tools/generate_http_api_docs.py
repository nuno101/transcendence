import sys
import inspect
import importlib
import shutil
import os

CLASS_BLACKLIST = ["__class__"]

BODY_REQESTS = ["POST", "PATCH"]

def generate_object_table(data):
    if len(data) == 0:
        print("None")
        return

    keys = data.keys()
    print("<table>\n<tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr>")
    for key in keys:
        print(f"<tr><td>{key}</td><td>{data[key]['type']}</td><td>{data[key]['required']}</td><td>{data[key]['description']}</td></tr>")
    print("</table>\n")

def generate_object_2Dtable(table_data):
    keys = table_data.keys()
    # print("<tr><th>Body Parameters</th><th>Query Parameters</th></tr><tr><td>\n")
    print("<table>\n<tr>")
    for key in keys:
        print(f"<th>{key}</th>")
    print("</tr><tr><td>\n")

    first = True
    for key in keys:
        if first:
            first = False
        else:
            print("</td><td>")
        generate_object_table(table_data[key])

    for _ in keys:
        print("</td></tr>")
    print("</table>\n")

def generate_multitable(table_data):
    keys = table_data.keys()
    print("<table>\n<tr>")
    for key in keys:
        print(f"<th>{key}</th>")
    print("</tr><tr><td>\n")

    first = True
    for key in keys:
        if first:
            first = False
        else:
            print("</td><td>\n")
        generate_table(table_data[key])

    print("</td></tr></table>\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_endpoint_docs.py <path_to_constants_endpoint_structure.py>")
        exit(1)

    # Warn in stderr that the script uses hardcodedr
    # relative paths and needs to be executed from the tools directory
    print("\033[93mINFO: This script uses hardcoded relative paths " +
          "and needs to be executed from the tools directory\033[0m", file=sys.stderr)

    # Copy file to current directory
    shutil.copyfile(sys.argv[1], "constants_endpoint_structure.py")

    # Import module
    import constants_endpoint_structure as c

    # Delete file
    os.remove("constants_endpoint_structure.py")
    
    # Generate header and statistics section
    print(f"# Statistics\n")
    url_endpoint_count = len(c.ENDPOINTS.keys())
    print(f"Total number of urls: {url_endpoint_count}\n")

    print(f"# Table of Contents\n")
    for endpoint in c.ENDPOINTS.keys():
        link_name= endpoint.replace('/', '-')[1:]
        print(f"- [{endpoint}](#{link_name})")
    print()
    # print(f"Total number of methods: {output['method_endpoint_count']}")
    # print(f"- GET: {output['GET_endpoint_count']}")
    # print(f"- POST: {output['POST_endpoint_count']}")
    # print(f"- PATCH: {output['PATCH_endpoint_count']}")
    # print(f"- DELETE: {output['DELETE_endpoint_count']}\n")

    # Generate endpoints section
    print(f"# Endpoint description\n")
    for endpoint in c.ENDPOINTS.keys():
        name = endpoint.replace('/', '-')[1:]
        print(f"## {name}\n")
        
        # Generate method section
        for method in c.ENDPOINTS[endpoint]["methods"]:
            print(f"### {method}\n")

            method_data = c.ENDPOINTS[endpoint]["methods"][method]
            table_data = {
                "Body Parameters": method_data["body_params"],
                "Query Parameters": method_data["query_params"],
                "Response": []
            }
            generate_object_2Dtable(table_data)   

if __name__ == "__main__":
    main()