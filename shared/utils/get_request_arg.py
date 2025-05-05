def get_int_request_arg(args, arg_name: str, default=10) -> int:
    """
    Get the value of a request argument from the provided dictionary.

    :param args: Dictionary containing request arguments.
    :param arg_name: Name of the argument to retrieve.
    :param default: Default value to return if the argument is not found.
    :return: Value of the argument or default value.
    """

    try:
        return int(args.get(arg_name, default))
    except ValueError:
        raise ValueError(f"Invalid value for argument '{arg_name}'")