#run pip3 install requests to install requests package
import requests

url = "https://adsbexchange-com1.p.rapidapi.com/v2/registration/N8737L/"

headers = {
	"X-RapidAPI-Key": "f32fdda07amsh1e0587bbdf16af4p19e04ejsn1d49db0c5cdf",
	"X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())