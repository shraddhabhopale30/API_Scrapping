import requests
from bs4 import BeautifulSoup
import json

def get_company_details(cin):
    url = f"https://www.mca.gov.in/mcafoportal/showCompanyDetails.do?cin={cin}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mca.gov.in/mcafoportal/showCompanyDetails.do',  
    }

    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")  
    print(f"Response Content (first 500 chars): {response.text[:500]}")  
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        company_name = soup.find('span', {'id': 'company_name'})
        if company_name:
            company_name = company_name.text.strip()
        else:
            company_name = "Not Found"
        
        status = soup.find('span', {'id': 'status'})
        if status:
            status = status.text.strip()
        else:
            status = "Not Found"
        
        directors = [director.text.strip() for director in soup.find_all('span', {'class': 'director-name'})]
        
        registered_address = soup.find('span', {'id': 'registered_address'})
        if registered_address:
            registered_address = registered_address.text.strip()
        else:
            registered_address = "Not Found"
        
        result = {
            "cin": cin,
            "company_name": company_name,
            "status": status,
            "directors": directors,
            "registered_address": registered_address
        }
        
        return json.dumps(result, indent=4)
    
    else:
        print("Error fetching data.")
        return None

if __name__ == "__main__":
    cin_number = "U72900BR2021PTC053947"
    
    result = get_company_details(cin_number)
    
    if result:
        with open('outputs/company_details.json', 'w') as file:
            file.write(result)
        
        print(result)
