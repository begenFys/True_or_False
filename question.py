from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str
