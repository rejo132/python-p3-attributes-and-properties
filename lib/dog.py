#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Beagle", breed="Beagle"):
        if not isinstance(name, str) or len(name.strip()) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = "Beagle"
        else:
            self.name = name
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = "Beagle"
        else:
            self.breed = breed
    
    def sit(self):
        print("The dog is sitting.")