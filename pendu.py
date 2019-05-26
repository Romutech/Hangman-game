import os
from fonctions import *

shots = 8
word_is_not_found = 1
loop = 1
lost = 0

print("Bonjour et bienvenue dans le jeu du pendu")
player_name = str(input("saisissez votre nom : "))
secret_word = choose_word()
hidden_word = init_hidden_word(secret_word)
print("C'est parti {} ! Vous avez {} chances pour deviner le mot mystère.".format(player_name, shots))

while(loop) :
	while shots > 0 and lost == 0:
		if shots < 8:
			print("Il vous reste {} chances pour deviner le mot mystère.".format(shots))

		print(hidden_word)
		letter = str(input("Proposez une lettre qui pourrait être contenu dans le mot mystère: "))
		
		if letter_is_in_word(secret_word, letter):
			print('Bravo la lettre est dans le mot')
			hidden_word = make_hidden_word(secret_word, letter, hidden_word)
			word_is_not_found = word_not_found(hidden_word)
		else :
			print('Désolé la lettre n\'est pas dans le mot')
			shots -= 1

		if word_is_not_found and shots == 0 :
			lost = 1
			print("Désolé vous avez perdu ! Votre score reste inchangé.")
			print('il est de {} points'.format(reading_player_score(player_name)))
		elif word_is_not_found == 0 and shots > 0:
			recording_player_score(player_name, shots)
			print("Bravo ! Vous avez gagnez")
			print("Votre score est maintenant de {} points".format(reading_player_score(player_name)))
			shots = 0

	answer_to_continue = str(input("Voulez-vous rejouer ? (Taper \"oui\" ou \"non\")"))

	if answer_to_continue == "oui" :
		word_is_not_found = 1
		shots = 8
		lost = 0
		secret_word = choose_word()
		hidden_word = init_hidden_word(secret_word)
	elif answer_to_continue == "non" :
		print("Au revoir !")
		loop = 0

	print(reading_scores())
