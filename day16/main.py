# template
import os

YEAR = 2015
DAY = 16

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

target = dict()
target["children"] = 3
target["cats"] = 7
target["samoyeds"] = 2
target["pomeranians"] = 3
target["akitas"] = 0
target["vizslas"] = 0
target["goldfish"] = 5
target["trees"] = 3
target["cars"] = 2
target["perfumes"] = 1


def correlates(sample, target):
    keys = target.keys()
    
    for k in sample:
        #print(k)
        if k not in keys:
            #print("k not in keys")
            return False
        elif target[k] != sample[k]:
            #print(f"target_k {target[k]} does not equal sample_k {sample[k]}")
            return False

    return True

def re_correlates(sample, target):
    keys = target.keys()
    
    for k in sample:
        #print(k)
        if k not in keys:
            #print("k not in keys")
            return False
        elif k in ["cats", "trees"]:
            if sample[k] <= target[k]:
                return False
        elif k in ["pomeranians", "goldfish"]:
            if sample[k] >= target[k]:
                return False
        elif target[k] != sample[k]:
            return False
    return True


def parse(line):
    dd =line.split(" ")
    sue_num = int(dd[1][:-1])
    i = 2
    signature = dict()
    while i < len(dd):
        ele = dd[i][:-1]
        amount = dd[i+1]
        amount = amount[:-1] if ',' in amount else amount
        signature[ele] = int(amount)
        i += 2
    
    return sue_num, signature

def main():
    data = [i.strip() for i in get_data().readlines()]
    for d in data:
        sue, signature = parse(d)
        won = None
        if correlates(signature, target):
            won = sue
            break
    print("won :: ",won)
    
    for d in data:
        sue, signature = parse(d)
        won = None
        if re_correlates(signature, target):
            won = sue
            break
    print("won :: ",won)

    pass

if __name__ == "__main__":
    main()

