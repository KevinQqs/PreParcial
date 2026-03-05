from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class pokemon(BaseModel):
    id: int
    nombre: str
    vida: int =100
    ataque: int
    vivo: bool = True


p1 = pokemon(id=1, nombre="Bulbasaur", vida=100, ataque=15, vivo=True)
p2 = pokemon(id=25, nombre="Pikachu", vida=100, ataque=16, vivo=True)
p3 = pokemon(id=50, nombre="Cubone", vida=100, ataque=17, vivo=True)
p4 = pokemon(id=4, nombre="Charmander", vida=100, ataque=18, vivo=True)
p5 = pokemon(id=7, nombre="Squirtle", vida=100, ataque=14, vivo=True)
p6 = pokemon(id=39, nombre="Jigglypuff", vida=100, ataque=13, vivo=True)
p7 = pokemon(id=52, nombre="Meowth", vida=100, ataque=12, vivo=True)
p8 = pokemon(id=133, nombre="Eevee", vida=100, ataque=16, vivo=True)
p9 = pokemon(id=92, nombre="Gastly", vida=100, ataque=15, vivo=True)
p10 = pokemon(id=143, nombre="Snorlax", vida=120, ataque=20, vivo=True)

new_pokemon:list[pokemon]=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]


@app.get("/hola")
def hello():
    return{"Hola desde FastAPI"}

@app.get("/kevin")
def kevin():
    return {"Kevin esta aqui"}

@app.get("/suma/{a}/{b}")
def sumar(a,b):
    res = int (a) + int(b)
    return {"La suma da ": res}


@app.get("/reto/{a}/{n}")
def reto(a,n):
    nombre = n
    s = 2026 - int(a) 
    return {"Tu ": nombre ,"Tu edad es ": s}


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