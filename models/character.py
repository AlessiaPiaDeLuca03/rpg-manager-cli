"""
Modello personaggio RPG.
"""


class Character:

    def __init__(
        self,
        name: str,
        character_class: str,
        level: int,
        user_id: int
    ) -> None:

        self.name = name
        self.character_class = character_class
        self.level = level
        self.user_id = user_id