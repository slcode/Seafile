import requests
from settings import base_url, token

def delete_files_directories(base_url, token, repo, file_names):

    headers = {
        'Authorization': f'Token {token}',
    }

    params = (
        ('p', '/'),
    )

    data = {
    'file_names': ":".join(file_names)
    }

    response = requests.post(f'{base_url}/api2/repos/{repo}/fileops/delete/', 
                                headers=headers, params=params, data=data)
    
    if response.status_code // 100 != 2:
        response.raise_for_status()
    print(response.status_code)


if __name__=="__main__":

    repo = 'f2f55fcf-b04e-427d-a4c9-9fb4e5652fa8'
    fnames = ['PHA_20190517200223108402', 'teest', 'BYC01_QC__PHA_FBN1394__BYC01_PHA_FBN1394_0001.zip']
    delete_files_directories(base_url, token, repo, fnames)
    
