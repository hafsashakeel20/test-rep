#2
def occr():
    print("")
    sent = "The quick brown fox jumps over the lazy dog on a cool evening"
    print(sent)
    sent_list= list(sent)
    #print(sent_list)
    vowel_list=['a','e','i','o','u']
    vowel_count=0
    const_count=0
    for i in sent_list:
        if i in vowel_list:
            vowel_count+=1
        else:
            const_count+=1
    print("number of vowels in the sentence = ", vowel_count)
    print("number of consonants in the sentence = ",const_count)
occr()