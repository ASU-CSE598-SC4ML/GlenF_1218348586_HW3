import crypten
import torch

crypten.init()


def promo_code(x,y,m0, m1):
    
    # Alice's share
    x = torch.tensor(x)

    x_enc = crypten.cryptensor(x)

    # Alice sends her share to Bob along with key

    # Bob encrypts his share using key sent by Alice and Also encrypts the promo codes

    y = torch.tensor(y)
    m0 = torch.tensor(m0)
    m1 = torch.tensor(m1)
    one = torch.tensor(1)

    #Bob's encrypted share
    y_enc = crypten.cryptensor(y)

    # Promo code1 encrypted
    m0 = crypten.cryptensor(m0)

    # Promo code encrypted
    m1 = crypten.cryptensor(m1)

    one = crypten.cryptensor(one)

    
    # Bob computing promo code based on comparision

    encrypted_out = getattr(x_enc, "gt")(y_enc)
    
    promocode = encrypted_out * m0 + (one - encrypted_out) *m1

    return promocode

rec = promo_code(10,5,20,30)
print("testcase 1, when x>y")
print('Alice share: 10')
print('Bobs share: 5')
print("The recieved promocode is:", rec.get_plain_text())

rec = promo_code(10,50,20,30)
print("testcase 1, when x<y")
print('Alice share: 10')
print('Bobs share: 50')
print("The recieved promocode is:", rec.get_plain_text())
    














    