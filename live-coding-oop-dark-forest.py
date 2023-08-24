class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self, enemy):
        enemy.take_damage(self.damage)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, damage=30)

    def special_ability(self, enemy):
        enemy.take_damage(self.damage * 2)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=60, damage=45)

    def special_ability(self, enemy):
        self.health += 15
        for i in range(3):
            enemy.take_damage(10)


class EvilMage(Mage):
    pass


class GoodMage(Mage):
    pass


class StoryGame:
    def __init__(self):
        self.player = None
        self.current_enemy = None
        self.story_progress = 0
        self.choices = [
            "1. Explore the forest",
            "2. Enter the dark cave",
            "3. Return to the village",
            "4. Exit the game"
        ]

    def start(self):
        print("Welcome to the Story Game!")
        player_name = input("Enter your character's name: ")
        player_class = input("Choose your class (Warrior/Mage): ").lower()
        if player_class == "warrior":
            self.player = Warrior(player_name)
        elif player_class == "mage":
            self.player = Mage(player_name)
        else:
            print("Invalid input, you will be a warrior!")
            self.player = Warrior(player_name)
        self.play()

    def play(self):
        print(
            f"Welcome {self.player.name} the amazing {type(self.player).__name__} ")
        print("You find yourself at a crossroad. What will you do?\n")
        while self.player.is_alive():
            print("\n".join(self.choices))
            choice = input("Enter your choice: ")
            if choice == "1":
                self.explore_forest()
            elif choice == "2":
                self.enter_cave()
            elif choice == "3":
                self.return_to_village()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")
        print("Game Over. You have been defeated.")

    def explore_forest(self):
        print("You venture into the forest and encounter Hydra!")
        self.current_enemy = Character("Hydra", health=50, damage=20)
        self.battle()

    def enter_cave(self):
        print("You enter the dark cave and find Chalizard")
        self.current_enemy = Character("Chalizard", health=60, damage=30)
        self.battle()

    def return_to_village(self):
        print("You return to the village.")
        self.player.health += 10
        self.story_progress += 1
        if self.story_progress > 4:
            self.player.damage += 20
        print(f'Your current progress {self.story_progress}')

    def battle(self):
        i = 1
        while self.current_enemy.is_alive() and self.player.is_alive():
            print(
                f"{self.player.name} (Health: {self.player.health}) vs {self.current_enemy.name} (Health: {self.current_enemy.health})"
            )
            action = input(
                "Enter 'a' to attack or 'f' to flee or 's' for special ability: "
            )

            if action == "a":
                self.player.attack_enemy(self.current_enemy)
                i += 1
                if self.current_enemy.is_alive():
                    self.current_enemy.attack_enemy(self.player)

            elif action == "s":
                if i % 3 == 0:
                    self.player.special_ability(self.current_enemy)
                else:
                    print(
                        "You need to wait for the right moment to use your special ability!")

                if self.current_enemy.is_alive():
                    self.current_enemy.attack_enemy(self.player)

                i += 1

            elif action == "f":
                print("You flee from the battle.")
                break
            else:
                print("Invalid action. Try again.")
        if not self.current_enemy.is_alive():
            print(f"You have defeated {self.current_enemy.name}!")
            self.story_progress += 1


# Main part of the program
game = StoryGame()
game.start()
