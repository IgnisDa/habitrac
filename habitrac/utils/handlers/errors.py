from typing import Dict


def check_if_errors_exist(error_dict):
    """This function checks that all the values of the
    `error_dict` dictionary evaluate to `None`. If they don't, it means that
    there exists errors and it returns `True`, otherwise `False`."""
    if error_dict is None:
        # there are no errors
        return False
    return any(value is not None for value in error_dict.values())


class ErrorContainer:
    """This is a special class that will help to manage errors in resolvers
    and keep the code clean and maintainable."""

    fields: Dict = {}

    def __init__(self, *args, **kwargs):
        for arg in args:
            self.fields[arg] = None

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.fields})>"

    def __bool__(self):
        return check_if_errors_exist(self.get_all_errors())

    def get_all_errors(self):
        if all(value is None for value in self.fields.values()):
            return None
        return self.fields

    def update_with_error(self, field_name, error_string):
        if field_name not in self.fields:
            raise AttributeError(
                f"`{field_name}` should be among `{list(self.fields.keys())}`"
            )
        if not self.fields[field_name]:
            self.fields[field_name] = [error_string]
        else:
            self.fields[field_name].append(error_string)
