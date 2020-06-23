"""Unit tests for the parsers file"""

import filesystem.parsers as sut
import pathlib
from unittest.mock import patch

# region get_project_xml_data()


def test_get_project_xml_data_when_add_environment_variables_is_false_then_return_dict_with_env_variables(paths):
    """When add_environment_variables is false, then return dict with xml data"""

    # Arrange
    expected_result = {"PROJECT_FOO1": "foo1", "PROJECT_FOO2": "foo2", "PROJECT_FOO3": "foo3"}
    with patch.object(pathlib.Path, "joinpath") as joinpath_mock:
        joinpath_mock.return_value = paths.file_foo_xml_project_path
        # Act
        result = sut.get_project_xml_data(False)
        # Assert
        assert expected_result == result


def test_get_project_xml_data_when_add_environment_variables_is_true_then_call_create_env_variables(paths):
    """When add_environment_variables is false, then return dict with xml data"""

    # Arrange
    expected_result = {"PROJECT_FOO1": "foo1", "PROJECT_FOO2": "foo2", "PROJECT_FOO3": "foo3"}
    with patch.object(pathlib.Path, "joinpath") as joinpath_mock:
        joinpath_mock.return_value = paths.file_foo_xml_project_path
        with patch.object(sut, "platform_specific") as platform_specific_mock:
            with patch.object(platform_specific_mock, "create_environment_variables") as create_env_vars_mock:
                # Act
                sut.get_project_xml_data(True)
                # Assert
                create_env_vars_mock.assert_called_once_with(expected_result)


# endregion
