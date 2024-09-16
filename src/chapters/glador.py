# This is the begging of the game, the first chapter

from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *
from src.utils.typing_effect import *

# First chapter.
def glador(player_stats, save_player_stats, main_gameplay, battle, current_enemy=0):
    # Function to start the glador encounter.
    clear_terminal()
    draw_line()
    print('')
    typingPrint(chapter_1_story.title)
    typingPrint(chapter_1_story.description)
    draw_line()
    typingInput('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_1_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('save_game_file/save_game/save.txt', player_stats)
# end of chapter one.