class builder:
    def __init__(self,cores,mana_wheight=24,mana_division="E") -> None:

        # Bibliotecas ---
        
        self.json = __import__("json")

        # Base de dados ---
        
        self.CardsDb =DbSingleton()

        # Tabelas de conversão ---

        self.mana_conversion_table = {
            "B":["Swamp"],
            "U":["Island"],
            "W":["Plains"],
            "R":["Mountais"],
            "G":["Forest"]
        }

        
        # Variáveis iniciais ---
        self.cores = cores
        self.mana_curve_calc = lambda mana_wheight,cores:  {lane:int(abs(mana_wheight/len(cores))) for item in cores for lane in self.mana_conversion_table[item]} if mana_division == "E" else {lane:mana_division[cores.index(item)] for item in cores for lane in self.mana_conversion_table[item]}
        self.mana_curve = self.mana_curve_calc(mana_wheight,cores)
        
        self.deck ={}


# --- Classe e função responsável por instanciar a base de dados apenas uma vez ---

def genDatabase():
    import json

    with open("../cards_Database.json","r") as file:
        cards = json.load(file)

    with open("datassets/planeswalkers.json","r") as file:
        planeswalkers = json.load(file)

    with open("datassets/subtipos.json","r") as file:
        subtipos = json.load(file)

    return {"cards":cards,"planeswalkers":planeswalkers,"subtipos":subtipos}

class DbSingleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = genDatabase()
        return cls.instance
       