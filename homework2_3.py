import json
import chardet
from pprint import pprint

def oepn_read(filename):
	"""Открывает фаил и считывает его, аргумент - (имя фаила)."""
	with open(filename, 'rb') as file:
		data = file.read()
		result = json.loads(data.decode(chardet.detect(data)['encoding']))
	return result

def take_description(dictionery):
	"""
	Достает из словаря значение 'description', 'title' 
	и возвращаем список слов, аргумент - (исходный словарь)
	"""
	words = str()
	for value in dictionery['rss']['channel']['items']:
		words =  words + ' ' + value['description'].strip() + ' ' + value['title'].strip()
	words = words.split()
	return words

def six_letter(list_word):
	"""Определяет слова длинее 6 символов, аргумент - (список слов)"""
	list_word_six_letter = []
	for index, value in enumerate(list_word):
		if len(value) >= 6:
			list_word_six_letter.append(value)
	return list_word_six_letter

def dictionery_word(list_word):
	"""Возврящает словарь слов(слово : повторений), аргумен - (список слов)"""
	sorting_word = {}
	for index, value in enumerate(list_word):
		if sorting_word.get(value) == None:
			sorting_word[value] = 1
		else:
			sorting_word[value] = sorting_word[value] + 1
	return sorting_word

def sorting(value):
	"""Функция сортировки по значениям словаря для метода .sort()"""
	return value[1]

def sorting_dictionery_word(dictionery):
	"""Возвращает список ТОП-10 слов из словаря слов(слово : повторений), аргумент - (словарь слов)"""
	dictionery = list(dictionery.items())
	dictionery.sort(key = sorting)
	
	#pprint(dictionery) # Отладочный принт

	word = []
	for value in reversed(dictionery):
		if len(word) <10:
			word.append(value[0])
	return word


def main():
	file = input('Укажите имя фаила с расширением: ')
	list_word = sorting_dictionery_word(dictionery_word(six_letter(take_description(oepn_read(file)))))
	print('ТОП-10 слов встречающихся в новостях:')
	print('\n'.join(list_word))

main()