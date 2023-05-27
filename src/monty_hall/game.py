import dataclasses as dc

@dc.dataclass
class Door:
    content: str
    open: bool = False


def play_round():
    pass