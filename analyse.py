#alle Sonderfaelle der Nachrichten filtern, extra Funktion

import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

#ToDo take this line for command line parameter
#chat = open(sys.argv[1], "r", encoding="utf-8")	#your text file

chat = open("WhatsApp Chat mit Paul W.txt", "r", encoding="utf-8")
#WhatsApp Chat mit Paul W.txt

totalMessages = 0 				#number of total messages in chat
medias = 0						#number of medias
users = []
totaldays = 0

#ToDo Keymap User:Anzahl Nachrichten schreiben
dictionary = {}						#map values User: Messages
#read() reads the whole file
#print(chat.read())

#read one line
#print(chat.readline())
firstdate = ""
lastdate = ""

has_run = False
#read all lines
for line in chat:
	
	if line.startswith('.', 2, 3) and line.startswith('.', 5, 6):	#filter messages over more lines
		totalMessages+=1
		if line.find("<Medien ausgeschlossen>") != -1:
			medias+=1

		#filter the username
		username = line.split(':')[1]
		username = username[5:]
		
		currentdate = line[0:8]
		if has_run == False:
			firstdate = currentdate
		lastdate = currentdate		
		#ToDo function for special messages
		if username.find("Ende-zu-Ende-Verschlüsselung") == -1 \
		and username.find("Die Sicherheitsnummer von") == -1 \
		and username.find("hat eine neue Telefonnummer") == -1 \
		and username.find("Gruppenbild geändert") == -1 \
		and username.find("Du hast die Gruppe") == -1:
			if not username in users: #Sonderfall ausschließen
				users.append(username)
				dictionary[username] = 1
			else:
				dictionary[username] += 1
	
	has_run = True	
	#print(line)


chat.close()

print("Total messages: ", totalMessages)
print("Total medias: ", medias)
#print("Users appearing in this chat: ", users)

for username in dictionary:
	print("Messages from ", username, ": ", dictionary[username])

#Date analysis
print("First message at:  ", firstdate)
print("Last message at:   ", lastdate)
f_date = date(int(firstdate[6:]) + 2000, int(firstdate[3:5]), int(firstdate[0:2]))
l_date = date(int(lastdate[6:]) + 2000, int(lastdate[3:5]), int(lastdate[0:2]))
dif = l_date - f_date
print("Total days: ", dif.days)
print("Average messages per day: ", round(totalMessages / dif.days, 2))

#Data for plotting piechart
pielabels = []
messages = []
for username, values in dictionary.items():
	pielabels.append(username)
	messages.append(values)

plt.pie(messages, labels=pielabels, shadow = True, autopct = '%1.1f%%')

plt.axis('equal')
plt.show()

