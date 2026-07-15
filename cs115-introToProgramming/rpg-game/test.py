import unittest
import hw5

class TestItem(unittest.TestCase):
    def test_item_constructor(self):
        sword = hw5.Item("sword", 5, 0, "physical", False)
        self.assertEqual(sword.name, "sword")
        self.assertEqual(sword.damage_points, 5)
        self.assertEqual(sword.regeneration_points, 0)
        self.assertEqual(sword.damage_type, "physical")
        self.assertFalse(sword.is_consumable)

    def test_item_str_contains_name_and_damage(self):
        potion = hw5.Item("health potion", 0, 10, "viral", True)
        s = str(potion)
        self.assertIn("health potion", s)
        self.assertIn("0", s)


class TestCharacter(unittest.TestCase):
    def test_character_default_inventory(self):
        c = hw5.Character("testbot", 10)
        items = list(c.inventory.keys())
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "rusty axe")
        self.assertEqual(c.inventory[items[0]], 1)

    def test_character_less_than(self):
        smallbot = hw5.Character("smallbot", 2)
        bigbot = hw5.Character("bigbot", 5)
        self.assertLess(smallbot, bigbot)
        self.assertGreater(bigbot, smallbot)
        self.assertEqual(max([bigbot, smallbot]), bigbot)

    def test_transfer_loot_transfers_and_empties(self):
        main = hw5.Character("main", 10)
        enemy = hw5.Character("enemy", 1)
        item = list(main.inventory.keys())[0]
        enemy.inventory[item] = 1
        enemies = [enemy]

        main.transfer_loot(enemy.inventory)

        self.assertIn(item, main.inventory)
        self.assertGreater(main.inventory[item], 0)

        self.assertTrue(
            enemy.inventory == {} or enemy.inventory[item] == 0
        )

    def test_perform_move_reduces_target_health(self):
        attacker = hw5.Character("attacker", 10)
        target = hw5.Character("target", 10)
        item = list(attacker.inventory.keys())[0]
        move = hw5.Move(target, item)
        attacker.perform_move(move)
        self.assertEqual(target.health_points, 9)

    def test_perform_move_consumable_reduces_quantity(self):
        attacker = hw5.Character("attacker", 10)
        target = hw5.Character("target", 10)
        potion = hw5.Item("virus bomb", 2, 0, "viral", True)
        attacker.inventory[potion] = 1
        move = hw5.Move(target, potion)
        attacker.perform_move(move)
        self.assertEqual(attacker.inventory[potion], 0)

    def test_perform_move_with_regeneration(self):
        c1 = hw5.Character("attacker", 10)
        c2 = hw5.Character("target", 5)
        health_potion = hw5.Item("health potion", 0, 5, "viral", True)
        c1.inventory[health_potion] = 1

        move = hw5.Move(c2, health_potion)
        c1.perform_move(move)

        self.assertEqual(c2.health_points, 5)
        self.assertEqual(c1.health_points, 15)
        self.assertEqual(c1.inventory[health_potion], 0)

    def test_get_next_move_returns_lowest_hp_target(self):
        c1 = hw5.Character("main", 10)
        weak = hw5.Character("weak", 1)
        strong = hw5.Character("strong", 5)
        move = c1.get_next_move([weak, strong])
        self.assertEqual(move.other_character, weak)




class TestRobotAndZombie(unittest.TestCase):

    def test_robot_has_shock_baton(self):
        r = hw5.Robot("bender", 10)
        baton = hw5.Item("shock baton", 1, 0, "electrical", False)
        axe = hw5.Item("rusty axe", 1, 0, "physical", False)
        self.assertIn(baton, r.inventory)
        self.assertIn(axe, r.inventory)

    def test_zombie_has_brain_grenades(self):
        z = hw5.Zombie("maduxwane", 10)
        grenade = hw5.Item("brain grenade", 5, 0, "viral", True)
        axe = hw5.Item("rusty axe", 1, 0, "physical", False)
        self.assertIn(grenade, z.inventory)
        self.assertIn(axe, z.inventory)
        self.assertEqual(z.inventory[grenade], 3)

    def test_robot_double_damage_electrical(self):
        r = hw5.Robot("r2d2", 10)
        max_c_hp = 10
        c = hw5.Character("target", max_c_hp)
        baton = hw5.Item("shock baton", 1, 0, "electrical", False)
        move = hw5.Move(c, baton)
        r.perform_move(move)
        self.assertEqual(c.health_points, max_c_hp - 2*baton.damage_points)

    def test_zombie_double_damage_viral(self):
        max_c_hp = 10
        z = hw5.Zombie("zombi", 10)
        c = hw5.Character("target", max_c_hp)
        grenade_dmg  = 5
        grenade = hw5.Item("brain grenade", grenade_dmg, 0, "viral", True)
        move = hw5.Move(c, grenade)
        z.perform_move(move)
        self.assertEqual(c.health_points, max_c_hp - 2* grenade_dmg)

    def test_zombie_attacks_first_character(self):
        z = hw5.Zombie("zonbi", 10)
        a = hw5.Character("A", 10)
        b = hw5.Character("B", 5)
        move = z.get_next_move([a, b])
        self.assertEqual(move.other_character, a)


class TestBattle(unittest.TestCase):
    def test_standard_battle_basic_flow(self):
        main_max_hp = 10
        enemy_max_hp = 5
        main = hw5.Character("main", main_max_hp)
        enemy = hw5.Character("enemy",enemy_max_hp)
        enemies = [enemy]
        hw5.standard_battle(main, enemies, enemy)
        # check one has less HP 
        self.assertTrue(main.health_points < main_max_hp or enemy.health_points < enemy_max_hp)

    def test_standard_battle_transfers_loot_on_defeat(self):
        main = hw5.Character("main", 10)
        enemy = hw5.Character("enemy", 1)
        item = list(main.inventory.keys())[0]
        enemy.inventory[item] = 1
        enemies = [enemy]

        hw5.standard_battle(main, enemies, enemy)

        self.assertIn(item, main.inventory)
        self.assertTrue(len(enemy.inventory.keys()) == 0 or enemy.inventory[item] == 0)



if __name__ == "__main__":
    unittest.main()

