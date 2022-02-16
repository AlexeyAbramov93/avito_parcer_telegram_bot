import re

# Ссылка на поиск авито: Автомобили (Иваново:+100км, иномарки до 1млн, от 2007, до 180.000км, бензин, от 1.6л, частные)
url_search_auto='https://www.avito.ru/ivanovo/avtomobili/inomarki/benzin-ASgBAQICAUTgtg2kijQBQOy2DRTetyg?cd=1&f=ASgBAQECAkTyCrCKAeC2DaSKNAFA7LYNFN63KARF~AIWeyJmcm9tIjo5MDAsInRvIjpudWxsfbwVGHsiZnJvbSI6MTU3ODYsInRvIjpudWxsfb4VGHsiZnJvbSI6bnVsbCwidG8iOjE1NTQwfcaaDBd7ImZyb20iOjAsInRvIjoxMDAwMDAwfQ&radius=100&s=104&user=1'

# Классы необходимых заголовков
title_auto = 'link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'
publication_auto = 'date-text'
view_auto = 'title-info-metadata-item title-info-metadata-views'

# Ссылка на поиск авито: Квартиры ()
url_search_flat='https://www.avito.ru/ivanovo/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&f=ASgBAQICAUSSA8YQBEDkByT~UfhRyggkglmEWeYWFOb8Aay~DRSkxzU'

# Классы необходимых заголовков
title_flat = 'link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH'
publication_flat = 'date-text'
view_flat = 'title-info-metadata-item title-info-metadata-views'

