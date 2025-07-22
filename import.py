# import.py
import csv
from app import create_app, db
from app.models import Character  # adjust as needed


app = create_app()

def main(file_path="characters.csv"):
    with app.app_context():
        csv_character_names = set()

        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for name, slug, game in reader:
                csv_character_names.add(name)

                char = Character.query.filter_by(name=name).first()
                if char:
                    char.slug = slug
                    char.game = game
                    print(f"Updated character: {name}")
                else:
                    char = Character(name=name, slug=slug, game=game)
                    db.session.add(char)
                    print(f"Added character: {name}")

        existing_characters = Character.query.all()
        for character in existing_characters:
            if character.name not in csv_character_names:
                db.session.delete(character)
                print(f"Deleted character: {character.name}")

        db.session.commit()

if __name__ == "__main__":
    main()  # no arguments passed
