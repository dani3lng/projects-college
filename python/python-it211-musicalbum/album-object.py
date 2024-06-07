import album

#main definition
def main():
    #get a list of objects
    tracks = make_list()
    #display data in list
    print('You have enter the following:')
    display_list(tracks)
def make_list():
    #create empty list
    album_list = []

    #add 3 albums
    print('Enter the data for 3 albums')
    for count in range(1,4):
        #get album data
        artist = input('Enter the name of the ablum artist: ')
        title = input('Enter the title of the album: ')
        length = input('Enter the number of songs in the album: ')
        year = input('Enter the year the album was released: ')
        print()
        
        #create an object in memory
        track = album.Album(artist,title,length,year)

        #add object to list
        album_list.append(track)

    #return list
    return album_list
def display_list(album_list):
    for item in album_list:
        print(item.get_artist())
        print(item.get_title())
        print(item.get_length())
        print(item.get_year())
        print()

#call main function
main()