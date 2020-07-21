#---------------
import discord
import sys
import os
import time
import json
import datetime
import asyncio
#---------------

## La partie liste n'a pas été testée. A tester


class Bot():
    def __init__(self):

        self.bot()

    def bot(self):
        TOKEN = None
        with open("token.json") as fichier:
            TOKEN = json.load(fichier)["token"]

        if TOKEN == None:
            print("ERREUR PAS DE TOKEN !!!")
            sys.exit(0)


        PREFIX = None
        with open("token.json") as fichier:
            PREFIX = json.load(fichier)["prefix"]

        if PREFIX == None:
            print("ERREUR PAS DE PREFIX !!!")
            sys.exit(0)


        bot = discord.Client()
        
        @bot.event
        async def on_ready():
            jour = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
            print()
            print('------')
            print()
            print('Bot démarré')
            print()
            print(jour)
            print()
            print(bot.user.name)
            print(bot.user.id)
            print(f"Nb de users : {len(set(bot.get_all_members()))}")
            print('------')


        @bot.event
        async def on_message(message):

            if message.author == bot.user:
                return

            serveur = bot.get_guild(662642246763544586)
            channel = bot.get_channel(664149572964188196)

            if message.content.startswith(f"{PREFIX}kill") and message.author.id == 257255974480510976:
                print("------------------------\nKilled\n------------------------")
                await bot.logout()
                return

            if message.content.startswith(f"{PREFIX}help") or message.content.startswith(f"{PREFIX}aide"):
                embed = discord.Embed(title="Aide :", color=0x00ff00)
                # embed.add_field(name=f"{PREFIX}liste", value=f"Liste les différentes actions déjà programmées", inline=False)
                embed.add_field(name=f"{PREFIX}ajouter", value=f"Programmer une chasse au trésor", inline=False)
                await message.channel.send(embed=embed)
                return

            if message.content.startswith(f"{PREFIX}ajouter"):
                if message.author.id != 161908043439800320:
                    await message.channel.send("Erreur, tu n'as pas la permission de faire ça.")
                    return

                text_msg = "**__Menu pour ajouter une action__**\n\n:one: = Programmer une chasse au trésor"#\n:two: = Envoyer un message dans un channel précis à une heure précise"
                msg_base = await message.channel.send(text_msg)
                await msg_base.add_reaction("1️⃣")
                # await msg.add_reaction("two")

                
                def check(reaction, user):
                    return user == message.author and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣")

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    await msg_base.edit(content="Trop Tard...")
                    return
                

                if reaction.emoji == "1️⃣":
                    text_msg = "**__Programmer une chasse au trésor__**\n\nEcrivez le channel de la future chasse au trésor" \
                               "(Il faut mettre # devant le nom. Le salon doit être " \
                               "cliquable.) "
                    # await msg_base.clear_reactions()
                    # await msg_base.edit(content=text_msg)
                    msg_base = await message.channel.send(text_msg)

                    def check(m):
                        return m.author == message.author and m.channel == message.channel

                    try:
                        msg_channel = await bot.wait_for('message', timeout=60.0, check=check)
                        msg_channel = msg_channel.content
                    except asyncio.TimeoutError:
                        await msg_base.edit(content="Trop Tard...")

                    try:
                        channel_a_rendre_public = bot.get_channel(int(msg_channel.replace("<","").replace(">","").replace("#","")))
                    except Exception as e:
                        print(e)
                        await message.channel.send(f"Erreur, le salon {msg_channel} n'a pas été trouvé")
                        return

                    # text_msg = "__**Quel jour voulez-vous rendre ce channel accessible ?**__\n\n" \
                    #            ":one: = Ajourd'hui\n:two: = Demain"

                    # def check(reaction, user):
                    #     return user == message.author and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣")

                    # try:
                    #     reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                    # except asyncio.TimeoutError:
                    #     await msg_base.edit(content="Trop Tard...")
                    #     return

                    text_msg = f"__**A quelle heure voulez-vous que la chasse au trésor commence ?**__\n\nExemple: Ecrivez 20h pour rendre ce channel accessible à 20h00 heure française."
                    # await msg_base.edit(content=text_msg)
                    msg_base = await message.channel.send(text_msg)

                    def check(m):
                        return m.author == message.author and m.channel == message.channel

                    try:
                        heures = await bot.wait_for('message', timeout=60.0, check=check)
                        heure_chasse_tresor = int(heures.content.replace("h",""))
                    except asyncio.TimeoutError:
                        await msg_base.edit(content="Trop Tard...")
                    except Exception as e:
                        print(e)
                        await message.channel.send("ERREUR !!!")


                    text_msg = "__**Voulez-vous envoyer un message au moment de l'ouverture du salon ?**__\n\n" \
                               ":one: = Oui\n:two: = Non"
                    # await msg_base.edit(content=text_msg)
                    msg_base = await message.channel.send(text_msg)
                    await msg_base.add_reaction("1️⃣")
                    await msg_base.add_reaction("2️⃣")

                    def check(reaction, user):
                        return user == message.author and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣")

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                    except asyncio.TimeoutError:
                        await msg_base.edit(content="Trop Tard...")
                        return

                    if reaction.emoji == "1️⃣":
                        annonce = True
                        text_msg = "**__Ecrivez le nom du salon dans lequel vous voulez mettre un message__**\n\nIl faut mettre # devant le nom."\
                                   " Le salon doit être cliquable"
                        # await msg_base.clear_reactions()
                        # await msg_base.edit(content=text_msg)
                        msg_base = await message.channel.send(text_msg)

                        def check(m):
                            return m.author == message.author and m.channel == message.channel

                        try:
                            msg_channel = await bot.wait_for('message', timeout=60.0, check=check)
                            msg_channel = msg_channel.content
                        except asyncio.TimeoutError:
                            await msg_base.edit(content="Trop Tard...")

                        try:
                            channel_annonce = bot.get_channel(int(msg_channel.replace("<","").replace(">","").replace("#","")))
                        except Exception as e:
                            print(e)
                            await message.channel.send(f"Erreur, le channel {msg_channel} n'a pas été trouvé")
                            return



                        text_msg = "**__Ecrivez le message que vous voulez envoyer au moment de l'ouverture de la chasse au trésor__**"
                        # await msg_base.edit(content=text_msg)
                        msg_base = await message.channel.send(text_msg)

                        try:
                            message_a_envoyer = await bot.wait_for('message', timeout=60.0, check=check)
                            message_a_envoyer = message_a_envoyer.content
                        except asyncio.TimeoutError:
                            await msg_base.edit(content="Trop Tard...")
                        

                    elif reaction.emoji == "2️⃣":
                        annonce = False

                    # Récap

                    message_recap = "**__Voici un récapitulatif : __**\n\n" \
                                    f"Heure de la chasse au trésor : aujourd'hui à {heure_chasse_tresor}h \n" \
                                    f"Salon de la chasse au trésor : <#{channel_a_rendre_public.id}>\n" \

                    if annonce == True:
                        message_recap += f"Salon de l'annonce de la chasse au trésor : <#{channel_annonce.id}>\n" \
                                    f"Message d'annonce : {message_a_envoyer}\n\n" \

                    message_recap += f":one: pour confirmer\n:two: pour annuler"

                    msg_base = await message.channel.send(message_recap)
                    await msg_base.add_reaction("1️⃣")
                    await msg_base.add_reaction("2️⃣")

                    def check(reaction, user):
                        return user == message.author and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣")

                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                    except asyncio.TimeoutError:
                        await msg_base.edit(content="Trop Tard...")
                        return
                    try:
                        await msg_base.clear_reactions()
                    except Exception as e:
                        print("Erreur clear reactions : ",e)


                    if reaction.emoji == "1️⃣":
                        if annonce == True:
                            retour = self.ajouter_data_json(heure_chasse_tresor, channel_a_rendre_public.id, annonce, channel_annonce.id, message_a_envoyer)
                        else:
                            retour = self.ajouter_data_json(heure_chasse_tresor, channel_a_rendre_public.id, annonce)
                        

                        if retour == "Ok":
                            text_msg = message_recap + "\n\nChasse au trésor enregistrée !"
                            # await msg_base.edit(content=text_msg)
                            msg_base = await message.channel.send(text_msg)
                        else:
                            await message.channel.send(retour)

                        
                    elif reaction.emoji == "2️⃣":
                        text_msg = message_recap + "\n\nChasse au trésor annulée..."
                        msg_base = await message.channel.send(text_msg)
                        # await msg_base.edit(content=text_msg)
                        return

            if message.content.startswith(f"{PREFIX}liste"):
                data = self.recup_data_json()
                if data == []:
                    msg_liste = "Pas de chasse au trésor programmée"
                    await message.channel.send(msg_liste)
                    return

                msg_liste = "__**Voici la liste des chasses au trésor : **__\n\n"

                a = 0
                for i in data:
                    a += 1

                    msg_liste += f"__Chasse au trésor {a} : __\n" \
                                f"Heure de la chasse au trésor : aujourd'hui à {i['heure_chasse']}h \n" \
                                f"Salon de la chasse au trésor : <#{i['salon_chasse']}>\n" \

                    if i["annonce"] == True:
                        msg_liste += f"Salon de l'annonce de la chasse au trésor : <#{i['salon_annonce']}>\n" \
                                    f"Message d'annonce : {i['message_annonce']}\n\n" \

                msg_liste += "\nPour supprimez une chasse, cliquez sur la réaction :one:"

                msg_base = await message.channel.send(msg_liste)
                await msg_base.add_reaction("1️⃣")

                def check(reaction, user):
                    return user == message.author and (str(reaction.emoji) == "1️⃣")

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
                except asyncio.TimeoutError:
                    # await msg_base.edit(content="Trop Tard...")
                    return
                await msg_base.remove_reaction("1️⃣",bot.user)
                try:
                    await msg_base.clear_reactions()
                except Exception as e:
                    print("Erreur clear reactions : ",e)

                msg = "__**Suppression d'une chasse au trésor**__\n\n"
                msg += "Voici la liste des chasses programmées : \n\n"
                a = 0
                for i in data:
                    a += 1
                    msg += f"__Chasse au trésor {a} : __\n" \
                    f"Heure de la chasse au trésor : aujourd'hui à {i['heure_chasse']}h \n" \
                    f"Salon de la chasse au trésor : <#{i['salon_chasse']}>\n" \

                    if i["annonce"] == True:
                        msg += f"Salon de l'annonce de la chasse au trésor : <#{i['salon_annonce']}>\n" \
                        f"Message d'annonce : {i['message_annonce']}\n\n" 
                msg += "Ecrivez le numéro de la chasse que vous voulez supprimer (Exemple : pour supprimer la chasse numéro 2, écrivez 2)"

                await message.channel.send(msg)

                def check(m):
                    return m.author == message.author and m.channel == message.channel

                try:
                    nombre_a_suppr = await bot.wait_for('message', timeout=60.0, check=check)
                    nombre_a_suppr = nombre_a_suppr.content
                except asyncio.TimeoutError:
                    return

                try:
                    nombre_a_suppr = int(nombre_a_suppr)
                except Exception as e:
                    print(e)
                    await message.channel.send(f"Erreur, {nombre_a_suppr} n'est pas un nombre")
                    return

                try:
                    del data[nombre_a_suppr - 1]
                    self.enregister_data_json(data)
                    await message.channel.send("La chasse a été supprimée.")
                except Exception as e:
                    print(e)
                    await message.channel.send(f"Erreur, la chasse {nombre_a_suppr} n'a pas pu être supprimée.")
                    return




        async def background():
            await bot.wait_until_ready()
            while True:

                data = self.recup_data_json()
                new_data = data[:]

                modif = False

                for i in range(len(data)):
                    if datetime.datetime.now().hour == data[i]["heure_chasse"]:
                        modif = True

                        id_salon_chasse = data[i]["salon_chasse"]
                        salon_chasse = bot.get_channel(id_salon_chasse)

                        await salon_chasse.set_permissions(salon_chasse.guild.default_role, 
                            read_messages=True, send_messages=False)

                        annonce = data[i]["annonce"]
                        if annonce == True:
                            id_salon_annonce = data[i]["salon_annonce"]
                            message_annonce = data[i]["message_annonce"]
                            salon_annonce = bot.get_channel(id_salon_annonce)
                            await salon_annonce.send(message_annonce)

                        new_data.remove(data[i])

                if modif == True:
                    self.enregister_data_json(new_data)

                await asyncio.sleep(5)




        bot.loop.create_task(background())
        bot.run(TOKEN)


    def ajouter_data_json(self, heure_chasse_tresor, channel_a_rendre_public, annonce, channel_annonce="", message_a_envoyer=""):
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


    def recup_data_json(self):
        try:
            with open("data.json", "r") as fichier:
                data = json.load(fichier)
            return data
        except Exception as e:
            print(e)
            return f"Erreur : {e}\nZone erreur 3"

    def enregister_data_json(self, data):
        try:
            with open("data.json", "w") as fichier:
                json.dump(data, fichier)
        except Exception as e:
            print(e)
            return f"Erreur : {e}\nZone erreur 4"


if __name__ == '__main__':
    bot = Bot()