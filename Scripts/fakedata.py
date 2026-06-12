import os
import random
from datetime import datetime, timedelta

import pandas as pd

# 1. Mapowanie lokalizacji
company_1_map = {
    1: "RUDA SLASKA",
    4: "LUBLIN",
    6: "BIALYSTOK",
    7: "KRAKOW",
    10: "WARSZAWA",
    142: "OLSZTYN",
    146: "SUWALKI",
}

company_2_map = {
    1: "POZNAN",
    2: "ASO",
    11: "PARTEX",
    126: "VCAR",
    104: "WROCLAW",
    138: "SOSNOWIEC",
    150: "MAGAZYN CENTRALNY",
}

status_list = [
    "PRZEKIEROWANE",
    "WYSLANE",
    "PRZYDZIELONE",
    "ZAFAKTUROWANE",
    "NIEZREALIZOWANE",
    "WSTRZYMANE",
    "ZAWIESZONE",
]
users_list = ["AK", "MB", "JN", "XYZ", "PL", "TS", "DK"]

auto_parts = [
    "Silnik kompletny",
    "Glowica silnika",
    "Blok silnika",
    "Wal korbowy",
    "Walek rozrzadu",
    "Tlok silnika",
    "Pierscienie tlokowe",
    "Miska olejowa",
    "Pompa oleju",
    "Turbosprezarka",
    "Wtryskiwacz paliwa",
    "Pompa paliwa",
    "Przepustnica",
    "Kolektor ssacy",
    "Kolektor wydechowy",
    "Tlumik koncowy",
    "Tlumik srodkowy",
    "Katalizator",
    "Filtr DPF",
    "Sonda lambda",
    "Chlodnica wody",
    "Wentylator chlodnicy",
    "Termostat",
    "Pasek wieloklinowy",
    "Rolka napinacza",
    "Sprzeglo dwumasowe",
    "Skrzynia biegow",
    "Polos napedowa",
    "Przegub napedowy",
    "Wal napedowy",
    "Amortyzator przod",
    "Amortyzator tyl",
    "Sprezyna zawieszenia",
    "Lozysko amortyzatora",
    "Wahacz poprzeczny",
    "Wahacz wzdluzny",
    "Tuleja wahacza",
    "Sworzen wahacza",
    "Lacznik stabilizatora",
    "Guma stabilizatora",
    "Drazek kierowniczy",
    "Koncowka drazka kierowniczego",
    "Przekladnia kierownicza",
    "Pompa wspomagania",
    "Piasta kola",
    "Lozysko kola",
    "Pompa hamulcowa",
    "Serwo hamulcowe",
    "Zacisk hamulcowy przod",
    "Zacisk hamulcowy tyl",
    "Klocki hamulcowe przod",
    "Klocki hamulcowe tyl",
    "Tarcza hamulcowa",
    "Szczeki hamulcowe",
    "Beben hamulcowy",
    "Plyn hamulcowy",
    "Linka hamulca recznego",
    "Czujnik ABS",
    "Alternator",
    "Rozrusznik",
    "Akumulator 12V",
    "Akumulator AGM",
    "Przewody zaplonowe",
    "Modul zaplonowy",
    "Czujnik polozenia walu",
    "Czujnik temperatury",
    "Przeplywomierz powietrza",
    "Silniczek krokowy",
    "Wlacznik swiatel",
    "Przekaznik pompy",
    "Bezpiecznik glowny",
    "Wiazka elektryczna",
    "Swieca zaplonowa",
    "Swieca zarowa",
    "Cewka zaplonowa",
    "Zderzak przedni",
    "Zderzak tylny",
    "Blotnik lewy",
    "Blotnik prawy",
    "Maska silnika",
    "Klapa bagaznika",
    "Drzwi przednie lewe",
    "Drzwi przednie prawe",
    "Drzwi tylne lewe",
    "Drzwi tylne prawe",
    "Lusterko zewnetrzne lewe",
    "Lusterko zewnetrzne prawe",
    "Reflektor lewy LED",
    "Reflektor prawy LED",
    "Lampa tylna lewa",
    "Lampa tylna prawa",
    "Halogen przeciwmgielny",
    "Szyba czolowa",
    "Szyba boczna",
    "Podnosnik szyby",
    "Zamek drzwi",
    "Klamka zewnetrzna",
    "Fotel kierowcy",
    "Kanapa tylna",
    "Deska rozdzielcza",
    "Kierownica",
    "Poduszka powietrzna",
    "Pasy bezpieczenstwa",
    "Filtr oleju",
    "Filtr kabinowy",
    "Filtr powietrza",
    "Filtr paliwa",
    "Olej silnikowy 5W30",
    "Olej przekladniowy",
    "Plyn chlodniczy",
    "Pioro wycieraczki przod",
    "Pioro wycieraczki tyl",
    "Pompka spryskiwacza",
    "Zbiorniczek wyrownawczy",
    "Kompresor klimatyzacji",
    "Chlodnica klimatyzacji",
    "Czujnik parkowania",
    "Kamera cofania",
]

os.makedirs("Company_1", exist_ok=True)
os.makedirs("Company_2", exist_ok=True)

random.seed(42)
part_pool = {
    str(random.randint(10000, 999999999)): random.choice(auto_parts) for _ in range(200)
}
part_numbers_list = list(part_pool.keys())

sharepoint_body_rows = []
sharepoint_shop_rows = []
lp_counter_body = 1
lp_counter_shop = 1

start_date = datetime(2026, 1, 1)
days_to_generate = 100

