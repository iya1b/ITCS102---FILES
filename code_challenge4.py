print("Let me suggest some good stuff manga or manhwa for you")

man = input("What do you prefer? manga or manhwa: ").lower().strip()
genre = input("What genre do you like? (action, romance, comedy, sports, horror): ").lower().strip()
year = input("What era do you prefer? (2000s or 2010s): ").lower().strip()
duration = input("What about the duration or length of the read? (short, medium, long): ").lower().strip()

if man == 'manga':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Claymore' (155 chapters)")
            elif duration == 'medium':
                print("Try reading 'D.Gray-man' (240+ chapters, ongoing)")
            elif duration == 'long':
                print("Check out 'Bleach' (686 chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'Lovely★Complex' (24 volumes / 68 chapters)")
            elif duration == 'medium':
                print("Try 'Nana' (84 chapters, hiatus)")
            elif duration == 'long':
                print("Go for 'Boys Over Flowers' (241 chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'School Rumble' (283 chapters but fast-paced arcs)")
            elif duration == 'medium':
                print("Try 'Detroit Metal City' (113 chapters)")
            elif duration == 'long':
                print("Check out 'Kochikame' (1,900 chapters – very long!)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Prince of Tennis' (379 chapters)")
            elif duration == 'medium':
                print("Go for 'Major' (747 chapters, baseball)")
            elif duration == 'long':
                print("Check out 'Hajime no Ippo' (1400+ chapters, ongoing)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Uzumaki' (20 chapters)")
            elif duration == 'medium':
                print("Try 'Higanjima' (330 chapters across main series)")
            elif duration == 'long':
                print("Go for 'Berserk' (380+ chapters, ongoing)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Akame ga Kill!' (78 chapters)")
            elif duration == 'medium':
                print("Try 'Black Clover' (370+ chapters, ongoing)")
            elif duration == 'long':
                print("Check out 'Fairy Tail' (545 chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go for 'Orange' (22 chapters)")
            elif duration == 'medium':
                print("Try 'Wolf Girl and Black Prince' (57 chapters)")
            elif duration == 'long':
                print("Go read 'Domestic Girlfriend' (276 chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Barakamon' (167 chapters)")
            elif duration == 'medium':
                print("Try 'Silver Spoon' (131 chapters)")
            elif duration == 'long':
                print("Check out 'Sket Dance' (288 chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Yowamushi Pedal' (700+ chapters, ongoing)")
            elif duration == 'medium':
                print("Go for 'Baby Steps' (469 chapters)")
            elif duration == 'long':
                print("Check out 'Ace of Diamond' (400+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'I Am a Hero' (264 chapters, but reads quick)")
            elif duration == 'medium':
                print("Go for 'Ajin: Demi-Human' (86 chapters)")
            elif duration == 'long':
                print("Try 'Terra Formars' (220+ chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")

elif man == 'manhwa':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("Try 'Veritas' (82 chapters)")
            elif duration == 'medium':
                print("I suggest reading 'Shin Angyo Onshi' (83 chapters)")
            elif duration == 'long':
                print("Check out 'Noblesse' (544 chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'He Dedicated to Roses' (66 chapters)")
            elif duration == 'medium':
                print("Try 'Love in the Mask' (82 chapters)")
            elif duration == 'long':
                print("Go for 'Goong' (179 chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'UnTouchable' (140 chapters, light comedy vibe)")
            elif duration == 'medium':
                print("Try 'The Gamer' (430+ chapters, action-comedy mix)")
            elif duration == 'long':
                print("Check out 'Tower of God' (500+ chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Girls of the Wild's' (260 chapters)")
            elif duration == 'medium':
                print("Go for 'King of Hell' (300+ chapters)")
            elif duration == 'long':
                print("Check out 'The God of High School' (500+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Jack Frost' (100+ chapters, action-horror mix)")
            elif duration == 'medium':
                print("Try 'Distant Sky' (100+ chapters)")
            elif duration == 'long':
                print("Go for 'Island' (307 chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Solo Leveling' (179 chapters)")
            elif duration == 'medium':
                print("Try 'Red Storm' (380 chapters)")
            elif duration == 'long':
                print("Check out 'Peerless Dad' (300+ chapters, ongoing)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'Seasons of Blossom' (120+ chapters)")
            elif duration == 'medium':
                print("Try 'Light and Shadow' (103 chapters)")
            elif duration == 'long':
                print("Go for 'Something About Us' (115 chapters but dense romance)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'The Sound of Your Heart' (500+ mini comedy strips)")
            elif duration == 'medium':
                print("Try 'The Legendary Moonlight Sculptor' (300+ chapters, comedy-fantasy)")
            elif duration == 'long':
                print("Check out 'Yumi’s Cells' (512 chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'The Boxer' (133 chapters)")
            elif duration == 'medium':
                print("Check out 'Wind Breaker' (400+ chapters, cycling)")
            elif duration == 'long':
                print("Go for 'Lookism' (470+ chapters, ongoing with sports/fighting themes)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Shotgun Boy' (55 chapters)")
            elif duration == 'medium':
                print("Try 'Bastard' (93 chapters)")
            elif duration == 'long':
                print("Go for 'Sweet Home' (141 chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")
else:
    print("Please select a valid option for manga/manhwa.")
