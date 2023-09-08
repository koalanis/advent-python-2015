# template
import os

YEAR = 2015
DAY = 19

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

def parse_rule(str):
    tt = str.split(" => ")
    return tt[0], tt[1]


def one_replacement_count(ini, rule):
    pattern, transform = rule
    results = set()
    scan = len(pattern)
    for i in range(len(ini)):
        window = ini[i:i+scan]
        if pattern == window:
            pre = ini[:i]
            mid = transform
            post = ini[i+scan:]
            print(f"pre={pre}, mid={mid}, post={post}")
            next = pre + mid + post
            #print(rule, i, next)
            results.add(next)

    
    return results


def part_one(ini, rules):
    molecules = set()
    for rule in rules:
        res = one_replacement_count(ini, rule)
        molecules.update(res)
    print(molecules)
    print(len(molecules))

def main():
    d = [i.strip() for i in get_data("data.txt")]
    rules = [parse_rule(i) for i in d[:-2]]
    initial = d[-1]

    print(rules, initial)
    part_one(initial, rules)

if __name__ == "__main__":
    main()

