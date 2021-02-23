from coffee import MENU
from coffee import resources

quarters = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01


def machine():
    escolha = input("O que você gostaria? (espresso, latte, cappuccino): ")

    def coins():
        q1 = quarters * float(input("Quantos quarters? ($0,25 cada): "))
        d1 = dime * float(input("Quantos Dimes?($0,10 cada): "))
        n1 = nickel * float(input("Quantos Nickles?($0,05 cada): "))
        p1 = penny * float(input("Quantos Pennies?($0,01 cada): "))
        if escolha == "espresso":
            pagamento = q1 + d1 + n1 + p1
            if pagamento >= MENU["espresso"]["cost"]:
                troco = pagamento - MENU["espresso"]["cost"]
                print(f"Aqui está ${troco:.2f} de troco")
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
                print(f"Aqui está ${troco:.2f} de troco")
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
                print(f"Aqui está ${troco:.2f} de troco")
                print("Aqui está o seu Espresso!")
                print(pagamento)
                machine()
            else:
                print("desculpe, dinheiro insuficiente. Devolvendo dinheiro.")
                pagamento == 0
                machine()

    def coffee_machine():

        if escolha == "espresso":
            if resources["water"] - MENU["espresso"]["ingredients"]["water"] >= 0:
                if resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] >= 0:
                    resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                    print("por favor, insira as moedas.\n")
                    coins()
                else:
                    print("Desculpe, não há café suficiente.")
                    machine()
            else:
                print("Desculpe, não há água suficiente.")
                machine()
        elif escolha == "latte":
            if resources["water"] - MENU["latte"]["ingredients"]["water"] >= 0:
                if resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] >= 0:
                    if resources["milk"] - MENU["latte"]["ingredients"]["milk"] >= 0:
                        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                        print("por favor, insira as moedas.\n")
                        coins()
                    else:
                        print("Desculpe, não há leite suficiente.")
                        machine()
                else:
                    print("Desculpe, não há café suficiente.")
                    machine()
            else:
                print("Desculpe, não há água suficiente.")
                machine()
        elif escolha == "cappuccino":
            if resources["water"] - MENU["cappuccino"]["ingredients"]["water"] >= 0:
                if resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] >= 0:
                    if resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"] >= 0:
                        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                        print("por favor, insira as moedas.\n")
                        coins()
                    else:
                        print("Desculpe, não há leite suficiente.")
                        machine()
                else:
                    print("Desculpe, não há café suficiente.")
                    machine()
            else:
                print("Desculpe, não há água suficiente.")
                machine()
        elif escolha == "report":
            print(resources)
            machine()
        else:
            machine()

    coffee_machine()


machine()
