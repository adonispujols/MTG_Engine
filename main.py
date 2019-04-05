import event_handler
import game
import player

if __name__ == "__main__":
    deck_1 = []
    deck_2 = []
    for i in range(20):
        deck_1.append("1: " + str(i))
        deck_2.append("2: " + str(i))

    core_event_handler = event_handler.EventHandler()
    main_game = game.Game([player.Player(deck_1), player.Player(deck_2)], core_event_handler)
    main_game.start_game()
