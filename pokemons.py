from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class pokemon(BaseModel):
    id: int
    nombre: str
    vida: int =100
    ataque: int
    vivo: bool = True
    tipo: str


p1 = pokemon(id=1, nombre="Bulbasaur", vida=100, ataque=15, vivo=True, tipo="Fuego")
p2 = pokemon(id=25, nombre="Pikachu", vida=100, ataque=16, vivo=True, tipo="Electrico")
p3 = pokemon(id=50, nombre="Cubone", vida=100, ataque=17, vivo=True, tipo="Animal")
p4 = pokemon(id=4, nombre="Charmander", vida=100, ataque=18, vivo=True, tipo="Agua")
p5 = pokemon(id=7, nombre="Squirtle", vida=100, ataque=14, vivo=True, tipo="Volador")
p6 = pokemon(id=39, nombre="Jigglypuff", vida=100, ataque=13, vivo=True, tipo="Agua")
p7 = pokemon(id=52, nombre="Meowth", vida=100, ataque=12, vivo=True, tipo="Electrico")
p8 = pokemon(id=133, nombre="Eevee", vida=100, ataque=16, vivo=True, tipo=" Animal")
p9 = pokemon(id=92, nombre="Gastly", vida=100, ataque=15, vivo=True, tipo="Volador")
p10 = pokemon(id=143, nombre="Snorlax", vida=120, ataque=20, vivo=True, tipo="Fuego")
p11 = pokemon(id=11, nombre="Caterpie", vida=90, ataque=10, vivo=True, tipo="Animal")
p12 = pokemon(id=12, nombre="Butterfree", vida=95, ataque=14, vivo=True, tipo="Volador")
p13 = pokemon(id=13, nombre="Weedle", vida=85, ataque=11, vivo=True, tipo="Animal")
p14 = pokemon(id=14, nombre="Kakuna", vida=90, ataque=9, vivo=True, tipo="Animal")
p15 = pokemon(id=15, nombre="Beedrill", vida=100, ataque=17, vivo=True, tipo="Volador")
p16 = pokemon(id=16, nombre="Pidgey", vida=90, ataque=12, vivo=True, tipo="Volador")
p17 = pokemon(id=17, nombre="Pidgeotto", vida=100, ataque=15, vivo=True, tipo="Volador")
p18 = pokemon(id=18, nombre="Pidgeot", vida=110, ataque=18, vivo=True, tipo="Volador")
p19 = pokemon(id=19, nombre="Rattata", vida=85, ataque=13, vivo=True, tipo="Animal")
p20 = pokemon(id=20, nombre="Raticate", vida=95, ataque=16, vivo=True, tipo="Animal")

p21 = pokemon(id=21, nombre="Spearow", vida=90, ataque=14, vivo=True, tipo="Volador")
p22 = pokemon(id=22, nombre="Fearow", vida=105, ataque=18, vivo=True, tipo="Volador")
p23 = pokemon(id=23, nombre="Ekans", vida=95, ataque=14, vivo=True, tipo="Animal")
p24 = pokemon(id=24, nombre="Arbok", vida=110, ataque=17, vivo=True, tipo="Animal")
p25 = pokemon(id=26, nombre="Raichu", vida=110, ataque=19, vivo=True, tipo="Electrico")
p26 = pokemon(id=27, nombre="Sandshrew", vida=100, ataque=15, vivo=True, tipo="Animal")
p27 = pokemon(id=28, nombre="Sandslash", vida=115, ataque=18, vivo=True, tipo="Animal")
p28 = pokemon(id=29, nombre="NidoranF", vida=95, ataque=14, vivo=True, tipo="Animal")
p29 = pokemon(id=30, nombre="Nidorina", vida=105, ataque=16, vivo=True, tipo="Animal")
p30 = pokemon(id=31, nombre="Nidoqueen", vida=120, ataque=20, vivo=True, tipo="Animal")

p31 = pokemon(id=32, nombre="NidoranM", vida=95, ataque=14, vivo=True, tipo="Animal")
p32 = pokemon(id=33, nombre="Nidorino", vida=105, ataque=16, vivo=True, tipo="Animal")
p33 = pokemon(id=34, nombre="Nidoking", vida=120, ataque=21, vivo=True, tipo="Animal")
p34 = pokemon(id=35, nombre="Clefairy", vida=100, ataque=13, vivo=True, tipo="Volador")
p35 = pokemon(id=36, nombre="Clefable", vida=110, ataque=16, vivo=True, tipo="Volador")
p36 = pokemon(id=37, nombre="Vulpix", vida=100, ataque=15, vivo=True, tipo="Fuego")
p37 = pokemon(id=38, nombre="Ninetales", vida=115, ataque=19, vivo=True, tipo="Fuego")
p38 = pokemon(id=40, nombre="Wigglytuff", vida=120, ataque=17, vivo=True, tipo="Volador")
p39 = pokemon(id=41, nombre="Zubat", vida=90, ataque=13, vivo=True, tipo="Volador")
p40 = pokemon(id=42, nombre="Golbat", vida=110, ataque=17, vivo=True, tipo="Volador")

p41 = pokemon(id=43, nombre="Oddish", vida=95, ataque=12, vivo=True, tipo="Animal")
p42 = pokemon(id=44, nombre="Gloom", vida=105, ataque=15, vivo=True, tipo="Animal")
p43 = pokemon(id=45, nombre="Vileplume", vida=115, ataque=18, vivo=True, tipo="Animal")
p44 = pokemon(id=46, nombre="Paras", vida=90, ataque=13, vivo=True, tipo="Animal")
p45 = pokemon(id=47, nombre="Parasect", vida=110, ataque=17, vivo=True, tipo="Animal")
p46 = pokemon(id=48, nombre="Venonat", vida=100, ataque=14, vivo=True, tipo="Animal")
p47 = pokemon(id=49, nombre="Venomoth", vida=110, ataque=17, vivo=True, tipo="Volador")
p48 = pokemon(id=51, nombre="Dugtrio", vida=110, ataque=18, vivo=True, tipo="Animal")
p49 = pokemon(id=53, nombre="Persian", vida=110, ataque=18, vivo=True, tipo="Animal")
p50 = pokemon(id=54, nombre="Psyduck", vida=100, ataque=15, vivo=True, tipo="Agua")

new_pokemon:list[pokemon]=[
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,
p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,
p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,
p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,
p41,p42,p43,p44,p45,p46,p47,p48,p49,p50]

@app.get("/pokemon")
def show_pokemon(skip: int= 0, limit:int=3):
    return new_pokemon[skip:skip+limit]

pokemon_db = [{"name":"Bulbasaur"},{"name":"Cubone"},{"name":"Pikachu"},{"name":"Gengar"}]

@app.get("/allPokemon")
def show_all_pokemon():
    return new_pokemon


@app.get("/onepokemon")
def show_one_pokemon(pos:int=0):
    for pokemon in new_pokemon:
        if (pokemon.id ==pos):
            return new_pokemon[pos]
    else:
        return {"Pokemon no enctontrado"}
    

@app.get("/PokemonID/{id}")
def pokemon_ID(id: int):
    for poke in new_pokemon:
        if poke.id == id:
            return poke
    return {"Pokemon no encontrado"}


#HOLAAA
    
    