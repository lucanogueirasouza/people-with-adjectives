nome = []  
while True: 
    print("----Pessoas com adjetivos----")
    escolha = int(input("1 - Add Nomes\n2 - Ver Todos\n3 - Filtrar por Adjetivos\n4 - Retirar alguma pessoa\n5 - Sair\nDigite: "))
    if escolha == 1: 
        pessoa = str(input("Digite um nome: ")).capitalize()
        adjetivo = str(input("Digite o Adjetivo: ")).capitalize()
        nome.append({"Pessoa": pessoa, "Adjetivo": adjetivo})  
        print(f"{pessoa} adicionado!")
    elif escolha == 2: 
        if nome:
            print("Lista de Pessoas:")
            for p in nome:
                print(f"Nome: {p["Pessoa"]}, Adjetivo: {p["Adjetivo"]}")
        else:
            print("Nenhuma pessoa ainda...")
    elif escolha == 3: 
        adjetivoescolha = str(input("Digite o adjetivo para filtrar: ")).capitalize()
        filtrados = [p for p in nome if p["Adjetivo"] == adjetivoescolha]  
        if filtrados:
            print(f"Pessoas com o adjetivo {adjetivoescolha}:")
            for p in filtrados:
                print(f"{p["Pessoa"]}")
        else:
            print("Não existe pessoas com este adjetivo.")
    elif escolha == 4:
        pessoa_retirar = str(input("Digite o nome da pessoa para retirar: ")).capitalize()
        nomes_lista = [p["Pessoa"] for p in nome] 
        if pessoa_retirar in nomes_lista:
            encontrar_nome = nomes_lista.index(pessoa_retirar)  
            nome.pop(encontrar_nome)  
            print(f"{pessoa_retirar} foi retirado(a) com sucesso!")
        else:
            print ("Nao tem pessoas com esse nome")
    elif escolha == 5: 
        print("Saindo...")
        break  
    else:
        print("Opção Inválida!")