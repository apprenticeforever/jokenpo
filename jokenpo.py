import jokenpo_config as joken
import detalhes as det

meu_github = 'github.com/apprenticeforever'
print(f"Bem-vindo ao Jokenpo!\nFeito por: {meu_github}")

while True:
	escolha = input("\nDigite 'c' para continuar, 'd' para detalhes sobre o jogo,"
		+ " ou, digite qualquer tecla para sair: ")

	if escolha.lower() == 'c':
		joken.iniciar_jogo()
		break
	elif escolha.lower() == 'd':
		det.show()
		pass
	elif escolha.lower() != 'c' or escolha.lower != 'd':
		print("\nUma pena não podermos jogar agora! :(\n")
		break
	else:
		pass
