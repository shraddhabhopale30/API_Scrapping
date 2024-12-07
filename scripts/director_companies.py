import requests
from bs4 import BeautifulSoup
import json

def get_director_companies(din, director_name):
    url = f"https://www.mca.gov.in/mcafoportal/showDirectorCompanyDetails.do?din={din}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mca.gov.in/mcafoportal/showDirectorCompanyDetails.do', 
    }

    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}") 
    print(f"Response Content (first 500 chars): {response.text[:500]}") 

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        companies = []
        for company in soup.find_all('div', {'class': 'company-details'}):
            company_name = company.find('span', {'class': 'company-name'})
            if company_name:
                company_name = company_name.text.strip()
            else:
                company_name = "Not Found"
                
            cin = company.find('span', {'class': 'cin'})
            if cin:
                cin = cin.text.strip()
            else:
                cin = "Not Found"
                
            incorporation_date = company.find('span', {'class': 'incorporation-date'})
            if incorporation_date:
                incorporation_date = incorporation_date.text.strip()
            else:
                incorporation_date = "Not Found"
                
            status = company.find('span', {'class': 'status'})
            if status:
                status = status.text.strip()
            else:
                status = "Not Found"
            
            companies.append({
                "company_name": company_name,
                "cin": cin,
                "incorporation_date": incorporation_date,
                "status": status
            })

        result = {
            "din": din,
            "director_name": director_name,
            "companies": companies
        }
        
        return json.dumps(result, indent=4)
    else:
        print("Error fetching data.")
        return None

if __name__ == "__main__":
    din_number = "09313226"
    director_name = "Naresh Ahirwar"

    result = get_director_companies(din_number, director_name)
    
    if result:
        with open('outputs/director_companies.json', 'w') as file:
            file.write(result)
        
        print(result)
