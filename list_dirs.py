import requests
import json

def get_list_from_lib(base_url, token, repo, dirname):
    ''' dirname could be "/" or "/foo"
    '''
    headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/json; indent=4',
    }

    params = (
        ('p', dirname), 
    )

    response = requests.get(f'{base_url}/api2/repos/{repo}/dir/', headers=headers, params=params)
    return response.text

if __name__=="__main__":
    base_url = "https://seafile.com"
    token = '24fd3c026886e3121b2ca630805ed425c272cb96'
    repo = '73ddb2b8-dda8-471b-b7a7-ca742b07483c'
    dirname = '/'
    all_dirs = get_list_from_lib(base_url, token, repo, dirname)
    print(json.dumps(all_dirs, indent=4))
