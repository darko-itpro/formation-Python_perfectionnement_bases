from exos import exo_01

def test_add_1_knight():
    # Arrange
    exo_01.kingdom.clear()
    exo_01.count = 0

    # Act
    exo_01.add_knight("Arthur")

    #Assert
    assert exo_01.kingdom == ["Arthur"]
    assert exo_01.count == 1

def test_add_2_knights():
    exo_01.kingdom.clear()
    exo_01.count = 0
    #print(id(count), id(kingdom))
    exo_01.add_knight("Arthur")
    #print(id(count), id(kingdom))
    exo_01.add_knight("Lancelot")
    #print(id(count), id(kingdom))
    assert exo_01.count == 2
    assert exo_01.kingdom == ["Arthur", "Lancelot"]
