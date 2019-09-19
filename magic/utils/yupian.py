import requests


class YuPian():
    def __init__(self,apk,url):
        self.apk = apk
        self.url = url

    def sms_message(self,mobile,code):
        params = {
            "apikey":self.apk,
            "mobile":mobile,
            'text': '【娇莲黛】您的验证码是{code}'.format(code=code)
        }
        response = requests.post(self.url,data=params)
        data = response.json()
        return data


