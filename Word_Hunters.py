import random

# Function to randomly choose a word based on the game level
def choose_word(level):
    if level == "easy":
        words = {
    "ace": "I'm the lone beacon, illuminating the path to greatness.",
    "age": "I'm the silent river, flowing through the canyons of time.",
    "air": "I'm the whispered breath, carrying dreams to distant shores.",
    "awe": "I'm the silent thunder, echoing the vastness of the universe.",
    "bat": "I'm the nocturnal dancer, gliding through the midnight symphony.",
    "bee": "I'm the diligent architect, weaving honeyed tapestries.",
    "bus": "I'm the chariot of journeys, ferrying souls to new horizons.",
    "cat": "I'm the elegant hunter, prowling through the shadows of night.",
    "cup": "I'm the vessel of hopes, brimming with the elixir of life.",
    "dog": "I'm the steadfast sentinel, guarding the gates of loyalty.",
    "ear": "I'm the silent listener, capturing the echoes of existence.",
    "eye": "I'm the mirror of the soul, reflecting the depths of being.",
    "fan": "I'm the gentle zephyr, whispering secrets through the ether.",
    "fly": "I'm the daring acrobat, pirouetting through the heavens.",
    "hat": "I'm the crown of sovereignty, adorning the brow of nobility.",
    "joy": "I'm the elusive sprite, dancing on beams of sunlight.",
    "key": "I'm the keeper of secrets, unlocking doors to the unknown.",
    "map": "I'm the cartographer's canvas, charting the expanse of dreams.",
    "net": "I'm the weaver of connections, linking hearts across realms.",
    "pen": "I'm the scribe's quill, inscribing tales of imagination.",
    "pie": "I'm the sweet melody, serenading the taste buds with delight.",
    "sky": "I'm the azure tapestry, adorned with stars of destiny.",
    "sun": "I'm the radiant sovereign, casting warmth upon the earth.",
    "tea": "I'm the elixir of serenity, calming the storms within.",
    "toy": "I'm the playful sprite, dancing through realms of innocence.",
    "web": "I'm the spinner of fate, weaving threads of connection.",
    "win": "I'm the triumphant phoenix, rising from ashes of adversity.",
    "yes": "I'm the whispered affirmation, echoing the chambers of possibility.",
    "zip": "I'm the fleeting whisper, racing on winds of fleeting moments.",}

        
    elif level == "medium":
        words ={"Amber": "I'm sunlight's memory, trapped in golden tears.",
                "Angel": "I wear the sky's wings, with a halo of grace.",
                "Apple": "I'm a round temptation, hiding sweet secrets within.",
                "Arrow": "I'm a silent messenger, flying straight and true.",
                "Beach": "Where land and sea embrace, I'm nature's sandy kiss.",
                "Black": "I'm darkness's canvas, where secrets find their hiding.",
                "Blink": "I'm a moment's whisper, gone before you notice.",
                "Brave": "I'm courage's shadow, casting fear aside.",
                "Bread": "I rise from earth's embrace, sustaining life with each bite.",
                "Brick": "I'm solid resolve, building paths to dreams.",
                "Brush": "I'm an artist's whisper, painting colors on the canvas of life.",
                "Burst": "I'm a sudden eruption, breaking through the silence.",
                "Cabin": "I'm nature's refuge, nestled among the trees.",
                "Chair": "I'm a silent supporter, cradling weary souls.",
                "Charm": "I'm luck's silent whisper, dangling from the threads of fate.",
                "Chess": "I'm a battle of minds, where strategy reigns supreme.",
                "Cloud": "I'm a dream's journey, drifting through the endless sky.",
                "Coast": "I'm the meeting of worlds, where land and sea embrace.",
                "Creek": "I'm nature's melody, singing through the rocks.",
                "Crime": "I'm society's shadow, lurking in the depths of the night.",
                "Crown": "I'm royalty's embrace, adorned with jewels of power.",
                "Dance": "I'm rhythm's heartbeat, moving souls in harmony.",
                "Diary": "I'm a whisper of secrets, bound in pages of time.",
                "Diver": "I'm an explorer of depths, diving into the unknown.",
                "Dream": "I'm imagination's playground, where reality takes flight.",
                "Drink": "I'm thirst's relief, flowing through the rivers of life.",
                "Eagle": "I'm freedom's symbol, soaring on the winds of change.",
                "Earth": "I'm nature's cradle, holding life in my embrace.",
                "Edgey": "I'm life's sharp edge, cutting through the haze of existence.",
                "Ember": "I'm fire's memory, glowing in the darkness.",
                "Empty": "I'm the void's echo, waiting to be filled.",
                "Error": "I'm logic's stumble, tripping over the wires of reason.",
                "Fairy": "I'm magic's whisper, dancing on the edge of dreams.",
                "False": "I'm truth's illusion, hiding in plain sight.",
                "Flame": "I'm passion's embrace, burning bright in the night.",
                "Fleet": "I'm nature's rush, sailing on the winds of change.",
                "Flood": "I'm nature's fury, washing away the sins of man.",
                "Flour": "I'm nature's bounty, ground from the seeds of life.",
                "Flute": "I'm nature's melody, singing in the winds of time.",
                "Forge": "I'm creation's fire, shaping dreams from the flames.",
                "Frame": "I'm memory's embrace, holding moments in the threads of time.",
                "Frost": "I'm winter's touch, painting the world in icy hues.",
                "Ghost": "I'm memory's echo, whispering through the halls of time.",
                "Giant": "I'm strength's colossus, standing tall against the tides.",
                "Globe": "I'm nature's canvas, painted with the colors of life.",
                "Grace": "I'm elegance's whisper, dancing on the edge of beauty.",
                "Grass": "I'm nature's carpet, covering the earth in green.",
                "Grave": "I'm life's final embrace, holding memories in my silent arms.",
                "Green": "I'm nature's color, painting life with my vibrant brush.",
                "Happy": "I'm joy's laughter, ringing through the halls of time.",
                "Heart": "I'm love's rhythm, beating in the chest of life.",
                "Heavy": "I'm burden's weight, pressing down on weary shoulders.",
                "Honey": "I'm nature's sweetness, dripping from the lips of life.",
                "House": "I'm shelter's embrace, holding warmth in my walls.",
                "Ideal": "I'm perfection's whisper, guiding dreams to their heights.",
                "Image": "I'm memory's echo, captured in the frames of time.",
                "Ivory": "I'm nature's treasure, gleaming in the moon's embrace.",
                "Jewel": "I'm nature's treasure, sparkling in the depths of time.",
                "Joint": "I'm connection's embrace, linking worlds in my arms.",
                "Judge": "I'm justice's scale, weighing the sins of man.",
                "Knife": "I'm life's sharp edge, cutting through the fabric of existence.",
                "Laugh": "I'm joy's echo, ringing through the halls of time.",
                "Light": "I'm life's beacon, shining in the darkness of existence.",
                "Limbo": "I'm existence's edge, dancing on the brink of life.",
                "Limit": "I'm freedom's boundary, holding back the tides of time.",
                "Logic": "I'm reason's whisper, guiding minds through the maze of existence.",
                "Lucky": "I'm fate's embrace, smiling on the chosen few.",
                "Magic": "I'm wonder's whisper, dancing on the edge of dreams.",}

    else:  # Hard level
        words = {
            "computer": "What has keys but can't open locks, space but no room, and you can enter but not go inside?",
            "absolute": "I'm the unwavering North Star, guiding you through uncertainty.",
            "activity": "I'm the lively dance of autumn leaves, swirling in the breeze.",
            "addition": "I'm the gentle kiss of raindrops, merging into a soothing melody.",
            "adventure": "I'm the untamed river, carving paths through rugged terrain.",
            "afternoon": "I'm the warm embrace of a sunbeam, painting golden hues.",
            "alphabet": "I'm the magical wand of a storyteller, weaving tales into existence.",
            "although": "I'm the silent pause between heartbeats, bridging worlds apart.",
            "annoying": "I'm the persistent echo of a dripping faucet, testing your serenity.",
            "anything": "I'm the boundless sky, embracing dreams with open arms.",
            "anywhere": "I'm the whispering wind, carrying secrets to distant shores.",
            "approach": "I'm the gentle tide, luring wanderers to uncharted lands.",
            "argument": "I'm the fierce storm, raging within conflicting minds.",
            "athletic": "I'm the graceful flight of a soaring eagle, defying gravity's grasp.",
            "attitude": "I'm the radiant sunflower, basking in the warmth of self-belief.",
            "audience": "I'm the enchanted forest, echoing tales of the past.",
            "backward": "I'm the silent guardian of forgotten dreams, retracing footsteps.",
            "baseball": "I'm the symphony of cheers and cries, echoing across the diamond.",
            "beautiful": "I'm the kaleidoscope of colors, painting life with vibrant hues.",
            "birthday": "I'm the glowing ember, marking the passage of time.",
            "building": "I'm the towering oak, rooted deep in the earth's embrace.",
            "business": "I'm the bustling marketplace, alive with commerce's song.",
            "calendar": "I'm the timeless river, flowing through the pages of history.",
            "campaign": "I'm the silent sentinel, guarding the fortress of aspirations.",
            "capacity": "I'm the vessel of dreams, brimming with endless possibilities.",
            "careless": "I'm the reckless breeze, dancing with abandon through the fields.",
            "century": "I'm the ancient stone, etched with tales of bygone eras.",
            "champion": "I'm the blazing phoenix, rising from ashes to conquer skies.",
            "chemical": "I'm the alchemist's elixir, transforming lead into gold.",
            "chocolate": "I'm the tempting aroma of freshly baked memories, melting on tongues.",
            "circuit": "I'm the intricate labyrinth, guiding currents on their journey.",
            "civilian": "I'm the peaceful meadow, untouched by the scars of conflict.",
            "cleaning": "I'm the gentle rain, cleansing the earth with purity's touch.",
            "computer": "I'm the digital symphony, orchestrating harmonies of information.",
            "conflict": "I'm the tempestuous sea, colliding with shores in turbulent embrace.",
            "constant": "I'm the steadfast lighthouse, illuminating paths through darkness.",
            "creative": "I'm the poet's quill, dancing across parchment in a frenzy of inspiration.",
            "critical": "I'm the sharpened arrow, piercing veils of illusion with precision's aim.",
            "currency": "I'm the river of abundance, flowing through markets in currents of exchange.",
            "database": "I'm the silent librarian, preserving tales within the labyrinth of memory.",
            "daughter": "I'm the budding flower, blooming with the essence of generations past.",
            "delivery": "I'm the tireless messenger, traversing realms to bridge hearts.",
            "distance": "I'm the intangible veil, separating souls in the dance of existence.",
            "dividend": "I'm the silent benefactor, sharing wealth with open palms.",
            "document": "I'm the parchment scroll, chronicling journeys in inked symphony.",
            
        }
    return random.choice(list(words.items()))

