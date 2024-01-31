class Analize:
    def __init__(self, nosaukums, min, max):
        self.nosaukums = nosaukums
        self.min = min
        self.max = max


hemoglobins=Analize('Hemoglobīns',12,17 )
limfociti=Analize('Limfocīti',20,41 )
eritrociti=Analize('Eritrocīti',3,18 )
glikoze=Analize('Glikoze',4,6 )
vitd=Analize('vitD',30,100 )

minHemoglobins = hemoglobins.min
maxHemoglobins = hemoglobins.max
minLimfociti = limfociti.min
maxLimfociti = limfociti.max
minEritrociti = eritrociti.min
maxEritrociti = eritrociti.max
minGlikoze = glikoze.min
maxGlikoze = glikoze.max
minVitd = vitd.min
maxVitd = vitd.max
