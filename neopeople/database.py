# database.py

from neo4j import GraphDatabase
import config

class Database:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            config.NEO4J_URI,
            auth=(config.NEO4J_USER, config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def create_person(self, name, age):
        with self.driver.session() as session:
            session.run("CREATE (:Person {name: $name, age: $age})", name=name, age=age)

    def list_people(self):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Person) RETURN p.name AS name, p.age AS age")
            return [{"name": r["name"], "age": r["age"]} for r in result]

    def update_person(self, current_name, new_name):
        with self.driver.session() as session:
            session.run("""
                MATCH (p:Person {name: $current_name})
                SET p.name = $new_name
            """, current_name=current_name, new_name=new_name)

    def delete_person(self, name):
        with self.driver.session() as session:
            session.run("MATCH (p:Person {name: $name}) DELETE p", name=name)
