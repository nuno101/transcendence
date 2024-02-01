import sys
import inspect
import importlib
import shutil
import os

BODY_REQESTS = ["POST", "PATCH"]

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
        "url_endpoint_count": 0,
        "url_endpoints": []
    }

    # Iterate over all classes in the file and add it to the url endpoint
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            url_endpoint = {
                "url": obj.url,
                "methods": []
            }

            # Iterate over all subclasses of the class and add it to the url entry
            for name_subclass, obj_subclass in inspect.getmembers(obj):
                if inspect.isclass(obj_subclass):
                    if name_subclass == "__class__":
                        continue

                    method = name_subclass.upper()

                    # Get params and params_optional for method
                    params = []
                    if method in BODY_REQESTS:
                        params = obj_subclass.PARAMS

                    # Add method to url endpoint
                    url_endpoint["methods"].append({
                        "method": method,
                        "params": params,
                    })
                    output["method_endpoint_count"] += 1
                    output[f"{method}_endpoint_count"] += 1

            # Add url endpoint to output
            output["url_endpoints"].append(url_endpoint)
            output["url_endpoint_count"] += 1

    # Delete file
    os.remove("constants_endpoint_structure.py")
    
    # Generate header and statistics section
    print(f"# Endpoint documentation\n")
    print(f"## Statistics\n")
    print(f"Total number of urls: {output['url_endpoint_count']}")
    for endpoint in output["url_endpoints"]:
        name = endpoint["url"].replace('<', '\<').replace('>', '\>')
        print(f"- [{name}](#`{name}`)")
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
        print(f"### `{name}`\n")
        
        # Generate generate method section
        for method in endpoint["methods"]:
            print(f"#### {method['method']}\n")
            print(f"| Param | Type | Required | Description |")
            print(f"| --- | --- | --- | --- |")
            for param in method["params"]:
                print(f"| {param['name']} | {param['type']} | {param['required']} | {param['description']} |")
            print()

if __name__ == "__main__":
    main()