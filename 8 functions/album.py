def make_album(artist_name, album_title, tracks=''):
	""" craets a deictionary describing an album"""
	album={"artist" : artist_name, "album title" : album_title}
	if tracks:
		album['number of tracks']=tracks
	return album
	
print(make_album("beetles", "love me do"))
print(make_album("girl dead monster", "alchemy", 3))
print(make_album("bob johny", "ghostbusters"))

while True:
	print("\nyou can make a dictionay of music albums by inputing the neccery data")
	print("to quit input 	'q' at any point")
	artist=input("artist name: ")
	if artist=="q":
		break
	album_name=input("album name: ")
	if album_name=="q":
		break
	tracks=input("number of tracks (leave empty if unknown): ")
	if tracks=="q":
		break
	int(tracks)	
	new_album=make_album(artist, album_name, tracks)
	print(" album:\n"+str(new_album)+"\nwas created")
	

