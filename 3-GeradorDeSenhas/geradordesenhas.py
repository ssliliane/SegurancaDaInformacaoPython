import random
import string


tamanho = input("Informe o tamanho da senha:")
chars = string.ascii_letters + string.digits + "!@#$%&*-=.;:/?()"
rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(int(tamanho))))