from plottah.config import Settings

import pytest


@pytest.fixture
def return_settings():
    return {
        "file_path": "/Users/otaniels/Library/CloudStorage/OneDrive-TheBostonConsultingGroup,Inc/Documents/NielsOta/Code/univariate_plotter/data/test_sample.csv",
        "output_path": "/Users/otaniels/Library/CloudStorage/OneDrive-TheBostonConsultingGroup,Inc/Documents/NielsOta/Code/univariate_plotter/data/images",
        "features": [
            {"name": "A_TENURE_MONTHS_N"},
            {"name": "T_PPG_AVG_6M_N"},
            {"name": "D_MAX_DAYS_PAST_DUE_6M_N", "bins": [0, 1, 5, 10, 100]},
            {"name": "LN_LEXISNEXIS_SBFE_SCORE_CURRENT_N"},
            {"name": "T_TOTAL_TRX_NON_FUEL_PROPORTION_1M_N"},
        ],
        "target": "FLAG_60_DPD_366_DAYS",
        "primary_color": "231, 30, 87",
        "secondary_color": "153, 204, 235",
        "tertiary_color": "254, 189, 64",
        "grey_tint_color": "110, 111, 115",
    }


def test_correct_settings(return_settings):
    # get correct settings
    settings = return_settings.copy()
    Settings(**settings)


def test_wrong_path(return_settings):
    # get correct settings
    settings = return_settings.copy()

    # add wrong path
    settings["file_path"] = "foobar.csv"

    with pytest.raises(ValueError):
        Settings(**settings)


def test_wrong_feature(return_settings):
    # get correct settings
    settings = return_settings.copy()

    # add wrong feature
    settings["features"].append({"name": "foobar"})

    with pytest.raises(ValueError):
        Settings(**settings)


def test_wrong_target(return_settings):
    # get correct settings
    settings = return_settings.copy()

    # add wrong target
    settings["target"] = "foobar"

    with pytest.raises(ValueError):
        Settings(**settings)


def test_wrong_color(return_settings):
    # get correct settings
    settings = return_settings.copy()

    # add wrong color
    settings["primary_color"] = "foobar"

    with pytest.raises(ValueError):
        Settings(**settings)