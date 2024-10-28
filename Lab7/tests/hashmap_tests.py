import pytest
from Lab7.myHashMap import MyHashMap

def test_put():                     #Test if put method correctly adds a new key and value pair

    map = MyHashMap()
    result = map.put(1, "rat")

    assert result == True


def test_replace():                 #Test if replace method correctly updates the value of specified key

    map = MyHashMap()
    map.set(1, "rat")
    result = map.replace(1, "mouse")

    assert result == True
    assert map.get(1) == "mouse"


def test_remove():                  #Test if remove method correctly deletes a key and value pair

    map = MyHashMap()
    map.put(1, "rat")
    result = map.remove(1)
    
    assert result == True
    assert map.get(1) == None