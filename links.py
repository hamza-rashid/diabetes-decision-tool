def getlink(app, platform):
    """
    This function takes an input of the app name and returns the app url based on the 
    platform (iOS or Android).
    """
    
    
    if app == "myfitnesspal":
        if platform == "ios":
            return "https://apps.apple.com/us/app/calorie-counter-diet-tracker/id341232718"
        else:
            return "https://play.google.com/store/apps/details?id=com.myfitnesspal.android"
    elif app == "carbmanager":
        if platform == "ios":
            return "https://apps.apple.com/us/app/carb-manager-keto-diet-app/id410089731"
        else:
            return "https://play.google.com/store/apps/details?id=com.wombatapps.carbmanager"
    elif app == "loseit":
        if platform == "ios":
            return "https://apps.apple.com/us/app/lose-it-calorie-counter/id297368629"
        else:
            return "https://play.google.com/store/apps/details?id=com.fitnow.loseit"
    elif app == "flo":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/flo-ovulation-period-tracker/id1038369065"
        else:
            return "https://play.google.com/store/apps/details?id=org.iggymedia.periodtracker&gl=GB"
    elif app == "eve":
        if platform == "ios":
            return "https://apps.apple.com/us/app/period-tracker-eve/id1002275138"
        else:
            return "https://play.google.com/store/apps/details?id=com.glow.android.eve&gl=GB"
    elif app == "clue":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/clue-period-tracker/id657189652"
        else:
            return "https://play.google.com/store/apps/details?id=com.clue.android&gl=GB"
    elif app == "zombiesrun":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/zombies-run/id503519713"
        else:
            return "https://play.google.com/store/apps/details?id=com.sixtostart.zombiesrunclient"
    elif app == "fitbit":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/fitbit-coach/id535640259"
        else:
            return "https://play.google.com/store/apps/details?id=com.fitstar.pt"
    elif app == "mapmyfitness":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/map-my-fitness-by-under-armour/id298903147"
        else:
            return "https://play.google.com/store/apps/details?id=com.mapmyfitness.android2"
    elif app == "8fit":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/8fit-workout-meal-planner/id866617777"
        else:
            return "https://play.google.com/store/apps/details?id=com.eightfit.app"
    elif app == "happify":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/happify-for-stress-worry/id730601963"
        else:
            return "https://play.google.com/store/apps/details?id=com.happify.happifyinc"
    elif app == "thinkup":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/thinkup-positive-affirmations/id906660772"
        else:
            return "https://play.google.com/store/apps/details?id=com.think.up"
    elif app == "sanvello":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/sanvello-anxiety-depression/id922968861"
        else:
            return "https://play.google.com/store/apps/details?id=com.pacificalabs.pacifica"
    elif app == "calm":
        if platform == "ios":
            return "https://apps.apple.com/gb/app/calm/id571800810"
        else:
            return "https://play.google.com/store/apps/details?id=com.calm.android"
