from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# .env variables
X_RapidAPI_Key = os.getenv("X-RapidAPI-Key")
X_RapidAPI_Host = os.getenv("X-RapidAPI-Host")


url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": f"{X_RapidAPI_Key}",
	"X-RapidAPI-Host": f"{X_RapidAPI_Host}"
}

response = requests.get(url, headers=headers)
print(response.json())