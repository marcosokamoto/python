contatos = {"marcos@gmail.com": {"nome": "Marcos", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["marcos@gmail.com"] = {"nome": "Gui"}

print(contatos["marcos@gmail.com"])  # {"nome": "marcos", "telefone": "3333-2221"}

print(copia["marcos@gmail.com"])  # {"nome": "Gui"}
