def parse_input(input_path):
    text_file = open(input_path, 'r')
    lines = text_file.readlines()
    text_file.close()

    words = lines[0].strip().split(',')
    grid = []
    for line in lines[1:]:
        grid.append(line.strip().split(','))
    
    return (words, grid)


def write_output(solution, output_path):
    out_file = open(output_path, "w")

    for word in solution:
       out_file.write('%s: %s\n'%(word, str(solution[word]).lstrip('[').rstrip(']')))
    
    out_file.close()
