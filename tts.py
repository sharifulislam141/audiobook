import pyttsx3
txt = input("Enter amy world:")
book = open('book.txt','w')
book.write(txt)
book.close()
book = open(r'book.txt')
bookt = book.readlines()
engine = pyttsx3.init()
for i in bookt:
    engine.say(i)
    engine.runAndWait()