import requests
import json

def get_page_response():
    users = []

    for i in range(1, 13):
        page_api = "https://reqres.in/api/users?page=" + str(i)
        page_response = requests.get(url = page_api).text
        
        page_data = json.loads(page_response)
        # print(page_data)
        # print()
        
        users.append(page_data['data'])
    
    num_users = len(users)
    print(f"Total number of users = {num_users}")

if __name__=='__main__':
    get_page_response()
