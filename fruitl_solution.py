def choose_option(name):
    print(f"Hallo {name}! Wie kann ich dir heute helfen?")
    print(" 1: Zwei Zahlen addieren")
    print(" 2: Das Wetter abfragen")
    print(" 3: Mit BeckOnline suchen")
    choice = input("§§> ")

    if choice == "1":
        add_two_numbers()
    elif choice == "2":
        query_weather()
    elif choice == "3":
        search_beckonline()
    else:
        print("Das habe ich leider nicht verstanden. Gib die zugehörige Zahl ein.")
        choose_option(name)

    print("Möchtest du noch etwas anderes machen? (j/n)")
    choice = input("§§> ")
    if choice == "j":
        choose_option(name)
    else:
        print(f"Bis zum nächsten Mal, {name}!")


def add_two_numbers():
    print("Gib die erste Zahl ein:")
    a = float(input("§§> "))
    print("Gib die zweite Zahl ein:")
    b = float(input("§§> "))
    print(f"{a} + {b} = {a + b}")


def query_weather():
    import requests
    print("Von welchem Ort möchtest du das Wetter wissen?")
    place = input("§§> ")
    url = f"https://wttr.in/{place}?format=v2"
    response = requests.get(url)
    print(response.text)


def search_beckonline():
    import webbrowser
    print("Wonach möchtest du suchen?")
    query = input("§§> ")
    url = f"https://beck-online.beck.de/Search?words={query}"
    webbrowser.open(url)


def main():
    print("Guten Tag, ich bin Fruitl. Wie heißt du?")
    name = input("§§> ")
    choose_option(name)


if __name__ == "__main__":
    main()
