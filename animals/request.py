from models.animals import Animal
import sqlite3
from database import DB_FILE


def get_all_animals():  # pylint: disable=missing-docstring
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.breed,
                a.status,
                a.location_id,
                a.customer_id
            FROM animal a
        """)
        animals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            animal = Animal(row['id'],
                            row['name'],
                            row['breed'],
                            row['status'],
                            row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)
        return animals


def get_single_animal(id):  # pylint: disable=missing-docstring
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.breed,
                a.status,
                a.location_id,
                a.customer_id
            FROM animal a
            WHERE id = ?
        """, (id,))
        animal = None
        dataset = db_cursor.fetchone()
        animal = Animal(
            dataset['id'],
            dataset['name'],
            dataset['breed'],
            dataset['status'],
            dataset['location_id'],
            dataset['customer_id']
        )
        return animal


def post_single_animal(animal):  # pylint: disable=missing-docstring
    with sqlite3.connect(DB_FILE) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO Animal
                ( name, breed, status, location_id, customer_id )
            VALUES
                ( ?, ?, ?, ?, ?);
        """, (
            animal['name'],
            animal['breed'],
            animal['status'],
            animal['location_id'],
            animal['customer_id']
        ))


def delete_single_animal(id):  # pylint: disable=missing-docstring
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
                DELETE FROM animal
                WHERE id = ?
            """, (id, ))
