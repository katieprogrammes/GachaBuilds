# import.py
import csv
from app import create_app, db
from app.models import Genshin8Multi # adjust as needed


app = create_app()

def main(file_path="genshin8multi.csv"):
    with app.app_context():
        csv_character_names = set()

        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for name, slug, build1name, weapon0a, weapon1a, weapon2a, weapon3a, artifact0a, artifact1a, artifact2a, artifact3a, sandsstata, gobletstata, circletstata, substatsa, build2name, weapon0b, weapon1b, weapon2b, weapon3b, artifact0b, artifact1b, artifact2b, artifact3b, sandsstatb, gobletstatb, circletstatb, substatsb in reader:
                csv_character_names.add(name)

                char = Genshin8Multi.query.filter_by(name=name).first()
                if char:
                    char.slug = slug
                    char.build1name = build1name
                    char.weapon0a = weapon0a
                    char.weapon1a = weapon1a
                    char.weapon2a = weapon2a
                    char.weapon3a = weapon3a
                    char.artifact0a = artifact0a
                    char.artifact1a = artifact1a
                    char.artifact2a = artifact2a
                    char.artifact3a = artifact3a
                    char.sandsstata = sandsstata
                    char.gobletstata = gobletstata
                    char.circletstata = circletstata
                    char.substatsa = substatsa
                    char.build2name = build2name
                    char.weapon0b = weapon0b
                    char.weapon1b = weapon1b
                    char.weapon2b = weapon2b
                    char.weapon3b = weapon3b
                    char.artifact0b = artifact0b
                    char.artifact1b = artifact1b
                    char.artifact2b = artifact2b
                    char.artifact3b = artifact3b
                    char.sandsstatb = sandsstatb
                    char.gobletstatb = gobletstatb
                    char.circletstatb = circletstatb
                    char.substatsb = substatsb
                    print(f"Updated character: {name}")
                else:
                    char = Genshin8Multi(name=name, slug=slug, build1name = build1name, weapon0a = weapon0a, weapon1a = weapon1a, weapon2a = weapon2a, 
                                         weapon3a = weapon3a, artifact0a = artifact0a, artifact1a = artifact1a, artifact2a = artifact2a, artifact3a = artifact3a, 
                                         sandsstata = sandsstata, gobletstata = gobletstata, circletstata = circletstata, substatsa = substatsa, build2name = build2name, 
                                         weapon0b = weapon0b, weapon1b = weapon1b, weapon2b = weapon2b, weapon3b = weapon3b, artifact0b = artifact0b,
                                        artifact1b = artifact1b, artifact2b = artifact2b, artifact3b = artifact3b, sandsstatb = sandsstatb, gobletstatb = gobletstatb, 
                                        circletstatb = circletstatb, substatsb = substatsb)
                    db.session.add(char)
                    print(f"Added character: {name}")

        existing_characters = Genshin8Multi.query.all()
        for character in existing_characters:
            if character.name not in csv_character_names:
                db.session.delete(character)
                print(f"Deleted character: {character.name}")

        db.session.commit()

if __name__ == "__main__":
    main()  # no arguments passed
