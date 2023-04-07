# template
import os

YEAR = 2015
DAY = 15

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


def main():
    data = [d.strip() for d in get_data("dataSample.txt").readlines()]
    for d in data:
        print(d)
    pass

if __name__ == "__main__":
    main()

