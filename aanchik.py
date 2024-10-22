import cianparser

moscow_parser = cianparser.CianParser(location="Московская область")
data = moscow_parser.get_flats(deal_type="sale", rooms=("all"), with_saving_csv=True, additional_settings={"start_page":1, "end_page":54})

print(data[0])