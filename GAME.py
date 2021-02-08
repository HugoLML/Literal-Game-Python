import random
from time import time
import sys
from termcolor import colored


PositionPersoX = 0
PositionPersoY = 0


StatsPersoLVL = 1    
StatsPersoHP = 100
StatsPersoATT = 25
StatsPersoDEF = 25
StatsPersoXP = 0

StatsEnnemisLVL = 1    
StatsEnnemisHP = 65
StatsEnnemisATT = 10
StatsEnnemisDEF = 10

StatsPersoHPCombat = StatsPersoHP
StatsPersoATTCombat = StatsPersoATT
StatsPersoDEFCombat = StatsPersoDEF
StatsEnnemisHPCombat = StatsEnnemisHP

PointsXPCombat = 50
PointsXPNivSup = 100


Couteau = "un couteau"
Taser = "un taser surchargé"
Pistolet = "un pistolet"
Fusil = "un fusil à pompe"

CouteauPtsATT = 10
TaserPtsATT = 15
PistoletPtsATT = 20
FusilPtsATT = 25

InventaireNomArmes = [Couteau]
InventaireStatsArmes = [CouteauPtsATT]
ListeArmesTrouvables = [Taser, Pistolet, Fusil]


GiletRembourré = "un gilet rembourré"
AntiCouteau = "un gilet anti-couteau"
CombinaisonKevlar = "une combinaison en kevlar"
PareBalle = "un gilet pare-balle"

GiletRembourréDispo = 0
AntiCouteauDispo = 0
CombinaisonKevlarDispo = 0
PareBalleDispo = 0

InventaireNomArmures = []
ListeArmuresTrouvables = [GiletRembourré, AntiCouteau, CombinaisonKevlar, PareBalle]


BoostHP = "du pain (+35 HP)"
BoostATT = "un steak (+15 ATT)"
BoostDEF = "une pomme (+15 DEF)"

BoostHPStats = 35
BoostATTStats = 15
BoostDEFStats = 15

BoostHPQuantité = 0
BoostATTQuantité = 0
BoostDEFQuantité = 0

InventaireNomBoosts = []
InventaireStatsBoosts = [BoostHPStats, BoostATTStats, BoostDEFStats]
InventaireQuantitéBoosts = [BoostHPQuantité, BoostATTQuantité, BoostDEFQuantité]
ListeBoostsTrouvables = [BoostHP, BoostATT, BoostDEF]


Carte = 0


ArgentQuantité = 100
ListeArgentTrouvable = [100, 250, 500]


def ResetVariables(): ### Reinitialise toutes les variables pour relancer une game
    
    global PositionPersoX, PositionPersoY
    global StatsPersoLVL, StatsPersoHP, StatsPersoATT, StatsPersoDEF, StatsPersoDEF, StatsPersoXP
    global StatsEnnemisLVL, StatsEnnemisHP, StatsEnnemisATT, StatsEnnemisDEF
    global StatsPersoHPCombat, StatsPersoATTCombat, StatsPersoDEFCombat, StatsEnnemisHPCombat
    global PointsXPCombat, PointsXPNivSup
    global InventaireNomArmes, InventaireStatsArmes, ListeArmesTrouvables
    global TaserPtsATT, PistoletPtsATT, FusilPtsATT
    global GiletRembourréDispo, AntiCouteauDispo, CombinaisonKevlarDispo, PareBalleDispo
    global InventaireNomArmures, ListeArmuresTrouvables
    global BoostHPQuantité, BoostATTQuantité, BoostDEFQuantité
    global InventaireNomBoosts, InventaireStatsBoosts, InventaireQuantitéBoosts, ListeBoostsTrouvables
    global Carte
    global ArgentQuantité, ListeArgentTrouvable
    
    PositionPersoX = 0
    PositionPersoY = 0


    StatsPersoLVL = 1    
    StatsPersoHP = 100
    StatsPersoATT = 25
    StatsPersoDEF = 25
    StatsPersoXP = 0

    StatsEnnemisLVL = 1    
    StatsEnnemisHP = 65
    StatsEnnemisATT = 10
    StatsEnnemisDEF = 10

    StatsPersoHPCombat = StatsPersoHP
    StatsPersoATTCombat = StatsPersoATT
    StatsPersoDEFCombat = StatsPersoDEF
    StatsEnnemisHPCombat = StatsEnnemisHP

    PointsXPCombat = 50
    PointsXPNivSup = 100


    Couteau = "un couteau"
    Taser = "un taser surchargé"
    Pistolet = "un pistolet"
    Fusil = "un fusil à pompe"

    CouteauPtsATT = 10
    TaserPtsATT = 15
    PistoletPtsATT = 20
    FusilPtsATT = 25

    InventaireNomArmes = [Couteau]
    InventaireStatsArmes = [CouteauPtsATT]
    ListeArmesTrouvables = [Taser, Pistolet, Fusil]


    GiletRembourré = "un gilet rembourré"
    AntiCouteau = "un gilet anti couteau"
    CombinaisonKevlar = "une combinaison en kevlar"
    PareBalle = "un gilet pare-balle"

    GiletRembourréDispo = 0
    AntiCouteauDispo = 0
    CombinaisonKevlarDispo = 0
    PareBalleDispo = 0

    InventaireNomArmures = []
    ListeArmuresTrouvables = [GiletRembourré, AntiCouteau, CombinaisonKevlar, PareBalle]


    BoostHP = "du pain (+35 HP)"
    BoostATT = "un steak (+15 ATT)"
    BoostDEF = "une pomme (+15 DEF)"

    BoostHPStats = 35
    BoostATTStats = 15
    BoostDEFStats = 15

    BoostHPQuantité = 0
    BoostATTQuantité = 0
    BoostDEFQuantité = 0

    InventaireNomBoosts = []
    InventaireStatsBoosts = [BoostHPStats, BoostATTStats, BoostDEFStats]
    InventaireQuantitéBoosts = [BoostHPQuantité, BoostATTQuantité, BoostDEFQuantité]
    ListeBoostsTrouvables = [BoostHP, BoostATT, BoostDEF]


    Carte = 0

    ArgentQuantité = 100
    ListeArgentTrouvable = [100, 250, 500]

