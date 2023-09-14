from dataclasses import dataclass


@dataclass
class FontStyle:
    font_size: int = None
    font_bold: bool = None
    font_color: str = None

@dataclass
class BorderStyle:
    cell_width: int = None
    cell_height: int = None
    cell_border_style: str = None
    cell_border_color: str = None
    cell_alignment_horizontal: str = None
    cell_alignment_vertical: str = None
