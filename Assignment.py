class EvenNumber:
    def __init__(self):
        self.word=""
        self.output=""

    def indexcheck(self):
        self.word=input("Enter a string to be filtered: ")

        for i in self.word:
            if self.word.index(i)%2==0:
                self.output+=i

        return self.output

    def print_output(self):
        print("Answer:", self.output)

if __name__ =="__main__":
    test = EvenNumber()
    test.indexcheck()
    test.print_output()
0