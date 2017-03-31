from funcao_batalha import batalha
from dicionario import pokedex

while True:
	print("Charmander")
	print("Bulbassauro")
	print("Squirtle")
	escolha = input("Escolha um dos pokemons iniciais. ")
	pokemon=pokedex[escolha]
	pp=pokemon["poder"]
	vp=pokemon["vida"]
	dp=pokemon["defesa"]
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
