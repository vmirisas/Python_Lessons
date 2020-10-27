def favorite_author(author):
    if "Tolkien" in str(author):
        for i in range(500):
            print(f"{i}: Tolkien is the best")
    else:
        print(f"{author} is good")


favorite_author("Tolkien")
favorite_author("Lena Manda")
