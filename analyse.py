#filestream einlesen - check
#file als parameter nutzen
#Chat Teilnehmer identifizieren(erstmal nur fuer einzelchats)
import sys

#ToDo take this line for command line parameter
#chat = open(sys.argv[1], "r", encoding="utf-8")	#your text file

chat = open("WhatsApp Chat mit Paul W.txt", "r", encoding="utf-8")


totalMessages = 0 				#number of total messages in chat
medias = 0						#number of medias
users = []
dictionary = {}						#map values User: Messages
#read() reads the whole file
#print(chat.read())

#read one line
#print(chat.readline())

#read all lines
for line in chat:
	
	
	if line.startswith('.', 2, 3) and line.startswith('.', 5, 6):	#filter messages over more lines
		totalMessages+=1
		if line.find("<Medien ausgeschlossen>") != -1:
			medias+=1

		#filter the username
		username = line.split(':')[1]
		username = username[5:]
		if not username in users and username.find("Ende-zu-Ende-Verschlüsselung") == -1: #Sonderfall ausschließen
			users.append(username)
		
	#print(line)

print("Total messages: ", totalMessages)
print("Total medias: ", medias)
print("Users appearing in this chat: ", users)
chat.close()