def extract(dicionario, keys):
    return {key: dicionario[key] for key in keys if key in dicionario}


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
resultado = extract(sample_dict, keys)
print(resultado)  # {'name': 'Kelly', 'salary': 8000}
