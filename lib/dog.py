#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Fido")
print(f"name: {fido.name}, breed: {fido.breed}")

pass