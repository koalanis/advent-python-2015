# template
import os

YEAR = 2015
DAY = 10

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



def look_and_say(num):
    agg = ""
    
    ith = 1
    count = 1
    ch = num[0]
    while ith < len(num):
        if num[ith] == ch:
            count += 1
        else:
            agg += str(count) + str(ch)
            ch = num[ith]
            count = 1
        ith += 1
    agg += str(count) + str(ch)

    return agg

def main():    
    num = get_data().readline().strip()
    iterations = 40
    val = num
    for _ in range(iterations):
        val = look_and_say(val)
    
    print(len(val))

    iterations = 50
    val = num
    for _ in range(iterations):
        val = look_and_say(val)
    
    print(len(val))





if __name__ == "__main__":
    main()

