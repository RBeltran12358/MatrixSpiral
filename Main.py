def main():
    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35, 36]]

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    test = [1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 35, 34, 33, 32, 31, 25, 19, 13, 7, 8, 9, 10, 11, 17, 23, 29, 28, 27,
            26, 20, 14, 15, 16, 22, 21]

    spiral = []
    # for row in matrix:
    #     print(row)
    # spiral.extend(matrix[0][::-1][1:3])
    # matrix[0]
    # addTop(matrix, 1)
    numRings = (min(matrix_rows, matrix_cols) + 1) // 2

    for ring_i in range(numRings):
        print(ring_i)
        addRing(matrix, spiral, ring_i)
        print()

    # print(addBottom(matrix, 2))
    print(spiral)
    # print(test)
    # print(spiral == test)


def addRing(matrix, spiral, ring):
    spiral.extend(addTop(matrix, ring))
    print("Top Layer : " + str(addTop(matrix, ring)))
    spiral.extend(downCol(matrix, ring))
    print("Right Layer : " + str(downCol(matrix, ring)))
    spiral.extend(addBottom(matrix, ring))
    print("Bottom Layer : " + str(addBottom(matrix, ring)))
    spiral.extend(upCol(matrix, ring))
    print("Left Layer : " + str(upCol(matrix, ring)))


def downCol(matrix, ring):
    new = []
    for rowIndex in range(ring, len(matrix) - ring - 1, 1):
        new.append(matrix[rowIndex][::-1][ring])
        # new.extend(matrix[rowIndex][matrix[ring)
    return new


def upCol(matrix, ring):
    new = []
    for rowIndex in range(ring + 1, len(matrix) - ring, 1):
        new.append(matrix[rowIndex][ring])
        # new.extend(matrix[rowIndex][matrix[ring)
    return new[::-1]


def addTop(matrix, ring):
    if (ring + 1 == len(matrix[ring]) - ring):
        return [matrix[ring][ring]]
    return matrix[ring][ring:len(matrix[ring]) - ring - 1]  # -1 bc i don't want to access the last number


def addBottom(matrix, ring):
    return matrix[len(matrix) - 1 - ring][ring + 1:len(matrix[ring]) - ring][
           ::-1]  # -1 bc i don't want to access the last number


if __name__ == "__main__":
    main()
