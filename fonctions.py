## on definit notre fonction nommé salutation() sans parametre
def salutations():
    # ici on dit le resultat que cela doit nous retourner
    return("coucou")


## appel de la focntion avec la variable message
message =  salutations()
## on affiche
print(message)

## on definit la fonction name() avec un parametre nom
def name(nom):
    # a cause du paramettre le return on ajoute f"{parametre}"
    return f"C est quoi votre nom: {nom}"
## on appelle la fonction avec la variable message, mais comme notre fonction defini
## plus haut on un parametre à l'interrier alors dans notre
## variable message on entrera aussi la valeur du parametre
## donc fonction -> name(nom)
### message appel -> messge = name("Alexis") si on ne met pas de valeur on aura un message erreur
## donc fonction name() -> sans paramettre -> return " " ==> message appel message = name()
## fonction name(nom) -> avec parametre --> return f"{parametre}" ==> message = name("Valeur")
message = name("Alexis")
print(message)




def somme():
    return "resultat"

message = somme()
print(message)

## fonction pour additionner x+Y 
def add(x, Y):
    return f"le resultat est: {x+Y}"

valeur = add(5, 7)
print(valeur)

## 
def calcul(x, y, z):
    return f" le produit et la somme donne: {x*(y*z)+(x+y+z)}"
resulat = calcul(10, 2, 5)
print(resulat)



### fonction avec 2 parametres où un est a une valeur attribué
#On definit la fonction avec un parametre nom='name'
def identifiant(prenom, nom='Sam'):
    ## on retourne le prenom et le nom (qui est sam)
    return f" Mes idesntifiants sont: {prenom}, et mon nom est: {nom}"
## on declare la variable message pour appeler la fonction definie 
## Comme on a deja un parametre qui a été définie dans la definition de la fonction alors on ne va plus donner 
## une valeur à nom car nom à deja une valeur qui " Sam"
message = identifiant("Dave")
print(message)


## 2 eme cas avec le if
def vetement(short, pantalon='jean'):
    if pantalon == 'jean':
        return f" J'ai un {short}, et un pantalon: {pantalon}"
    else:
        return f"J'ai un culotte: {short}, et un pantalon: {pantalon}"
    
 ## Comme on un if et else et 2 return alors on doit avoir deux messages
 # ## d ou message1 pour le if et message2 pur le else   
message1 = vetement('culotte')
print(message1)

message2 = vetement('calecon', 'jogging')
print(message2)




def name(prenom='dave'):
    return f" mon prenom est: {prenom}"
message = name('Luis')
print(message)



