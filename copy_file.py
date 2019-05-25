import requests

headers = {
    'Authorization': 'Token 24fd3c026886e3121b2ca630805ed425c272cb96',
    'Accept': 'application/json; charset=utf-8; indent=4',
}

params = (
    ('p', '/file0017.zip'),
)

data = {
  'operation': 'copy',
  'dst_repo': '73ddb2b8-dda8-471b-b7a7-ca742b07483c',
  'dst_dir': '/newcopy_20190520/'
}

response = requests.post('https://cloud.seafile.com/api2/repos/7460f7ac-a0ff-4585-8906-bb5a57d2e118/file/', 
                        headers=headers, params=params, data=data)