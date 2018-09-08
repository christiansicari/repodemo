# i dizionari sono strutture dati built in basati sul modello chiave-valore
# hanno una struttura molto simile a JSON
# struttura : {key1: value1, key2: value2}
# un qualunque oggetto immutabile puo essere usato come chiave: tuple,stringe, numeri
# le chiavi sono oggetti mutabili

_dict = {"primo": 1, 2: 3, (1, 2, 3): 10}
print(type(_dict))

#ottenere valore tramite chiave

if (1, 2, 3) in _dict:  #verifico che esista quella chiave
    print(_dict[(1,2,3)])

# aggiungo valore a dizionario con nuova chiave
_dict["abc"] = "Ciao"
print(_dict)

# metodi per dizionario

print("Chiavi del dizionario: ", _dict.keys())
print("Elementi del dizionario: ", _dict.items())  #restituisce una lista di tuple, ogni tupla e' la coppia chiave valore
print("Valori del dizionario:" , _dict.values())
print("Rimozione e restituzione elemento dizionario con chiave (1,2,3): ", _dict.pop((1, 2, 3)))

_dict2 = {"secondo": "Mondo"}
_dict.update(_dict2)
print("Concatenazione dizionari: ", _dict)

_dict2.clear()
print("Eliminazione lista:", _dict2)

#aggiungo una modifica per testare git
print("git"
