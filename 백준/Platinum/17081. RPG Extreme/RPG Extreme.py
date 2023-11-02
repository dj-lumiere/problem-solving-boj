# 17081 RPG Extreme
from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def convert_to_int_if_possibie(target: str):
    if target.isnumeric():
        return int(target)
    return target


class GameObject:
    def __init__(self, pos_x, pos_y, is_passable=True):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_passable = is_passable

    def __str__(self):
        return f"Blank Game Object @ ({self.pos_x}, {self.pos_y})"

    def __repr__(self):
        return self.__str__()


class LivingEntity(GameObject):
    def __init__(self, pos_x, pos_y, hp_current, hp_max, atk_barebody, def_barebody):
        super().__init__(pos_x, pos_y)
        self.is_alive = True
        self.hp_current = hp_current
        self.hp_max = hp_max
        self.atk_barebody = atk_barebody
        self.def_barebody = def_barebody

    def take_damage(self, damage):
        self.hp_current -= damage
        if self.hp_current <= 0:
            self.is_alive = False
            self.hp_current = 0


class Player(LivingEntity):
    DEFAULT_DAMAGE = 1
    MONSTER_KILLED = 0
    KILLED_IN_BATTLE = 1
    RESURRECTED = 2
    BATTLE_CONTINUE = 3

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 20, 20, 2, 2)
        self.starting_pos_x = pos_x
        self.starting_pos_y = pos_y
        self.level = 1
        self.exp_current = 0
        self.exp_max = 5
        self.atk_weapon = 0
        self.def_armor = 0
        self.accessory_slot = {
            "HR": False,
            "RE": False,
            "CO": False,
            "EX": False,
            "DX": False,
            "HU": False,
            "CU": False,
        }
        self.accessory_count = 0
        self.death_cause = GameObject(-1, -1)

    def has_encountered(self, other: "GameObject"):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y

    def is_promotable(self):
        return self.exp_current >= self.exp_max

    def level_up(self):
        self.level += 1
        self.exp_current = 0
        self.exp_max += 5
        self.hp_max += 5
        self.hp_current = self.hp_max
        self.atk_barebody += 2
        self.def_barebody += 2

    def hp_regeneration(self):
        self.hp_current += 3
        if self.hp_current > self.hp_max:
            self.hp_current = self.hp_max

    def is_resurrectable(self):
        return not self.is_alive and self.accessory_slot["RE"]

    def can_avoid_spike_trap(self):
        return self.accessory_slot["DX"]

    def resurrect(self):
        self.hp_current = self.hp_max
        self.is_alive = True
        self.accessory_slot["RE"] = False
        self.accessory_count -= 1
        self.pos_x = self.starting_pos_x
        self.pos_y = self.starting_pos_y

    def resurrect_with_other(self, other: "Monster"):
        self.resurrect()
        other.hp_current = other.hp_max

    def spike_trap_encounter(self, other: "SpikeTrap"):
        if not self.has_encountered(other):
            return
        if self.can_avoid_spike_trap():
            self.take_damage(self.DEFAULT_DAMAGE)
        else:
            self.take_damage(other.atk_barebody)
        if self.is_resurrectable():
            self.resurrect()
        elif not self.is_alive:
            self.death_cause = other

    def calculate_monster_damage(self, other: "Monster", turn_count: int):
        if self.accessory_slot["DX"] and self.accessory_slot["CO"] and turn_count == 0:
            return max(
                self.DEFAULT_DAMAGE,
                (self.atk_barebody + self.atk_weapon) * 3 - other.def_barebody,
            )
        elif self.accessory_slot["CO"] and turn_count == 0:
            return max(
                self.DEFAULT_DAMAGE,
                (self.atk_barebody + self.atk_weapon) * 2 - other.def_barebody,
            )
        return max(
            self.DEFAULT_DAMAGE,
            (self.atk_barebody + self.atk_weapon) * 1 - other.def_barebody,
        )

    def normal_fight_turn(self, other: "NormalMonster", turn_count: int):
        other.take_damage(self.calculate_monster_damage(other, turn_count))
        if not other.is_alive:
            return self.MONSTER_KILLED
        self.take_damage(other.calculate_player_damage(self, turn_count))
        if not self.is_alive and self.is_resurrectable():
            self.resurrect_with_other(other)
            # print("resurrected")
            return self.RESURRECTED
        elif not self.is_alive:
            return self.KILLED_IN_BATTLE
        else:
            return self.BATTLE_CONTINUE

    def boss_fight_turn(self, other: "BossMonster", turn_count: int):
        if turn_count == 0 and self.accessory_slot["HU"]:
            self.hp_current = self.hp_max
        other.take_damage(self.calculate_monster_damage(other, turn_count))
        if not other.is_alive:
            return self.MONSTER_KILLED
        if turn_count != 0 or not self.accessory_slot["HU"]:
            self.take_damage(other.calculate_player_damage(self, turn_count))
        if not self.is_alive and self.is_resurrectable():
            self.resurrect_with_other(other)
            # print("resurrected")
            return self.RESURRECTED
        elif not self.is_alive:
            return self.KILLED_IN_BATTLE
        else:
            return self.BATTLE_CONTINUE

    def exp_increment(self, other: "Monster"):
        exp_increment_value = other.exp_giving
        if self.accessory_slot["EX"]:
            exp_increment_value = exp_increment_value * 6 // 5
        self.exp_current += exp_increment_value
        if self.is_promotable():
            self.level_up()

    def normal_monster_encounter(self, other: "NormalMonster"):
        if not self.has_encountered(other):
            return 0
        if not other.is_alive:
            return 0
        turn_count = 0
        turn_status = self.BATTLE_CONTINUE
        while turn_status == self.BATTLE_CONTINUE:
            # print(turn_count, "before", f"{self!r}", f"{other!r}")
            turn_status = self.normal_fight_turn(other, turn_count)
            # print(turn_count, "after", f"{self!r}", f"{other!r}")
            turn_count += 1
            # print()
        if turn_status == self.KILLED_IN_BATTLE:
            self.death_cause = other
        elif turn_status == self.MONSTER_KILLED:
            if self.accessory_slot["HR"]:
                self.hp_regeneration()
            self.exp_increment(other)
        return turn_count, turn_status

    def boss_monster_encounter(self, other: "BossMonster"):
        if not self.has_encountered(other):
            return 0
        if not other.is_alive:
            return 0
        turn_count = 0
        turn_status = self.BATTLE_CONTINUE
        while turn_status == self.BATTLE_CONTINUE:
            # print(turn_count, "before", f"{self!r}", f"{other!r}")
            turn_status = self.boss_fight_turn(other, turn_count)
            # print(turn_count, "after", f"{self!r}", f"{other!r}")
            turn_count += 1
            # print()
        if turn_status == self.KILLED_IN_BATTLE:
            self.death_cause = other
        elif turn_status == self.MONSTER_KILLED:
            if self.accessory_slot["HR"]:
                self.hp_regeneration()
            self.exp_increment(other)
        return turn_status

    def acquire_weapon(self, other: "Weapon"):
        self.atk_weapon = other.item_effect
        other.is_used = True

    def acquire_armor(self, other: "Armor"):
        self.def_armor = other.item_effect
        other.is_used = True

    def acquire_accessories(self, other: "Accessories"):
        if self.accessory_count >= 4:
            other.is_used = True
            return
        if self.accessory_slot[other.item_type] == True:
            other.is_used = True
            return
        self.accessory_slot[other.item_type] = True
        self.accessory_count += 1
        other.is_used = True

    def acquire_item(self, other: "Item"):
        if other.is_used:
            return
        if isinstance(other, Weapon):
            self.acquire_weapon(other)
        elif isinstance(other, Armor):
            self.acquire_armor(other)
        elif isinstance(other, Accessories):
            self.acquire_accessories(other)

    def __str__(self):
        return f"LV : {self.level}\nHP : {self.hp_current}/{self.hp_max}\nATT : {self.atk_barebody}+{self.atk_weapon}\nDEF : {self.def_barebody}+{self.def_armor}\nEXP : {self.exp_current}/{self.exp_max}"

    def __repr__(self):
        if self.is_alive:
            return f"Alive Player @ ({self.pos_x}, {self.pos_y}) : LV : {self.level}, HP : {self.hp_current}/{self.hp_max}, ATT : {self.atk_barebody}+{self.atk_weapon}, DEF : {self.def_barebody}+{self.def_armor}, EXP : {self.exp_current}/{self.exp_max}, Accessories : {[k for k,v in self.accessory_slot.items() if v]}"
        else:
            return f"Dead Player @ ({self.pos_x}, {self.pos_y}) : LV : {self.level}, HP : {self.hp_current}/{self.hp_max}, ATT : {self.atk_barebody}+{self.atk_weapon}, DEF : {self.def_barebody}+{self.def_armor}, EXP : {self.exp_current}/{self.exp_max}, Accessories : {[k for k,v in self.accessory_slot.items() if v]}, Death Cause : {self.death_cause!r}"


