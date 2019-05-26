import requests
import json
from settings import base_url, token

def copy_directory(base_url, token, repo, dirname): # does not work
    ''' dirname could be "/" or "/foo"
    '''
    headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/json; charset=utf-8; indent=4',
        'Content-Type': 'application/json'
    }

    data = '{ "src_repo_id":"f2f55fcf-b04e-427d-a4c9-9fb4e5652fa8",  "dst_repo_id":"f2f55fcf-b04e-427d-a4c9-9fb4e5652fa8",  ' \
         + '"paths":[{"src_path":"/PHA_20190504171013046359","dst_path":"/PHA_20190517200223108402"},{"src_path":"/BYC01_QC__PHA_FBN1394__BYC01_PHA_FBN1394_0017.zip","dst_path":"/PHA_20190517200223108402"}  ] }'

    response = requests.post(f'{base_url}/api/v2.1/repos/batch-copy-item/', headers=headers, data=data)
    if response.status_code // 100 != 2:
        response.raise_for_status()
    print(response.status_code)
    return response.text

def batch_copy_directory(base_url, token, src_repo, src_dir, dst_repo, dst_dir, file_names):
    # src_dir and dst_dir should be empty string if files are under repo root dir.
    headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/json; indent=4',
    }

    params = (
        ('p', f'/{src_dir}'),
    )

    data = {
    'dst_repo': dst_repo,
    'dst_dir': f'/{dst_dir}',
    'file_names': ':'.join(file_names)
    }

    response = requests.post(f'{base_url}/api2/repos/{src_repo}/fileops/copy/', headers=headers, params=params, data=data)  
    if response.status_code // 100 != 2:
        response.raise_for_status()
    print(response.status_code)


if __name__=="__main__":

    src_repo = 'd4f596ed-09ea-4ac6-8d59-12acbd089097'
    src_dir = ''
    dst_repo = 'dae8cecc-2359-4d33-aa42-01b7846c4b32'
    dst_dir = 'test'
    fnames = ['file2.zip', 'file11.txt', 'address.txt']
    batch_copy_directory(base_url, token, src_repo, src_dir, dst_repo, dst_dir, fnames)
    
