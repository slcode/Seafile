import requests
import json
import secrets
import string

from settings import base_url, token

def create_download_link(base_url, token, repo_id, fname, expire_days): 
    pwd_chars = string.ascii_letters + string.digits + '!%@#'
    passwd = ''.join(secrets.choice(pwd_chars) for i in range(10))

    headers={
        'Authorization': 'Token {token}'. format(token=token),
        'Accept': 'application/json; indent=4',
    } 

    flink = "%s/api/v2.1/share-links/" %(base_url)
    data = {
        'path': '/%s/' %fname,
        'repo_id': repo_id,
        'password': passwd,
        'expire_days': expire_days
        }    

    response = requests.post(flink, headers=headers, data=data)
    if response.status_code // 100 != 2:
        response.raise_for_status()
    return passwd, response.json()['link']

if __name__ == "__main__":
    repo = 'f2f55fcf-b04e-427d-a4c9-9fb4e5652fa8'
    dirname = 'test'

    passwd, link = create_download_link(base_url, token, repo, dirname, 21)
    print(passwd, link)