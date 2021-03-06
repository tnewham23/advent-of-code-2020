from p1 import total_occupied_seats

def visible_occupied_seats(model, row, col):
    ''' returns the number of visible occupied seats from a given seat '''
    # constraints
    max_row = len(model)
    max_col = len(model[0])
    
    seats = 0
    # check NW
    diff = 1
    while True:
        if row - diff < 0 or col - diff < 0:
            break
        if model[row - diff][col - diff] == '#':
            seats += 1
            break
        elif model[row - diff][col - diff] == 'L':
            break
        diff += 1
    # check N
    diff = 1
    while True:
        if row - diff < 0:
            break
        if model[row - diff][col] == '#':
            seats += 1
            break
        elif model[row - diff][col] == 'L':
            break
        diff += 1
    # check NE
    diff = 1
    while True:
        if row - diff < 0 or col + diff >= max_col:
            break
        if model[row - diff][col + diff] == '#':
            seats += 1
            break
        elif model[row - diff][col + diff] == 'L':
            break
        diff += 1
    # check E
    diff = 1
    while True:
        if col + diff >= max_col:
            break
        if model[row][col + diff] == '#':
            seats += 1
            break
        elif model[row][col + diff] == 'L':
            break
        diff += 1
    # check SE
    diff = 1
    while True:
        if row + diff >= max_row or col + diff >= max_col:
            break
        if model[row + diff][col + diff] == '#':
            seats += 1
            break
        elif model[row + diff][col + diff] == 'L':
            break
        diff += 1
    # check S
    diff = 1
    while True:
        if row + diff >= max_row:
            break
        if model[row + diff][col] == '#':
            seats += 1
            break
        elif model[row + diff][col] == 'L':
            break
        diff += 1
    # check SW
    diff = 1
    while True:
        if row + diff >= max_row or col - diff < 0:
            break
        if model[row + diff][col - diff] == '#':
            seats += 1
            break
        elif model[row + diff][col - diff] == 'L':
            break
        diff += 1
    # check W
    diff = 1
    while True:
        if col - diff < 0:
            break
        if model[row][col - diff] == '#':
            seats += 1
            break
        elif model[row][col - diff] == 'L':
            break
        diff += 1
    
    return seats


if __name__ == '__main__':
     # extract input from file
    with open('input.txt', 'r') as f:
        model = [list(x.rstrip()) for x in f.readlines()]
    
    max_row = len(model)
    max_col = len(model[0])
    while True:
        # copy model - normal model.copy() still contains references to original model rows
        new_model = list(map(list, model))
        num_changes = 0
        for row in range(max_row):
            for col in range(max_col):
                seat = model[row][col]
                if seat == 'L' and visible_occupied_seats(model, row, col) == 0:
                    # update seat in new model
                    new_model[row][col] = '#'
                    num_changes += 1
                elif seat == '#' and visible_occupied_seats(model, row, col) >= 5:
                    # update seat in new model
                    new_model[row][col] = 'L'
                    num_changes += 1
        # update model
        model = new_model
        # no changes made during iteration
        if num_changes == 0:
            print(total_occupied_seats(model))
            break
