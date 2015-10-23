#!/usr/bin/python3
import pandas as pd


def extract_coordinates(s):
    s = s[s.find('['):s.find(']') + 1]
    a = float(s.replace('[', '').replace(']', '').split(',')[0])
    b = float(s.replace('[', '').replace(']', '').split(',')[1])
    return (a, b)


def check_coordinates(c, box):
    if(c[0] >= box[0] and c[0] <= box[2]):
        if(c[1] >= box[1] and c[1] <= box[3]):
            return True
    return False

if __name__ == "__main__":
    with open('samples/sampling_schipol.json') as f:
        l = [line for line in f]
    l = l[0:-1]

    lines = []
    for i in range(0, len(l), 2):
        lines.append(l[i])

    json_str = '[' + ','.join(lines) + ']'
    tweets_df = pd.read_json(json_str)

    tweet_coordinates = []
    for i in tweets_df['coordinates'].values:
        if i is not None:
            tweet_coordinates.append(extract_coordinates(str(i)))

    box = [4.73, 52.29, 4.77, 52.32]  # Schipol
    #box = [4.73, 52.29, 4.98, 52.42]  # Amsterdam

    count = 0
    for i in tweet_coordinates:
        if check_coordinates(i, box) is True:
            count = count + 1
    print("Tweets from schipol: %d" % count)
