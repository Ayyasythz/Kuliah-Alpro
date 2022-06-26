class Agent:
    def __init__(self, hname, htype, weapon, round):
        self.hname = hname
        self.htype = htype
        self.weapon = weapon
        self.round = round
        self.hp = 100

    def print_status(self):
        print(f"Agent Name            : {self.hname}")
        print(f"Agent Type            : {self.htype}")
        print(f"Weapon                : {self.weapon}")
        print(f"Round                 : {self.round}")
        print(f"Hp                    : {self.hp}")

    def kill(self, tot):
        self.hp += 25 * tot
        if self.hp > 150:
            self.hp = 150
        print(f"Total HP {self.hname} : {self.hp}")

    def dmg_taken(self, tot):
        self.hp -= tot
        if self.hp < 0 :
            self.hp = 0
        if self.hp > 150:
            self.hp = 150
        print(f"Total HP {self.hname} setelah menerima damage : {self.hp}")

    def last_health(self):
        print(f"======== {self.hname} HP : {self.hp} ========")


if __name__ == '__main__':
    reyna = Agent("Reyna", "Duelist", "Vandal", 9)
    reyna.print_status()
    print("=======================================")
    slain = int(input("Kill berapa musuh ? : "))
    reyna.kill(slain)
    dmg = int(input("Damage yang diterima sebesar ? : "))
    reyna.dmg_taken(dmg)
    reyna.last_health()
