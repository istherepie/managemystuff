from unittest import TestCase


class PhaserTest(TestCase):

    def test_phaser_fire(self):

        shoot_four_times = True

        expected = True

        self.assertEqual(expected, shoot_four_times)


    def test_more_phaser_fire(self):

        shoot_eight_times = True

        expected = True

        self.assertEqual(expected, shoot_eight_times)

    def test_phaser_max_setting(self):

        crank_it_all_the_way_up = "MAX DAMAGE"

        expected = "MAX DAMAGE"

        self.assertEqual(expected, crank_it_all_the_way_up)

    def test_overload_phaser(self):

        set_it_to_overload = "BOOM"

        expected = "BOOM"

        self.assertEqual(expected, set_it_to_overload)

    def test_if_phaser_works_after_overload(self):

        does_it_work = "no"

        expected = "no"

        self.assertEqual(expected, does_it_work)
