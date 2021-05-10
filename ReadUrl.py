import urllib.request
page = urllib.request.urlopen('https://bscscan.com/accounts')
print(page.read())