def PlayGame(): ### Choisir le mode de jeu (classique ou speedrun)
    print("\n")
    print("Choisis ton mode de jeu :")
    print(colored("Partie classique ?", attrs=['bold']), "(= 1)")
    print(colored("Partie speedrun ?", attrs=['bold']), "(= 2)")
    
    global ChoixMode
    ChoixMode = int(input())
    
    if ChoixMode == 1:
        print("\n")
        Pseudo = input("Entre ton pseudo : ")
        print("C'est parti", colored(Pseudo, 'cyan', attrs=['bold']),"!")
        print(colored("Tu viens d'être réveillé par l'alarme générale !", 'red'))
        print(colored("Toutes les cellules sont ouvertes et tes co-détenus de la prison de Fox River sont en train de s'échapper !", 'red'))
        StartGame()
    
    elif ChoixMode == 2:
        print("\n")
        print("Le chrono se lancera dès que tu auras rentré ton pseudo !")
        Pseudo = input("Entre ton pseudo : ")
        print("\n")
        print("C'est parti", colored(Pseudo, 'cyan', attrs=['bold']),"!")
        print(colored("Tu viens d'être réveillé par l'alarme générale !", 'red'))
        print(colored("Toutes les cellules sont ouvertes et tes co-détenus de la prison de Fox River sont en train de s'échapper !", 'red'))
        Start = time()
        StartGame()
        End = time()
        Time = End - Start
        print("\n")
        print("Bravo ! Tu as complété ton évasion en", colored(round(Time, 2), 'cyan', attrs=['bold']), "secondes !")
        ResetVariables()
        Menu()

