def count_neighbours(grid, row, col):
    neighbour = ((-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1), (1, -1),
                 (1, 0), (1, 1))
    count = 0
    for shift in neighbour:
        n_row = row + shift[0]
        n_col = col + shift[1]
        if (0 <= n_row < len(grid)) and (0 <= n_col < len(grid[0])):
            count += grid[n_row][n_col]
    return count


if __name__ == '__main__':
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
