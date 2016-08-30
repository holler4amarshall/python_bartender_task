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
    
names = {
        "descriptives": ["jumping", "whirling", "fluffy", "cranky", "porky"], 
        "nouns": ["lion", "bunny", "ship", "pirate", "holly", "dolphin"],
        }

responses = {}

def preferences():
        '''a function to return user response to questions as a dictionary containing taste:preference'''

        for question in questions:
                preference = raw_input((questions)[question] + ": ")
                if str.lower(preference) == 'yes' or str.lower(preference) == 'y':
                        responses[question] = "True"
                else:
                        responses[question] = "False"
        return responses

#preferences()


def mixed_drink(preferences):
        ''' a function to return the ingredients for a drink based on preference provided by separate function'''
        
        drink = []
        for preference, answer in preferences().items():
                if answer == 'True':
                        ingredient = ingredients[preference]
                        drink.append(random.choice(ingredient))
        #print drink
        return drink

#mixed_drink(preferences)

def cocktail_name():
        '''a function to return a cocktail name based on a randomly selected descriptive word and a noun'''
        name = ""
        for adjective, noun in names.items():
                first_name = names['descriptives']
                last_name = names['nouns']
                name = random.choice(first_name) + ' ' + random.choice(last_name)
     
        return name

def main():
        '''a function to run mixed_drink function, with arguments from preferences \
        function to return a list of ingredients that will be included in the drink. \
        the function will be executed when file is exected on command line.'''
        
        suggested_drink = mixed_drink(preferences)
        suggested_drink_sentence = ""
        for item in suggested_drink: 
                suggested_drink_sentence += item + ", "
        print "...Nice choice, Captain. 1 " + cocktail_name() + " with a " + suggested_drink_sentence \
        + "poured over ice and specially mixed by your favourite Pirate, coming right up!"

if __name__ == '__main__':
    main()