import hmac
import hashlib

secret_key = b'This_is a_secret_key'
with open('/home/kali/Desktop/WIRESHARK/Pocox51.pcapng','rb') as f:
	packet_data  =f.read()
hmac_obj = hmac.new(secret_key,digestmod = hashlib.sha512)
hmac_obj.update(packet_data)
hmac_value = hmac_obj.hexdigest()
print(f'HMAC value : {hmac_value}')
f.close()
with open('hash_value.txt','w') as f:
	f.write(hmac_value)
f.close()
