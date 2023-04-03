# template
import os

YEAR = 2015
DAY = 11

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


def inc_ch(ch):
    n_ch = chr( ord(ch) + 1 )
    wrap = ord(n_ch) > ord('z')
    return n_ch if not wrap else 'a', wrap

def increment(pwd):
    
    password = list(pwd)
    i = 7
    carry = False
    inc = True
    while i >= 0 and (inc or carry):
        inc = False
        ch = password[i]
        n_ch, wrap = inc_ch(ch)
        password[i] = n_ch
        i -= 1
        carry = wrap

    return "".join(password)


def include_straight(pwd):
    pl = list(pwd)
    for i in range(len(pl)-3):
        j,k = i+1,i+2
        v_i ,v_j, v_k = pl[i], pl[j], pl[k]
        if ord(v_i) < ord(v_j) < ord(v_k):
            if ord(v_j) - ord(v_i) == 1 and ord(v_k) - ord(v_j) == 1:
                return True
    
    return False


def has_illegal_letters(pwd):
    return 'i' in pwd or 'o' in pwd or 'l' in pwd


def has_two_pairs(password):
    pwd = list(password)
    count = 0
    l = list()

    i = 0
    while i < len(pwd):
        if i+1 < len(pwd) and pwd[i] == pwd[i+1]:
            l.append(i)
        i += 1
     
    i=0
    l.sort()
    f = list()
    while i < len(l):
        if i + 1 < len(l):
            if l[i+1] - l[i] >= 2:
                f.append(l[i])
        else:
            f.append(l[i])
        i += 1
    return len(f) >= 2
            


def check_if_valid(pwd):
    return include_straight(pwd) and not has_illegal_letters(pwd) and has_two_pairs(pwd)


def main():
    val = get_data().readline().strip()

    while not check_if_valid(val):
        val = increment(val)
    print(val)
   
    val = increment(val)
    while not check_if_valid(val):
        val = increment(val)
    print(val)
   


if __name__ == "__main__":
    main()

