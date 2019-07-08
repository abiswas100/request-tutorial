import requests
r = requests.get('https://www.google.co.in/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2F216xvaj_OAA%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D216xvaj_OAA&docid=eb7gsMRglpfK-M&tbnid=rSao52qotb_b1M%3A&vet=10ahUKEwi978fQhcbhAhVrHKYKHeR0AssQMwhsKAEwAQ..i&w=1280&h=720&hl=en&authuser=0&bih=633&biw=1366&q=youtube&ved=0ahUKEwi978fQhcbhAhVrHKYKHeR0AssQMwhsKAEwAQ&iact=mrc&uact=8')

print(r.headers)