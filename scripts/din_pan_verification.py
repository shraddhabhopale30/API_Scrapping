import requests
from bs4 import BeautifulSoup
import json

def verify_din(din):
    url = "https://www.mca.gov.in/mcafoportal/showDINVerification.do"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mca.gov.in/mcafoportal/showDINVerification.do',  
    }

    payload = {'din': din}
    
    response = requests.post(url, headers=headers, data=payload)

    print(f"Status Code: {response.status_code}") 
    print(f"Response Content: {response.text[:500]}") 
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        director_name = soup.find('span', {'id': 'director_name'}).text.strip()
        pan_verified = 'Yes' in soup.find('span', {'id': 'pan_status'}).text.strip()

        result = {
            "din": din,
            "director_name": director_name,
            "pan_verified": pan_verified
        }
        return json.dumps(result, indent=4)
    else:
        print("Error fetching data.")
        return None

if __name__ == "__main__":
    din_number = "09313226"
    result = verify_din(din_number)
    if result:
        with open('outputs/din_details.json', 'w') as file:
            file.write(result)
        print(result)
