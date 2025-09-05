import hangman_game as game 

def test_mask_text_masks_letters_only():
    assert game.mask_text("Hello World!") == "_ _ _ _ _  _ _ _ _ _ !"
