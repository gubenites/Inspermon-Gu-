import random as randint

import random

import json
with open('dicionario.json') as arquivo:
	pokedex = json.load(arquivo)

print(""" 
	Bem vindo!
	1 - Começar um jogo novo
    	2 - Carregar jogo
    	""")
res=int(input("Selecione uma opção: "))

if res == 1:
	suapokedex=[]
	exp=0
	print("""
	0 - Charmander
	1 - Bulbassauro
	2 - Squirtle
	""")
	escolha = int(input("Escolha um dos pokemons iniciais: "))
	if escolha == 0 or escolha==1 or escolha==2:
		pokemon=pokedex[escolha]
		np=pokemon["nome"]
		pp=pokemon["ataque"]
		vp=pokemon["vida"]
		dp=pokemon["defesa"]
		vida_max=vp


elif res==2:
	res=input("Qual o nome do arquivo? ")
	res=res+".json"
	with open(res) as arquivo:
		progresso = json.load(arquivo)
	pokemon=progresso["pokemon_jogador"]
	exp=progresso["xp_jogador"]
	suapokedex=progresso["insperdex"]
	np=pokemon["nome"]
	pp=pokemon["ataque"]
	vp=pokemon["vida"]
	dp=pokemon["defesa"]
	vida_max=pokemon["vidamax"]
	
while True:
	print(" ")
	print("O seu pokemon é {0}, vida: {1}, ataque: {2}, defesa: {3}.".format(np,vp,pp,dp))
	print("Sua experiência é igual a {0}".format(exp))
	print("""
	1 - Passear
	2 - Dormir
	3 - Enfermaria
	4 - Academia
	5 - Ver minha pokedex
	""")
	pergunta=int(input("Escolha o que você quer fazer: "))
	print("  ")
	if pergunta==2:
		print("""
	1 - Sim
	2 - Não
	3 - Voltar ao jogo
		""")
		res=int(input("Deseja salvar? "))
		if res==2:
			print("Ok, até a próxima!")
			break
		elif res==1:
			status=dict(nome=np, ataque=pp, vida=vp, defesa=dp, vidamax=vida_max)
			progresso=dict(pokemon_jogador=status, xp_jogador=exp, insperdex=suapokedex)
			progresso=json.dumps(progresso, indent=4, sort_keys=False)
			sal=input("Qual o nome do arquivo? ")
			sal=sal+".json"
			arquivo = open(sal,"w")
			arquivo.write(progresso)
			arquivo.close()
			print("Jogo salvo, volte logo!")
			break
		elif res==3:
			pass
	elif pergunta==1:
		import random as randint
		print("Você encontrou um oponente!")
		x = randint.choice(pokedex)
		suapokedex.append(x)
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
			print("""
	1 - atacar
	2 - tentar fugir
	3 - simular batalha
			""")
			acao=int(input("O que deseja fazer? "))
			if acao == 1:
				a=random.randint(60,140)/100
				b=random.randint(60,140)/100
				e=random.randint(80,145)/100
				c=random.randint(80,145)/100
				seuataque=int((pp*a-d*e))
				if seuataque<0:
					seuataque=0
				v=v-seuataque
				if v<=0:
					v=0
					break
				opoataque=int((p*b-dp*c))	
				if opoataque<0:
					opoataque=0	
				vp=vp-opoataque
				if vp<=0:
					vp=0
					break
			elif acao == 2:
				from random import randint
				a=randint(0,99)
				if a < 39:
					print("Você conseguiu fugir!")
					break
				else:
					print("Você não conseguiu fugir")
					b=random.randint(60,140)/100
					c=random.randint(80,145)/100
					opoataque=int((p*b-dp*c))	
					if opoataque<0:
						opoataque=0
					vp=vp-opoataque
					if vp<=0:
						vp=0
						break
			elif acao ==3:
				res=int(input("Parar de simular quando atingir nivel de vida for inferior a: "))
				while vp > 0 and v > 0:
					a=random.randint(60,140)/100
					b=random.randint(60,140)/100
					e=random.randint(80,145)/100
					c=random.randint(80,145)/100
					seuataque=int((pp*a-d*e))
					if seuataque<0:
						seuataque=0
					v=v-seuataque
					if v<=0:
						v=0
						break
					opoataque=int((p*b-dp*c))	
					if opoataque<0:
						opoataque=0	
					vp=vp-opoataque
					if vp<=res:
						if vp<=0:
							vp=0
						break

		if vp==0:
			print(""" 
			Seu pokemon morreu.
			Game over!
			
			1 - Ver pokedex
			2 - Fim de jogo""")
			res=int(input("O que fazer? "))
			print(" ")
			if res==1:
				print("Pokemons encontrados: ")
				for i in range (len(suapokedex)):
					print(suapokedex[i])
			elif res==2:
				print("Até a próxima!")
				pass
			break
		elif v==0:
			ra=random.randint(70,160)/100
			ran=random.randint(10,50)/100
			a=int(xp*ra+vp*ran)
			exp=exp+a
			print(" ")
			print("Parabéns, você ganhou a luta! ")
			print("Adquiriu {0} de experiência!".format(a))
			
	elif pergunta==3:
		print("""
	Bem vindo a enfermaria.
	Recuperar sua vida custa 30 pontos de experiência.
	1 - Curar
	2 - Sair
	""")
		res=int(input("O que quer fazer: "))
		if res==1:
			if exp>=30:
				vp=vida_max
				exp=exp-30
				print("Vida restaurada.")
			else:
				print("Você não tem experiencia suficiente.")
		print("Boa sorte lá fora!")

	elif pergunta==4:
		while True:
			print("""
			Bem vindo a academia, aqui você pode melhorar seu pokemon.
			1 - Melhorar ataque (50 pontos de exp)
			2 - Melhorar defesa (50 pontos de exp)
			3 - Melhorar vida (70 pontos de exp)
			4 - Sair
			""")
			resp=int(input("O que deseja fazer? "))
			print(" ")
			if resp==1:
				if exp>=50:
					t=random.randint(1,3)
					exp=exp-50
					pp=pp+t
					print("Seu novo ataque é {0}".format(pp))
					print("Sua experiência é igual a {0}".format(exp))
				else:
					print("Você não tem experiencia suficiente.")
			if resp==2:
				if exp>=50:
					r=random.randint(1,3)
					exp=exp-50
					dp=dp+r
					print("Sua nova defesa é {0}".format(dp))
					print("Sua experiência é igual a {0}".format(exp))
				else:
					print("Você não tem experiencia suficiente.")	
			if resp==3:
				if exp>=70:
					exp=exp-70
					a=random.randint(20,35)
					vida_max=vida_max+a
					vp=vp+a
					print("Sua nova vida é {0} e sua vida máxima é {1}.".format(vp,vida_max))
					print("Sua experiência é igual a {0}".format(exp))				
				else:
					print("Você não tem experiencia suficiente.")				
			if resp==4:
				print("Boa luta!")
				break	

	elif pergunta==5:
		print("Pokemons encontrados: ")
		for i in range (len(suapokedex)):
			print(suapokedex[i])	