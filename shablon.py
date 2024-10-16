from m import *
import json
print('Assalom aleykum bizning medatamonxonamizga dataush kelibsiz')
y = True
while y :
    a = "xona roydataati"
    print("\n 1 ----> xona roydataati")
    xona_royxat = int(input("Tanlang:"))
    malumot()
    print("Mexmo qoshmoqchi bolsangiz 1 tanlang o'chirmoqchi bolsangiz 2 tanlang:")
    if xona_royxat == 1:
        mexmon = int(input("Tanlang:"))
        # JSON faylini o'qish
        with open('data.json', 'r+') as file:
            data = json.load(file)
        tip_royxati()
        tip_for = int(input("Tanlang:"))
        if mexmon == 1:
            if f"{tip_for} -->tip" in data:
                # for i in data[f"{tip_for} -->tip"]:
                #     print(i)

                # Qiymatni chiqarish
                if f"{tip_for} -->tip" in data:
                    rooms = data[f"{tip_for} -->tip"]

                    if isinstance(rooms, dict):  # Agar rooms lug'at bo'lsa
                        for key, value in rooms.items():
                            if value.strip():  # Agar qiymat bo'sh bo'lmasa
                                print(f"\t{key}: '{value}'Bo'sh emas")
                            else:  # Agar qiymat bo'sh bo'lsa
                                print(f"\t{key}: 'Bo'sh'")
                    else:
                        print(f"Xato: '{tip_for} -->tip' uchun 'rooms' qiymati lug'at emas: {rooms}")
                else:
                    print(f"'{tip_for} -->tip' kaliti mavjud emas.")

                add_delet_xona = int(input("Tanlang:"))
                if f"xona-{add_delet_xona}" in data[f"{tip_for} -->tip"]:
                    value = data[f"{tip_for} -->tip"][f"xona-{add_delet_xona}"]
                    if value.strip() == "":  # Agar qiymat bo'sh bo'lsa (faqat bo'sh joy)
                        print(f"{add_delet_xona} qiymati bo'sh!")
                        ism = input("Ism kriting:")
                        new_data = {f'xona-{add_delet_xona}': f'{ism}'}
                        data[f"{tip_for} -->tip"][f'xona-{add_delet_xona}'] = f'{ism}'
                        with open('data.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)
                        malumot()
                    else:
                        print(f"{add_delet_xona} qiymati: '{value}' - Bosh emas")
                        r = int(input("O'chirmoqchi bo'lsangiz 1 ni bosin: "))
                        if r == 1:
                            value = data[f"{tip_for} -->tip"][f"xona-{add_delet_xona}"]
                            print(f"{add_delet_xona} qiymati bo'sh!")
                            new_data = {f'xona-{add_delet_xona}': ""}
                            data[f"{tip_for} -->tip"][f'xona-{add_delet_xona}'] = ""
                            with open('data.json', 'w', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                            malumot()
                        else:
                            # JSON faylini o'qish
                            with open('data.json', 'r', encoding='utf-8') as file:
                                data = json.load(file)
                            # Ma'lumotlarni chiqarish
                            for tip, rooms in data.items():
                                print(tip)
                                for key, value in rooms.items():
                                    if value:  # Agar qiymat bo'sh bo'lmasa
                                        print(f"\t{key}: '{value}'")
                                    else:  # Agar qiymat bo'sh bo'lsa
                                        print(f"\t{key}: '{value}'")
                else:
                    # del data[f"{add_delet} -->tip"][f"xona-{add_delet_xona}"]
                    print(f"{tip_for} kaliti mavjud emas.")
            else:
                pass
        elif y == 2:
            if f"{tip_for} -->tip" in data:
                add_delet_xona = int(input("xona raqamini tanlang (1-4): "))
                if f"xona-{add_delet_xona}" in data[f"{tip_for} -->tip"]:
                    value = data[f"{tip_for} -->tip"][f"xona-{add_delet_xona}"]
                    print(f"{add_delet_xona} qiymati: '{value}' - Bosh emas")
                    r = int(input("O'chirmoqchi bo'lsangiz 1 ni bosin: "))
                    if r == 1:
                        value = data[f"{tip_for} -->tip"][f"xona-{add_delet_xona}"]
                        print(f"{add_delet_xona} qiymati bo'sh!")
                        new_data = {f'xona-{add_delet_xona}': ""}
                        data[f"{tip_for} -->tip"][f'xona-{add_delet_xona}'] = ""
                        with open('data.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)
                        print(data)
                    else:
                        # JSON faylini o'qish
                        with open('data.json', 'r', encoding='utf-8') as file:
                            data = json.load(file)

                        # Ma'lumotlarni chiqarish
                        for tip, rooms in data.items():
                            print(tip)
                            for key, value in rooms.items():
                                if value:  # Agar qiymat bo'sh bo'lmasa
                                    print(f"\t{key}: {value} - Bosh emas")
                                else:  # Agar qiymat bo'sh bo'lsa
                                    print(f"\t{key}: {value} - Bosh")
                else:
                    print(f"{tip_for} kaliti mavjud emas.")
            else:
                pass
        else:
            print("Kechirasz bunday malumot yoq")

y = False




