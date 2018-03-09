import urllib3
import pickle

http = urllib3.PoolManager()
r = http.urlopen('GET', 'http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.loads(r.data)
for d in data:
    str = ""
    for lst in d:
        str += lst[0] * lst[1]
    print(str)

# gives channel
