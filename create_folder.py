import requests
from settings import base_url, token

def create_folder(url, repo_id, folder_name, token): # folder_name starts and ends with "/" 
    headers={
        'Authorization': 'Token {token}'. format(token=token),
        'Accept': 'application/json; charset=utf-8; indent=4',
    }  
    data = {
        'operation': "mkdir"
        }    
    params = (
        ('p', folder_name),
        )
    print('creating folder: %s/api2/repos/%s/dir/' %(url, repo_id))
    response = requests.post('%s/api2/repos/%s/dir/' %(url, repo_id), 
                    headers = headers, data = data, params = params)
    if response.status_code // 2 != 100:
        response.raise_for_status()                    

    print("create seafile folder: %s" %response.status_code)

if __name__=="__main__":
    repo = "/f2f55fcf-b04e-427d-a4c9-9fb4e5652fa8"
    create_folder(base_url, repo, "/test", token)
