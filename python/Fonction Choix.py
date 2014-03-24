Créer un Tableaux avec des choix qui réagit à des touches de clavier sur Python
-------------------------------------------------------------------------------
a="Vous arrivez devant une rivière, elle vous semble peu profonde mais l'eau est trouble et vous empêche de voir. Une forêt se trouve a proximité et pourrait mener à un autre chemin. Il a aussi un pont a coté de vous mais les planches semblent pourries."
b="    Q)Vous traversez à la nage"
c="    Z)Vous traversez le pont"
d="    D)Vous préférez touver un autre chemin en passant par la forêt"
bf="Une sangsue vous attrape la jambe et vous ruez sur le bord pour l'arracher (-20pv)"
cf="Vous continuez"
df="Vous vous perdez pendant 2 jours, vous êtes mort de faim (-10pv)"
print(a)
print(b)
print(c)
print(d)
r=input("Choisissez votre voie: ")
while r!='q' and r!='z' and r!='d':
    r=input("Cette voie n'exite pas: ")

if r=='q':
    print(bf)
elif r=='z':
    print(cf)
elif r=='d':
    print(df)

