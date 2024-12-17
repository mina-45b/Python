#Version mejorada del programa yell usando compresión de listas

def main():
    yell("This", "is", "C550")
    

    
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

    
    
if __name__ == "__main__":
    main()