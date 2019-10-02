import wikipedia


def between(num, min, max):
    return min - 1 < num < max + 1


def add_breakline(text):
    lista = []
    for letra in text:
        lista.append(letra)
    for c in range(len(lista)):
        if c % 48 == 0 and c is not 0:
            for j in range(c, 0, -1):
                if lista[j] == ' ':
                    lista.insert(j, '\n')
                    break

    return ''.join(lista)


def text_wiki(term, complement=''):
    complement = ' ' + complement if complement != '' else complement
    info = wikipedia.summary(term + complement)
    info = info.split('.')

    for element in info:
        if element == '':
            info.remove(element)  # Isso foi porque algumas vezes aparecia uma string vazia no final ;-;

    for c in range(len(info)):
        info[c] = info[c] + '.'

    for c in range(len(info[0:8])):
        info[c] = add_breakline(info[c])
    if len(info) <= 5:
        raise Exception
    elif between(len(info), 6, 8):
        return info[0: len(info) - 1]
    elif len(info) > 8:
        return info[0:8]
    raise Exception(f'Foram encontrados somente {len(info)} paragrafos sobre: {term}')
    
    
    
    
    
    
    
    
