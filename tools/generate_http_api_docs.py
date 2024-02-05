import sys
import inspect
import importlib
import shutil
import os

CLASS_BLACKLIST = ["__class__"]

BODY_REQESTS = ["POST", "PATCH"]

def generate_object_table(data, name = None):
    if len(data) == 0:
        return

    keys = data.keys()
    is_last = True
    for key in keys:
        if isinstance(data[key], dict):
            is_last = False
            break

    if is_last:
        # Create vertical table
        print("<table>\n")
        for key in keys:
            print(f"<tr><td>{key}</td><td>{data[key]}</td></tr>\n")
        print("</table>\n")
    else:
        # Create vertical table and call recursively
        print("<table>\n")
        if name:
            print(f"<tr><th>{name}</th><th></th></tr>\n")
        for key in keys:
            print(f"<tr><td>{key}</td><td>")
            generate_object_table(data[key])
            print("</td></tr>\n")
        print("</table>\n")

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
    method_endpoint_count = 0
    for endpoint in c.ENDPOINTS.keys():
        method_endpoint_count += len(c.ENDPOINTS[endpoint]["methods"].keys())
    print(f"Total number of methods: {method_endpoint_count}")

    # print(f"- GET: {output['GET_endpoint_count']}")
    # print(f"- POST: {output['POST_endpoint_count']}")
    # print(f"- PATCH: {output['PATCH_endpoint_count']}")
    # print(f"- DELETE: {output['DELETE_endpoint_count']}\n")

    print(f"# Table of Contents\n")
    for endpoint in c.ENDPOINTS.keys():
        link_name= endpoint.replace('/', '-')[1:]
        print(f"- [{endpoint}](#{link_name})")
    print()

    # Generate endpoints section
    print(f"# Endpoint description\n")
    for endpoint in c.ENDPOINTS.keys():
        name = endpoint.replace('/', '-')[1:]
        print(f"## {name}\n")
        
        # Generate method section
        for method in c.ENDPOINTS[endpoint]["methods"]:
            method_data = c.ENDPOINTS[endpoint]["methods"][method]
            if method_data.get("description"):
                name = f'{method} - {method_data["description"]}'
            else:
                name = method
            print(f"### {name}\n")
            generate_object_table(method_data["query_params"], "Query Parameters")
            generate_object_table(method_data["body_params"], "Body Parameters")
            # TODO: Implement response documentation

if __name__ == "__main__":
    main()