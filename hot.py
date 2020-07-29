import random
heads = tails = 0
print("Tossing a coin...")
for n in range(3):
    print(f"Round {n}: ", end="")
    if random.random() < 0.5:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
print(f"Heads: {heads}, Tails: {tails}")
if heads > tails:
    print("You won,")
else:
    print("You lost.")