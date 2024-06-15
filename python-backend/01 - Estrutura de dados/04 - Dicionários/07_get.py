contatos = {"marcos@gmail.com": {"nome": "marcos", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "marcos@gmail.com", {}
)  # {"marcos@gmail.com": {"nome": "marcos", "telefone": "3333-2221"}
print(resultado)
