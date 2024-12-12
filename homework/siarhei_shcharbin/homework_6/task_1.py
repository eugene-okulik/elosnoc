input_phrase = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
                'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
output_phrase = []
for word in input_phrase.split(' '):
    if word[-1] == ',':
        word = word.replace(',', 'ing,')
        output_phrase.append(word)
    elif word[-1] == '.':
        word = word.replace('.', 'ing.')
        output_phrase.append(word)
    else:
        word = word + 'ing'
        output_phrase.append(word)
print(' '.join(output_phrase))
