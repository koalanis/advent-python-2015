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
        file = open(path, "r")
        return file
    except IOError:
        print(f"Could not fetch file {file} ")
        return None


def to_data(line):
    tokens = [i.strip() for i in line.strip().split(",")]
    data = dict()
    for t in tokens:
        tt = t.split(" ")
        k, v = tt[0], int(tt[1])
        data[k] = v
    return data


def parse(line):
    tokens = line.strip().split(":")
    name = tokens[0].strip()
    info = to_data(tokens[1])
    return name, info


def partitions(amount, count):
    if count <= 1:
        yield [amount]
    else:
        for i in range(amount + 1):
            for subpartition in partitions(amount - i, count - 1):
                yield [i] + subpartition



def calculate_score(amounts, properties, data):
    score = 1
    for prop in properties:
        score_sum = sum(amounts[i] * data[i][prop] for i in amounts)
        
        if score_sum > 0:
            score *= score_sum
        else:
            return 0

    return score


def calculate_score_2(amounts, properties, data):
    if sum(amounts[i]*data[i]["calories"] for i in amounts) != 500:
        return 0

    return calculate_score(amounts, properties, data)



def solve1(data):
    pass


def main():
    data = [d.strip() for d in get_data().readlines()]
    data = {name: info for name, info in (parse(d) for d in data)}

    total = 100
    properties = set()
    items = list(sorted(data.keys()))
    for _, info in data.items():
        for key in info:
            properties.add(key)
    properties.remove('calories')
    m_score = 0
    m_score_b = 0
    for part in partitions(total, len(items)):
        amounts = dict(zip(items, part))
        score = calculate_score(amounts, properties, data)
        m_score = max(score, m_score)
        score = calculate_score_2(amounts, properties, data)
        m_score_b = max(score, m_score_b)


    print(m_score, m_score_b)




pass


if __name__ == "__main__":
    main()
