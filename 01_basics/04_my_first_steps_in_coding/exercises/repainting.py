nyln_sq_m = int(input())
paint_ltr = int(input())
desolv_ltr = int(input())
workers_hrs = int(input())

total_nyln = nyln_sq_m + 2
total_paint = paint_ltr + (paint_ltr * 0.1)
total_materials = total_nyln * 1.5 + total_paint * 14.5 + desolv_ltr * 5 + 0.4
total_workers = total_materials * 0.3 * workers_hrs

final_price = total_materials + total_workers
print(final_price)