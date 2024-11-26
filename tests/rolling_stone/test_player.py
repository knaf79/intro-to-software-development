from rolling_stone.player import Player
import pytest

@pytest.fixture
def new_player():
    return Player()

def test_player(new_player):
    assert isinstance(new_player, Player)

def test_player_receive_scoe(new_player):
    RECEIVED_SCORE = 10
    assert new_player.score == 0
    new_player.receive_score(RECEIVED_SCORE)
    assert new_player.score == RECEIVED_SCORE


def test_input_name_for_player(mocker, new_player):
    TEST_NAME = "Ola Nordmann"
    mocker.patch.object(
        Player, "_get_name_for_player_from_input",
        return_value=TEST_NAME
    )
    assert new_player.name is None

    new_player.prompt_for_name()

    assert new_player.name is TEST_NAME
