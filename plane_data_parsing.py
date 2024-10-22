import cianparser
from time import sleep

a = 0
while a < 52:
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=("studio"),
        with_saving_csv=True,
        additional_settings={"start_page": 125 + a, "end_page": 127 + a},
        with_extra_data=True,
    )
    sleep(120)
    a += 2
print(data[0])