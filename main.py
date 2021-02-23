from coffee import MENU
quarters = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def machine():
    escolha = input("O que você gostaria? (espresso, latte, cappuccino): ")


    def coins():
        q1 = quarters * float(input("Quantos quarters?: "))
        d1 = dime * float(input("Quantos Dimes?: "))
        n1 = nickel * float(input("Quantos Nickles?: "))
        p1 = penny * float(input("Quantos Pennies?: "))
        if escolha == "espresso":
            pagamento = q1 + d1 + n1 + p1
            if pagamento >= MENU["espresso"]["cost"]:
                troco = pagamento - MENU["espresso"]["cost"]
                print(f"Aqui está ${troco} de troco")
                print("Aqui está o seu Espresso!")
                machine()
            else:
                print("desculpe, dinheiro insuficiente. Devolvendo dinheiro.")
                pagamento == 0
                machine()

        elif escolha == "latte":
            pagamento = q1 + d1 + n1 + p1
            if pagamento >= MENU["espresso"]["cost"]:
                troco = pagamento - MENU["espresso"]["cost"]
                print(f"Aqui está ${troco} de troco")
                print("Aqui está o seu Espresso!")
                machine()
            else:
                print("desculpe, dinheiro insuficiente. Devolvendo dinheiro.")
                pagamento == 0
                machine()


        elif escolha == "cappuccino":
            pagamento = q1 + d1 + n1 + p1
            if pagamento >= MENU["espresso"]["cost"]:
                troco = pagamento - MENU["espresso"]["cost"]
                print(f"Aqui está ${troco} de troco")
                print("Aqui está o seu Espresso!")
                print(pagamento)
                machine()
            else:
                print("desculpe, dinheiro insuficiente. Devolvendo dinheiro.")
                pagamento == 0
                machine()


    def coffee_machine():

        if escolha == "espresso":
            print("por favor, insira as moedas.\n")
            coins()
        elif escolha == "latte":
            print("por favor, insira as moedas.\n")
            coins()
        elif escolha == "cappuccino":
            print("por favor, insira as moedas.\n")
            coins()

    coffee_machine()
machine()
