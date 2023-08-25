from project.player import Player
from project.supply.supply import Supply
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    # VALID_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player: Player):
        added_players = []
        for curr_player in player:
            if curr_player not in self.players:
                self.players.append(curr_player)
                # added_players.append(curr_player.name)
                added_players.append(curr_player)
        # return f"Successfully added: {', '.join(added_players)}"
        return f"Successfully added: {', '.join(p.name for p in added_players)}"

    def add_supply(self, *supply: Supply):
        for curr_supply in supply:
            self.supplies.append(curr_supply)

    def sustain(self, player_name: str, sustenance_type: str):
        curr_supply = [s for s in self.supplies[::-1] if s.__class__.__name__ == sustenance_type]
        curr_player = [p for p in self.players if p.name == player_name]

        if curr_player:
            curr_player = curr_player[0]
        else:
            return

        if curr_player.stamina == 100:
            return f"{player_name} have enough stamina."

        if curr_supply:
            curr_supply = curr_supply[0]
        elif not curr_supply:
            if sustenance_type == "Food":
                raise Exception(f"There are no food supplies left!")
            elif sustenance_type == "Drink":
                raise Exception(f"There are no drink supplies left!")

            return

        if curr_supply.energy + curr_player.stamina > 100:
            curr_player.stamina = 100
        else:
            curr_player.stamina += curr_supply.energy

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i] == curr_supply:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {curr_supply.name}."

        # curr_supply = None
        # curr_player = None

        # for supply in self.supplies[::-1]:
        #     if supply.__class__.__name__ == sustenance_type:
        #         curr_supply = supply
        #         break
        #
        # for player in self.players:
        #     if player.name == player_name:
        #         curr_player = player
        #         break
        # else:
        #     return




        # if sustenance_type not in self.VALID_TYPES:
        #     return   # връща None (или буквално връща нищо, недей да правиш друго нищо)
        #
        # for curr_player in self.players:
        #     if curr_player.name == player_name:
        #         curr_player
        #         break
        # else:
        #     return   # връща None, ако не открие player-a (или буквално връща нищо, недей да правиш друго нищо)
        #
        # if not curr_player.need_sustenance:
        #     return f"{player_name} have enough stamina."
        #
        # for i in range(len(self.supplies)-1, -1, -1):
        #     curr_supply = self.supplies[i]
        #     if curr_supply.__class__.__name__ == sustenance_type:
        #         self.supplies.pop(i)
        #         break
        # if not curr_supply:
        #     if sustenance_type == "Food":
        #         raise Exception(f"There are no food supplies left!")
        #     elif sustenance_type == "Drink":
        #         raise Exception(f"There are no drink supplies left!")
        #
        #     return


        # else:
        #     raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        #
        # if curr_player.stamina + curr_supply.energy > 0:
        #     curr_player.stamina = 100
        # else:
        #     curr_player.stamina += curr_supply.energy
        #
        # return f"{player_name} sustained successfully with {curr_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p1 for p1 in self.players if p1.name == first_player_name][0]
        second_player = [p2 for p2 in self.players if p2.name == second_player_name][0]

        result = []
        if first_player.stamina == 0:
            result.append(f"Player {first_player_name} does not have enough stamina.")
        if second_player.stamina == 0:
            result.append(f"Player {second_player_name} does not have enough stamina.")
        if result:
            return "\n".join(result)

        if first_player.stamina < second_player.stamina:
            second_player.stamina = max(second_player.stamina - (first_player.stamina / 2), 0)
            first_player.stamina = max(first_player.stamina - (second_player.stamina / 2), 0)
        else:
            first_player.stamina = max(first_player.stamina - (second_player.stamina / 2), 0)
            second_player.stamina = max(second_player.stamina - (first_player.stamina / 2), 0)

        if first_player.stamina < second_player.stamina:
            # if first_player.stamina <= 0:
            #     first_player.stamina = 0
            return f"Winner: {second_player.name}"
        elif second_player.stamina < first_player.stamina:
            # if second_player.stamina <= 0:
            #     second_player.stamina = 0
            return f"Winner: {first_player.name}"

    def next_day(self):
        for curr_player in self.players:
            curr_player.stamina = max(curr_player.stamina - (curr_player.age * 2), 0)

        for curr_player in self.players:
            self.sustain(curr_player.name, "Food")
            self.sustain(curr_player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)






