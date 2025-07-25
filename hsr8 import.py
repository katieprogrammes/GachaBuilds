# import.py
import csv
from app import create_app, db
from app.models import HSRGame8 # adjust as needed


app = create_app()

def main(file_path="hsrgame8.csv"):
    with app.app_context():
        csv_character_names = set()

        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for name, slug, lightcone0, lightcone1, lightcone2, lightcone3, relic0, relic1, relic2, ornament0, ornament1, ornament2, bodystat, feetstat, spherestat, ropestat, substats in reader:
                csv_character_names.add(name)

                char = HSRGame8.query.filter_by(name=name).first()
                if char:
                    char.slug = slug
                    char.lightcone0 = lightcone0
                    char.lightcone1 = lightcone1
                    char.lightcone2 = lightcone2
                    char.lightcone3 = lightcone3
                    char.relic0 = relic0
                    char.relic1 = relic1
                    char.relic2 = relic2
                    char.ornament0 = ornament0
                    char.ornament1 = ornament1
                    char.ornament2 = ornament2
                    char.bodystat = bodystat
                    char.feetstat = feetstat
                    char.spherestat = spherestat
                    char.ropestat = ropestat
                    char.substats = substats
                    print(f"Updated character: {name}")
                else:
                    char = HSRGame8(name=name, slug=slug, lightcone0 = lightcone0, lightcone1 = lightcone1, lightcone2 = lightcone2, lightcone3 = lightcone3, relic0 = relic0,
                                    relic1 = relic1, relic2 = relic2, ornament0 = ornament0, ornament1 = ornament1, ornament2 = ornament2, bodystat = bodystat,
                                    feetstat = feetstat, spherestat = spherestat, ropestat = ropestat, substats = substats)
                    db.session.add(char)
                    print(f"Added character: {name}")

        existing_characters = HSRGame8.query.all()
        for character in existing_characters:
            if character.name not in csv_character_names:
                db.session.delete(character)
                print(f"Deleted character: {character.name}")

        db.session.commit()

if __name__ == "__main__":
    main()  # no arguments passed
