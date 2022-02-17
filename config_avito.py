import re


# Ссылка на поиск авито: Автомобили (Иваново:+100км, иномарки до 1млн, от 2006, до 250.000км, бензин, от 1.6л, частные)
url_search_auto='https://www.avito.ru/ivanovo/avtomobili/inomarki/benzin-ASgBAQICAUTgtg2kijQBQOy2DRTetyg?cd=1&f=ASgBAQECAUTgtg2kijQBQOy2DRTetygERfgCFnsiZnJvbSI6ODk5LCJ0byI6bnVsbH28FRh7ImZyb20iOjE1Nzg2LCJ0byI6bnVsbH2~FRh7ImZyb20iOm51bGwsInRvIjoxNTU1NH3GmgwXeyJmcm9tIjowLCJ0byI6MTAwMDAwMH0&radius=100&s=104&user=1'
# Классы необходимых заголовков
title_auto = 'link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'
publication_auto = 'date-text'
view_auto = 'title-info-metadata-item title-info-metadata-views'


# Ссылка на поиск авито: Квартиры ()
url_search_flat='https://www.avito.ru/ivanovo/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?cd=1&f=ASgBAQICAUSSA8YQBUDkByT~UfhR5gcUjFLKCCSCWYRZ5hYU5vwBrL4NFKTHNQ&s=104'
# Классы необходимых заголовков
title_flat = 'link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'
publication_flat = 'date-text'
view_flat = 'title-info-metadata-item title-info-metadata-views'


# Ссылка на поиск Циан: Квартиры ()
url_search_flat_cian = 'https://ivanovo.cian.ru/cat.php?deal_type=sale&engine_version=2&floornl=1&house_material%5B0%5D=1&house_material%5B1%5D=2&house_material%5B2%5D=8&is_first_floor=0&object_type%5B0%5D=1&offer_type=flat&region=4767&room2=1&room3=1&sort=creation_date_desc&with_neighbors=0'
# Классы необходимых заголовков
title_flat_cian = '_93444fe79c--link--eoxce'
# publication_flat = 'date-text'
# view_flat = 'title-info-metadata-item title-info-metadata-views'