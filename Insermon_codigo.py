exp=0
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
	print("Sua experiência é igual a {0}".format(exp))
	print(" ")
	print("1 - Passear")
	print("2 - Dormir")
	print("3 - Enfermaria")
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
		xp=x["experiencia"]
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
			ra=random.randint(70,160)/100
			ran=random.randint(10,50)/100
			a=int(xp*ra+vp*ran)
			exp=exp+a
			print(" ")
			print("Parabéns, você ganhou a luta! ")
			print("Adquiriu {0} de experiência!".format(a))

	elif pergunta==3:
		print("Bem vindo a enfermaria.")
		print("Recuperar sua vida custa 30 pontos de experiência.")
		print("1 - Curar")
		print("2 - Sair")
		res=int(input("O que quer fazer: "))
		if res==1:
			if exp>=30:
				vp=vida_max
				exp=exp-30
				print("Vida restaurada.")
			else:
				print("Você não tem experiencia suficiente.")
		print("Boa sorte lá fora!")