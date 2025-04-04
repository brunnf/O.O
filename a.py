contatos = []

def main():
    
    while True:
        print("\n" + "="*40)
        print("📒 AGENDA TELEFÔNICA".center(40))
        print("="*40)
        print("1️⃣  Adicionar Contato")
        print("2️⃣  Listar Contatos")
        print("3️⃣  Editar Contato")
        print("4️⃣  Remover Contato")
        print("5️⃣  Sair")
        print("="*40)

        opcao = input("👉 Escolha uma opção (1 a 5): ")
        
        #======================================================================
        #1️⃣Adicionar Contato:
        #======================================================================

        if opcao == "1":
            nome = input("digite o nome do contato\n")
            telefone = input("digite o telefone do contato\n")
            contatos.append([nome, telefone])
            print("contato adicionado com sucesso!")

        #======================================================================
        #2️⃣Listar Contatos:
        #======================================================================

        elif opcao == "2":
            if not contatos:
                print("agenda vazia")
            else:
                for i, c in enumerate(contatos):
                    print(f"{i+1}. Nome: {c[0]} - Telefone: {c[1]}")

        #======================================================================
        #3️⃣Editar Contatos:
        #======================================================================

        elif opcao == "3":
            if not contatos:
                print("agenda vazia")
            else:
                for i, c in enumerate(contatos):
                    print(f"{i+1}. Nome: {c[0]} - Telefone: {c[1]}")
                indice = int(input("Número do contato para editar: ")) - 1
                if 0 <= indice < len(contatos):
                    novo_nome = input("Novo nome (ou Enter pra manter): ")
                    novo_tel = input("Novo telefone (ou Enter pra manter): ")
                    if novo_nome:
                        contatos[indice][0] = novo_nome
                    if novo_tel:
                        contatos[indice][1] = novo_tel
                    print("Contato atualizado!")

        #======================================================================
        #4️⃣Remover contatos:
        #======================================================================

        elif opcao == "4":
            if not contatos:
                print("Agenda vazia!")
            else:
                for i, c in enumerate(contatos):
                    print(f"{i+1}. Nome: {c[0]} - Telefone: {c[1]}")
                indice = int(input("Número do contato para remover: ")) - 1
                if 0 <= indice < len(contatos):
                    contato_removido = contatos.pop(indice)
                    print(f"Contato '{contato_removido[0]}' removido!")

        #======================================================================
        #5️⃣Encerrando programa:
        #======================================================================

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
main()