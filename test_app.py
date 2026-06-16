import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app


def test_header_is_present():
    """Test that the header H1 element is present in the layout."""
    layout_str = str(app.layout)
    assert "Pink Morsel Sales Visualiser" in layout_str, (
        "Header with 'Pink Morsel Sales Visualiser' not found in layout"
    )


def test_visualisation_is_present():
    """Test that the sales chart graph component is present in the layout."""
    layout_str = str(app.layout)
    assert "sales-chart" in layout_str, (
        "Graph component with id 'sales-chart' not found in layout"
    )


def test_region_picker_is_present():
    """Test that the region radio button filter is present with all five options."""
    layout_str = str(app.layout)
    assert "region-filter" in layout_str, (
        "RadioItems component with id 'region-filter' not found in layout"
    )
    for region in ["all", "north", "east", "south", "west"]:
        assert region in layout_str, (
            f"Region option '{region}' not found in the radio button options"
        )
