from main import *

def test_starting_dashes():
    assert starting_dashes("moon") == ["_","_","_","_"]
    assert starting_dashes("horse") == ["_","_","_","_","_"]

def test_replace_dashes():
    assert replace_dashes(["_","_","_","_"], "moon", "o") == ["_","o","o","_"]
    assert replace_dashes(["_","_","_","_","_"], "horse", "o") == ["_","o","_","_","_"]
    assert replace_dashes(["_","_","_"], "cat", "o") == ["_","_","_"]

def test_check_guess():
    word_list, used_list, incorrect = check_guess(["_","_","_","_"], "moon", "o",["e","a"],2)
    assert word_list == ["_","o","o","_"]
    assert used_list == ["e","a","o"]
    assert incorrect == 2

    word_list, used_list, incorrect = check_guess(["_","_","_","_"], "moon", "i",["e","a"],2)
    assert word_list == ["_","_","_","_"]
    assert used_list == ["e","a","i"]
    assert incorrect == 3

    word_list, used_list, incorrect = check_guess(["_","_","_","_"], "moon", "i",["e","a"],2)
    assert word_list == ["_","_","_","_"]
    assert used_list == ["e","a"]
    assert incorrect == 2
    
    