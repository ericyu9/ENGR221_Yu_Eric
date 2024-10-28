import pytest
from Lab7.myHashMap import MyHashMap
def test_put():
    map = MyHashMap()
    result = map.put(1, "rat")
    assert result == True

def test_replace():
    map = MyHashMap()
    map.set(1, "rat")
    result = map.replace(1, "mouse")
    assert result == True
    assert map.get(1) == "mouse"

def test_remove():
    map = MyHashMap()
    map.put(1, "rat")
    result = map.remove(1)
    assert result == True
    assert map.get(1) == None