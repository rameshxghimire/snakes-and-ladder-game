""" Main file for the game logic."""

from colors import print_custom

# # Create the grid Method 1
# # Rows for the grid
# rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
# rows = reversed([reversed(rows[i]) if i%2 else rows[i] for i in range(len(rows))])

# # Create a function to show the grid
# def show_grid():
#     for row in rows:
#         print("|".join(row))
# show_grid()

# # Create Grid: Method 2:
# # This method does not create the intermediary list.

# def make_row(start, stop, reverse):
#     #return list(reversed(range(start, stop))) if reverse else list(range(start, stop))
#     return "|".join(str(e) for e in (list(reversed(range(start, stop))) if reverse else list(range(start, stop))))

# def make_rows(size):
#     grid = [make_row(size**2 - size*(row + 1) + 1, size**2 - size*row + 1, row % 2 == 0) for row in range(size)]
#     return grid

# # Test if it works
# size = 10
# for rows in make_rows(size):
#     print(rows)

# Create Grid: Method 3
rows = []
for n in range(81, 0, -20):
    rows.append(list(range(n + 19, n + 9, -1)))  # Going from 100 to 90 in the first list
    rows.append(list(range(n, n + 10)))

for row in rows:
    print_custom(' | '.join([f"{col:03}" for col in row]))  # use print_custom function from colors module to get the output in color.
