""" Contains dotnet's cli argument converters """

def convert_debug_parameter(value: bool) -> str:
    """ Converts force boolean into the correspondent parameter
    Arguments:
        value: The value to be converted

    Returns: --force when true, empty value otherwise
    """
    if value:
        return "--verbosity=diagnostic"
    return ""


def convert_force_parameter(value: bool) -> str:
    """ Converts force boolean into the correspondent parameter
    Arguments:
        value: The value to be converted

    Returns: --force when true, empty value otherwise
    """
    if value:
        return "--force"
    return ""


def convert_self_contained_parameter(value: bool) -> str:
    """ Converts force boolean into the correspondent parameter
    Arguments:
        value: The value to be converted

    Returns: --self-contained [false|true]
    """
    return f"--self-contained {str(value).lower()}"


def convert_with_restore_parameter(value: bool) -> str:
    """ Converts with_restore boolean into the correspondent parameter
    Arguments:
        value: The value to be converted

    Returns: --no-restore when false, empty value otherwise
    """
    if not value:
        return "--no-restore"
    return ""


def convert_argument_set(**kwargs) -> str:
    """ Convert all kwargs passed to the dotnet cli expected format """
    str_arguments : str = ""
    for key, value in kwargs.items():
        if isinstance(value, bool):
            if value:
                arg = f"--{key}"
            else:
                arg = ""
        else:
            arg = f"--{key} '{value}'"

        str_arguments = ''.join([str_arguments, arg]) if str_arguments == "" else ' '.join([str_arguments, arg])

    return str_arguments




if __name__ == "__main__":
    help(__name__)
