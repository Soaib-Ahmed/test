
class Phone:
    price =1200
    color='blue'
    brand = 'iphone'
    feature= ['camera','speker','5g']

    def call(self):
        print("call me")
    def send_sms(self,phone,sms):
        text=f'sending sms to :{phone} and messege :{sms}'
        return text

my_phone=Phone()
print(my_phone.brand)
print(my_phone.feature)
my_phone.call()
res=my_phone.send_sms(5565,'i miss you')
print(res)