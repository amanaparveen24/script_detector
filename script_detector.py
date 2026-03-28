def detect_script(text):
    malayalam_count = 0
    arabic_count = 0

    for char in text:
        if '\u0D00' <= char <= '\u0D7F':
            malayalam_count += 1
        elif '\u0600' <= char <= '\u06FF':
            arabic_count += 1

    if malayalam_count >0 and arabic_count >0:
        print('Mixed Script')
    elif malayalam_count > 0 and arabic_count == 0:
        print('Malayalam Script')
    elif arabic_count > 0 and malayalam_count == 0:
        print('Arabic Script')
    else:
        print('Unknown Script')

with open("sample.txt","r",encoding="utf-8") as file:
    text = file.read()

detect_script(text)
