# Game.py

import rankade.RankadeObject


class Game(rankade.RankadeObject.RankadeObject):

    """Represents a single Game object returned by Rankade

    Attributes
    ----------
    id : str
        Rankade id of the game.
    name : str
        Games name.
    weight : str
        Should be ultralight, light, midlight, normal, heavy, massive.
        A heavier game will result in a larger variation of the ree score.
    weightLabel : str
        Appears to be a nicely formatted version of the weight attribute.
    mediumImage : str
        URL for game art.
    thumbnail : str
        URL for game art thumbnail.
    bggIdGame : Optional[int]
        Board Game Geek id for the game.
    """

    def _set_attributes(self, attributes):
        self.id = attributes.get("id")
        self.name = attributes.get("name")
        self.weight = attributes.get("weight")
        self.weightLabel = attributes.get("weightLabel")
        self.mediumImage = attributes.get("mediumImage")
        self.thumbnail = attributes.get("thumbnail")
        self.bggIdGame = attributes.get("bggIdGame")
