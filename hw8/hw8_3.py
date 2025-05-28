import json
import pickle

products = [
    {"id": 1, "name": "Человек Печенька", "price": 123, "category": "Ничего"},
    {"id": 2, "name": "Run Table", "price": 456, "category": "What"},
    {"id": 3, "name": "Деньги Облако", "price": 789, "category": "Фигня"},
    {"id": 4, "name": "Sleep Banana", "price": 321, "category": "Nope"},
    {"id": 5, "name": "Кровать Понимать", "price": 654, "category": "Странности"},
    {"id": 6, "name": "Jump Emotion", "price": 987, "category": "Absurd"},
    {"id": 7, "name": "Смеяться Вода", "price": 159, "category": "Невідомо"},
    {"id": 8, "name": "Chair Fly", "price": 753, "category": "None"},
    {"id": 9, "name": "Бежать Стена", "price": 951, "category": "Мрак"},
    {"id": 10, "name": "Dream Potato", "price": 258, "category": "Nothing"}
]

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

with open('products.pcl', 'wb') as f:
    pickle.dump(products, f)
