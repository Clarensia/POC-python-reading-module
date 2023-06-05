import ast
from docstring_parser import parse

def extract_info(file_name):
    with open(file_name, "r") as source:
        tree = ast.parse(source.read())
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            print("Name of the class:", node.name)
            class_docstring = ast.get_docstring(node)
            if class_docstring:
                print("Description of the class:", class_docstring)
            for sub_node in node.body:
                if isinstance(sub_node, ast.AsyncFunctionDef):
                    print("function")
                    print("\nFunction definition:", ast.unparse(sub_node).split(':')[0] + ':')
                    func_docstring = ast.get_docstring(sub_node)
                    if func_docstring:
                        docstring_obj = parse(func_docstring)
                        print("Function description:", docstring_obj.short_description)
                        print("\nParams:")
                        for param in docstring_obj.params:
                            print("-", param.arg_name + ":", param.description)
                            print("-", param.arg_name + "_type:", param.type_name)
                        print("\nReturns:")
                        print(docstring_obj.returns.description)
                        print("Example response:", docstring_obj.meta[0].description.split('Example response:')[1].strip())
                        print("Return type:", docstring_obj.returns.type_name)
                        print("\nExceptions raised:")
                        for meta in docstring_obj.meta:
                            if 'raises' in meta.description:
                                print("-", meta.description)

if __name__ == "__main__":
    extract_info("input/BlockchainAPIs.py")
