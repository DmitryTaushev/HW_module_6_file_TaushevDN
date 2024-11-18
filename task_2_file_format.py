

list_text = ['Если б мишки были пчелами,','То они бы нипочем,','Никогда и не подумали,','Так высоко строить дом.']
def write_text(filename):
    with open(f'{filename}.txt','w',encoding = 'utf-8') as text:
        count = 0
        for i in list_text:
            text.write(f'{list_text[count]}\n')
            count += 1

filename = 'HW_text'

write_text(filename)

def read_text(filename):
    with open(f'{filename}.txt','r',encoding = 'utf-8') as text:
        content = text.read()
        print(content)
read_text(filename)
