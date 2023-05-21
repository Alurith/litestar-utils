import re
from typing import List, Tuple

from pydantic import BaseModel


class SlugifyOptions(BaseModel):
    """
    Slugify options

    collapse_whitespace: Collapse the whitespaces. Default `True`.
    disallowed_characters: A regex for the disallowed_characters.
    separator: The separator. Default `-`.
    replacements: A list of replacement.
    """

    collapse_whitespace: bool = True
    disallowed_characters: str = r"[^\w\s-]"
    separator: str = "-"
    replacements: List[Tuple[str, str]] = []


def slugify(text: str, options: SlugifyOptions = SlugifyOptions()):
    """
    Slugify a text.

    text: The initial text.
    options: A `SlugifyOptions` object containing all the settings.
    return: The slugify text
    """
    for replacement in options.replacements:
        text = text.replace(replacement[0], replacement[1])

    text = re.sub(options.disallowed_characters, " ", text.lower())

    pattern = re.compile(r"\W+") if options.collapse_whitespace else re.compile(r"\W")
    return re.sub(pattern, options.separator, text).lower().strip("-_")
