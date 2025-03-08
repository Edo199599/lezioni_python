# codice del linguaggio predefinito del dispositivo
linguaggio = 'it'

# analisi valore acquisito per impostazione GUI (Graphic User Interface)
match linguaggio:
    case "fr":
        print("impostiamo interfaccia in francese")
    case "it" | "IT":
        print("impostiamo interfaccia in italiano")
    case "de":
        print("impostiamo interfaccia in tedesco")
    case _:
        print("impostiamo interfaccia in inglese")