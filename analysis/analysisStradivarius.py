import json

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0 
    total = sum(numbers)
    average = total / len(numbers)
    return average

with open('../data/productsStradivarius.json', 'r') as jsonFile:
    data = json.load(jsonFile)

prices = []
categoryPrices = []
todo = []
sections = []
for category in data['categories']:
    if category['section'] is None:
        for items in category['products']:
            prices.append(items['price'])
        
        todo.append({ "name": category['name'], "number of items": category['quantity'], "average price": round(calculate_average(prices),2) })
        prices = []

    else:
        for section in category['section']:
            for items in section['products']:
                categoryPrices.append(items['price'])
                prices.append(items['price'])

            sections.append({ "name": section['name'], "number of items": section['quantity'], "average price": round(calculate_average(prices),2) })
            prices = []

        todo.append({ "name": category['name'], "number of items": category['quantity'], "average price": round(calculate_average(categoryPrices),2), "sections": sections })
        categoryPrices = []
        sections = []


with open('../data/analysisStradivarius.json', 'w', encoding='utf-8') as output_file:
    jsonData = { "categories": todo }
    json.dump(jsonData, output_file, indent=4)
