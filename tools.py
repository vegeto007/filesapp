"""Tools module."""


def process_file(file_path, start=1, end=10000):
    """Process file.

    Get content of files between start and end line numbers.

    :param str file_path: Absolute file path
    :param int start: Start position of line
    :param int end: End position of line
    :return: Text file content
    :return type: str
    """
    text = ''
    try:
        with open(file_path, encoding="utf-8", errors='ignore') as f:
            for i, line in enumerate(f, 1):
                if start <= i <= end:
                    text += line
                elif i > end:
                    break
    except FileNotFoundError:
        raise FileNotFoundError(
            'File doesnt exist. Please ensure correct file is specified '
            'and file is present in path {}'.format(file_path))
    return text
