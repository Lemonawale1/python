
class CountString:
    def countst(self):
        userin=input("Enter String:")
        check=input("Enter last string counted: ")

        result = userin.count(check)

        print(result)

if __name__ == "__main__":
    test = CountString()
    test.countst()