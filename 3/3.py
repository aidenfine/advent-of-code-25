def max_n_digit_subsequence(num_str: str, n: int) -> str:
    remove = len(num_str) - n
    stack = []

    for digit in num_str:
        while remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)  # type:ignore

    return "".join(stack[:n])


def sol(n: int):
    with open("3/input.txt", "r") as f:
        batteries = [line.strip() for line in f]
    res = 0

    for battery in batteries:
        res += int(max_n_digit_subsequence(battery, n))
    print(f"{res=} with {n=}")


sol(2)
sol(12)
