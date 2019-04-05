import requests as r

host = 'https://music-jp-api.line-apps.com/v3/bgm/'

lct = ''
#x-lctを入力

did = ''
#x-lm-didを入力

mid = input("please input music id:")

points = host + mid

header = {'x-lct': lct, 'Accept': 'application/json', 'x-lm-did': did, 'timeout': 30, 'User-Agent': 'LineMusic/3.9.2  (iPhone; U; iOS 12.1.4; ja-JP;)', 'Accept-Language': 'ja-JP;q=1', 'Accept-Encoding': 'br, gzip, deflate', 'Cookie': ''}

p = r.get(points, headers=header)

if p.status_code == 200:
    print('ok')
else:
    p.raise_for_status()
    print(p.text)
