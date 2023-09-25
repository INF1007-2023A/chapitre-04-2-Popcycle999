#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	return name.split('-')[0].lower().capitalize()

def get_random_sentence(animals, adjectives, fruits):
	return [random.choice(animals), random.choice(adjectives), random.choice(fruits)]

def encrypt(text, shift):
	text_1 = text[:-shift]
	text_1 = text[len(text) - shift:] + text_1

	return text_1

def decrypt(encrypted_text, shift):
	txt = encrypted_text[shift:]
	txt = txt + encrypted_text[:shift]

	return txt


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
