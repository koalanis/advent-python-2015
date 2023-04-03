# template
import os
import json

YEAR = 2015
DAY = 12

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


def tree_trav(data, num_list):
    if type(data) is list:
        for ele in data:
            tree_trav(ele, num_list)
    elif type(data) is dict:
        for k,v in data.items():
            tree_trav(v, num_list)
    elif type(data) is int:
        num_list.append(data)


def solve1(data):
    num_list = []
    
    tree_trav(data, num_list)

    return sum(num_list)


def tree_trav_2(data, num_list):
    if type(data) is list:
        for ele in data:
            tree_trav_2(ele, num_list)
    elif type(data) is dict and "red" not in data and "red" not in data.values():
        for k,v in data.items():
            tree_trav_2(v, num_list)
    elif type(data) is int:
        num_list.append(data)


def solve2(data):
    num_list = []
    
    tree_trav_2(data, num_list)

    return sum(num_list)



def main():
    
    data = get_data().read()
    obj = json.loads(data)
    
    s1 = solve1(obj)
    print(s1)

    s2 = solve2(obj)
    print(s2)

    pass

if __name__ == "__main__":
    main()

