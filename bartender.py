import random

questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
    }

ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }

responses = {}

def preferences():

        for question in questions:
                preference = raw_input((questions)[question] + ": ")
                if str.lower(preference) == 'yes' or str.lower(preference) == 'y':
                        responses[question] = "True"
                else:
                        responses[question] = "False"
        return responses

#preferences()


def mixed_drink(preferences):
        drink = []
        for preference, answer in preferences().items():
                if answer == 'True':
                        ingredient = ingredients[preference]
                        drink.append(random.choice(ingredient))
        #print drink
        return drink

#mixed_drink(preferences)

def main():
        suggested_drink = mixed_drink(preferences)
        suggested_drink_sentence = ""
        for item in suggested_drink: 
                suggested_drink_sentence += item + ", "
        print "...Nice choice, Captain. 1 special drink with a " + suggested_drink_sentence + "poured over ice and specially mixed by your favourite Pirate, coming right up!"

if __name__ == '__main__':
    main()