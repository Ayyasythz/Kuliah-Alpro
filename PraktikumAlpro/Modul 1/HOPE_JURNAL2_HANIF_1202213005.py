







thai_tea_med, es_teh_susu_large,es_teh_leci_small = 15000, 20000,7000
total = thai_tea_med + (3 * (es_teh_susu_large - (es_teh_susu_large * (10/100)))) + es_teh_leci_small
print("===== Es Teh Indoensia =====")
print(f"Harga Es Thai Tea Indonesia = {thai_tea_med}")
print(f"Harga Es Teh Susu Indoensia = {es_teh_susu_large}")
print(f"Harga Es Teh Leci Indonesia = {es_teh_leci_small}")
print(f"Total {total}")