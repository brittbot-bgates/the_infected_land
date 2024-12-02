#!/usr/bin/python3
from improve_loadout import improve_loadout
from non_beast_battle import non_beast_battle
from regain_health import regain_health
from sleep_print import sleep_print


def after_beast_battle_story() -> None:
    """
    This function displays the game's storyline after the hero defeats the beast.
    :return: None
    """
    from hero import hero  # Placing the import statement here to avoid a circular import error
    print()
    sleep_print()
    print("After the battle the other beasts start to disintegrate.".center(55))
    print()
    sleep_print()
    print("The wind picks up and blows away the remnants.".center(55))
    print()
    sleep_print()
    print("Eventually the land is free of the beasts.".center(55))
    print()
    sleep_print()
    print("The hero walks around looking around at the changes.".center(55))
    print()
    sleep_print()
    print("Green grass appears and spreads out.".center(55))
    print()
    sleep_print()
    print("All types of flowers bloom within the lush blades.".center(55))
    print()
    sleep_print()
    print("Trees shoot up from the ground and extend their branches.".center(55))
    regain_health()
    improve_loadout()
    print()
    print("An evil scream reverberates through the land.".center(55))
    print()
    sleep_print()
    print("The hero and the residents look around in confusion.".center(55))
    print()
    sleep_print()
    print("Then the malevolent voice returns:".center(55))
    print()
    sleep_print()
    print("\"You defeated my beast?\"".center(55))
    print()
    sleep_print()
    print("\"I underestimated you.\"".center(55))
    print()
    sleep_print()
    print("\"Well, one of my non-beasts will destroy you.\"".center(55))
    print()
    sleep_print()
    print("The malevolent voice ceases.".center(55))
    print()
    sleep_print()
    print(f"{hero.name} nods to the residents and departs for the infected land.".center(55))
    print()
    sleep_print()
    print("The hero readies their sword and shield ready to fight!".center(55))
    print()
    sleep_print()
    print(f"All types of evil non-beasts plod toward the hero.".center(55))
    print()
    sleep_print()
    print("Towering skeletons beat the earth with a bone.".center(55))
    print()
    sleep_print()
    print("Decaying ghouls moan as pus oozes from their bodies.".center(55))
    print()
    sleep_print()
    print("A mummy walks around with their arms extended.".center(55))
    print()
    sleep_print()
    print("A lich practices their evil magic.".center(55))
    print()
    sleep_print()
    print("Banshees howl as they soar around.".center(55))
    non_beast_battle()
