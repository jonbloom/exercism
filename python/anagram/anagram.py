from itertools import permutations

def detect_anagrams(original_word,words_to_check):
	detected_anagrams = []
	anagrams = permutations(original_word)
	for word in words_to_check:
		if word != original_word and word in anagrams:
			detected_anagrams.append(word)
	return detected_anagrams