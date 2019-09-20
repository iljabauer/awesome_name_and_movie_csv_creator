#!/bin/python3
name_to_good_movies_table = {
    "Benita": "Snow Piercer",
    "Christina": "Batman",
    "Daniela": "Star Wars",
    "Eva": "Frozen",
    "Josepha": "Cars",
    "Josephine": "Avengers",
    "Judith": "IT",
    "Juliane": "Lord of the Rings",
    "June": "Toy Story",
    "Levi": "Mulan",
    "Linda": "Spider-Man",
    "Lotus": "Fight Club",
}
def save_names_to_csv_file():
    with open("table.csv", mode="w") as excel_file:
        for name, movie in name_to_good_movies_table.items():
            excel_file.write(name+";"+movie+"\n")
        

save_names_to_csv_file()


