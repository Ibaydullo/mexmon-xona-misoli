
# import json
#
# def malumot():
#     # Berilgan ma'lumotlar
#     data = {
#         "1tip": {
#             "xona-1": '1',
#             'xona-2': '2',
#             'xona-3': '3',
#             'xona-4': '4',
#         },
#         "2 -->tip": {
#             "xona-1": '',
#             'xona-2': '',
#             'xona-3': '',
#             'xona-4': '',
#         },
#         "3 -->tip": {
#             "xona-1": '',
#             'xona-2': '',
#             'xona-3': '',
#             'xona-4': '',
#         },
#         "4 -->tip": {
#             "xona-1": '',
#             'xona-2': '',
#             'xona-3': '',
#             'xona-4': '',
#         }
#     }
#
#     # JSON faylga yozish
#     with open('data.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
# # malumot()

# JSON faylini o'qish





# Barcha xona qiymatlarini tekshirish

# import json
# for tip, rooms in data.items():
#     print(tip)
#     for key, value in rooms.items():
#         if value:  # Agar qiymat bo'sh bo'lmasa
#             print(f"\t{key}: {value} - Bosh emas")
#         else:  # Agar qiymat bo'sh bo'lsa
#             print(f"\t{key}: {value} - Bosh")
#     #











import json

# JSON faylini o'qish
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
def malumot():


    # Ma'lumotlarni chiqarish
    for tip, rooms in data.items():
        print(tip)
        for key, value in rooms.items():
            if value:  # Agar qiymat bo'sh bo'lmasa
                print(f"\t{key}: {value} - Bosh emas")
            else:  # Agar qiymat bo'sh bo'lsa
                print(f"\t{key}: {value} - Bosh")
def tip_royxati():
    for tip, rooms in data.items():
        print(tip)
        # for key, value in rooms.items():
        #     if value:  # Agar qiymat bo'sh bo'lmasa
        #         print(f"\t{key}: '{value}'")
        #     else:  # Agar qiymat bo'sh bo'lsa
        #         print(f"\t{key}: '{value}'")

def xona_fun():
    for tip, rooms in data.items():
        for key, value in rooms.items():
            if value:  # Agar qiymat bo'sh bo'lmasa
                print(f"\t{key}: '{value}'")
            else:  # Agar qiymat bo'sh bo'lsa
                print(f"\t{key}: '{value}'")





