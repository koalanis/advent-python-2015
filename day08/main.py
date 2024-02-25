# template
import os

YEAR = 2015
DAY = 8

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





def is_hex(st):
    return (ord('0') <= ord(st) <= ord('9')) or (ord('a') <= ord(st) <= ord('f'))

def chars_in_code(st):
    return len(st)

def chars_in_mem(st):
    raw = st[1:-1]
    
    agg = ""
    ith = 0
    while ith < len(raw):
        ch = raw[ith]
        if ch == '\\':
            if ith + 1 < len(raw) and raw[ith+1] in ["\\", '"', "x"]:
                ch_n = raw[ith+1]
                if ch_n in ["\\", '"']:
                    agg += ch_n
                    ith += 1
                else:
                    if ith + 3 < len(raw) and is_hex(raw[ith+2]) and is_hex(raw[ith+3]):
                        agg += 'a'
                        ith += 3
                    else:
                        agg += ch
                                                                            
            else:
                agg += ch
        else:
            agg += ch
        
        ith += 1

    return len(agg)

def transform_diff(data, fn, gn):
    total_a = 0
    total_b = 0
    
    for l in data:
        total_a += fn(l)
        total_b += gn(l)

    return total_a - total_b



def solve1(data):
    return transform_diff(data, chars_in_code, chars_in_mem)


def encode_chars(st):
    agg = ""
    for ch in st:
        if ch == '"':
            agg += '\\"'
        elif ch == "\\":
            agg += ch +"\\"
        else:
            agg += ch


    res = '"' + agg + '"'
    return len(res)

def solve2(data):
    return transform_diff(data, encode_chars, chars_in_code)

def main():
    file = get_data()
    data = [l.strip() for l in file.readlines()]
    sol1 = solve1(data)
    print("Part1 = ", sol1)

    sol2 = solve2(data)
    print("Part2 = ", sol2)
    pass

if __name__ == "__main__":
    main()
