# import.py
import csv
from app import create_app, db
from app.models import GenshinGame8 # adjust as needed


app = create_app()

def main(file_path="genshin8.csv"):
    with app.app_context():
        csv_character_names = set()

        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for name, slug, weapon0, weapon1, weapon2, weapon3, artifact0, artifact1, artifact2, artifact3, sandsstat, gobletstat, circletstat, substats in reader:
                csv_character_names.add(name)

                char = GenshinGame8.query.filter_by(name=name).first()
                if char:
                    char.slug = slug
                    char.weapon0 = weapon0
                    char.weapon1 = weapon1
                    char.weapon2 = weapon2
                    char.weapon3 = weapon3
                    char.artifact0 = artifact0
                    char.artifact1 = artifact1
                    char.artifact2 = artifact2
                    char.artifact3 = artifact3
                    char.sandsstat = sandsstat
                    char.gobletstat = gobletstat
                    char.circletstat = circletstat
                    char.substats = substats
                    print(f"Updated character: {name}")
                else:
                    char = GenshinGame8(name=name, slug=slug, weapon0 = weapon0, weapon1 = weapon1, weapon2 = weapon2, weapon3 = weapon3, artifact0 = artifact0,
                                    artifact1 = artifact1, artifact2 = artifact2, artifact3 = artifact3, sandsstat = sandsstat, gobletstat = gobletstat, 
                                    circletstat = circletstat, substats = substats)
                    db.session.add(char)
                    print(f"Added character: {name}")

        existing_characters = GenshinGame8.query.all()
        for character in existing_characters:
            if character.name not in csv_character_names:
                db.session.delete(character)
                print(f"Deleted character: {character.name}")

        db.session.commit()

if __name__ == "__main__":
    main()  # no arguments passed
