import ast

import docstring_parser

from src.dataclasses.MainClass import MainClass
from src.dataclasses.MainClassMethod import MainClassMethod
from src.dataclasses.MethodException import MethodException
from src.dataclasses.MethodParameter import MethodParameter


class MainClassParser:
    """
    Parse the main file that has multiple functions.
    """

    def _parse_function(self, node: ast.stmt) -> MainClassMethod:
        """Transform an ast node to a MainClassMethod

        :param node: The node that we use
        :type node: ast.stmt
        :return: The MainClassMethod
        :rtype: MainClassMethod
        """
        ret = MainClassMethod()
        ret.definition = ast.unparse(node).split(':')[0] + ':'
        func_dostring = ast.get_docstring(node)
        if func_dostring:
            docstring_obj = docstring_parser.parse(func_dostring)
            ret.short_description = docstring_obj.short_description
            if docstring_obj.long_description:
                ret.long_description = docstring_obj.long_description
            else:
                ret.long_description = docstring_obj.short_description
            for param in docstring_obj.params:
                ret.parameters.append(
                    MethodParameter(
                        param.arg_name,
                        param.description,
                        param.type_name,
                        # TODO: Find a way to add the example
                        None
                        # TODO: Allow us to know if it is an optional or mandatory parameter
                    )
                )
            ret_with_example = docstring_obj.meta[-1].description.split('Example response:')
            ret.return_description = ret_with_example[0]
            ret.example_response = ret_with_example[1]
            ret.return_type = docstring_obj.returns.type_name
            for exception in docstring_obj.raises:
                ret.exceptions.append(
                    MethodException(
                        exception.type_name,
                        exception.description
                    )
                )
        return ret

    def parse_file(self, path: str) -> MainClass:
        """Parse the given file at path and transform it into a MainClass
        instance that we can then use to write the documentation

        :param path: The path to the file that we have to parse
        :type path: str
        :return: The class parsed
        :rtype: MainClass
        """
        with open(path, "r") as source:
            tree = ast.parse(source.read())
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                ret = MainClass()
                ret.name = node.name
                class_docstring = ast.get_docstring(node)
                if class_docstring:
                    ret.long_description = class_docstring
                    docstring_lines = class_docstring.split("\n", 1)
                    ret.short_description = docstring_lines[0]
                for sub_node in node.body:
                    if isinstance(sub_node, ast.AsyncFunctionDef) or isinstance(sub_node, ast.FunctionDef):
                        ret.methods.append(self._parse_function(sub_node))

        return ret
