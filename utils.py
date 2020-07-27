import json


def ajouter_data_json(heure_chasse_tresor, channel_a_rendre_public, annonce, channel_annonce="", message_a_envoyer=""):
    try:
        with open("data.json", "r") as fichier:
            data = json.load(fichier)
    except Exception as e:
        print(e)
        return f"Erreur : {e}\nZone erreur 1"


    if annonce == True:
        data.append({"heure_chasse":heure_chasse_tresor, "salon_chasse":channel_a_rendre_public, 
                    "annonce":annonce, "salon_annonce":channel_annonce, "message_annonce":message_a_envoyer})
    else:
        data.append({"heure_chasse":heure_chasse_tresor, "salon_chasse":channel_a_rendre_public, 
                    "annonce":annonce})
    

    try:
        with open("data.json", "w") as fichier:
            json.dump(data, fichier)
    except Exception as e:
        print(e)
        return f"Erreur : {e}\nZone erreur 2"

    return "Ok"


def recup_data_json():
    try:
        with open("data.json", "r") as fichier:
            data = json.load(fichier)
        return data
    except Exception as e:
        print(e)
        return f"Erreur : {e}\nZone erreur 3"


def enregister_data_json(data):
    try:
        with open("data.json", "w") as fichier:
            json.dump(data, fichier)
    except Exception as e:
        print(e)
        return f"Erreur : {e}\nZone erreur 4"



if __name__ == '__main__':
    print("Erreur, il faut lancer bot.py")