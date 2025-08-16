import ast
import operator as op

OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}

class VantaInterpreter:
    """Simple interpreter for the Vanta language."""

    def __init__(self):
        self.env = {}

    def eval_expr(self, expr: str):
        node = ast.parse(expr, mode="eval").body
        return self._eval(node)

    def _eval(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Unsupported constant type")
        if isinstance(node, ast.BinOp):
            if type(node.op) not in OPS:
                raise ValueError(f"Unsupported operator: {ast.dump(node.op)}")
            return OPS[type(node.op)](self._eval(node.left), self._eval(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -self._eval(node.operand)
        if isinstance(node, ast.Name):
            if node.id in self.env:
                return self.env[node.id]
            raise NameError(f"Undefined variable '{node.id}'")
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")

    def execute(self, code: str) -> str:
        """Execute Vanta code and return the printed output."""
        output = []
        for raw in code.strip().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("print "):
                expr = line[6:].strip()
                value = self.eval_expr(expr)
                output.append(str(value))
            elif "=" in line:
                name, expr = line.split("=", 1)
                self.env[name.strip()] = self.eval_expr(expr.strip())
            else:
                raise SyntaxError(f"Unknown statement: {line}")
        return "\n".join(output)

def run_file(path: str):
    with open(path, "r") as f:
        code = f.read()
    interpreter = VantaInterpreter()
    out = interpreter.execute(code)
    if out:
        print(out)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run a Vanta program.")
    parser.add_argument("file", help="Path to the Vanta source file")
    args = parser.parse_args()
    run_file(args.file)
