from random import randint

def iniciar_jogo():
	""" um jogo simples de jokenpo """
	rodadas_jogadas = 0
	pontos_jogador = 0
	pontos_bot = 0
	jogo_ativo = True
	numero_rodadas = 999999
	custom_rodadas = False

	jogador_1 = '\nVocê escolheu: Pedra,'
	jogador_2 = '\nVocê escolheu: Papel,'
	jogador_3 = '\nVocê escolheu: Tesoura,'
	pc_1 = 'e o computador escolheu: Pedra'
	pc_2 = 'e o computador escolheu: Papel'
	pc_3 = 'e o computador escolheu: Tesoura'
	perdeu = "Você perdeu a rodada!"
	ganhou = "Você ganhou a rodada!"

	nome_jogador = str(input("Escolha um nome para continuar: "))
	print (f"Bem-vindo vindo ao jogo, {nome_jogador}!\n")

	try: 
		escolha_rodadas = int(input("Escolha um número de rodadas, ou, digite qualquer tecla para um jogo contínuo: "))
		numero_rodadas = escolha_rodadas
		custom_rodadas = True
		print (f"Iniciando um jogo com total de {escolha_rodadas} rodadas!\n")
	except ValueError:
		pass
	
	while jogo_ativo == True and numero_rodadas > 0:
		jogada_pc = randint(1, 3)
		numero_rodadas -= 1
		try:
			r_jogada = int(input("\nEscolha uma opção:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n" +
				"Ou, digite qualquer tecla para encerrar o jogo!\n\n"))

			if r_jogada == 1 and jogada_pc == 1:
				rodadas_jogadas += 1
				print("\nEmpate!\nVocês escolheram a mesma opção: Pedra.")

			elif r_jogada == 2 and jogada_pc == 2:
				rodadas_jogadas += 1
				print("\nEmpate!\nVocês escolheram a mesma opção: Papel.")

			elif r_jogada == 3 and jogada_pc == 3:
				rodadas_jogadas += 1
				print("\nEmpate!\nVocês escolheram a mesma opção: Tesoura.")

			elif r_jogada == 1 and jogada_pc == 2:
				pontos_bot += 1
				rodadas_jogadas += 1
				print(jogador_1, pc_2)
				print(perdeu)

			elif r_jogada == 1 and jogada_pc == 3:
				pontos_jogador += 1
				rodadas_jogadas += 1
				print(jogador_1, pc_3)
				print(ganhou)

			elif r_jogada == 2 and jogada_pc == 1:
				pontos_jogador += 1
				rodadas_jogadas += 1
				print(jogador_2, pc_1)
				print(ganhou)

			elif r_jogada == 2 and jogada_pc == 3:
				pontos_bot += 1
				rodadas_jogadas += 1
				print(jogador_2, pc_3)
				print(perdeu)

			elif r_jogada == 3 and jogada_pc == 1:
				pontos_bot += 1
				rodadas_jogadas += 1
				print(jogador_3, pc_1)
				print(perdeu)

			elif r_jogada == 3 and jogada_pc == 2:
				pontos_jogador += 1
				rodadas_jogadas += 1
				print(jogador_3, pc_2)
				print(ganhou)

			elif r_jogada != 1 and r_jogada != 2 and r_jogada != 3:
				print("\nPor favor, escolha um número válido.")
				numero_rodadas += 1
				pass

			if custom_rodadas == True and numero_rodadas > 0:				
				print(f"Rodadas restantes: {numero_rodadas}")

		except ValueError:
			while True:
				resposta_final = input("Tem certeza que deseja sair? S/N \n")
				if resposta_final.lower() == 's':
					if pontos_jogador > pontos_bot:
						print(f"\n{nome_jogador}, você ganhou! :D" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
							f"Total de rodadas jogadas: {rodadas_jogadas}")
					if pontos_jogador < pontos_bot:
						print(f"\n{nome_jogador}, você perdeu para o bot! :(" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
							f"Total de rodadas jogadas: {rodadas_jogadas}")
					if pontos_jogador == pontos_bot:
						print(f"\n{nome_jogador}, você empatou com o bot!" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
							f"Total de rodadas jogadas: {rodadas_jogadas}")
					
					jogo_ativo = False
					break

				elif resposta_final.lower() == 'n':
					break

				else:
					print("Insira 'S' ou 'N': ")
					
		if numero_rodadas == 0:
			if pontos_jogador > pontos_bot:
				print(f"\n{nome_jogador}, você ganhou! :D" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
					f"Total de rodadas jogadas: {rodadas_jogadas}")
			if pontos_jogador < pontos_bot:
				print(f"\n{nome_jogador}, você perdeu para o bot! :(" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
					f"Total de rodadas jogadas: {rodadas_jogadas}")
			if pontos_jogador == pontos_bot:
				print(f"\n{nome_jogador}, você empatou com o bot!" + f"\nResultado: Você {pontos_jogador} x {pontos_bot} bot.\n" + 
					f"Total de rodadas jogadas: {rodadas_jogadas}")