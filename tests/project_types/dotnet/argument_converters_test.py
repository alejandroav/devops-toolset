""" Unit-core for the dotnet/argument_converters.py module"""

import pytest

import project_types.dotnet.argument_converters as sut

# region convert_debug_parameter()


@pytest.mark.parametrize("value,expected", [(False, ""), (True, "--verbosity=diagnostic")])
def test_convert_debug_parameter_returns_conversion_argument(value, expected):
    """ Given value argument, should test the two possibilities and return desired value """
    # Arrange
    # Act
    result = sut.convert_debug_parameter(value)
    # Assert
    assert result == expected

# endregion convert_debug_parameter()

# region convert_force_parameter()


@pytest.mark.parametrize("value,expected", [(False, ""), (True, "--force")])
def test_convert_force_parameter_returns_conversion_argument(value, expected):
    """ Given value argument, should test the two possibilities and return desired value """
    # Arrange
    # Act
    result = sut.convert_force_parameter(value)
    # Assert
    assert result == expected

# endregion convert_force_parameter()

# region convert_with_restore_parameter()


@pytest.mark.parametrize("value,expected", [(False, "--no-restore"), (True, "")])
def test_convert_with_restore_parameter_returns_conversion_argument(value, expected):
    """ Given value argument, should test the two possibilities and return desired value """
    # Arrange
    # Act
    result = sut.convert_with_restore_parameter(value)
    # Assert
    assert result == expected

# endregion convert_with_restore_parameter()

# region convert_self_contained_parameter()


@pytest.mark.parametrize("value,expected", [(False, "--self-contained false"), (True, "--self-contained true")])
def test_convert_self_contained_parameter_returns_conversion_argument(value, expected):
    """ Given value argument, should test the two possibilities and return desired value """
    # Arrange
    # Act
    result = sut.convert_self_contained_parameter(value)
    # Assert
    assert result == expected

# endregion convert_self_contained_parameter()
