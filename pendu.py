shots = 8
word_is_not_found = 1
loop = 1

print("Bonjour et bienvenue dans le jeu du pendu")
player_name = str(input("saisissez votre nom : "))
register_player_name(player_name)
print("C'est parti ! Vous avez 8 chances pour deviner le mot mystère.")
secret_word = choose_word()
hidden_word = make_hidden_word(secret_word)

while(loop)
	while shots > 0 and word_is_not_found:
		print(hidden_word)
		letter = input("Proposez une lettre qui pourrait être contenu dans le mot mystère")
		
		if letter_is_in_word(secret_word, letter) :
			hidden_word = make_hidden_word(secret_word, letter)
			word_is_not_found = word_is_not_found(hidden_word)
		else :
			shots -= 1

	if word_is_not_found :
		print("Désolé vous avez perdu ! Votre score reste inchangé.")
	else :
		recording_player_score(player_name)
		print("Bravo ! Vous avez gagnez")
		print("Votre score est maintenant de " + player_score_reading(player_name))

	answer_to_continue = str(input("Voulez-vous rejouer ? (Taper \"oui\" ou \"non\")"))

	if answer_to_continue == "oui" :
		word_is_not_found = 1
		shots = 8
		secret_word = choose_word()
		hidden_word = make_hidden_word(secret_word)
	elif answer_to_continue == "non" :
		print("Au revoir !")
		loop = 0
