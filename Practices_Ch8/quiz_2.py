def word_length(sentence):
    sentence_array=sentence.split(" ")
    num_words=len(sentence_array)
    sum=0
    for i in sentence_array:
        length_word=len(i)
        sum += length_word
    return(sum/num_words)

def main():
    user_sentence=input("What is the sentence?")
    print(word_length(user_sentence))
main()

