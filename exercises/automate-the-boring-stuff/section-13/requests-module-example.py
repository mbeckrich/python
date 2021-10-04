import requests

res = requests.get("https://www.automatetheboringstuff.com/files/rj.txt")
# Must open() file as a write binary ('wb') file. This is to maintain the
# unicode encoding.

play_file = open("RomeoAndJuliet.txt", "wb")

for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()

# requests.readthedocs.org
