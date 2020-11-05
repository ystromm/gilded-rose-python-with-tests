SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            if SULFURAS == item.name:
                #do something with sulfuris
                #item.quality = 80
                pass
            elif AGED_BRIE == item.name:
                GildedRose.update_aged_brie(item)
                GildedRose.cap_quality(item)
            elif BACKSTAGE_PASSES == item.name:
                GildedRose.update_backstage_passes(item)
                GildedRose.cap_quality(item)
            elif item.name == 'Conjured Mana Cake':
                pass
            else:
                GildedRose.update_item(item)
                GildedRose.cap_quality(item)
        return items

    def cap_quality(item):
        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def update_item(item):
        # TODO: Improve this code.  Word.
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1

    @staticmethod
    def update_backstage_passes(item):
        if item.quality < 50:
            item.quality = item.quality + 1
            # Increases the Quality of the stinky cheese if it's 11 days to due date.
            if item.sell_in < 11:
                # See revision number 2394 on SVN.
                if item.quality < 50:
                    item.quality = item.quality + 1
            # Increases the Quality of Backstage Passes if the Quality is 6 or less.
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            # TODO: Fix this.
            item.quality = 0

    @staticmethod
    def update_aged_brie(item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 6:
                item.quality = item.quality + 1
            # Increases the Quality of the stinky cheese if it's 11 days to due date.
            if item.sell_in < 11:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1
            item.quality = 0
