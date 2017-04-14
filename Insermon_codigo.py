print(" ")
print("0 - Charmander")
print("1 - Bulbassauro")
print("2 - Squirtle")
print(" ")
escolha = int(input("Escolha um dos pokemons iniciais: "))
pokemon=pokedex[escolha]
np=pokemon["nome"]
pp=pokemon["ataque"]
vp=pokemon["vida"]
dp=pokemon["defesa"]
vida_max=vp
while True:
	print(" ")
	print("O seu pokemon é {0}, vida: {1}, ataque: {2}, defesa: {3}.".format(np,vp,pp,dp))
	print(" ")
	print("1 - Passear")
	print("2 - Dormir")
	pergunta=int(input("Escolha o que você quer fazer: "))
	print("  ")
	if pergunta==2:
		print("Ok, até a próxima!")
	elif pergunta==1:
		print("Você encontrou um oponente!")
		x = randint.choice(pokedex)
		n=x["nome"]
		p=x["ataque"]
		v=x["vida"]
		d=x["defesa"]
		print("O seu oponente é {0}, vida: {1}, ataque: {2}, defesa: {3}.".format(n,v,p,d))
		print(" ")
		while vp > 0 and v > 0:
			print("Sua vida é {0}".format(vp))
			print("A vida do oponente é {0}".format(v))
			print(" ")
			seuataque=(pp-d)
				if seuataque<0:
					seuataque=0
				v=v-seuataque
				if v<=0:
					v=0
					break
				opoataque=(p*-dp*)	
				if opoataque<0:
					opoataque=0	
				vp=vp-opoataque
				if vp<=0:
					vp=0
					break
		if vp==0:
				print(" ")
				print("Seu pokemon morreu. ")
				print("Game over!")
		elif v==0:
			print(" ")
			print("Parabéns, você ganhou a luta! ")