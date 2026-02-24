from lab1 import zigzag


def move_time(a, b):
    di = abs(a[0] - b[0])
    dj = abs(a[1] - b[1])

    if di == 1 and dj == 1:
        return 2
    return 1


def time_to_target(path, target):
    time = 0

    for i in range(len(path)):
        if path[i] == target:
            return time

        if i + 1 < len(path):
            time += move_time(path[i], path[i + 1])

    return None

def main():

    m = int(input("Введіть кількість рядків m: "))
    n = int(input("Введіть кількість стовпців n: "))

    ti = int(input("Рядок трупа: "))
    tj = int(input("Стовпець трупа: "))
    target = (ti, tj)

    matrix = [[(i, j) for j in range(n)] for i in range(m)]

    path_forward = zigzag(matrix)
    path_backward = path_forward[::-1]

    t1 = time_to_target(path_forward, target)
    t2 = time_to_target(path_backward, target)

    print("\n Труп у клітинці:", target)
    print("Час сховання трупа:", t1, "хв")
    print("Час на прибирання крові:", t2, "хв")


if __name__ == "__main__":
    main()