# template
import os
import itertools

YEAR = 2015
DAY = 9

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


def get_pairs(l):
    i = 0
    while i+1 < len(l):
        yield l[i],l[i+1]
        i += 1

def dist_of_path(perm, m):
    pairs = list(get_pairs(perm))
    acc = 0
    for l,r in pairs:
        acc += m[l][r]
    return acc
    

def parse_data(line):
    tokens_a = line.strip().split("to")
    city_a = tokens_a[0].strip()
    token_b = tokens_a[1].strip()
    tokens_b = token_b.strip().split("=")
    city_b = tokens_b[0].strip()
    dist = int(tokens_b[1].strip())
    return city_a, city_b, dist

def main():
    m = dict()
    data = get_data()
    s = set()
    for line in data:
        a,b,d = parse_data(line.strip())
        m[a] = m.get(a, dict())
        m[b] = m.get(b, dict())
        m[a][b] = d
        m[b][a] = d
        s.add(a)
        s.add(b)
    perms = list(itertools.permutations(list(s)))
     
    min_dist = min(map(lambda x: dist_of_path(x,m), perms))
    print(min_dist)
   
    max_dist = max(map(lambda x: dist_of_path(x,m), perms))
    print(max_dist)


if __name__ == "__main__":
    main()

