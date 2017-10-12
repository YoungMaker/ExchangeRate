import urllib, json
url = 'http://api.fixer.io/latest?base=USD'


if __name__ == '__main__':
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print 1/(data['rates']['GBP'])