class Monster(LivingEntity):
    DEFAULT_DAMAGE = 1

    def __init__(
        self,
        pos_x,
        pos_y,
        name,
        hp_current,
        hp_max,
        atk_barebody,
        def_barebody,
        exp_giving,
    ):
        super().__init__(pos_x, pos_y, hp_current, hp_max, atk_barebody, def_barebody)
        self.name = name
        self.exp_giving = exp_giving

    def calculate_player_damage(self, other: "Player", turn_count: int):
        return max(
            self.DEFAULT_DAMAGE,
            (self.atk_barebody) * 1 - (other.def_barebody + other.def_armor),
        )

    def __str__(self):
        return f"Name : {self.name}\nHP : {self.hp_current}/{self.hp_max}\nATT : {self.atk_barebody}\nDEF : {self.def_barebody}"

    def __repr__(self):
        return f"{'Alive' if self.is_alive else 'Dead'} Monster {self.name} @ ({self.pos_x}, {self.pos_y}) : HP : {self.hp_current}/{self.hp_max}, ATT : {self.atk_barebody}, DEF : {self.def_barebody}, EXP : {self.exp_giving}"


class NormalMonster(Monster):
    def __init__(
        self,
        pos_x,
        pos_y,
        name,
        hp_current,
        hp_max,
        atk_barebody,
        def_barebody,
        exp_giving,
    ):
        super().__init__(
            pos_x,
            pos_y,
            name,
            hp_current,
            hp_max,
            atk_barebody,
            def_barebody,
            exp_giving,
        )

    def __str__(self):
        return super().__str__()


