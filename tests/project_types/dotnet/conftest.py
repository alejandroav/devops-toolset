"""Test configuration file for linux module.

Add here whatever you want to pass as a fixture in your core."""
import pytest


class DotnetCliData:
    """Class used to create the PathsData fixture"""
    file_path = "path/to/file"
    debug_argument = "--verbosity=diagnostic"
    force_argument = "--force"
    output_argument = "test/output"
    runtime_argument = "test-runtime"
    with_restore_argument = "--no-restore"
    framework_argument = "test-framework"
    configuration_argument = "Test"
    self_contained_argument = "--self-contained false"
    args = {"force": True, "output": output_argument}
    converted_args = f"--force --output '{output_argument}'"


@pytest.fixture
def dotnetclidata():
    """ Sample paths configuration data for testing"""
    yield DotnetCliData()
    # Below code is executed as a TearDown
    print("Teardown finished. ")