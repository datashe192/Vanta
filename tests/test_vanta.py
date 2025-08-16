import pathlib
import sys

# Ensure the project root is on the path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import vanta


def run(code: str) -> str:
    interpreter = vanta.VantaInterpreter()
    return interpreter.execute(code)


def test_arithmetic_and_print():
    code = """
    x = 2 + 3
    y = x * 5
    print y
    """
    assert run(code) == "25"


def test_multiple_prints():
    code = """
    a = 1
    b = a + 2
    print a
    print b
    """
    assert run(code) == "1\n3"
