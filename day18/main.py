# template
import os

YEAR = 2015
DAY = 18

def get_advent_folder_name(year, day):
    base = os.environ["ADVENT_HOME"]
    if not base:
        raise "ADVENT_HOME folder not set"
    
    return f"{base}/{year}/data/day{day}"

def get_data(name="data.txt"):
  data = []
  filename = get_advent_folder_name(YEAR, DAY)
  path = f"{filename}/{name}"
  try:
      file = open(path, 'r')
      return file
  except IOError:
      print(f"Could not fetch file {file} ")
      return None

def char_row(size = 100):
    return ["."] * size

def char_grid(size = 100):
    return [char_row(size)] * size

def in_grid(grid, i, j):
    return 0 <= i < len(grid) and 0<=j<(len(grid[i]))

def get_neighbors(grid, i, j):
    possible = [(i-1, j-1), (i-1, j), (i-1, j+1), 
                (i, j-1), (i, j+1), 
                (i+1, j-1), (i+1, j), (i+1, j+1)] 
    
    return [(k,l) for (k,l) in possible if in_grid(grid, k,l)]    

def count_lights(grid):
    count = 0
    for i in range(len(grid)):
        count += count_lights_list(grid[i])
    return count

def count_lights_list(ll):
    count = 0
    for i in range(len(ll)):
        if ll[i] == "#":
            count += 1
    return count

def grid_print(grid):
    print("pritning grid")
    print(grid)
    if True:
        for i in grid:
            print(i)
        print()
        

def set_corner_lights(grid):
    grid[0][0] = '#'
    grid[len(grid)-1][0] = '#'
    grid[0][len(grid[0])-1] = '#'
    grid[len(grid)-1][len(grid[0])-1] = '#'

# steps = 4
steps = 100

def part_one(grid_buffer):  
    print("part one start") 
    print()
    grid_print(grid_buffer)
    
    on_next = set()
    for step in range(steps):
        for ri in range(len(grid_buffer)):
            for ci in range(len(grid_buffer[ri])):
                idx = (ri,ci)
                nei = get_neighbors(grid_buffer, ri, ci)
                vals = [grid_buffer[ii[0]][ii[1]] for ii in nei]
                on_count = count_lights_list(vals)
                current = grid_buffer[ri][ci]
                if current == "#":
                    if on_count == 2 or on_count == 3:
                        on_next.add(idx)
                else:
                    if on_count == 3:
                        on_next.add(idx)
         
        for ri in range(len(grid_buffer)):
            for ci in range(len(grid_buffer[ri])):
                grid_buffer[ri][ci] = "."

        for ri,ci in on_next:
            grid_buffer[ri][ci] = "#"
        print(step)
        on_next.clear()
        
    print("part 1")     
    print(count_lights(grid_buffer))
    pass


def part_two(grid):   
    print("part two start")
    grid_buffer = grid
    
    set_corner_lights(grid_buffer)
    
    on_next = set()
    for step in range(steps):
        
        for ri in range(len(grid_buffer)):
            for ci in range(len(grid_buffer[ri])):
                idx = (ri,ci)
                nei = get_neighbors(grid_buffer, ri, ci)
                vals = [grid_buffer[ii[0]][ii[1]] for ii in nei]
                on_count = count_lights_list(vals)
                current = grid_buffer[ri][ci]
                if current == "#":
                    if on_count == 2 or on_count == 3:
                        on_next.add(idx)
                else:
                    if on_count == 3:
                        on_next.add(idx)

        for ri in range(len(grid_buffer)):
            for ci in range(len(grid_buffer[ri])):
                grid_buffer[ri][ci] = "."

        for ri,ci in on_next:
            grid_buffer[ri][ci] = "#"

        
        on_next.clear()
        
        set_corner_lights(grid_buffer)
        on_next = set()

        
    print("part 2")
    print(count_lights(grid_buffer))
    pass

def copy_grid(grid):
    back_buffer = char_grid(len(grid))
   
    for ri in range(len(grid)):
       back_buffer[ri] = list(grid[ri])
    
    return back_buffer

def main():
    d = [list(i.strip()) for i in get_data("data.txt").readlines()]
    size = len(d[0])
    
    grid_buffer = copy_grid(d)
    grid_buffer2 = copy_grid(d)
    
    part_one(grid_buffer)
    part_two(grid_buffer2)
    

if __name__ == "__main__":
    main()

