class Shop:
    shoppig_mall='Planet SR'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]

    def add_to_cart(self,item):
        self.cart.append(item)

sraboni=Shop('Sraboin Colthing House')
sraboni.add_to_cart('Beg')
sraboni.add_to_cart('Watch')
sraboni.add_to_cart('Galsses')
sraboni.add_to_cart('Shoes')
print(sraboni.cart)

seaum=Shop('Seaum Brand House')
seaum.add_to_cart('Headphones')
seaum.add_to_cart('Wallet')
seaum.add_to_cart('Sun Glass')
print(seaum.cart)