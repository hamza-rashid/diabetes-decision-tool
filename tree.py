def decision(category, network, goals, push, positive, gamification, science):
    if int(category) == 1:
        if int(gamification) > 3:
            return "carbmanager"
        else:
            if int(positive) > 3:
                return "loseit"
            else:
                return "myfitnesspal"
    
    elif int(category) == 2:
        if int(gamification) > 3:
            return "zombiesrun"
        else:
            if int(network) > 3:
                if int(positive) > 3:
                    return "fitbit"
                else:
                    return "mapmyfitness"
            else: 
                return "8fit"
    
    elif int(category) == 3:
        if int(network) > 3:
            if int(positive) > 3:
                return "flo"
            else:
                return "eve"
        else:
            if int(positive) > 3:
                return "flo"
            else: 
                return "clue"

    elif int(category) == 4:
        if int(gamification) > 3:
            return "happify"
        else:
            if int(science) > 3:
                return "thinkup"
            else:
                if int(network) > 3:
                    return "sanvello"
                else:
                    return "calm"