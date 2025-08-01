# import.py
import csv
from app import create_app, db
from app.models import HSRGame8multi # adjust as needed


app = create_app()

def main(file_path="hsr8multi.csv"):
    with app.app_context():
        csv_character_names = set()

        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for name, slug, build1name, lightcone0a, lightcone1a, lightcone2a, lightcone3a, relic0a, relic1a, relic2a, ornament0a, ornament1a, ornament2a, bodystata, feetstata, spherestata, ropestata, substatsa, build2name, lightcone0b, lightcone1b, lightcone2b, lightcone3b, relic0b, relic1b, relic2b, ornament0b, ornament1b, ornament2b, bodystatb, feetstatb, spherestatb, ropestatb, substatsb in reader:
                csv_character_names.add(name)

                char = HSRGame8multi.query.filter_by(name=name).first()
                if char:
                    char.slug = slug
                    char.build1name = build1name
                    char.lightcone0a = lightcone0a
                    char.lightcone1a = lightcone1a
                    char.lightcone2a = lightcone2a
                    char.lightcone3a = lightcone3a
                    char.relic0a = relic0a
                    char.relic1a = relic1a
                    char.relic2a = relic2a
                    char.ornament0a = ornament0a
                    char.ornament1a = ornament1a
                    char.ornament2a = ornament2a
                    char.bodystata = bodystata
                    char.feetstata = feetstata
                    char.spherestata = spherestata
                    char.ropestata = ropestata
                    char.substatsa = substatsa
                    char.build2name = build2name
                    char.lightcone0b = lightcone0b
                    char.lightcone1b = lightcone1b
                    char.lightcone2b = lightcone2b
                    char.lightcone3b = lightcone3b
                    char.relic0b = relic0b
                    char.relic1b = relic1b
                    char.relic2b = relic2b
                    char.ornament0b = ornament0b
                    char.ornament1b = ornament1b
                    char.ornament2b = ornament2b
                    char.bodystatb = bodystatb
                    char.feetstatb = feetstatb
                    char.spherestatb = spherestatb
                    char.ropestatb = ropestatb
                    char.substatsb = substatsb
                    print(f"Updated character: {name}")
                else:
                    char = HSRGame8multi(name=name, slug=slug, build1name = build1name, lightcone0a = lightcone0a, lightcone1a = lightcone1a, lightcone2a = lightcone2a, lightcone3a = lightcone3a, relic0a = relic0a,
                                    relic1a = relic1a, relic2a = relic2a, ornament0a = ornament0a, ornament1a = ornament1a, ornament2a = ornament2a, bodystata = bodystata,
                                    feetstata = feetstata, spherestata = spherestata, ropestata = ropestata, substatsa = substatsa, build2name = build2name, lightcone0b = lightcone0b, lightcone1b = lightcone1b, lightcone2b = lightcone2b, lightcone3b = lightcone3b, relic0b = relic0b,
                                    relic1b = relic1b, relic2b = relic2b, ornament0b = ornament0b, ornament1b = ornament1b, ornament2b = ornament2b, bodystatb = bodystatb,
                                    feetstatb = feetstatb, spherestatb = spherestatb, ropestatb = ropestatb, substatsb = substatsb)
                    db.session.add(char)
                    print(f"Added character: {name}")

        existing_characters = HSRGame8multi.query.all()
        for character in existing_characters:
            if character.name not in csv_character_names:
                db.session.delete(character)
                print(f"Deleted character: {character.name}")

        db.session.commit()

if __name__ == "__main__":
    main()  # no arguments passed
