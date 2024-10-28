import pytest

from ..box import Box

def test_add_success():
    box = Box()
    result = box.add("Kazza", "abra")
    assert result == True
    assert box.nicknameMap.containsKey("Kazza") == True


def test_find_existing_entry():
    box = Box()
    box.add("Kazza", "abra")
    entry = box.find("Kazza", "abra")
    assert entry is not None
    assert entry.getSpecies() == "abra"



def test_find_entry_by_nickname():
    box = Box()
    box.add("Kazza", "abra")
    entry = box.findEntryByNickname("Kazza")
    assert entry is not None
    assert entry.getSpecies() == "abra"

