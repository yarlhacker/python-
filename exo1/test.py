# liste = range(700,1099)

# # for i in liste:
# #     if i%7 == 0:
# #         print(i)

# z = [ i for i in liste if i%7 == 0 and i%5 !=0 and i%2 !=0]
# print(z)
    

    # EXO 2

# stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra",310.28,"Haut-parleurs", 27.00,"Télévision", 1000,"Cartes mères","souris","clavier",500,"barrettes de mémoire"]

# s = [ [i for i in stock if type(i) ==str] , [i for i in stock if type(i) != str]]
# print(s)

#   EXO3

# moyennes=[14.84,14.14,16.22,86,85,85,14.84,13,15.85,9.99,12.04,15.03,16.22,12,84,10.20,11.03,11.03]
# moyennes_tri=sorted(moyennes)
# print(f'les moyennes de la classe sont : {moyennes_tri}')
# print(f'les trois mauvaise moyennes sont : {moyennes_tri[:3]}')
# print(f'les trois bonnes moyennes sont : {moyennes_tri[-3:]}')

#m = 'bonjour'

# for i in range(len(m)) :
#     if m[i]=='o':
#         print(i)
#l = [ i for i in range(len(m)) if m[i]=='o']


# notes = [12 , 4 , 14 , 11 ,  18 , 13 ,  7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
# liste = [ note for note in notes if note >= 10]
# print(liste)

def Chaine(s):
    up = 0
    low = 0
    for i in s:
        if i in s.upper():
            up+=1
        else:
            low+=1
    print(f"le nombre de majuscule dans s est : {up} ")
    print(f"le nombre de muniscule dans s est : {low} ")
(Chaine('Ismael Tu Es Le Meilleur '))

#     # l = []
#     # for i in chaine:
#     #     e =i+n
#     #     l.append(e)
#     # ln = "".join(l)
#     # print(ln)
#     z = [i+n for i in chaine]
#     new_z =''.join(z)
#     print(new_z)

# InsertEtoile('ismael','*')
