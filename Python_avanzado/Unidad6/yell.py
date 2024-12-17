#Programa para demostrar el uso de map

def main():
    yell("This", "is", "C550")
    
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
   #uppercased = []
    '''for word in words:
        uppercased.append(word.upper())'''
    
    
if __name__ == "__main__":
    main()