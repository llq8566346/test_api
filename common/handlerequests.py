import requests



class handlerequests(object):

        def __init__(self):
            self.session = requests.session()


        def send(self,url,method,params=None,json=None,data=None,files=None,headers=None):
            method = method.lower()
            if method == "get":
                response = self.session.get(url=url,params=params,headers=headers)

            if method == "post":
                response = self.session.post(url=url,json=json,data=data,files=files,headers=headers)

            if method == "patch":
                response = self.session.patch(url=url,json=json,data=data,files=files,headers=headers)

            return response
