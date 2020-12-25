import requests

payload = {'v': '5.71','access_token': '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
           'user_ids': '210700286'}
r = requests.get('https://api.vk.com/method/users.get', params=payload)
print(r.text)