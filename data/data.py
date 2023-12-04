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


@dataclass
class ResultingTableFields:
    field_1: str = None,
    field_2: str = None,
    field_3: str = None,
    field_4: str = None,
    field_5: str = None,
    field_6: str = None,
