contatos = {"marcos@gmail.com": {"nome": "marcos", "telefone": "3333-2221"}}

resultado = contatos.pop("marcos@gmail.com")  # {'nome': 'marcos', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("marcos@gmail.com", {})  # {}
print(resultado)
