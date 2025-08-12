from voiture import voiture

toyotaX1 = voiture("Toyota", "X1", 40, "noir, rouge, bleu, bleu ciel et gris matte", 220, "martigny, sion et brigue")
bmwZ3 = voiture("BMW", "Z3", 45, "noir et blanc", 250, "lausanne, genève")
audiA3 = voiture("Audi", "A3", 42, "gris et bleu", 240, "zurich, bâle")

voitures = (toyotaX1, bmwZ3, audiA3)

(rapide) =0

(terminer)= 0

while (terminer) !=  len(voitures) :

    if (rapide) < (voitures[terminer].vitesseMax) :
        (rapide) = (voitures[terminer].vitesseMax)
        (voitureActuelle) = ((voitures[terminer].marque), (voitures[terminer].modele))

    (terminer)= (terminer)+1

print((rapide), (voitureActuelle))






 

