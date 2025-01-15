import numpy as np
#Plotting
import matplotlib.pyplot as plt
#Lese CSV
import csv

header = []
data = []
filename = '0alAMP-kopi.csv'

#Henter data fra csvfil
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
#Leser første linje i csv-fila (den med navn til kanalene)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)

#Legger inn data fra hver kanal i hver sin liste
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data]
ch2 = [(p[2]) for p in data]


#----- Enkelt plot ------
plt.plot(time, ch1)
plt.plot(time, ch2)
plt.savefig('filnavn.png', dpi=500) #Lagrer figuren, endre filnavn
#plt.show() #Viser figuren



#----- Subplots ------
fig, (channel1, channel2) = plt.subplots(2,1) #2 rader, 1 kolonne
#fig.suptitle('Tittel')
channel1.plot(time, ch1) #Bruk labels med legend()
channel2.plot(time, ch2)

plt.savefig('filnavn2.png', dpi=500)


#----- Titler ++ ------
fig, (ax) = plt.subplots(1,1) #1 rad, 1 kolonne
ax.plot(time,ch1, label = 'ch1') # Bruk labels med legend()
ax.plot(time,ch2, label = 'ch2', color='hotpink', ) #Endre farge
ax.legend(loc='upper right')

ax.set_title('Oscilloskop')
ax.set_xlabel('Tid (s)')
ax.set_ylabel('Spenning (V)')

ax.grid(True) #Rutenett

#ax.set_xlim(-0.02,0.02) #Endrer utsnitt

plt.savefig('filnavn3.png', dpi=500)
#show the fig
#plt.show()


