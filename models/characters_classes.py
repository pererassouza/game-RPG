from characters import Characters

class Warrior(Characters):
    def __init__(self, name: str) -> None:
        self.class_ = "Warrior"
        self.resistance_against_magic = 7
        self.physical_damage = 15
        self.magical_damage = 9
        super().__init__(name=name, damage=15, life=110, weapons=["Sword", "Shield"], class_=self.class_)
    
    def especial_ability(self) -> None:
        print(f"{self.name} used especial atack! 30atck damage")
    

class Healer(Characters):
    def __init__(self, name:str) -> None:
        self.class_ = "Healer"
        super().__init__(name=name, damage=9, life=150, weapons="staff", class_=self.class_)
    
    def especial_ability(self) -> None:
        print(f"{self.name} used especial atack! 22atck damage")

class Mage(Characters):
    def __init__(self, name:str):
        self.class_ = "Mage"
        super().__init__(name=name, damage=12, life=120, weapons="staff", class_=self.class_)

    def especial_ability(self) -> None:
        print(f"{self.name} used especial atack! 50atck damage")

if __name__ == "__main__":
    warrior = Warrior("Jack")
    healer = Healer("Iza")
    mage = Mage("Isaac")
    
    warrior.take_damage(100)
    healer.take_damage(100)
    mage.take_damage(100)
    
    warrior.especial_ability()
    healer.especial_ability()
    mage.especial_ability()
    
    warrior.check_status()
    healer.check_status()   
    mage.check_status()   
    
    print(warrior)
    print(healer)
    print(mage)
