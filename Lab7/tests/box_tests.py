import pytest

from ..box import Box

def test_add_success():                         #Test the add method to see if it correctly adds a Pokemon entry

    box = Box()
    result = box.add("Kazza", "abra")

    assert result == True
    assert box.nicknameMap.containsKey("Kazza") == True


def test_find_existing_entry():                 #Test the find method to search for specified entry 

    box = Box()
    box.add("Kazza", "abra")
    entry = box.find("Kazza", "abra")

    assert entry != None
    assert entry.getSpecies() == "abra"



def test_find_entry_by_nickname():              #Test the find by nickname for specified entry

    box = Box()
    box.add("Kazza", "abra")
    entry = box.findEntryByNickname("Kazza")
    
    assert entry != None
    assert entry.getSpecies() == "abra"