# Function to generate feedback for the player's guess
def generate_feedback(hidden_word, guess):
    feedback = ''
    # Check each letter in the guess
    for i in range(len(guess)):
        letter = guess[i]
        # If the letter is correctly placed, capitalize it
        if letter == hidden_word[i]:
            feedback += letter.upper()
        # If the letter is in the hidden word but not in the correct position
        elif letter in hidden_word:
            feedback += letter.lower()
        # If the letter is not in the hidden word at all, use a full stop
        else:
            feedback += '.'
    return feedback

# Function to check if the guess is correct
def check_guess(hidden_word, guess):
    return guess == hidden_word

# Function to calculate the score based on attempts left
def calculate_score(attempts_left):
    if attempts_left == 5:
        return 1000
    elif attempts_left == 4:
        return 800
    elif attempts_left == 3:
        return 500
    elif attempts_left == 2:
        return 300
    elif attempts_left == 1:
        return 100
    else:
        return 0

# Main function to run the game
def main():
    total_score = 0
    level = "easy"  # Start with the easy level
    print("")
    print("-----------------------------------------------RIDDLE-MASTERS------------------------------------------------")
    print("RIDDLE--WORD--MASTERS is an engaging word-guessing game where players solve riddles to unveil hidden words.")
    print("With each riddle presented, players must decipher the clues to correctly guess the corresponding word.")
    print("Starting at the 'easy' level, they progress through 'medium' and 'hard' levels by accumulating points for each correct guess.")
    print("The challenge lies in deducing the word within a limited number of attempts, with the ultimate goal of achieving the highest possible score.")
    print("Each level introduces new riddles and longer words, ensuring continuous excitement and mental stimulation for players of all ages.\n")
    print("-------------------------------------------------[FEEDBACK]-----------------------------------------------------")
    print(">>> You will get an uppercase for the correct positioned letter found in the hidden word")
    print(">>> You will get an lowercase for the incorrect positioned letter found in the hidden word")
    print(">>> You will get an full stop for the letter not found in the hidden word")
    print("\n_________________________________________________GOODLUCK_______________________________________________________\n")
    
    while True:
        if total_score < 3000:
            level = "easy"
            min_score = 0
            max_score = 2999
            word_length = 3
            print(">>> Instructions: You need to guess a 3-letter word based on the given riddle & have 5 attempts limit.")
        elif total_score >= 3000 and total_score < 8000:
            level = "medium"
            min_score = 3000
            max_score = 7999
            word_length = 5
            print(">>> Instructions: You need to guess a 5-letter word based on the given riddle & have 5 attempts limit.")
        elif total_score >= 8000:
            level = "hard"
            min_score = 8000
            word_length = 8
            print(">>> Instructions: You need to guess an 8-letter word based on the given riddle & have 5 attempts limit.")

        hidden_word, riddle = choose_word(level)
        attempts_left = 5
        print(f"\n{level.capitalize()} Level:")
        print("Riddle:", riddle)

        while attempts_left > 0:
            print("\nAttempts left:", attempts_left)
            guess = input(f"Enter your guess ({word_length} letters), or enter '###' to quit: ").strip().lower()
            
            # Check if the player wants to quit
            if guess == "###":
                print("Quitting the game...")
                print("Final Score:", total_score)
                print("\n______________________________________BYE, YOU COULD HAVE SCORED BETTER!___________________________________\n")
                return

            if len(guess) != word_length or not guess.isalpha():
                print(f"Invalid input. Please enter a {word_length}-letter word.")
                continue

            if check_guess(hidden_word, guess):
                score = calculate_score(attempts_left)
                total_score += score
                print("\nCongratulations! You guessed the word:", hidden_word)
                print("Score for this word:", score)
                print("Total Score:", total_score)
                print("\n________________________________________NICE! KEEP YOUR WIN STREAK!________________________________________\n")
                break  # Exit the guessing loop when the word is correctly guessed

            feedback = generate_feedback(hidden_word, guess)
            print("Feedback:", feedback)

            attempts_left -= 1

            if check_guess(hidden_word, guess):  # Check if the guess is correct again after decrementing attempts_left
                break  # Exit the guessing loop when the word is correctly guessed

        if attempts_left == 0:
            print("\nSorry, you're out of attempts. The word was:", hidden_word)
            print("Total Score:", total_score)
            print("Game Over. Your highest score:", total_score)
            print("\n_____________________________________________GAME-OVER, YOU TRIED THOUGH!_______________________________________\n")
            break

        if total_score >= min_score and total_score <= max_score:
            if level == "easy":
                level = "medium"
            elif level == "medium":
                level = "hard"
            else:
                print("\nCongratulations! You have completed this levels!")
                print("Game Over >>> Your highest score:", total_score)
                return
        else:
            hidden_word, riddle = choose_word(level)
            attempts_left = 5
            print("\n__________________________________________WOW! TIME TO LEVEL UP NOW___________________________________________\n")
            print("New level unlocked, the letter count for each word has increased, and yet the attempts are kept at 5 only.\n[ *not smiling*:) isn't that just amazing]")
            

    print("\nFinal Score:", total_score)

if __name__ == "__main__":
    main()
