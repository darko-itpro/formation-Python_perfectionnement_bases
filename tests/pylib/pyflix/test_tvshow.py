import pytest
from pylib.pyflix.mediatheque import TvShow, DuplicateEpisode

def test_create_show():
    show = TvShow("onE piece")
    assert show.name == "One Piece"

def test_show_has_episodes_attr():
    show = TvShow("onE piece")
    
    assert show.episodes == []
    
def test_add_one_episode():
    show = TvShow("onE piece")
        
    show.add_episode('Grand Line', 2, 1)
    
    assert len(show.episodes) == 1
    assert show.episodes[0].title == "Grand Line"
 
 
def test_duplicate_episode_must_raise():
    show = TvShow("onE piece")
        
    show.add_episode('Grand Line', 2, 1)

    with pytest.raises(DuplicateEpisode):
        show.add_episode('Grand Line', 2, 1)
