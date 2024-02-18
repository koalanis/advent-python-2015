# howdy👋
# so this one as easy but i fell for jumping into a 'neat' / mathy solution and took too long with it
# its a story about the dance between hustirics, algorithms, and simulations
# i jumped into integer factorization and finding the number that way but it didnt work well for large numbers (would hang)
# so i then tried to incorporate binary search with this. with no luck with this, i decided to look at what this function even looks like
# https://mathworld.wolfram.com/DivisorFunction.html
# funny, before i decided to peek at reddit, I was thinking "maybe hill-climbing w/ binary search". that looking at the function, that would have sucked
# 
# hints on reddit just said: do it the dumb way. Eureka!  I remembered something: 3600000 integers isnt that much. merely simulating the elves is much faster
import os
YEAR = 2015
DAY = 20

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
    num = [int(i) for i in get_data().readlines()][0]

    N = num//10
    house = [0]*N
    for i in range(1, N):
        for j in range(i, N, i):
            house[j] += i * 10
    
    for i in range(1,N):
        if house[i] >= num:
            print(i)
            break


    house = [0]*N
    for i in range(1, N):
        c = 0
        for j in range(i, N, i):
            if c >= 50:
                break
            house[j] += i * 11
            c += 1
           

    for i in range(1,N):
        if house[i] >= num:
            print(i)
            break

if __name__ == "__main__":
    main()

