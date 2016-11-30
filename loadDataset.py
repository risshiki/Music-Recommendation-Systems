

##def loadpartialDataset(path="", parameter,flag):
##	""" To load the dataSet"
##		Parameter: The folder where the data files are stored
##		Return: the dictionary with the data
##	"""
##	#Recover the titles of the books
##	books = {}
##	for line in open(path+"BX-Books.csv"):
##            line = line.replace('"', "")
##            (id,title,author,year,publisher) = line.split(";")[0:5]
##            if flag == 0:
##                if publisher == parameter:
##                    books[id] = title
##            if flag == 1:
##                if author == parameter:
##                    books[id] = title
##                
##                    
##	#Load the data
##	prefs = {}
##	count = 0
##	for line in open(path+"BX-Book-Ratings.csv"):
##		line = line.replace('"', "")
##		line = line.replace("\\","")
##		(user,bookid,rating) = line.split(";")
##		try:
##		    if float(rating) > 0.0:
##			if books[bookid] is not None:
##                            prefs.setdefault(user,{})
##                            prefs[user][books[bookid]] = float(rating)
##		except ValueError:
##			count+=1
##			print ("value error found! " + user + bookid + rating)
##		except KeyError:
##			count +=1
##			print ("key error found! " + user + " " + bookid)
##	return prefs
##


def loadDataset():
    """
We are building a dataset in a 2D Dictionary. The user will act as the key to the list of bands he likes

    """
    import pickle
    import csv
    
    #Basically a dictionary that allows us to store artist indexes
    artists = {}
    f = open("artist.csv")
    for line in f:
        line = line.replace('"',"")
        line = line.replace("\\","")
        strings = line.split(",")
        i = 0
        for artist in strings:
            artists[str(i)] = artist 
            i +=1
    f.close()

    prefs = {}
    
    f = open("data.csv")

    for line in f:
        line = line.replace('"',"")
        line = line.replace("\\","")
        strings = line.split(",")
        i = 1
        user = strings[0]

        for value in strings[1:]:
            if int(value)==1:
                if user not in prefs:
                    prefs[user] = [artists[str(i)]]
                else:
                    prefs[user].append(artists[str(i)])
            i+=1


    f = open('userprefs1.csv', 'w')
    for key,value in prefs.items():
        for item in value:
            f.write(item + ',')
        f.write("\n")
    f.close()
    
##    print("\n")
##    print(artists['211'])
##
##
##    f = open('artistlist' + '.pkl', 'wb')
##    pickle.dump(artists,f,pickle.HIGHEST_PROTOCOL)
##    f.close()
##        
##    f = open('userprefs' + '.pkl', 'wb')
##    pickle.dump(prefs, f, pickle.HIGHEST_PROTOCOL)
##    f.close()
##
##    f = open('userprefs' + '.pkl', 'rb')
##    newdict = pickle.load(f)
##    f.close()
##
##    for artist_id in newdict['7211']:
##        print(artists[artist_id])
##
##    f = open('artistlist' + '.pkl', 'rb')
##    newartist = pickle.load(f)
##    f.close()
##    print("\n")
##    print(newartist['1'])
##                
def loadDataset2():
    """
We are building a dataset in a 2D Dictionary. The user will act as the key to the list of bands he likes

    """
    import pickle
    #Basically a dictionary that allows us to store artist indexes
    artists = {}
    f = open("artist.csv")
    for line in f:
        line = line.replace('"',"")
        line = line.replace("\\","")
        strings = line.split(",")
        i = 0
        for artist in strings:
            artists[str(i)] = artist 
            i +=1
    f.close()

    prefs = {}
    
    f = open("data.csv")

    for line in f:
        line = line.replace('"',"")
        line = line.replace("\\","")
        strings = line.split(",")
        i = 1
        user = strings[0]

        for value in strings[1:]:
            if int(value)==1:
                if user not in prefs:
                    prefs[user] = [str(i)]
                else:
                    prefs[user].append(str(i))
            i+=1

    for artist_id in prefs['8270']:
        print(artists[artist_id])

    print("\n")
    print(artists['211'])


    f = open('artistlist' + '.pkl', 'wb')
    pickle.dump(artists,f,pickle.HIGHEST_PROTOCOL)
    f.close()
        
    f = open('userprefs' + '.pkl', 'wb')
    pickle.dump(prefs, f, pickle.HIGHEST_PROTOCOL)
    f.close()

    f = open('userprefs' + '.pkl', 'rb')
    newdict = pickle.load(f)
    f.close()

    for artist_id in newdict['7211']:
        print(artists[artist_id])

    f = open('artistlist' + '.pkl', 'rb')
    newartist = pickle.load(f)
    f.close()
    print("\n")
    print(newartist['1'])
                




loadDataset()
    
