#!/usr/bin/env python3
# numbers
# provides information on a given number on the command line
# usage : numbers n
#         Where n is a number you are curious about

import requests

url = "https://numbersapi.p.rapidapi.com/random/trivia"

querystring = {"max":"20","fragment":"true","min":"10","json":"true"}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "9be3543240msh04b5ecbb90c408ep15f00bjsn4d5dfc210d07"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
