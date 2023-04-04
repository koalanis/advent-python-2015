import os
import itertools
YEAR = 2015
DAY = 13

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

# David would gain 25 happiness units by sitting next to Bob.
def parse(line):
    delim_a = "happiness units by sitting next to"
    tokens_a = line.split(delim_a)
    left = tokens_a[0]
    right = tokens_a[1]
    other = right.strip().replace(".","")
    tokens_l = left.split("would")
    this = tokens_l[0].strip()
    tokens = tokens_l[1].strip().split()
    delta = tokens[0]
    amount = int(tokens[1])
    scale = -1 if "lose" in delta else 1
    return (this, other, scale * amount)


def happiness(perm, m):
    l = len(perm)
    h = 0
    for ii, i in enumerate(perm):
        j = perm[(ii+1)%l]
        v = m[i][j]
        vv = m[j][i]
        h += v + vv
    return h


def main():
    
    data = [parse(l.strip()) for l in get_data().readlines()]
    people = set()
    m = dict()
    for d in data:
        p, o, h = d
        people.add(p)
        m[p] = m.get(p, dict())
        m[p][o] = int(h)



    people_list = list(people)
    perms = list(itertools.permutations(people_list))
    tot_h = max(map(lambda x: happiness(x, m), perms))
    print(tot_h)
    
    for p in people:
        m[p]["me"] = 0
        m["me"] = m.get("me", dict())
        m["me"][p] = 0

    people.add("me")
    people_list = list(people)
    perms = list(itertools.permutations(people_list))
    tot_h = max(map(lambda x: happiness(x, m), perms))
    print(tot_h)
       
    pass

if __name__ == "__main__":
    main()

