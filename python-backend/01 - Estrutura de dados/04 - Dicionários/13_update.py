contatos = {"marcos@gmail.com": {"nome": "marcos", "telefone": "3333-2221"}}

contatos.update({"marcos@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'marcos@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'marcos@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
