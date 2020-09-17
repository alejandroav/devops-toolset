"""Utilities and tools for the devops toolset repository"""

import tools.constants as constants
import requests
from zipfile import ZipFile
from tools.xmlparser import XMLParser
import os.path
import pathlib
import shutil


def get_devops_toolset(destination_path: str):
    """ Downloads and extracts devops-toolset from its public resource

    It performs a download into the desired folder, also this method will extract and clean the result by renaming the
    final folder and deleting the original downloaded .zip source.

    Args:
        destination_path: The destination path of the download / extraction

    """
    response = requests.get(constants.devops_toolset_download_resource, allow_redirects=True)
    devops_toolset_path_file = os.path.join(destination_path, constants.devops_toolset_save_as)
    with open(devops_toolset_path_file, 'ab') as devops_toolset:
        devops_toolset.write(response.content)
    with ZipFile(devops_toolset_path_file, 'r') as zip_object:
        zip_object.extractall(destination_path)
    zip_extension = pathlib.Path(constants.devops_toolset_save_as).suffixes[0]
    destination_file_without_zip_extension = constants.devops_toolset_save_as.replace(zip_extension, '')
    old_destination_folder = os.path.join(destination_path, destination_file_without_zip_extension)
    final_destination_folder = os.path.join(destination_path, constants.devops_toolset_folder)
    os.rename(old_destination_folder, final_destination_folder)
    os.remove(devops_toolset_path_file)


def update_devops_toolset(toolset_path: str):
    """ Compares and updates devops-toolset if needed

    Args:
        toolset_path: The path that will be checked
    """
    is_latest_version = compare_devops_toolset_version(toolset_path)
    if not is_latest_version:
        if os.path.exists(toolset_path):
            # Remove current version
            shutil.rmtree(toolset_path)
        get_devops_toolset(pathlib.Path(toolset_path).parent)


def compare_devops_toolset_version(toolset_path: str) -> bool:
    """ Returns true if version is the latest (no update required), false otherwise

    Args
        toolset_path: The path that will be checked
    """
    project_xml_path = os.path.join(toolset_path, constants.project_xml_name)
    if not os.path.exists(project_xml_path):
        return False
    xml_parser = XMLParser()
    # Get current version of devops-toolset
    xml_parser.parse_from_path(project_xml_path)
    current_version = xml_parser.get_attribute_value("version")
    # Get latest version from GitHub
    response = requests.get(constants.project_xml_download_resource, allow_redirects=True)
    xml_parser.parse_from_content(response.content.decode("utf-8"))
    latest_version = xml_parser.get_attribute_value("version")
    return current_version == latest_version


if __name__ == "__main__":
    help(__name__)
