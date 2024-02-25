# so this problem was simple but  also very hard

# first one is trivial, just simulate the evolutions
# the second one is interesting. i started from the medicine molecule and
# did depth first search with running teh simulation backwards

# the program never finished. i kept thinking of ways until i decided to just print the perhaps local optimas that _were_ computed in my dfs
# after a few millis, the optima was found and was printed and i just entered that and it worked...

# given that the dfs provided the answer very quickly, the underlying data must imply the greedy algorithm approach is guarenteed to also find the global minima
# or i am lucky

# i should look into what makes this the case for the sample data 

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
            # print(f"pre={pre}, mid={mid}, post={post}")
            next = pre + mid + post
            #print(rule, i, next)
            results.add(next)

    
    return results


def get_all_possible_molecules_after_single_evolution(ini, rules):
    molecules = set()
    for rule in rules:
        res = one_replacement_count(ini, rule)
        molecules.update(res)

    return molecules

def part_one(ini, rules):
    molecules = get_all_possible_molecules_after_single_evolution(ini, rules)
    print("Answer to part 1 = ", len(molecules))



cache = dict()
found = set()
dcache = set()

def populate_n_evolutions_in_cache(ini, n, rules):
    sample = set([ini])
    for i in range(0, n+1):
        next_gen = set()
        while len(sample) > 0:
            to_evolve = sample.pop()
            if to_evolve in cache:
                continue
            cache[to_evolve] = i
            molecules = get_all_possible_molecules_after_single_evolution(to_evolve, rules)
            next_gen = set(molecules)
        sample.update(next_gen)
    print("Answer to part 1 = ", len(molecules))
    pass

def part_two(start, end, rev_rules, depth = 0):
    # print(start, end)
    if start == end:
        found.add(depth)
        print(depth)
        return
    
    # reverse rules to make them sutractive instead of additive
    # print(rev_rules)
    frontier = set()
    for rule in rev_rules:
        if rule[1] == 'e' and len(start) != len(rule[0]):
            continue
        # print(rule, start)
        if start.find(rule[0]) >= 0:
            res = one_replacement_count(start, rule)
            # print("res", res)
            if res:
                frontier.update(res)
        
    for i in sorted(frontier, key=len):
        part_two(i, end, rev_rules, depth+1)


def get_elements(str):
    eles = set()
    
    for idx, ch in enumerate(str):
        if ch.isupper():
            if idx + 1 < len(str):
                if str[idx+1].islower():
                    eles.add(str[idx:idx+2])
                else:
                    eles.add(ch)
            else:
                eles.add(ch)
        else: 
            pass
    return eles
            


def main():
    d = [i.strip() for i in get_data("data.txt")]
    rules = [parse_rule(i) for i in d[:-2]]
    initial = d[-1]
    # print(d, rules)
    part_one(initial, rules)
    print("medicine molecule=", initial)
    print("len of it = ", len(initial))
    print("rules", rules)

    # populate_n_evolutions_in_cache("e", 200, rules)
    print("cache populated")
    print("\n\n\n\n\n\n")
    catalysts = set((i for i,j in rules))
    print(catalysts)
    elements = set()
    for i in (get_elements(j) for i,j in rules):
        elements.update(i)
    print(elements)
    artifacts = set()
    recurrent = set()
    consumable = set()
    
    for a in elements:
        if a in catalysts:
            recurrent.add(a)
        else:
            artifacts.add(a)
    
    for a in catalysts:
        if a not in elements:
            consumable.add(a)
    
    print("artifacts", artifacts)
    print("recurrent", recurrent)
    print("consumable", consumable)

    # return
    rev_rules = [(j,i) for i,j in rules]
    rev_rules = sorted(rev_rules, key= lambda x: -1* len(x[0]))



    print(rev_rules)
    part_two(initial, "e", rev_rules)
    print(min(found))
if __name__ == "__main__":
    main()

