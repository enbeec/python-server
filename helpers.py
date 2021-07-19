import inspect


def method_args(func):
    """Takes in a function and gives you back it's args (without self)

                Args:
                    func (callable): the function

                Returns:
                    list: the args for the function
        """
    args = str(inspect.signature(func))
    # get rid of parentheses
    args = args.strip('(').strip(')')
    # get rid of self and spaces
    args = args.replace('self, ', '').replace(' ', '')
    # convert to a list
    return list(map(strip_defaults, args.split(',')))


def strip_defaults(arg):
    """Removes unwanted characters resulting from arg defaults in a signature

        Args:
                arg (string): the original arg which might end in "=x" where x is some number

        Returns:
                string: the cleaned arg
        """

    # look for the index of an equals sign in our arg
    equals_position = arg.find("=")
    if equals_position == -1:
        return arg
    else:
        # return everything up to the equals
        return arg[:equals_position]
