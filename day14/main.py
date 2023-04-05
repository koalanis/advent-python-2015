# template
import os

YEAR = 2015
DAY = 14

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


def parse(line):
    tokens = line.split(" ")
    name = tokens[0]
    speed = tokens[3]
    sp_time = tokens[6]
    rest_time = tokens[-2]

    out = (name, int(speed), int(sp_time), int(rest_time))
    return out

def distance_traveled(reindeer, time_cap):
    dist = 0
    name, speed, sp_time, rest_time = reindeer
    moving = True
    while time_cap > 0:
        if moving:
            mv_time = min(time_cap, sp_time)
            dist += (speed * mv_time)
            moving = False
            time_cap -= mv_time
        else:
            time_cap -= rest_time
            moving = True
    return dist


def reindeer_race(reindeer, max_time):
    points = dict()
    for name, _, _, _ in reindeer:
        points[name] = 0
    
    for i in range(1, max_time+1):
        dist = dict()
        for deer in reindeer:
            dist[deer[0]] = distance_traveled(deer, i)
        points[max(dist, key=dist.get)] += 1

    return max(points.values())

def main():
    data = [i for i in get_data().readlines()]
    max_time = 2503
    
    reindeer = list(map(parse, data))
    
    print(max(map(lambda x: distance_traveled(x, max_time), reindeer)))
    print(reindeer_race(reindeer, max_time))

    pass

if __name__ == "__main__":
    main()

