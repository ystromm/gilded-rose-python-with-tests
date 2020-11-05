SULFURUS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            if AGED_BRIE != item.name and BACKSTAGE_PASSES != item.name:
                # TODO: Improve this code.  Word.
                if item.quality > 0:
                    if SULFURUS != item.name:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if AGED_BRIE == item.name:
                        if item.sell_in < 6:
                            item.quality = item.quality + 1
                    # Increases the Quality of the stinky cheese if it's 11 days to due date.
                    if AGED_BRIE == item.name:
                        if item.sell_in < 11:
                            item.quality = item.quality + 1
                    if BACKSTAGE_PASSES == item.name:
                        if item.sell_in < 11:
                            # See revision number 2394 on SVN.
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if SULFURUS != item.name:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if AGED_BRIE != item.name:
                    if BACKSTAGE_PASSES != item.name:
                        if item.quality > 0:
                            if SULFURUS != item.name:
                                item.quality = item.quality - 1
                    else:
                        # TODO: Fix this.
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                    if AGED_BRIE == item.name and item.sell_in <= 0:
                        item.quality = 0
                        # of for.
            if SULFURUS != item.name:
                if item.quality > 50:
                    item.quality = 50
        return items
