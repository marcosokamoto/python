contato = {"nome": "marcos", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "marcos"
print(contato)  # {'nome': 'marcos', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'marcos', 'telefone': '3333-2221', 'idade': 28}
