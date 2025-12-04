def line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return f"x = {x1}"
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return f"y = {k:.2f}x + {b:.2f}" if b >= 0 else f"y = {k:.2f}x - {abs(b):.2f}"

def are_parallel(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    if x1 == x2 and x3 == x4:
        return True
    if x1 == x2 or x3 == x4:
        return False
    return (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3)

def point_on_line(point, line):
    (x, y) = point
    (x1, y1), (x2, y2) = line
    if x1 == x2:
        return x == x1
    return abs((y - y1) - (y2 - y1) / (x2 - x1) * (x - x1)) < 1e-9