def StartGame(): ### Fonction principale du jeu

    def Deal(): ### Fonction d'achat avec le contrebandier
        
        print("\n")

        PrixTaser = 100
        PrixPistolet = 200
        PrixFusil = 300
        
        PrixGiletRembourré = 150
        PrixGiletAntiCouteau = 150
        PrixCombinaisonKevlar = 150
        PrixGiletPareBalle = 200

        PrixPain = 50
        PrixSteak = 25
        PrixPomme = 25
        
        def BuyAgainOrNot():  
            print("Souhaites-tu acheter autre chose ? (= 1)")
            print("Ou tracer ta route ? (= 2)")
            ContinuerAchatOuPas = int(input())
            if ContinuerAchatOuPas == 1:
                AskBuying()
            elif ContinuerAchatOuPas == 2:
                AskDirection()
            else:
                print("Tape 1 ou 2")
                BuyAgainOrNot()

        if ArgentQuantité > 0:    
            print("Il te fait signe de venir vers lui et te montre sa marchandise...")
            print("Ça pourrait te servir pour ton évasion.")
            
            def AskBuying():    
                global ArgentQuantité, GiletRembourréDispo, AntiCouteauDispo, CombinaisonKevlarDispo, PareBalleDispo
                global BoostHPQuantité, BoostDEFQuantité, BoostATTQuantité
                
                print("Que veux tu acheter ?")
                print(colored("Des armes ?", 'cyan'), "(= 1)")
                print(colored("Des armures ?", 'cyan'), "(= 2)")
                print(colored("Des boosts ?", 'cyan'), "(= 3)")
                print("Rien ? (= 4)")
                
                ChoixCatégorieObjets = int(input())
                
                if ChoixCatégorieObjets == 1:
                    print("Quelle arme veux tu acheter ?")
                    
                    print(colored("Un taser surchargé ?", 'cyan'), "(",TaserPtsATT,"points d'attaque )", "(",PrixTaser,"$ )", "(= 1)")
                    print(colored("Un pistolet ?", 'cyan'), "(",PistoletPtsATT,"points d'attaque )", "(",PrixPistolet,"$ )", "(= 2)")
                    print(colored("Un fusil à pompe ?", 'cyan'), "(",FusilPtsATT,"points d'attaque )", "(",PrixFusil,"$ )", "(= 3)")
                    print("Rien (= 4)")
                    
                    print("Ton arme équipée actuellement cause", colored(InventaireStatsArmes[0], 'cyan'), "points de dégats.")
                    print("Tu possèdes", colored(ArgentQuantité, 'cyan'), "$.")

                    StoreChoixArme = int(input())
                    
                    if StoreChoixArme == 1:
                        
                        if ArgentQuantité >= PrixTaser:
                            print("Tu viens d'acheter", colored(Taser, 'cyan'), "!")
                            print("Tu l'équipes directement !")
                            InventaireNomArmes.append(Taser)
                            InventaireStatsArmes.append(TaserPtsATT)
                            InventaireNomArmes.reverse()
                            InventaireStatsArmes.reverse()
                            ArgentQuantité -= PrixTaser
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArme == 2:
                        
                        if ArgentQuantité >= PrixPistolet:
                            print("Tu viens d'acheter", colored(Pistolet, 'cyan'), "!")
                            print("Tu l'équipes directement !")
                            InventaireNomArmes.append(Pistolet)
                            InventaireStatsArmes.append(PistoletPtsATT)
                            InventaireNomArmes.reverse()
                            InventaireStatsArmes.reverse()
                            ArgentQuantité -= PrixPistolet
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArme == 3:
                        
                        if ArgentQuantité >= PrixFusil:
                            print("Tu viens d'acheter", colored(Fusil, 'cyan'), "!")
                            print("Tu l'équipes directement !")
                            InventaireNomArmes.append(Fusil)
                            InventaireStatsArmes.append(FusilPtsATT)
                            InventaireNomArmes.reverse()
                            InventaireStatsArmes.reverse()
                            ArgentQuantité -= PrixFusil
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArme == 4:
                        AskBuying()
                    
                    else:
                        print("Tape 1, 2 ou 3.")
                        AskBuying()

                elif ChoixCatégorieObjets == 2:
                    print("Quelle armure veux tu acheter ?")
                    
                    print(colored("Un gilet rembourré ?", 'cyan'), "(Efficace contre garde et voleur)", "(",PrixGiletRembourré,"$ )", "(= 1)")
                    print(colored("Un gilet anti-couteau ?", 'cyan'), "(Efficace contre tueur en série et toxico)", "(",PrixGiletAntiCouteau,"$ )", "(= 2)")
                    print(colored("Une combinaison en kevlar ?", 'cyan'), "(Efficace contre schizophrène)", "(",PrixCombinaisonKevlar,"$ )", "(= 3)")
                    print(colored("Un gilet pare-balle ?", 'cyan'), "(Efficace contre boss)", "(",PrixGiletPareBalle,"$ )", "(= 4)")
                    print("Rien (= 5)")

                    if GiletRembourréDispo != 0:
                        print("Tu possèdes déjà", colored(GiletRembourré, 'cyan'),".")
                    if AntiCouteauDispo != 0:
                        print("Tu possèdes déjà", colored(AntiCouteau, 'cyan'),".")
                    if CombinaisonKevlarDispo != 0:
                        print("Tu possèdes déjà", colored(CombinaisonKevlar, 'cyan'),".")
                    if PareBalleDispo != 0:
                        print("Tu possèdes déjà", colored(PareBalle, 'cyan'),".")
                    print("Tu possèdes", colored(ArgentQuantité, 'cyan'), "$.")

                    StoreChoixArmure = int(input())
                    
                    if StoreChoixArmure == 1:
                        
                        if ArgentQuantité >= PrixGiletRembourré:
                            print("Tu viens d'acheter", colored(GiletRembourré, 'cyan'), "!")
                            print("Il est placé dans ton inventaire.")
                            GiletRembourréDispo += 1
                            InventaireNomArmures.append(GiletRembourré)
                            ArgentQuantité -= PrixGiletRembourré
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArmure == 2:
                        
                        if ArgentQuantité >= PrixGiletAntiCouteau:
                            print("Tu viens d'acheter", colored(AntiCouteau, 'cyan'), "!")
                            print("Il est placé dans ton inventaire.")
                            AntiCouteauDispo += 1
                            InventaireNomArmures.append(AntiCouteau)
                            ArgentQuantité -= PrixGiletAntiCouteau
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArmure == 3:
                        
                        if ArgentQuantité >= PrixCombinaisonKevlar:
                            print("Tu viens d'acheter", colored(CombinaisonKevlar, 'cyan'), "!")
                            print("Elle est placée dans ton inventaire.")
                            CombinaisonKevlarDispo += 1
                            InventaireNomArmures.append(CombinaisonKevlar)
                            ArgentQuantité -= PrixCombinaisonKevlar
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixArmure == 4:
                        
                        if ArgentQuantité >= PrixGiletPareBalle:
                            print("Tu viens d'acheter", colored(PareBalle, 'cyan'), "!")
                            print("Il est placé dans ton inventaire.")
                            PareBalleDispo += 1
                            InventaireNomArmures.append(PareBalle)
                            ArgentQuantité -= PrixGiletPareBalle
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()
                    
                    else:
                        print("Tape 1, 2, 3 ou 4.")
                        AskBuying()

                elif ChoixCatégorieObjets == 3:
                    print("Quel boost veux tu acheter ?")
                    
                    print(colored("Du pain ?", 'cyan'), "(+",BoostHPStats,"HP)", "(",PrixPain,"$ )", "(= 1)")
                    print(colored("Un steak ?", 'cyan'), "(+",BoostATTStats,"ATT)", "(",PrixSteak,"$ )", "(= 2)")
                    print(colored("Une pomme", 'cyan'), "(+",BoostDEFStats,"DEF)", "(",PrixPomme,"$ )", "(= 3)")
                    print("Rien (= 4)")

                    if BoostHPQuantité != 0:
                        print("Tu possèdes déjà", colored(BoostHP, 'cyan'), "(",BoostHPQuantité,")")
                    if BoostHPQuantité != 0:
                        print("Tu possèdes déjà", colored(BoostATT, 'cyan'), "(",BoostATTQuantité,")")
                    if BoostDEFQuantité != 0:
                        print("Tu possèdes déjà", colored(BoostDEF, 'cyan'), "(",BoostDEFQuantité,")")
                    print("Tu possèdes", colored(ArgentQuantité, 'cyan'), "$.")

                    StoreChoixBoost = int(input())
                    
                    if StoreChoixBoost == 1:
                        
                        if ArgentQuantité >= PrixPain:
                            print("Tu viens d'acheter", colored(BoostHP, 'cyan'), "!")
                            print("Il est placé directement dans ton inventaire !")
                            BoostHPQuantité += 1
                            ArgentQuantité -= PrixPain
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixBoost == 2:
                        
                        if ArgentQuantité >= PrixSteak:
                            print("Tu viens d'acheter", colored(BoostATT, 'cyan'), "!")
                            print("Il est placé directement dans ton inventaire !")
                            BoostATTQuantité += 1
                            ArgentQuantité -= PrixSteak
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixBoost == 3:
                        
                        if ArgentQuantité >= PrixPomme:
                            print("Tu viens d'acheter", colored(BoostDEF, 'cyan'), "!")
                            print("Elle est placée directement dans ton inventaire !")
                            BoostDEFQuantité += 1
                            ArgentQuantité -= PrixPomme
                            BuyAgainOrNot()
                        else:
                            print("Tu n'as pas assez d'argent pour l'acheter.")
                            AskBuying()

                    elif StoreChoixBoost == 4:
                        AskBuying()
                    
                    else:
                        print("Tape 1, 2 ou 3.")
                        AskBuying()

                elif ChoixCatégorieObjets == 4:
                    AskDirection()
                
                else:
                    print("Tape 1, 2, 3 ou 4.")
                    AskBuying()

            AskBuying()
        
        else:
            print("Tu n'as pas assez d'argent pour marchander avec lui !")
            print("Essaye de revenir le voir quand tu en auras !")
            AskDirection()

    def AskDirection(): ### Fonction qui demande la direction au joueur

        print("\n")
        print("Où veux tu aller ?")
        print("Au nord = 1")
        print("À l'est = 2")
        print("Au sud = 3")
        print("À l'ouest = 4")
        print("Retourner au menu = 5")

        ChoixDirection = int(input())
        
        global PositionPersoX
        global PositionPersoY

        if ChoixDirection == 1:
            if PositionPersoY < 3:
                PositionPersoY += 1
            else:
                print("\n")
                print(colored("Tu ne peux pas aller par là, c'est un cul de sac !", 'blue'))
                AskDirection()
        
        elif ChoixDirection == 2:
            if PositionPersoX < 3:
                PositionPersoX += 1
            else:
                print("\n")
                print(colored("Tu ne peux pas aller par là, c'est un cul de sac !", 'blue'))
                AskDirection()

        elif ChoixDirection == 3:
            if PositionPersoY > -3:
                PositionPersoY -= 1
            else:
                print("\n")
                print(colored("Tu ne peux pas aller par là, c'est un cul de sac !", 'blue'))
                AskDirection()
        
        elif ChoixDirection == 4:
            if PositionPersoX > -3:
                PositionPersoX -= 1
            else:
                print("\n")
                print(colored("Tu ne peux pas aller par là, c'est un cul de sac !", 'blue'))
                AskDirection()
        
        elif ChoixDirection == 5:
            ResetVariables()
            Menu()
        
        else:
            print(colored("Tape un nombre correspondant à une direction.", 'blue'))
            AskDirection()

    AskDirection()
    
    def PlacesDescription(): ### Fonction de description du lieu

        print("\n")
        if PositionPersoX == -3 and PositionPersoY == -3:
            print(colored("Tu arrives dans la cellule 900.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == -3:
            print(colored("Tu arrives sur le chemin de ronde des gardes.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == -3:
            print(colored("Tu arrives dans salle des biens des détenus.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == -3:
            print(colored("Tu arrives dans la cellule 790.", 'blue'))
        elif PositionPersoX == 1 and PositionPersoY == -3:
            print(colored("Tu arrives dans le batiment secret.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == -3:
            print(colored("Tu arrives dans l'atelier.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == -3:
            print(colored("Tu arrives dans la cellule 791.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == -2:
            print(colored("Tu arrives dans la cour intérieur.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == -2:
            print(colored("Tu arrives dans la cellule 792.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == -2:
            print(colored("Tu arrives dans la salle des machines.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == -2:
            print(colored("Tu croises un contrebandier !", 'blue'))
            Deal()
        elif PositionPersoX == 1 and PositionPersoY == -2:
            print(colored("Tu arrives dans les douches.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == -2:
            print(colored("Tu arrives dans la cellule 793.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == -2:
            print(colored("Tu arrives au dépot.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == -1:
            print(colored("Tu arrives au parloir.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == -1:
            print(colored("Tu arrives dans la salle de vidéo surveillance.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == -1:
            print(colored("Tu arrives dans la salle d'isolement.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == -1:
            print(colored("Tu arrives dans la cellule de C-Note.", 'blue'))
        elif PositionPersoX == 1 and PositionPersoY == -1:
            print(colored("Tu arrives dans la salle de repos des gardes.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == -1:
            print(colored("Tu arrives dans la cellule 901.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == -1:
            print(colored("Tu arrives dans la salle des travaux.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == 0:
            print(colored("Tu arrives dans la cellule 902.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == 0:
            print(colored("Tu croises un contrebandier !", 'blue'))
            Deal()
        elif PositionPersoX == -1 and PositionPersoY == 0:
            print(colored("Tu arrives dans la cellule d'Abruzzi.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == 0:
            print(colored("Tu es de retour dans ta cellule.", 'blue'))
        elif PositionPersoX == 1 and PositionPersoY == 0:
            print(colored("Tu arrives dans la cellule de T-bag.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == 0:
            print(colored("Tu croises un contrebandier !", 'blue'))
            Deal()
        elif PositionPersoX == 3 and PositionPersoY == 0:
            print(colored("Tu arrives dans la salle de sport.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cellule 903.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cantine.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cellule 904.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cellule de Sucre & Scofield.", 'blue'))
        elif PositionPersoX == 1 and PositionPersoY == 1:
            print(colored("Tu arrives dans la ventilation.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cellule d'isolement de Lincoln.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == 1:
            print(colored("Tu arrives dans la cellule de Charles Westmoreland.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == 2:
            print(colored("Tu arrives dans l'église.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == 2:
            print(colored("Tu arrives dans le batiment des fous.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == 2:
            print(colored("Tu arrives dans la cellule 905.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == 2:
            print(colored("Tu croises un contrebandier !", 'blue'))
            Deal()
        elif PositionPersoX == 1 and PositionPersoY == 2:
            print(colored("Tu arrives à l'infirmerie.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == 2:
            print(colored("Tu arrives dans le bureau du directeur.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == 2:
            print(colored("Tu arrives dans la cuisine.", 'blue'))
        elif PositionPersoX == -3 and PositionPersoY == 3:
            print(colored("Tu arrives dans la cellule 906.", 'blue'))
        elif PositionPersoX == -2 and PositionPersoY == 3:
            print(colored("Tu arrives dans la salle des visites.", 'blue'))
        elif PositionPersoX == -1 and PositionPersoY == 3:
            print(colored("Tu arrives au lavoir.", 'blue'))
        elif PositionPersoX == 0 and PositionPersoY == 3:
            print(colored("Tu arrives dans la cellule de Tweener.", 'blue'))
        elif PositionPersoX == 1 and PositionPersoY == 3:
            print(colored("Tu arrives aux toilettes.", 'blue'))
        elif PositionPersoX == 2 and PositionPersoY == 3:
            print(colored("Tu arrives dans la cour extérieure.", 'blue'))
        elif PositionPersoX == 3 and PositionPersoY == 3:
            print(colored("Ça y est ! Tu vois la sortie de Fox River !", 'blue'))

    PlacesDescription()

    def Event():
        print("\n")
        def Combat(): ### Fonction de combat
            
            ListeEnnemis = [1, 2, 3, 4, 5]
            EnnemiAléatoire = random.choice(ListeEnnemis)
            
            print(colored("Un ennemi t'attaque !", 'magenta'))
            if PositionPersoX == 3 and PositionPersoY == 3:
                print(colored("C'est le capitaine Bellick !", 'red'))
                print(colored("Il est bien plus déterminé à te remettre en prison que les autres adversaires que tu as croisé jusque là !", 'red'))
            else:    
                if EnnemiAléatoire == 1:
                    print(colored("C'est un garde de niveau",'magenta'),colored(StatsEnnemisLVL, 'magenta'),colored("!", 'magenta'))
                elif EnnemiAléatoire == 2:
                    print(colored("C'est un toxico de niveau",'magenta'),colored(StatsEnnemisLVL, 'magenta'),colored("!", 'magenta'))
                elif EnnemiAléatoire == 3:
                    print(colored("C'est un tueur en série de niveau",'magenta'),colored(StatsEnnemisLVL, 'magenta'),colored("!", 'magenta'))
                elif EnnemiAléatoire == 4:
                    print(colored("C'est un voleur de niveau",'magenta'),colored(StatsEnnemisLVL, 'magenta'),colored("!", 'magenta'))
                elif EnnemiAléatoire == 5:
                    print(colored("C'est un schizophrène de niveau",'magenta'),colored(StatsEnnemisLVL, 'magenta'),colored("!", 'magenta'))
            
            global StatsEnnemisHPCombat
            global StatsEnnemisATT
            global StatsEnnemisDEF

            global StatsPersoATTCombat
            global StatsPersoDEFCombat
            
            if PositionPersoX == 3 and PositionPersoY == 3:
                StatsEnnemisHPCombat = (StatsEnnemisHP * 1.5)                
                StatsEnnemisATT += (StatsEnnemisATT * 0.5)
                StatsEnnemisDEF += (StatsEnnemisDEF * 0.5)
                
                StatsPersoATTCombat = StatsPersoATT
                StatsPersoDEFCombat = StatsPersoDEF
            
            else:    
                StatsEnnemisHPCombat = StatsEnnemisHP               
                StatsPersoATTCombat = StatsPersoATT
                StatsPersoDEFCombat = StatsPersoDEF
            
            while StatsPersoHPCombat > 0 and StatsEnnemisHPCombat > 0:
                
                def YourTurn():    
                    print("Que veux-tu faire ?")
                    print("Attaquer = 1")
                    print("Equiper une armure = 2")
                    print("Utiliser un objet = 3")
                    print("Tenter de fuire = 4")
                    print("Soudoyer = 5")
                    print("Retourner au menu = 6")

                    ChoixCombat = int(input())

                    if ChoixCombat == 1:
                        
                        global StatsPersoLVL
                        global StatsPersoHP
                        global StatsPersoATT
                        global StatsPersoDEF
                        global StatsPersoXP

                        global StatsEnnemisLVL    
                        global StatsEnnemisHP
                        global StatsEnnemisATT
                        global StatsEnnemisDEF
                        
                        global PointsXPCombat
                        global PointsXPNivSup
                        
                        if random.randint(1,5) == 1:
                            global StatsPersoATTCombat
                            CoupCritique = StatsPersoATTCombat * 0.5
                        else:
                            CoupCritique = 0

                        Attaque = StatsPersoATTCombat - StatsEnnemisDEF/2 + InventaireStatsArmes[0] + CoupCritique

                        global StatsEnnemisHPCombat
                        StatsEnnemisHPCombat -= Attaque
                        
                        print("Tu attaques l'ennemi avec", colored(InventaireNomArmes[0], 'cyan'),"!")
                        print("Ton attaque a causé", colored(Attaque, 'cyan'), "points de dégats !")
                        if CoupCritique != 0:
                            print(colored("C'est un coup critique !", 'red'))
                        if StatsEnnemisHPCombat > 0:
                            print("Ton adversaire n'a plus que", colored(StatsEnnemisHPCombat, 'cyan'), "points de vie !")
                        else:
                            if PositionPersoX == 3 and PositionPersoY == 3:
                                print(colored("Bellick perd l'équilibre...", 'red'))
                                print(colored("Il tombe inconscient sur le sol.", 'red'))
                                print(colored("La voie est libre ! Dépêche toi avant de te faire rattraper !", 'red'))
                                print(colored("L'évasion est un succès ! GG WP !", 'red'))
                                print(colored("Retour au menu imminent...", 'red'))

                                if ChoixMode == 2:
                                    return
                                    
                                ResetVariables()
                                Menu()
                            
                            else:
                                print(colored("Tu l'as mis K-O ! Bien joué !", attrs=['bold']))
                                print("Tu as gagné", colored(PointsXPCombat, 'cyan'), "points d'expérience !")
                                StatsPersoXP += PointsXPCombat
                                if StatsPersoXP >= PointsXPNivSup:
                                    StatsPersoLVL += 1
                                    print("Niveau supérieur atteint ! Tu es maintenant au niveau", colored(StatsPersoLVL, 'cyan'), "!")
                                    PointsXPCombat += 25
                                    PointsXPNivSup += PointsXPNivSup
                                    StatsPersoHP += 25
                                    StatsPersoATT += 10
                                    StatsPersoDEF += 10
                                    StatsEnnemisLVL += 1
                                    StatsEnnemisHP += 25
                                    StatsEnnemisATT += 5
                                    StatsEnnemisDEF += 5

                    elif ChoixCombat == 2:
                        if not InventaireNomArmures:
                            print("Tu ne possèdes pas d'armure")
                            YourTurn()
                        else:
                            print("Tu possèdes :")

                            if GiletRembourréDispo != 0:
                                print(colored(GiletRembourré, 'cyan'), "(= 1) (Efficace contre garde et voleur.)")
                            if AntiCouteauDispo != 0:
                                print(colored(AntiCouteau, 'cyan'), "(= 2) (Efficace contre tueur en série et toxico.)")
                            if CombinaisonKevlarDispo != 0:
                                print(colored(CombinaisonKevlar, 'cyan'), "(= 3) (Efficace contre schizophrène.)")
                            if PareBalleDispo != 0:
                                print(colored(PareBalle, 'cyan'), "(= 4) (Efficace contre boss.)")
                            
                            print("Revenir en arrière = 5")
                            
                            print("Quelle armure veux-tu équiper ?")
                           
                            ChoixArmure = int(input())
                            global StatsPersoDEFCombat
                            
                            if ChoixArmure == 1 and GiletRembourréDispo != 0:
                                if EnnemiAléatoire == 1 or EnnemiAléatoire == 4:    
                                    StatsPersoDEFCombat += StatsPersoDEF * 0.5
                                    print("Défense augmentée contre les attaques à impact !")
                                else:
                                    print("Cette armure n'est pas éfficace contre cet ennemi !")
                            elif ChoixArmure == 2 and AntiCouteauDispo != 0:
                                if EnnemiAléatoire == 2 or EnnemiAléatoire == 3:    
                                    StatsPersoDEFCombat += StatsPersoDEF * 0.5
                                    print("Défense augmentée contre les attaques à l'arme blanche !")
                                else:
                                    print("Cette armure n'est pas éfficace contre cet ennemi !")
                            elif ChoixArmure == 3 and CombinaisonKevlarDispo != 0:
                                if EnnemiAléatoire == 5:    
                                    StatsPersoDEFCombat += StatsPersoDEF * 0.5
                                    print("Défense augmentée contre les attaques incendiaires !")
                                else:
                                    print("Cette armure n'est pas éfficace contre cet ennemi !")
                            elif ChoixArmure == 4 and PareBalleDispo != 0:
                                if PositionPersoX == 3 and PositionPersoY == 3:    
                                    StatsPersoDEFCombat += StatsPersoDEF * 0.5
                                    print("Défense augmentée contre les balles !")
                                else:
                                    print("Cette armure n'est pas éfficace contre cet ennemi !")
                            elif ChoixArmure == 5:
                                YourTurn()   
                            else:
                                print("Tape le nombre correspondant.")
                                YourTurn()

                    
                    elif ChoixCombat == 3:
                        
                        global BoostHPQuantité
                        global BoostATTQuantité
                        global BoostDEFQuantité
                        
                        if BoostHPQuantité == 0 and BoostATTQuantité == 0 and BoostDEFQuantité == 0:
                            print("Tu n'as pas d'objets.")
                            YourTurn()
                        
                        else:
                            print("Tu possèdes :")
                            print(colored(BoostHP, 'cyan'),"(", BoostHPQuantité, ") = 1")
                            print(colored(BoostATT, 'cyan'),"(", BoostATTQuantité, ") = 2")
                            print(colored(BoostDEF, 'cyan'),"(", BoostDEFQuantité, ") = 3")
                            print("Revenir en arrière = 4")
                            print("Quel objet veux tu utiliser ?")
                            
                            ChoixObjet = int(input())

                            if ChoixObjet == 1 and BoostHPQuantité != 0:
                                global StatsPersoHPCombat
                                if StatsPersoHPCombat <= (StatsPersoHP - BoostHPStats):
                                    StatsPersoHPCombat += BoostHPStats
                                    print("Tu gagnes", colored("35 points de vie", 'cyan'), "!")
                                    print("Tu as maintenant", colored(StatsPersoHPCombat, 'cyan'), "points de vie.")
                                    BoostHPQuantité -= 1
                                else:
                                    print("Tu n'as pas assez faim pour manger ce bout de pain.")
                                    print("Garde le pour plus tard, il te sera certainement utile.")
                                    YourTurn()
                            
                            elif ChoixObjet == 2 and BoostATTQuantité != 0:
                                StatsPersoATTCombat += BoostATTStats
                                print("Tu gagnes", colored("15 points d'attaque", 'cyan'), "!")
                                print("Tu as maintenant", colored(StatsPersoATTCombat, 'cyan'), "points d'attaque.")
                                BoostATTQuantité -= 1
                            
                            elif ChoixObjet == 3 and BoostDEFQuantité != 0:
                                StatsPersoDEFCombat += BoostDEFStats
                                print("Tu gagnes", colored("15 points de défense", 'cyan'), "!")
                                print("Tu as maintenant", colored(StatsPersoDEFCombat, 'cyan'), "points de défense.")
                                BoostDEFQuantité -= 1

                            elif ChoixObjet == 4:
                                YourTurn()
                            
                            else:
                                print("Tape 1, 2, 3 ou 4.")
                                YourTurn()
                    
                    elif ChoixCombat == 4:
                        ChancesFuite = random.randint(1,2)
                        if ChancesFuite > 1:
                            print("Tu prends la fuite !")
                            StartGame()
                        else:
                            print(colored("L'ennemi te bloque le passage !", 'red'))
                            print(colored("Tu ne peux pas t'enfuir ce tour là !", 'red'))
                    
                    elif ChoixCombat == 5:
                        if PositionPersoX == 3 and PositionPersoY == 3:
                            print("Tu ne peux pas soudoyer Bellick !")
                            YourTurn()                   
                        else:
                            global ArgentQuantité
                            print("Tu peux soudoyer l'ennemi pour qu'il te laisse passer.")
                            print("Souhaites tu dépenser 100 dollars pour t'enfuir tranquillement ?")
                            print("Tu possèdes actuellement", colored(ArgentQuantité, 'cyan'),"$.")
                            print("Oui = 1")
                            print("Non = 2")
                            ChoixSoudoyer = int(input())
                            if ChoixSoudoyer == 1:
                                if ArgentQuantité >= 100:    
                                    print("Tu lui donne 100 dollars ! L'ennemi te laise passer !")
                                    ArgentQuantité -= 100
                                    StartGame()
                                else:
                                    print("Tu n'as pas assez d'argent !")
                                    YourTurn()
                            elif ChoixSoudoyer == 2:
                                YourTurn()
                            else:
                                print("Tape 1 ou 2.")
                                YourTurn()

                    elif ChoixCombat == 6:
                        ResetVariables()
                        Menu()

                    else:
                        print("Tape 1, 2, 3, 4, 5 ou 6.")
                        YourTurn()
                YourTurn()
                
                def EnemyTurn():
                    
                    if ChoixMode == 2 and PositionPersoX == 3 and PositionPersoY == 3 and StatsEnnemisHPCombat <= 0:
                        return
                    
                    if PositionPersoX == 3 and PositionPersoY == 3:
                        print(colored("Bellick t'attaque à son tour avec son arme de service !", 'red'))
                    else:    
                        if EnnemiAléatoire == 1:
                            print("Le garde t'attaque à son tour avec", colored("une matraque", 'cyan'), "!")
                        elif EnnemiAléatoire == 2:
                            print("Le toxico t'attaque à son tour avec", colored("une seringue cassée", 'cyan'), "!")
                        elif EnnemiAléatoire == 3:
                            print("Le tueur en série t'attaque à son tour avec", colored("une lame cachée dans sa manche", 'cyan'), "!")
                        elif EnnemiAléatoire == 4:
                            print("Le voleur t'attaque à son tour avec", colored("un pied de biche", 'cyan'), "!")
                        elif EnnemiAléatoire == 5:
                            print("Le schizophrène t'attaque à son tour avec", colored("un cocktail molotov", 'cyan'), "!")
                    
                    AttaqueEnnemie = StatsEnnemisATT - StatsPersoDEFCombat/5
                    global StatsPersoHPCombat
                    StatsPersoHPCombat -= AttaqueEnnemie
                    print("Il t'inflige", colored(AttaqueEnnemie, 'cyan'), "points de dégats !")
                    if StatsPersoHPCombat > 0:    
                        print("Il te reste", colored(StatsPersoHPCombat, 'cyan'), "points de vie !")
                    else:
                        print(colored("Aïe aïe aïe... On dirait bien que l'aventure s'arrête ici pour toi !", 'red'))
                        print(colored("Retour au menu imminent...", 'red'))
                        ResetVariables()
                        Menu()

                if StatsEnnemisHPCombat > 0:
                    EnemyTurn()
            
            if ChoixMode == 2 and PositionPersoX == 3 and PositionPersoY == 3 and StatsEnnemisHPCombat <= 0:
                return
        
        def Item():
            
            ItemOuArgentOuSarahOuCarte = random.randint(1,10)
            
            if ItemOuArgentOuSarahOuCarte > 5:
                def GetItem(): ### Fonction qui permet d'avoir une arme ou un boost     
                    ArmeOuArmureOuBoost = random.randint(0,2)
                    
                    if ArmeOuArmureOuBoost == 0:
                        ArmeAléatoire = ListeArmesTrouvables[random.randint(0,2)]
                        
                        InventaireNomArmes.append(ArmeAléatoire)
                        
                        if ArmeAléatoire == Taser:
                            InventaireStatsArmes.append(TaserPtsATT)
                        elif ArmeAléatoire == Pistolet:
                            InventaireStatsArmes.append(PistoletPtsATT)
                        elif ArmeAléatoire == Fusil:
                            InventaireStatsArmes.append(FusilPtsATT)
                        
                        print("Tu viens de trouver", colored(ArmeAléatoire, 'cyan'), "!")
                        print("Elle cause", colored(InventaireStatsArmes[-1], 'cyan'), "points de dégats.")
                        
                        if ArmeAléatoire != InventaireNomArmes[0]:
                            print("Ton arme équipée actuellement cause", colored(InventaireStatsArmes[0], 'cyan'), "points de dégats.")
                            print("Souhaites-tu l'équiper ?")
                            print("Oui = 1")
                            print("Non = 2")
                            
                            def AskEquipWeapon():    
                                ChoixEquiperArme = int(input())

                                if ChoixEquiperArme == 1:
                                    InventaireNomArmes.reverse()
                                    InventaireStatsArmes.reverse()
                                    print("C'est équipé !")
                                
                                elif ChoixEquiperArme == 2:
                                    print("Arme non équipée.")
                                
                                else:
                                    print("Tape 1 pour l'équiper, 2 pour ne pas l'équiper.")
                                    AskEquipWeapon()
                            AskEquipWeapon()

                        else:
                            print("Tu as déjà équipé cette arme.")


                    elif ArmeOuArmureOuBoost == 1:
                        ArmureAléatoire = ListeArmuresTrouvables[random.randint(0,3)]
                        print("Tu viens de trouver", colored(ArmureAléatoire, 'cyan'), "!")
                        if ArmureAléatoire not in InventaireNomArmures:    
                            InventaireNomArmures.append(ArmureAléatoire)
                        
                        global GiletRembourréDispo
                        global AntiCouteauDispo
                        global CombinaisonKevlarDispo
                        global PareBalleDispo
                        
                        if ArmureAléatoire == GiletRembourré:
                            GiletRembourréDispo += 1
                        elif ArmureAléatoire == AntiCouteau:
                            AntiCouteauDispo += 1
                        elif ArmureAléatoire == CombinaisonKevlar:
                            CombinaisonKevlarDispo += 1
                        elif ArmureAléatoire == PareBalle:
                            PareBalleDispo += 1


                    elif ArmeOuArmureOuBoost == 2:
                        BoostAléatoire = ListeBoostsTrouvables[random.randint(0,2)]
                        print("Tu viens de trouver", colored(BoostAléatoire, 'cyan'), "!")
                        global BoostHPQuantité
                        global BoostATTQuantité
                        global BoostDEFQuantité
                        if BoostAléatoire == BoostHP:
                            BoostHPQuantité += 1
                        elif BoostAléatoire == BoostATT:
                            BoostATTQuantité += 1
                        elif BoostAléatoire == BoostDEF:
                            BoostDEFQuantité += 1
                GetItem()
            
            elif ItemOuArgentOuSarahOuCarte == 4 or ItemOuArgentOuSarahOuCarte == 5:
                def GetMoney(): ### Fonction qui permet de récupérer de l'argent
                    global ArgentQuantité
                    ArgentAléatoire = ListeArgentTrouvable[random.randint(0,2)]
                    if ArgentAléatoire == ListeArgentTrouvable[0]:
                        ArgentQuantité += ListeArgentTrouvable[0]
                        print("Tu viens de trouver", colored(ListeArgentTrouvable[0], 'cyan'), "$ !")
                        print("Tu as maintenant", colored(ArgentQuantité, 'cyan'), "$ !")
                    elif ArgentAléatoire == ListeArgentTrouvable[1]:
                        ArgentQuantité += ListeArgentTrouvable[1]
                        print("Tu viens de trouver", colored(ListeArgentTrouvable[1], 'cyan'), "$ !")
                        print("Tu as maintenant", colored(ArgentQuantité, 'cyan'), "$ !")
                    elif ArgentAléatoire == ListeArgentTrouvable[2]:
                        ArgentQuantité += ListeArgentTrouvable[2]
                        print("Tu viens de trouver", colored(ListeArgentTrouvable[2], 'cyan'), "$ !")
                        print("Tu as maintenant", colored(ArgentQuantité, 'cyan'), "$ !")
                GetMoney()
            
            elif ItemOuArgentOuSarahOuCarte == 2 or ItemOuArgentOuSarahOuCarte == 3:
                def Heal(): ### Fonction qui permet au joueur de se faire soigner par Dr. Tancredi
                    global StatsPersoHPCombat
                    if StatsPersoHPCombat != StatsPersoHP:
                        StatsPersoHPCombat += (StatsPersoHP - StatsPersoHPCombat)
                        print(colored("Quelqu'un te tape sur l'épaule...", 'red'))
                        print(colored("C'est Sarah Tancredi ! Michaël lui aurait parlé de toi en bien et elle décide de te soigner !", 'red'))
                        print("Tu as maintenant", colored(StatsPersoHPCombat, 'cyan'), "points de vie.")
                    else:
                        Item()
                Heal()
            
            elif ItemOuArgentOuSarahOuCarte == 1:
                def GetMap(): ### Fonction qui nous indique la sortie
                    global Carte
                    if Carte == 0:
                        print(colored("Tu viens de trouver un plan de la prison à moitié brûlé...", 'red'))
                        print(colored("Il semblerait que la sortie se trouve au nord-est de la prison !", 'red'))
                        Carte += 1
                    else:
                        Item()
                GetMap()
                

        CombatOuObjet = random.randint(0,1)
        
        if CombatOuObjet == 0:
            Combat()
        else:
            if PositionPersoX == 3 and PositionPersoY == 3:
                Combat()
            else:
                Item()
    
    Event()
    
    if ChoixMode == 2 and PositionPersoX == 3 and PositionPersoY == 3 and StatsEnnemisHPCombat <= 0:
        return
    
    StartGame()
    

def About(): ### About
    print("\n")
    print("Ce jeu a été crée par Hugo Lemerle, Lonis Mahi, Alexy Nautet et Samuel Ravel lors d'un projet en programmation (python) à HETIC en 2020/21.")
    print('Il est inspiré de l\'univers de la série "Prison Break".')
    Menu()


def Menu(): ### Menu
    print("\n")
    print(colored("MENU :", attrs=['bold']))
    print("1 :", colored("Play Game", attrs=['bold']))
    print("2 :", colored("About", attrs=['bold']))
    print("3 :", colored("Exit", attrs=['bold']))
    
    
    ChoixMenu = int(input())
    
    if ChoixMenu == 1:
        PlayGame()
    elif ChoixMenu == 2:
        About()
    elif ChoixMenu == 3:
        sys.exit()
    else:
        print("Tape 1, 2 ou 3.")
        Menu()

Menu()