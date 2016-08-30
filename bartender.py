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
        "nouns": ["lion", "whale shark", "ship", "pirate", "ant", "dolphin", "walrus"],
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
 
       
def suggest_another():
        '''a function to check if the customer would like another drink'''
        another_drink_response = raw_input("Would you like another drink? :")
        if str.lower(another_drink_response) == 'yes' or str.lower(another_drink_response) == 'y':
                main()
        else:
                print "Alrighty then, captain!"
                
def drink_phrase(suggested_drink):
        
        if len(suggested_drink) > 1: 
        
                final_item = suggested_drink.pop()
        
                phrase = ""
        
                for item in suggested_drink: 
                        phrase += item + ", "
                print "Nice choice, Captain! 1 " + cocktail_name() + " with a " + phrase[:-2] + " & a " + final_item \
                + " especially mixed by your favourite Pirate Bartender coming right up, arghhh!"
        
        else: 
                print "Too easy. 1 x " + cocktail_name() + " with a straight " + suggested_drink[0] + " coming right up!"


def main():
        '''a function to run mixed_drink function, with arguments from preferences \
        function to return a list of ingredients that will be included in the drink. \
        after any drink is served, a function will be called to ask if the customer wants another drink. \
        the main function will be executed when file is exected on command line.'''
        
        suggested_drink = mixed_drink(preferences)
        
        drink_phrase(suggested_drink)
        
        suggest_another()

if __name__ == '__main__':
    main()



