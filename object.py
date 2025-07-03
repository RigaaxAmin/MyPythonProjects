def get_size(size_str):
    sizes = {
        "Smaller": 2,
        "Small": 4,
        "Regular": 6,
        "Big": 8,
        "Bigger": 10
    }
    return sizes.get(size_str.capitalize(), -1)


def print_triangle(size):
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


def print_square(size):
    for _ in range(size):
        print('*' * size)


def print_diamond(size):
    if size % 2 != 0:
        size += 1  # Ensure symmetry
    half = size // 2
    for i in range(1, half + 1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    for i in range(half - 1, 0, -1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


def main():
    print("Shape Drawer")
    print("Type: Triangle, Square, Diamond")
    print("Size: Smaller, Small, Regular, Big, Bigger")

    shape_type = input("Enter the shape type: ").strip().capitalize()
    size_str = input("Enter the size: ").strip().capitalize()
    size = get_size(size_str)

    if size == -1:
        print("Invalid size. Please enter: Smaller, Small, Regular, Big, Bigger")
        return

    if shape_type == "Triangle":
        print_triangle(size)
    elif shape_type == "Square":
        print_square(size)
    elif shape_type == "Diamond":
        print_diamond(size)
    else:
        print("Invalid type. Please enter: Triangle, Square, Diamond")


if __name__ == "__main__":
    main()