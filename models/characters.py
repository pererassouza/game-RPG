import abc

class Characters(abc.ABC):
    def __init__(self, name:str, damage:int, life:int, weapons:str|list[str], class_:str) -> None:
        self.name = name
        self.damage = damage
        self.life = life
        self.weapons = weapons
        self.class_ = class_

    def take_damage(self, damage:int) -> None:
        self.life -= damage
    
    def heal(self, amount:int) -> None:
        self.life += amount
    
    def check_status(self) -> None:
        if self.life <= 0:
            print(f"{self.name} died!")
        else:
            print(f"{self.name} has {self.life}hp")
    
    def __repr__(self) -> str:
        msg = f"({self.class_})|{self.name} has {self.life}hp, take {self.damage} of power damage and use {self.weapons}"
        return msg

    
    @abc.abstractmethod
    def especial_ability(self) -> None: pass
