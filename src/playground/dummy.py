"""Dummy module"""


def add(x: int | float, y: int | float) -> int | float:
    return x + y


if __name__ == "__main__":
    print("Running dummy module entrypoint")
    print(f"The result of add(3, 4) is {add(3, 4)}")
