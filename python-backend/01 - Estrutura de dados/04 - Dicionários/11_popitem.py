contatos = {"marcos@gmail.com": {"nome": "marcos", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('marcos@gmail.com', {'nome': 'marcos', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