# 2. Glowna petla generujaca dane
for day_offset in range(days_to_generate):
    current_date = start_date + timedelta(days=day_offset)
    date_str = current_date.strftime("%Y-%m-%d")
    file_date_suffix = current_date.strftime("%Y_%m_%d")

    for company_id in [1, 2]:
        daily_csv_rows = []
        current_map = company_1_map if company_id == 1 else company_2_map
        num_orders = random.randint(35, 50)

        for _ in range(num_orders):
            order_num = str(random.randint(1000000, 9999999))
            ispe = random.choice(list(current_map.keys()))
            city = current_map[ispe]
            prefix = city[:3].replace(" ", "")

            rand_cat = random.random()
            is_sp_body = False
            is_sp_shop = False

            # --- POPRAWIONA LOGIKA GENEROWANIA NAZW ZAMOWIEN ---
            if rand_cat < 0.03:  # 3% Blacharka
                is_sp_body = True
                customer_order_num = f"{prefix}-{random.randint(100, 999)}X"
            elif rand_cat < 0.10:  # 7% Serwis/Sklep
                is_sp_shop = True
                customer_order_num = f"{prefix}-{random.randint(100, 999)}Y"
            elif rand_cat < 0.90:  # 80% UZUPELNIENIA
                customer_order_num = random.choice(
                    [
                        f"{prefix}-PRIM-{random.randint(10, 99)}",
                        f"{prefix}-{random.randint(10, 99)}@",
                    ]
                )
            elif rand_cat < 0.94:  # 4% Aftermarket (Bez PRIM i @)
                customer_order_num = random.choice(
                    [
                        f"{prefix}-IC-{random.randint(10, 99)}",
                        f"{prefix}-{random.randint(10, 99)}MOT",
                        f"INT-{prefix}",
                    ]
                )
            elif rand_cat < 0.97:  # 3% Subdealer (Bez PRIM, @, IC, MOT)
                subdealer_name = random.choice(["PARTEX", "VCAR", "ASO"])
                customer_order_num = (
                    f"{prefix}-{subdealer_name}-{random.randint(10, 99)}"
                )
            else:  # 3% Systemowe IVECO
                # Kluczowe: usuwamy prefiks miasta, aby wykluczyc konflikt z fraza "ASO"
                customer_order_num = random.choice(
                    [
                        f"109-{random.randint(1000, 9999)}",
                        f"NT-{random.randint(1000, 9999)}",
                    ]
                )

            if company_id == 1:
                order_type = "20" if random.random() < 0.34 else "10"
            else:
                order_type = "20" if random.random() < 0.25 else "10"

            sp_order_type = "pilne" if order_type == "20" else "stock"

            if is_sp_body:
                num_items = 1 if random.random() < 0.10 else random.randint(2, 50)
            elif is_sp_shop:
                num_items = 1 if random.random() < 0.50 else random.randint(2, 10)
            else:
                num_items = random.randint(1, 4)

            order_parts = random.sample(part_numbers_list, num_items)

            sp_dms_ncadea = (
                f"DMS-{random.randint(10000, 99999)}"
                if is_sp_body
                else f"NCA-{random.randint(10000, 99999)}"
            )
            sp_user = random.choice(users_list)
            sp_realizujacy = random.choice(users_list)

            sp_typ_zam = (
                random.choice(["gwarancyjne", "pilne", "stock"])
                if is_sp_body
                else sp_order_type
            )

            for part in order_parts:
                ordered_qty = random.randint(1, 30)
                status = random.choice(status_list)

                if random.random() < 0.20 and ordered_qty > 2:
                    split_1 = random.randint(1, ordered_qty - 1)
                    split_2 = ordered_qty - split_1
                    splits = [split_1, split_2]
                else:
                    splits = [ordered_qty]

                for split_qty in splits:
                    daily_csv_rows.append(
                        {
                            "P.N.": part,
                            "Status": status,
                            "Order Number": order_num,
                            "Customer order number": customer_order_num,
                            "Order date": date_str,
                            "PN Desc": part_pool[part],
                            "Ordered quantity": ordered_qty,
                            "Split quantity": split_qty,
                            "ISPE": ispe,
                            "Ord. Type": order_type,
                        }
                    )

                if is_sp_body:
                    sharepoint_body_rows.append(
                        {
                            "lp": lp_counter_body,
                            "Data zamowienia": date_str,
                            "Oddzial zamawiajacy": city,
                            "Uzytkownik zamawiajacy": sp_user,
                            "numer czesci": part,
                            "Ilosc": ordered_qty,
                            "Typ zamowienia": sp_typ_zam,
                            "Nr zamowienia DMS": sp_dms_ncadea,
                            "Realizujacy zamowienia": sp_realizujacy,
                            "Nr zam": order_num,
                        }
                    )
                    lp_counter_body += 1

                if is_sp_shop:
                    sharepoint_shop_rows.append(
                        {
                            "lp": lp_counter_shop,
                            "Data zamowienia": date_str,
                            "Oddzial zamawiajacy": city,
                            "Uzytkownik zamawiajacy": sp_user,
                            "numer czesci": part,
                            "Ilosc": ordered_qty,
                            "Typ zamowienia": sp_typ_zam,
                            "Nr zamowienia DMS": sp_dms_ncadea,
                            "Realizujacy zamowienia": sp_realizujacy,
                            "Nr zam": order_num,
                        }
                    )
                    lp_counter_shop += 1

        df_daily = pd.DataFrame(daily_csv_rows)
        file_name = f"Company_{company_id}/data_{file_date_suffix}.csv"
        df_daily.to_csv(file_name, index=False, sep=";")

pd.DataFrame(sharepoint_body_rows).to_excel(
    "SharePoint_Naprawy_Blacharskie.xlsx", index=False
)
pd.DataFrame(sharepoint_shop_rows).to_excel("SharePoint_Sklep_Serwis.xlsx", index=False)

print("Wygenerowano oczyszczone dane. Brak bledow nakladania sie kategorii w DAX.")
