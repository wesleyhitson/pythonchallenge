import urllib3, re, string

http = urllib3.PoolManager()
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
nothing = 12345
match = http.request('GET', url % nothing)

while match:
    r = http.request('GET', url % match)
    items = r.data.split()
    match = items[-1]
    print(" ".join(items))

# gets peak.html
