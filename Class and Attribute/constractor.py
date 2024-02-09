class Phone:
    manufractured: 'china'
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms):
        text=f'sending sms to :{phone} and messege :{sms}'
        print(text)

my_phone=Phone('Seaum','Mi',22000)
Kabila=Phone('Kabila','Oppo',25000)
Badhon=Phone('Badhon','Pixel',60000)
Abir=Phone('Abir','Iphone',100000)

print(my_phone.owner,my_phone.brand,my_phone.price)
print(Kabila.owner,Kabila.brand,Kabila.price)
print(Badhon.owner,Badhon.brand,Badhon.price)
print(Abir.owner,Abir.brand,Abir.price)