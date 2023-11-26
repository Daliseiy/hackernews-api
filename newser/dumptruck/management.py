from django.core.management import call_command
from django.conf import settings

def dump_database(output_file, format='json'):
    """
    Dump the current database to a file.

    Args:
        output_file (str): The path to the output file where the dump will be saved.
        format (str, optional): The format of the dump ('json' by default).

    Returns:
        bool: True if the dump was successful, False otherwise.
    """
    try:
        # Use the call_command to dump the database (no need to change the database)
        data = call_command('dumpdata', format=format)
        print(f"the task ran with result ${data}")
        return True
    except Exception as e:
        print(f"Error dumping database: {e}")
        return False


