def make_album(artist_name: str, album_title: str, number_of_songs: int=None):
    if number_of_songs:
        album = {album_title: artist_name,
                 "Number_of_songs": number_of_songs
                }
    else:
        album = {album_title: artist_name}

    return album

class Main:
    def test_make_album():
        print(make_album("kk", "KK"))
        print(make_album("jj", "JJ"))
        print(make_album("OO", "oo"))
        print(make_album("PP", "pp", 9))

    def test_ex_8_8():
        while True:
            album_title = input("Enter the album title: ")
            if album_title != "quit":
                artist_name = input(f"Enter the artist name for {album_title} album: ")
                if artist_name != "quit":
                    print(f"\n{make_album(artist_name, album_title)}\n")
                else:
                    print("\n")
                    break
            else:
                print("\n")
                break