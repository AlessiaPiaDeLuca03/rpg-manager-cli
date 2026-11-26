"""
Modello ruolo.
"""


class Role:

    def __init__(
        self,
        role_id: int,
        name: str
    ) -> None:

        self.role_id = role_id
        self.name = name