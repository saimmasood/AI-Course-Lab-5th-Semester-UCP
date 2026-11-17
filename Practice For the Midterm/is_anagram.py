def is_anagram(word1,word2):

    w1=word1.upper()
    w2=word2.upper()

    anagram=False
    for i in range(0,len(w1)):
        if w1[i] == ' ':
            continue

        if w1[i] in w2 and w1.count(w1[i])==w2.count(w1[i]):
            anagram=True
        else:
            anagram=False
            break

    for i in range(0,len(w2)):
        if w2[i] == ' ':
            continue

        if w2[i] in w1 and w2.count(w2[i])==w1.count(w2[i]):
            anagram=True
        else:
            anagram=False
            break

    return anagram


print("Enter a two words to check if they are anagram or not:\n" )
w1=input("Enter the word 1: ")
w2=input("Enter the word 2: ")

result=is_anagram(w1,w2)

if(result==1):
    print("Yes words are anagram: ",w1,w2)
else:
    print("No words are not anagram: ",w1,w2)

