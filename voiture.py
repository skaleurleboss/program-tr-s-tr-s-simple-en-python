class voiture:
    def __init__(self, marque, modele, roueTaille, couleurDisponible, vitesseMax, lieuxDachatDisponible):
        self.marque = marque
        self.modele = modele
        self.roueTaille = roueTaille
        self.couleurDisponible = couleurDisponible
        self.vitesseMax = vitesseMax
        self.lieuxDachatDisponible = lieuxDachatDisponible

toyotaX1 = voiture("Toyota", "X1", "40cm", "noir, rouge, bleu, bleu ciel et gris matte", "220kmh", "martigny, sion et brigue")


