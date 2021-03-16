import crypten
import torch

crypten.init()

# Alice's share
x = torch.tensor(5)

# Bob's share
y = torch.tensor(10)

print(f"Alice's share: {x}")
print(f"Bob's share: {y}")


# Cipher text using cryptensor
x_enc = crypten.cryptensor(x)
y_enc = crypten.cryptensor(y)

print("Alice's share, encrypted:", x_enc)
print("Bob's share, encrypted:", y_enc)

encrypted_out = getattr(x_enc, "gt")(y_enc)
print(encrypted_out)
answer = encrypted_out.get_plain_text()
if answer == 1:
    print("Alice share greater than Bob")
else:
    print("Bob share greater")