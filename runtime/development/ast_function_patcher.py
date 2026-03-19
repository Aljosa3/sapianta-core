import ast
from pathlib import Path


class ASTFunctionPatcher:

    @staticmethod
    def replace_function(file_path: str, function_name: str, new_code: str) -> bool:
        """
        Replace a function using AST (safe, structure-aware).
        """

        path = Path(file_path)

        if not path.exists():
            return False

        source = path.read_text(encoding="utf-8")

        try:
            tree = ast.parse(source)
        except Exception:
            return False

        # parse new function
        try:
            new_tree = ast.parse(new_code)
        except Exception:
            return False

        new_func = None
        for node in new_tree.body:
            if isinstance(node, ast.FunctionDef):
                new_func = node
                break

        if not new_func:
            return False

        class FunctionReplacer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == function_name:
                    return new_func
                return node

        new_tree = FunctionReplacer().visit(tree)

        try:
            new_source = ast.unparse(new_tree)
        except Exception:
            return False

        path.write_text(new_source, encoding="utf-8")

        return True