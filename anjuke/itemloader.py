from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose
from w3lib.html import remove_tags

class AnjukeItemLoader(ItemLoader):
    title_out = TakeFirst()
    price_out = Compose(TakeFirst(), lambda s: s.strip(), remove_tags)
    around_price_out = TakeFirst()
    house_type_out = Join()
    address_out = Compose(TakeFirst(), lambda s: s.strip())
    phone_out = Compose(TakeFirst(), lambda s: s.strip())
    opentime_out = Compose(TakeFirst(), lambda s: s.strip(), remove_tags)
    completetime_out = Compose(TakeFirst(), lambda s: s.strip(), remove_tags)
    url_out = TakeFirst()