class BossMonster(Monster):
    def __init__(
        self,
        pos_x,
        pos_y,
        name,
        hp_current,
        hp_max,
        atk_barebody,
        def_barebody,
        exp_giving,
    ):
        super().__init__(
            pos_x,
            pos_y,
            name,
            hp_current,
            hp_max,
            atk_barebody,
            def_barebody,
            exp_giving,
        )

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{'Alive' if self.is_alive else 'Dead'} BOSS Monster {self.name} @ ({self.pos_x}, {self.pos_y}) : HP : {self.hp_current}/{self.hp_max}, ATT : {self.atk_barebody}, DEF : {self.def_barebody}, EXP : {self.exp_giving}"


class NonLivingEntity(GameObject):
    def __init__(self, pos_x, pos_y, is_passable):
        super().__init__(pos_x, pos_y, is_passable)


class SpikeTrap(NonLivingEntity):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, True)
        self.name = "SPIKE TRAP"
        self.atk_barebody = 5

    def __str__(self):
        return f"SpikeTrap @ ({self.pos_x}, {self.pos_y})"


class Wall(NonLivingEntity):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, False)

    def __str__(self):
        return f"Wall @ ({self.pos_x}, {self.pos_y})"


class Item(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.is_used = False

    def __str__(self):
        return f"{'Used' if self.is_used else 'Unused'} Item @ ({self.pos_x}, {self.pos_y})"


class Weapon(Item):
    def __init__(self, pos_x, pos_y, effect):
        super().__init__(pos_x, pos_y)
        self.item_effect = effect

    def __str__(self):
        return f"{'Used' if self.is_used else 'Unused'} Weapon @ ({self.pos_x}, {self.pos_y}) : ATT +{self.item_effect}"


class Armor(Item):
    def __init__(self, pos_x, pos_y, effect):
        super().__init__(pos_x, pos_y)
        self.item_effect = effect

    def __str__(self):
        return f"{'Used' if self.is_used else 'Unused'} Armor @ ({self.pos_x}, {self.pos_y}) : DEF +{self.item_effect}"


class Accessories(Item):
    def __init__(self, pos_x, pos_y, item_type):
        super().__init__(pos_x, pos_y)
        self.item_type = item_type

    def __str__(self):
        return f"{'Used' if self.is_used else 'Unused'} Accessory @ ({self.pos_x}, {self.pos_y}) : Type : {self.item_type}"


def is_inbound(pos_x, size_x, pos_y, size_y):
    return 0 <= pos_x < size_x and 0 <= pos_y < size_y


grid_size_y, grid_size_x = map(int, input().split(" "))
grid = [list(input()) for _ in range(grid_size_y)]
movement_log = list(input())
objects: list[list[GameObject]] = [
    [GameObject(x, y) for x in range(grid_size_x)] for y in range(grid_size_y)
]
monster_count = 0
item_count = 0
game_player = GameObject(0, 0)
for x, y in product(range(grid_size_x), range(grid_size_y)):
    if grid[y][x] == "^":
        objects[y][x] = SpikeTrap(x, y)
    if grid[y][x] == "#":
        objects[y][x] = Wall(x, y)
    if grid[y][x] == "@":
        game_player = Player(x, y)
    if grid[y][x] in ("&", "M"):
        monster_count += 1
    if grid[y][x] == "B":
        item_count += 1
# print(f"{game_player!r}")
for _ in range(monster_count):
    (
        pos_y,
        pos_x,
        name,
        atk_barebody,
        def_barebody,
        hp,
        exp,
    ) = input().split(" ")
    if grid[int(pos_y) - 1][int(pos_x) - 1] == "M":
        objects[int(pos_y) - 1][int(pos_x) - 1] = BossMonster(
            int(pos_x) - 1,
            int(pos_y) - 1,
            name,
            int(hp),
            int(hp),
            int(atk_barebody),
            int(def_barebody),
            int(exp),
        )
    else:
        objects[int(pos_y) - 1][int(pos_x) - 1] = NormalMonster(
            int(pos_x) - 1,
            int(pos_y) - 1,
            name,
            int(hp),
            int(hp),
            int(atk_barebody),
            int(def_barebody),
            int(exp),
        )
for _ in range(item_count):
    pos_y, pos_x, item_type, effect = input().split(" ")
    if item_type == "W":
        objects[int(pos_y) - 1][int(pos_x) - 1] = Weapon(
            int(pos_x) - 1, int(pos_y) - 1, int(effect)
        )
    elif item_type == "A":
        objects[int(pos_y) - 1][int(pos_x) - 1] = Armor(
            int(pos_x) - 1, int(pos_y) - 1, int(effect)
        )
    else:
        objects[int(pos_y) - 1][int(pos_x) - 1] = Accessories(
            int(pos_x) - 1, int(pos_y) - 1, effect
        )
# print(objects)
DELTA = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
is_boss_dead = False
total_turn_count = 0

for movement in movement_log:
    dx, dy = DELTA[movement]
    total_turn_count += 1
    new_pos_x, new_pos_y = game_player.pos_x + dx, game_player.pos_y + dy
    if not is_inbound(new_pos_x, grid_size_x, new_pos_y, grid_size_y):
        new_pos_x, new_pos_y = game_player.pos_x, game_player.pos_y
    if isinstance(objects[new_pos_y][new_pos_x], Wall):
        new_pos_x, new_pos_y = game_player.pos_x, game_player.pos_y
    game_player.pos_x, game_player.pos_y = new_pos_x, new_pos_y
    encountered_object = objects[game_player.pos_y][game_player.pos_x]
    # print(f"{total_turn_count=} {encountered_object!r}")
    # print(f"BEFORE {game_player!r}")
    if isinstance(encountered_object, SpikeTrap):
        game_player.spike_trap_encounter(encountered_object)
    elif isinstance(encountered_object, NormalMonster):
        # print(f"Battle with {encountered_object!r}")
        game_player.normal_monster_encounter(encountered_object)
        # total_turn_count += turn_count
        # print(turn_count, turn_status)
    elif isinstance(encountered_object, BossMonster):
        # print(f"BOSS Battle with {encountered_object!r}")
        game_player.boss_monster_encounter(encountered_object)
        if not encountered_object.is_alive:
            is_boss_dead = True
        # total_turn_count += turn_count
        # print(turn_count, turn_status)
    elif isinstance(encountered_object, Item):
        game_player.acquire_item(encountered_object)
    # print(f"AFTER {game_player!r}")
    # print()
    if not game_player.is_alive or is_boss_dead:
        break

for x, y in product(range(grid_size_x), range(grid_size_y)):
    grid[y][x] = "."
for x, y in product(range(grid_size_x), range(grid_size_y)):
    current_object = objects[y][x]
    if isinstance(current_object, Wall):
        grid[y][x] = "#"
    if isinstance(current_object, SpikeTrap):
        grid[y][x] = "^"
    if isinstance(current_object, NormalMonster) and current_object.is_alive:
        grid[y][x] = "&"
    if isinstance(current_object, BossMonster) and current_object.is_alive:
        grid[y][x] = "M"
    if isinstance(current_object, Item) and not current_object.is_used:
        grid[y][x] = "B"
if game_player.is_alive:
    grid[game_player.pos_y][game_player.pos_x] = "@"
for y in range(grid_size_y):
    print(*grid[y], sep="")
print(f"Passed Turns : {total_turn_count}")
print(game_player)

if not game_player.is_alive:
    print(f"YOU HAVE BEEN KILLED BY {game_player.death_cause.name}..")
elif is_boss_dead:
    print("YOU WIN!")
else:
    print("Press any key to continue.")
