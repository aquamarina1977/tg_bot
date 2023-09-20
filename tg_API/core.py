import requests

url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": "5aa2540287mshfcf60e38477dd15p16b9f4jsn1df28dc18b5a",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
