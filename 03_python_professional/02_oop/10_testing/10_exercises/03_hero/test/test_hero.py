from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def test_initialising_data(self):
        hero = Hero("TestHero", 100, 100.0, 50.0)

        self.assertEqual("TestHero", hero.username)
        self.assertEqual(100, hero.level)
        self.assertEqual(100.0, hero.health)
        self.assertEqual(50.0, hero.damage)

    def test_battle_with_same_hero_raises(self):
        hero = Hero("TestHero", 100, 100.0, 50.0)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_self_zero_health_raises(self):
        hero = Hero("TestHero", 100, 0, 50.0)
        enemy_hero = Hero("TestEnemy", 100, 100.0, 25.0)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_zero_enemy_health_raises(self):
        hero = Hero("TestHero", 10, 100.0, 50.0)
        enemy_hero = Hero("TestEnemy", 5, 0, 25.0)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight TestEnemy. He needs to rest", str(ex.exception))

    def test_hero_health_decreasing_after_hero_win(self):
        hero = Hero("TestHero", 1, 100.0, 100.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 20.0)

        hero.battle(enemy_hero)

        self.assertEqual(85.0, hero.health)

    def test_enemy_health_decreasing_after_hero_loose(self):
        hero = Hero("TestHero", 1, 100.0, 20.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 100.0)

        hero.battle(enemy_hero)

        self.assertEqual(85.0, enemy_hero.health)

    def test_draw_after_battle(self):
        hero = Hero("TestHero", 10, 100.0, 20.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 100.0)

        result = hero.battle(enemy_hero)

        self.assertEqual("Draw", result)

    def test_win_hero_after_battle(self):
        hero = Hero("TestHero", 1, 100.0, 100.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 20.0)

        result = hero.battle(enemy_hero)

        self.assertEqual("You win", result)

    def test_loose_hero_after_battle(self):
        hero = Hero("TestHero", 1, 100.0, 20.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 100.0)

        result = hero.battle(enemy_hero)

        self.assertEqual("You lose", result)

    def test_string_method_result_after_battle(self):
        hero = Hero("TestHero", 1, 100.0, 100.0)
        enemy_hero = Hero("TestEnemy", 1, 100.0, 20.0)

        hero.battle(enemy_hero)
        result = str(hero)
        expected = f"Hero TestHero: 2 lvl\nHealth: 85.0\nDamage: 105.0\n"

        self.assertEqual(expected, result)
