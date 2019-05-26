import pickle
import random

def choose_word():
	print('recherche d\'un mot...')
	with open('data', 'rb') as file:
		my_depickler = pickle.Unpickler(file)
		words = my_depickler.load()
		word = random.choice(words)
		if len(word) <= 8:
			return word
		else:
			print('Mot ne corespondant pas au critère')
			file.close()
			print('Recherche d\'un nouveau mot...')
			return choose_word()

def init_hidden_word(secret_word):
	i = 0
	hidden_word = ''
	while i < len(secret_word):
		i += 1
		hidden_word += '*'
	return hidden_word

def make_hidden_word(secret_word, letter, hidden_word):
	i = 0
	hidden_word_bis = ''
	for letter_word in secret_word:
		if letter_word == letter :
			hidden_word_bis = hidden_word_bis + letter
		elif hidden_word[i] ==  '*': 
			hidden_word_bis = hidden_word_bis + '*'
		else:
			hidden_word_bis = hidden_word_bis + hidden_word[i]
		i += 1

	hidden_word = hidden_word_bis
	print('le mot')
	print(hidden_word_bis)
	return hidden_word

def letter_is_in_word(secret_word, letter):
	if letter in secret_word:
		return 1
	return 0

def word_not_found(hidden_word) :
	if '*' in hidden_word:
		return 1
	return 0

def recording_player_score(player_name, points) :
	with open('score', 'rb') as file:
		my_depickler = pickle.Unpickler(file)
		try:
			score = my_depickler.load()
			if score.get(player_name) == None:
				score[player_name] = points
			else:
				value = score.get(player_name)
				score[player_name] = value + points
		except EOFError as e:
			score = {player_name: points}

	with open('score', 'wb') as file:
		my_depickler = pickle.Pickler(file)
		my_depickler.dump(score)

def reading_player_score(player_name) :
	with open('score', 'rb') as file:
		my_depickler = pickle.Unpickler(file)
		try:
			score = my_depickler.load()
		except EOFError as e:
			return 0
		
		return score.get(player_name)	
		
def reading_scores() :
	print("LES SCORES : ")
	with open('score', 'rb') as file:
		my_depickler = pickle.Unpickler(file)
		try:
			return my_depickler.load()
		except Exception as e:
			return 'Pas de score pour le moment'




