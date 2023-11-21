def findParagraphsByTag(file_path):
    tag = input('Введіть тег: ')
    with open(file_path, 'r') as file:
        currentParagraph = ''

        for line in file:
            
            if line.strip() == '':
                if f'#{tag}' in currentParagraph:
                    print(currentParagraph)
                currentParagraph = ''
            else:
                currentParagraph += line
                
        if f'#{tag}' in currentParagraph:
            print(currentParagraph)

findParagraphsByTag('text.txt')
