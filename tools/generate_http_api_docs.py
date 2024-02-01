import sys
import inspect
import importlib
import shutil
import os

CLASS_BLACKLIST = ["__class__"]

BODY_REQESTS = ["POST", "PATCH"]

def generate_table(data):
    if len(data) == 0:
        print("None\n")
        return

    keys = data[0].keys()
    print(f"| {' | '.join(keys)} |")
    print(f"| {' | '.join(['---' for _ in keys])} |")
    for row in data:
        print(f"| {' | '.join([str(row[key]) for key in keys])} |")

def generate_multitable(table_data):
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
        generate_table(table_data[key])

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
            print("</td><td>")
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
    module = importlib.import_module("constants_endpoint_structure")
  
    output = {
        "method_endpoint_count": 0,
        "GET_endpoint_count": 0,
        "POST_endpoint_count": 0,
        "PATCH_endpoint_count": 0,
        "DELETE_endpoint_count": 0,
        "url_endpoints": []
    }

    # Iterate over all classes in the file and add it to the url endpoint
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            if name in CLASS_BLACKLIST:
                continue

            url_endpoint = {
                "url": obj.url,
                "methods": []
            }

            # Iterate over all subclasses of the class and add it to the url entry
            for name_subclass, obj_subclass in inspect.getmembers(obj):
                if inspect.isclass(obj_subclass):
                    if name_subclass in CLASS_BLACKLIST:
                        continue

                    method = name_subclass.upper()

                    # Get query params for method
                    query_params = []
                    if hasattr(obj_subclass, "QUERY_PARAMS"):
                        query_params = obj_subclass.QUERY_PARAMS

                    # Get body params for method
                    body_params = []
                    if method in BODY_REQESTS:
                        body_params = obj_subclass.BODY_PARAMS

                    # Add method to url endpoint
                    url_endpoint["methods"].append({
                        "name": method,
                        "query_params": query_params,
                        "body_params": body_params,
                    })
                    output["method_endpoint_count"] += 1
                    output[f"{method}_endpoint_count"] += 1

            # Add url endpoint to output
            output["url_endpoints"].append(url_endpoint)

    # Delete file
    os.remove("constants_endpoint_structure.py")
    
    # Generate header and statistics section
    print(f"# Endpoint documentation\n")
    print(f"## Statistics\n")
    url_endpoint_count = len(output["url_endpoints"])
    print(f"Total number of urls: {url_endpoint_count}")
    for endpoint in output["url_endpoints"]:
        name = endpoint["url"].replace('<', '\<').replace('>', '\>')
        link_name= name.replace('/', '-')[1:]
        print(f"- [{name}](#{link_name})")
    print()
    print(f"Total number of methods: {output['method_endpoint_count']}")
    print(f"- GET: {output['GET_endpoint_count']}")
    print(f"- POST: {output['POST_endpoint_count']}")
    print(f"- PATCH: {output['PATCH_endpoint_count']}")
    print(f"- DELETE: {output['DELETE_endpoint_count']}\n")

    # Generate endpoints section
    print(f"## Endpoints\n")
    for endpoint in output["url_endpoints"]:
        name = endpoint["url"].replace('<', '\<').replace('>', '\>')
        name = name.replace('/', '-')[1:]
        print(f"### {name}\n")
        
        # Generate generate method section
        for method in endpoint["methods"]:
            print(f"#### {method['name']}\n")

            table_data = {
                "Body Parameters": method["body_params"],
                "Query Parameters": method["query_params"],
                "Response": []
            }
            generate_multitable(table_data)


            # print("<table>")
            # print("<tr><th>Body Parameters</th><th>Query Parameters</th></tr><tr><td>\n")

            # generate_table(method["body_params"])

            # print("</td><td>")

            # generate_table(method["query_params"])

            # print("</td></tr></table>\n")

if __name__ == "__main__":
    main()