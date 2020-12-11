tabla=[
    {"categoria":"accion",
    "juegos":["GTA","COD","PUBG"]},
    {"categoria":"aventura",
    "juegos":["ASASSINS","CRASH","PRINCE_OF_PERSIA"]},
    {"categoria":"deportes",
    "juegos":["FIFA 21", "PRO 21", "MOTO GP 21"]}
]
for categoria in tabla:
    print(f"----{categoria['categoria']}----")
    for juegos in categoria['juegos']:
        print(juegos)