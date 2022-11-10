songs = open("songs.txt", "w")
songs.writelines(["Song Title: ", "Title Goes Here", "\n", "Album: ", "Album Goes Here", "\n", "Artist: ", "Artist Goes Here", "\n", "Duration: ", "Duration Goes Here", "\n", "Genre: ", "Genre Goes Here" ])

songs.close()

songs = open("songs.txt", "r")
print(songs.read())

