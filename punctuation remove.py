punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(text):
    return ''.join(char for char in text if char not in punctuations)

sample = "Hello, sohail kas'a ho! bha'i?"
result = remove_punctuation(sample)
print(result)

