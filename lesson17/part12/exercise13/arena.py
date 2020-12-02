from character import Character
from random import randrange


class Arena:
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B

    def __str__(self):
        st = "\n" + ("=" * 20)

        st += "\nTEAM A"
        for character in self.team_A:
            st += "\n" + str(character)

        st += "\n" + ("=" * 20)

        st += ("\nTEAM B")
        for character in self.team_B:
            st += "\n" + str(character)

        st += "\n" + ("=" * 20)
        return st

    def __repr__(self):
        st = f"Arena(["
        st += ", ".join([repr(character) for character in self.team_A])
        st += "],["
        st += ", ".join([repr(character) for character in self.team_B])
        st += "])"
        return st

    def play(self):
        time = -1
        while True:
            time += 1
            print("=" * 20)
            print("Time: " + str(time))
            print("=" * 20)
            print(self)

            # character list creation that are avalable
            chars_to_play = []
            for character in self.team_A:
                if character.delay == 0:
                    chars_to_play.append(('A', character))
            for character in self.team_B:
                if character.delay == 0:
                    chars_to_play.append(('B', character))

            # active characters attack
            for character in chars_to_play:
                attacking = character[1]
                if character[0] == 'A':
                    defending = self.team_B[randrange(len(self.team_B))]
                else:
                    defending = self.team_A[randrange(len(self.team_A))]

                damage = attacking.attack()
                defending.health -= damage
                print(f"{attacking.character_name} attacks {defending.character_name} for {damage} damage")

            # check for dead characters
            for position in range(len(self.team_A) - 1, -1, -1):
                if self.team_A[position].is_dead():
                    print(f"{self.team_A[position].character_name} is dead")
                    self.team_A.pop(position)
            for position in range(len(self.team_B) - 1, -1, -1):
                if self.team_B[position].is_dead():
                    print(f"{self.team_B[position].character_name} is dead")
                    self.team_B.pop(position)

            # check if game is ending
            if len(self.team_A) == 0:
                print("Team B wins!")
                break
            elif len(self.team_A) == 0:
                print("Team A wins!")
                break

            # end round
            for character in self.team_A:
                character.end_round()
            for character in self.team_B:
                character.end_round()

            input("Press enter to continue")
