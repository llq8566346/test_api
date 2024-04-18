"""
123123123
Administrator
2024/4/17
"""
import rsa
import base64
import time
class HandleSign(object):
    server_pub = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
        O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
        tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
        kKlZFc8Br7SHtbL2tQIDAQAB
        -----END PUBLIC KEY-----
        """
    def to_encrypt(self,msg,pub_key=None):
        if isinstance(msg , str):
            msg = msg.encode("utf-8")
        elif isinstance(msg , bytes):
            pass
        else:
            raise Exception("msg必须为字符串或者字节类型！")
        if isinstance(pub_key,str):
            pub_key = pub_key.encode("utf-8")
        elif isinstance(pub_key,bytes):
            pass
        elif pub_key == None:
            pub_key = self.server_pub
        else:
            raise Exception("pub_key必须为字符串或者字节类型或者None!")
        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)
        cryto_msg = rsa.encrypt(msg,public_key_obj)
        cryto_msg = base64.b64encode(cryto_msg)
        return cryto_msg.decode()
    def generate_sign(self,token,timestamp=None):
        timestamp = timestamp or int(time.time())
        prefix_50_token = token[:50]
        message = prefix_50_token+str(timestamp)
        sign = self.to_encrypt(message)
        return {"timestamp":timestamp,"sign":sign}
import hashlib
def md5_hash(text):
    md5_obj = hashlib.md5()
    md5_obj.update(text.encode())
    encrypted_text = md5_obj.hexdigest()
    return encrypted_text










# my_token = "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjI2NSwiZXhwIjoxNTc0NjY3MjMzfQ.ftrNcidmk_zxwl0wzdhE5_39bsGlILoSSoTCy043fjhbjhCFG4FwCnOj4iy5svbDlSbgCJM3qRa1zsXJLJmH4A"
#
# cryto_info = HandleSign().generate_sign(my_token)
#
# print(cryto_info)
