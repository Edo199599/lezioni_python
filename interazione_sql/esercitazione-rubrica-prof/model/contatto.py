import re
from exceptions.validation_exception import ValidationException

class Contatto:

    schema_validazione = {
        "Nome": "[a-zA-Zàèìòù\\s']{1,50}",
        "Cognome": "[a-zA-Zàèìòù\\s']{1,50}",
        "Telefono": "[\\d\\s+]{1,20}",
        "Mail": "[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z]{2,6}",
        "Via": "[a-zA-Z\\dàèìòù\\s']{1,50}",
        "Civico": "[a-zA-Z\\d\\s/-]{1,10}",
        "Cap": "[\\d]{5}",
        "Comune": "[a-zA-Zàèìòù\\s']{1,50}",
        "Provincia": "[A-Za-z]{2}"
        # A-Z vuol dire che accetta solo lettere maiuscole
        # \\s significa che accetta anche spazi
        # ' significa che accetta anche gli apostrofi
        # il numero tra {} indica il numero di caratteri accettati
        # \\d\\ significa che accetta anche i numeri
    }

    # inizializzazione oggetto e struttura
    def __init__(self, id=None, nome=None, cognome=None, telefono=None, mail=None, indirizzo=None):
        self.id = id
        self.nome = nome.title()
        self.cognome = cognome.title()
        self.telefono = telefono
        self.mail = mail.lower()
        self.indirizzo = indirizzo # gestione relazione 1:1 con indirizzo

    # rappresentazione testuale
    def __repr__(self):
        return (f"Contatto {self.id}:\n{self.nome} {self.cognome}\nTel: {self.telefono}\n"
                f"Mail: {self.mail}\n{self.indirizzo}")

    # validazione dinamica dei dati in input (registrazione)
    @classmethod
    def validazione(cls, input, campo):
        if not re.fullmatch(cls.schema_validazione[campo], input):
            raise ValidationException(f"Errore Campo {campo}")