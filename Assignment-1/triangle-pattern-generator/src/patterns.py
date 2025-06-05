def lower_triangle(n: int) -> str:
    return '\n'.join(['* ' * (i + 1) for i in range(n)])

def upper_triangle(n: int) -> str:
    return '\n'.join(['  ' * i + '* ' * (n - i) for i in range(n)])

def pyramid(n: int) -> str:
    return '\n'.join([' ' * (n - i - 1) + '* ' * (i + 1) for i in range(n)])
