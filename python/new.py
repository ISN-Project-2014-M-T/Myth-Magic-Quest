a="Vous arrivez devant une rivière, elle vous semble peu profonde mais l'eau est trouble et vous empêche de voir. Une forêt se trouve a proximité et pourrait mener à un autre chemin. Il a aussi un pont a coté de vous mais les planches semblent pourries."
r=0
b="    Q)Vous traversez à la nage"
c="    Z)Vous traversez le pont"
d="    D)Vous préférez touver un autre chemin en passant par la forêt"
bf="une sangsue cous attrape la jambe et vous ruez sur le bord pour l'arracher (-20pv)"
cf="Vous continuez"
df="Vous vous perdez pendant 2 jours, vous êtes mort de faim (-10pv)"
print(a)
print(b)
print(c)
print(d)
r=input()
while r!='q' or r!='z' or r!='d':
    r=input()

if r==q:
    print(bf)
if r==z:
    print(cf)
if r==d:
    print(df)
