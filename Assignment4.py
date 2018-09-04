
class Addition:
    def additionLast(self):
        x = [(10,20,40),(40,50,60),(70,80,90)]
        print("Input: ",x)
        print("output:",[t[:-1] + (100,) for t in x])

if __name__=="__main__":
    test = Addition()
    test.additionLast()