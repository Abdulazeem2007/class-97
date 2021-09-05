Intro = input("Enter Your Introduction: ")
print(Intro)

WordCount = 1
CharacterCount = 0

for i in Intro:
    CharacterCount= CharacterCount+1
    if(i == ' '):
        WordCount = WordCount+1
print(WordCount)
print(CharacterCount)