#class Persona:
 #   def __init__(self,nome,cognome):
  #      self._nome = nome
   #     self._cognome = cognome 
    #def __repr__(self):
     #   return ""    
#ar = Persona ("Andrea" "Ribuoli")
#print(ar)  


# Classe base Persona
class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

    def __repr__(self):
        return f"Persona(nome={self._nome}, cognome={self._cognome})"

# Classe Studente derivata da Persona
class Studente(Persona):
    def __init__(self, nome, cognome, voti):
        super().__init__(nome, cognome)
        self.voti = voti  # Lista di voti

    def __repr__(self):
        return f"Studente(nome={self._nome}, cognome={self._cognome}, voti={self.voti})"

# Classe Insegnante derivata da Persona
class Insegnante(Persona):
    def __init__(self, nome, cognome, materie_insegnate):
        super().__init__(nome, cognome)
        self.materie_insegnate = materie_insegnate  # Lista di materie insegnate

    def __repr__(self):
        return f"Insegnante(nome={self._nome}, cognome={self._cognome}, materie_insegnate={self.materie_insegnate})"

# Esempi di utilizzo
ar = Persona("Andrea", "Ribuoli")
print(ar)  # Output: Persona(nome=Andrea, cognome=Ribuoli)

# Creazione di un oggetto Studente
studente1 = Studente("Maria", "Bianchi", [8, 9, 10])
print(studente1)  # Output: Studente(nome=Maria, cognome=Bianchi, voti=[8, 9, 10])

# Creazione di un oggetto Insegnante
insegnante1 = Insegnante("Luca", "Verdi", ["Matematica", "Fisica"])
print(insegnante1)  # Output: Insegnante(nome=Luca, cognome=Verdi, materie_insegnate=['Matematica', 'Fisica'])