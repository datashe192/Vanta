# Vanta
Vanta is a tiny toy programming language implemented in Python. It supports
variables, basic arithmetic, and printing.

## Running a program

Create a file containing Vanta code and run it with the interpreter:

```bash
python vanta.py path/to/program.vanta
```

## Language features

- Assign variables using `name = expression`.
- Print the value of an expression with `print expression`.
- Expressions may contain integers, variables, `+`, `-`, `*`, `/`, and parentheses.

## Examples

### Single print

```
x = 2 + 3
y = x * 5
print y
```

Running this program produces:

```
25
```

### Multiple prints

```
a = 1
b = a + 2
print a
print b
```

Output:

```
1
3
```
