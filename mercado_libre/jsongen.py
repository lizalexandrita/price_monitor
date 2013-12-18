# coding:utf-8

# Lib imports
import json

def json_update(item_id, date, price):
    
    with open('mercado_libre/items.json','r') as f:
        data = json.load(f)
    
    for k,i in enumerate(data['items']):
        if data['items'][k]['item_id'] == item_id:
            data['items'][k]['price'].append({date: price})
    
    with open('mercado_libre/items.json', 'w') as f:
        json.dump(data, f, encoding="utf-8", sort_keys=True, indent=2, separators=(',', ': '))
        
    print price, data
    return data