# template
import os

YEAR = 2015
DAY = 17

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


def combinations(target, coin_vals, coins, used, acc):
    if target == 0:
        used = tuple(sorted(used))
        acc.append(used)
    else:
        for c_ptr in coins:
            c = coin_vals[c_ptr]
            if c <= target:
                n_used = used.copy()
                n_coins = coins.copy()
                n_used = n_used + [c_ptr]
                n_coins.remove(c_ptr)
                combinations(target-c, coin_vals, n_coins, n_used, acc)
    

def main():
    target = 150
    #target = 25

    coins = [int(c.strip()) for c in get_data()]
    
    acc = []
    combinations(target, coins, list(range(len(coins))), [], acc)
    acc = set(acc)
    print(len(acc))

    
    min_containers = min(map(lambda x: len(x), acc))
    print("min amount", min_containers)
    
    count = 0
    for i in acc:
        if len(i) == min_containers:
            count += 1

    print(count)


if __name__ == "__main__":
    main()

