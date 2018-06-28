
def clear_punctuation(string):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	cleared = ""
	for char in string:
		if char not in punctuations:
			cleared += char
	return cleared
	
	
def count(string):
	### Assert whether the given output is a string object:
    try:
        assert(type(string) == str)
    except Exception:
        print("Assertion Error.\nGiven input is not a string object. ABORT.")
        return
    #
    string = clear_punctuation(string).lower().split()
    freq_list = {}
    for word in string:
        if word in freq_list:
            freq_list[word] += 1
        else:
            freq_list[word] = 1
    return freq_list


string = "Başkanım partime sataşma var cevap vermek istiyorum. Sayın İnce bakar mısınız?"
number = 23
print(count(string)) # Will do the job just fine.
print(count(number)) # Will catch the exception and return 'None'
