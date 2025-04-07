from package.contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def iniciar(self):
        while True:
            print("\n" + "=" * 40)
            print("📒 AGENDA TELEFÔNICA".center(40))
            print("=" * 40)
            print("1️⃣  Adicionar Contato")
            print("2️⃣  Listar Contatos")
            print("3️⃣  Editar Contato")
            print("4️⃣  Remover Contato")
            print("5️⃣  Sair")
            print("=" * 40)

            opcao = input("👉 Escolha uma opção (1 a 5): ")

            if opcao == "1":
                self.adicionar_contato()
            elif opcao == "2":
                self.listar_contatos()
            elif opcao == "3":
                self.editar_contato()
            elif opcao == "4":
                self.remover_contato()
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def adicionar_contato(self):
        nome = input("Digite o nome do contato:\n")
        telefone = input("Digite o telefone do contato:\n")
        self.contatos.append(Contato(nome, telefone))
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia!")
        else:
            for i, contato in enumerate(self.contatos):
                print(f"{i + 1}. {contato}")

    def editar_contato(self):
        if not self.contatos:
            print("Agenda vazia!")
            return
        self.listar_contatos()
        try:
            indice = int(input("Número do contato para editar: ")) - 1
            if 0 <= indice < len(self.contatos):
                novo_nome = input("Novo nome (ou Enter pra manter): ")
                novo_tel = input("Novo telefone (ou Enter pra manter): ")
                if novo_nome:
                    self.contatos[indice].nome = novo_nome
                if novo_tel:
                    self.contatos[indice].telefone = novo_tel
                print("Contato atualizado!")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Entrada inválida!")

    def remover_contato(self):
        if not self.contatos:
            print("Agenda vazia!")
            return
        self.listar_contatos()
        try:
            indice = int(input("Número do contato para remover: ")) - 1
            if 0 <= indice < len(self.contatos):
                contato_removido = self.contatos.pop(indice)
                print(f"Contato '{contato_removido.nome}' removido!")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Entrada inválida!")
