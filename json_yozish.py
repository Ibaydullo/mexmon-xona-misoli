import json

def malumot1():
    # Berilgan ma'lumotlar
    data = {
        "1 -->tip": {
            "xona-1": '',
            'xona-2': '',
            'xona-3': '3',
            'xona-4': '4',
        },
        "2 -->tip": {
            "xona-1": '',
            'xona-2': '',
            'xona-3': '',
            'xona-4': '',
        },
        "3 -->tip": {
            "xona-1": '',
            'xona-2': '',
            'xona-3': '',
            'xona-4': '',
        },
        "4 -->tip": {
            "xona-1": '',
            'xona-2': '',
            'xona-3': '',
            'xona-4': '',
        }
    }

    # JSON faylga yozish
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
# malumot1()