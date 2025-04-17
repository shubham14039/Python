
def repeated_concatenation(document):
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    return letters

def appending_temp_list(document):
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    return ' '.join(temp)

def list_comp(document):
    letters = ''.join([c for c in document if c.isalpha()])
    return letters

def gen_comp(document):
    letters = ''.join(c for c in document if c.isalpha())
    return list(letters)
