# dial numbers are 0-99
# starting point is always 50
# L = subtract, R = add

# output: number of times the result of an operation is = 0


def operation(dir: str, n: int, curr: int) -> int:
    if dir == "r":
        return (curr + n) % 100
    return (curr - n) % 100


curr_dial_pos = 50
zero_count = 0
while True:
    line = input().strip()
    if not line:
        break
    direction = str(line[0])
    number = int(line[1:])
    result = operation(direction.lower(), number, curr_dial_pos)
    print(f"direction={direction}, number={number}, result={result}")
    if result == 0:
        zero_count += 1
    curr_dial_pos = result

print(f"{zero_count=}")
