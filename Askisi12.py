from urllib.request import Request, urlopen
import json

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
d = json.loads(data)
latest_r = d["round"]
last100 = latest_r - 100
url = "https://drand.cloudflare.com/public/"
list = []
for i in range(last100,latest_r+1):
    round = str(i)
    urli = url + round
    r = Request(urli, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(r).read()
    d = json.loads(data)
    intiger = int(d["randomness"],16)
    binary = bin(intiger)
    list.append(binary)
max_0seq = 0
max_0seq_item = ""
max_1seq = 0
max_1seq_item = ""
for item in list:
    previous = ""
    counter0 = 0
    counter1 = 0
    max0 = 0
    max1 = 0
    for number in item:
        if (previous != "1" and previous != "0"):
            previous = number
            if number == "0":
                counter0 += 1
            elif number == "1":
                counter1 += 1
        elif (number != previous and number == "1"):
            if counter0 > max0:
                max0 = counter0
            counter0 = 0
            previous = "1"
            counter1 += 1
        elif (number != previous and number == "0"):
            if counter1 > max1:
                max1 = counter1
            counter1 = 0
            previous = "0"
            counter0 += 1
        elif (number == previous and number == "1"):
            counter1 += 1
        elif (number == previous and number == "0"):
            counter0 += 1
    if max0 > max_0seq:
        max_0seq = max0
        max_0seq_item = item
    if max1 > max_1seq:
        max_1seq = max1
        max_1seq_item = item
print("The item with the maximum sequence of 0's was",max_0seq_item,"with:",max_0seq)
print("The item with the maximum sequence of 1's was",max_1seq_item,"with:",max_1seq)
