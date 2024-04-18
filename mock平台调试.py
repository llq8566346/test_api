"""
123123123
Administrator
2024/4/17
"""

import requests

body={'d1':'hi','d2':'falsk12312312'}


resp = requests.post('http://127.0.0.1:9090/post')

print(resp.text)




