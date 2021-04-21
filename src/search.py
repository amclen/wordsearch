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


def find_word(r, c, max_row, max_col, word, grid):
    directions = [(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]
    
    for x, y in directions:
        res = [(c, r)]
        curr=r+x
        curc=c+y

        curres = res
        for i in range(1, len(word)):
            if curr>=max_row or curr<0 or curc>=max_col or curc<0:
                break

            if grid[curr][curc] != word[i]:
                break

            curres.append((curc, curr))
            if len(curres)==len(word):
                return curres
            curr+=x
            curc+=y


def parse_input(input_path):
    text_file = open(input_path, 'r')
    lines = text_file.readlines()
    text_file.close()

    words = lines[0].strip().split(',')
    grid = []
    for line in lines[1:]:
        grid.append(line.strip().split(','))
    
    return (words, grid)
    