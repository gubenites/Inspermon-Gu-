while True:
	escolha = input("Escolha um dos pokemons iniciais. ")
	




	pergunta=input("Escolha se quer passear ou se quer dormir. ")
	if pergunta="dormir":
		break
	elif pergunta="passear":
		x = random.choice(pokedex)
		print(x)		
		p=x["poder"]
		v=x["vida"]
		d=x["defesa"]
		batalha(p,v,d)
		if v1=0:
			print("Você perdeu. ")
			break
		elif v1!=0:
			print("Parabens! ")
