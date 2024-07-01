# intro_texts.py
from intro_druggie1 import intro_druggie1
intro_texts = [
    {"text": "they say weed is a gateway drug and I never knew why until that day weed became a gateway to the rest of my life.", "speaker": 0},
    {"text": "10am I wake up and... to be honest... I think I'm still a bit stoned from eating edibles like popcorn last night. Suffice it to say: I got the damn munchies.", "speaker": 0},
    {"text": "Also, suffice it to say I would never let myself get caught without eggs, bacon, sourdough, and some italian roast coffee in my kitchen. Just a few hours from now and I'll have this whole munchies problem solved.", "speaker": 0},
    {"text": "Now that I really have been thinking hard about my breakfast strategy I kinda deserve a treat. Like a nice cold indica dab off of my bubbler E rig.", "speaker": 0},
    {"text": "God please don't let me get so high that I forget about eating again.", "speaker": 0},
    {"text": "****BOOOM CRASH!!****", "speaker": 0},
    {"text": "Damn looks like that liquor truck just hit a parked car", "speaker": 0},
    {"text": "Yo! Jeri did you see that car crash? Come on let's go check it out!", "speaker": 0},
    {"text": "This is ain't a bad wreck. Easy fix too. We better get some beers outta this", "speaker": 1},
    {"text": "Good morning sir! The two of us saw the whole thing happen and we happen to be the best mechanics in Anchorage", "speaker": 0},
    {"text": "Phew, I sure could use some help. I've just felt slow and stupid and hungry all day... hahaha. Anyway, look gentlemen, I'm not in a rush hahahaha so either we can fix this truck together now or I'm happy to sell ya'll some beer under the table and I'll take the rest of the day off.", "speaker": 1},
    {"text": """(1) I'd be god damned if I left a fellow American to suffer due to the forces of entropy... not to mention how bad this could affect the economy... we're gonna help!! \n \n (2) All this talking has me thirsting. We'll take the beer, sir.""", "speaker": 2, "input": {1: {"victory": "charitable", "VP": 10, "next": "intro-charitable1"}, 2: {"victory": "druggie", "VP": 10, "next": intro_druggie1}}},
]

