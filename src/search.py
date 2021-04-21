from utils import parse_input, write_output

def search(input_path, output_path):
    words, grid = parse_input(input_path)
    max_row = len(grid)
    max_col = len(grid[0])

    solution = {}
    for word in words:
        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == word[0]:
                    coords = find_word(r, c, max_row, max_col, word, grid)
                    if coords:
                        solution[word] = coords

    write_output(solution, output_path)


def find_word(row, col, max_row, max_col, word, grid):
    directions = [(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]
    
    for x, y in directions:
        initial_coordinate = [(col, row)]
        cur_row = row + x
        cur_col = col + y

        res = initial_coordinate
        for i in range(1, len(word)):
            if cur_row>=max_row or cur_row<0 or cur_col>=max_col or cur_col<0:
                break

            if grid[cur_row][cur_col] != word[i]:
                break

            res.append((cur_col, cur_row))
            if len(res)==len(word):
                return res
            cur_row += x
            cur_col += y
