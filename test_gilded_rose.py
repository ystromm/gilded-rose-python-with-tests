# -*- coding: utf-8 -*-

from unittest import TestCase, skip

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(TestCase):

    def test_foo(self):
        updated_items = self.gilded_rose_update_quality([Item("foo", 0, 0)])
        self.assertEqual("foo", updated_items[0].name)

    def test_empty_should_return_empty(self):
        updated_items = self.gilded_rose_update_quality([])
        self.assertEqual([], updated_items)

    def test_quality_should_decrease(self):
        updated_items = self.gilded_rose_update_quality([Item("foo", 1, 1)])
        self.assertEqual(0, updated_items[0].quality)

    def test_quality_should_decrease_double_if_sell_in_has_passed(self):
        updated_items = self.gilded_rose_update_quality([Item("foo", 0, 10)])
        self.assertEqual(8, updated_items[0].quality)

    def test_quality_should_not_become_negative(self):
        updated_items = self.gilded_rose_update_quality([Item("foo", 0, 0)])
        self.assertGreaterEqual(0, updated_items[0].quality)

    def test_sell_in_should_decrease(self):
        updated_items = self.gilded_rose_update_quality([Item("foo", 1, 1)])
        self.assertEqual(0, updated_items[0].sell_in)

    @skip
    def test_aged_brie_quality_should_increase_in_quality_after_sell_in(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", -1, 1)])
        self.assertEqual(3, updated_items[0].quality)

    @skip
    def test_aged_brie_quality_should_increase_in_quality(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 1, 1)])
        self.assertEqual(2, updated_items[0].quality)

    def test_aged_brie_quality_should_increase_in_quality_but_not_above_50(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 1, 50)])
        self.assertEqual(50, updated_items[0].quality)

    def test_sulfuras_should_keep_quality(self):
        updated_items = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 1, 80)])
        self.assertEqual(80, updated_items[0].quality)

    @skip
    def test_sulfuras_should_have_quality_80(self):
        updated_items = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 1, 1)])
        self.assertEqual(80, updated_items[0].quality)

    def test_sulfuras_should_keep_sell_in(self):
        updated_items = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 1, 80)])
        self.assertEqual(1, updated_items[0].sell_in)

    def test_backstage_passes_should_increase_in_quality(self):
        updated_items = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 20, 1)])
        self.assertEqual(2, updated_items[0].quality)

    def test_backstage_passes_should_increase_by_2_in_quality(self):
        updated_items = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 9, 1)])
        self.assertEqual(3, updated_items[0].quality)

    def test_backstage_passes_should_increase_by_3_in_quality(self):
        updated_items = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 4, 1)])
        self.assertEqual(4, updated_items[0].quality)

    def test_backstage_passes_should_have_zero_quailty_when_sell_in_is_passed(self):
        updated_items = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)])
        self.assertEqual(0, updated_items[0].quality)

    def gilded_rose_update_quality(self, items):
        items = GildedRose.update_quality(items)
        return items

    def test_regular_items_decrease_by_one(self):
        updated_items = self.gilded_rose_update_quality([Item("+5 Dexterity Vest", 10, 20)])
        self.assertEqual(updated_items[0].sell_in, 9)
        self.assertEqual(updated_items[0].quality, 19)

    def test_quality_goes_up_for_improving_products(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 20, 30),
                                                         Item("Backstage passes to a TAFKAL80ETC concert", 20, 30)])

        expected = [
            {'sell_in': 19, 'quality': 31},
            {'sell_in': 19, 'quality': 31},
        ]

        for index, expectation in enumerate(expected):
            item = updated_items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    @skip
    def test_quality_goes_up_by_two_for_improving_products_with_10_days_or_less_left(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 10, 34),
                                                         Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)])
        expected = [
            {'sell_in': 9, 'quality': 35},
            {'sell_in': 7, 'quality': 32},
        ]

        for index, expectation in enumerate(expected):
            item = updated_items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    @skip
    def test_quality_goes_up_by_three_for_improving_products_with_5_days_or_less_left(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 4, 11),
                                                         Item("Backstage passes to a TAFKAL80ETC concert", 5, 15)])
        expected = [
            {'sell_in': 3, 'quality': 12},
            {'sell_in': 4, 'quality': 18},
        ]

        for index, expectation in enumerate(expected):
            item = updated_items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_quality_and_sellin_decrease_twice_as_fast_after_sell_by(self):
        updated_items = self.gilded_rose_update_quality([Item("+5 Dexterity Vest", 0, 20),
                                                         Item("Conjured Mana Cake", 0, 6)])
        expected = [
            {'sell_in': -1, 'quality': 18},
            {'sell_in': -1, 'quality': 4},
        ]

        for index, expectation in enumerate(expected):
            item = updated_items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    @skip
    def test_backstage_passes_and_brie_go_to_quality_zero_after_sell_by(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 0, 20),
                                                         Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)])
        expected = [
            {'sell_in': -1, 'quality': 22},
            {'sell_in': -1, 'quality': 0},
        ]

        for index, expectation in enumerate(expected):
            item = updated_items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_sulfuras_the_immutable(self):
        updated_items = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 0, 80)])
        expected = {'sell_in': 0, 'quality': 80}
        item = updated_items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_quality_does_not_increase_past_50(self):
        updated_items = self.gilded_rose_update_quality([Item("Aged Brie", 4, 49)])
        expected = {'sell_in': 3, 'quality': 50}
        item = updated_items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])

    @skip
    def test_conjured_items_decrease_in_quality_twice_as_fast(self):
        updated_items = self.gilded_rose_update_quality([Item("Conjured Mana Cake", 3, 6)])
        expected = {'sell_in': 2, 'quality': 2}
        item = updated_items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])
