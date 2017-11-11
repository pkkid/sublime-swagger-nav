"""
This module provides functions for extracting YAML symbols.
"""
import copy, sublime
from . import utils


def _copy_refs(symbols, references, _symbols=None, level=0, maxlevels=3):
    if _symbols is None:
        _symbols = copy.deepcopy(symbols)
    for name, ref in references.items():
        prefix = name.replace('.$ref', '')
        for symbol in _symbols:
            if symbol['name'].startswith(ref):
                suffix = symbol['name'][len(ref):]
                if suffix:
                    subname = '{}{}'.format(prefix, suffix)
                    symbols.append({'name': subname, 'region': symbol['region']})


def get_yaml_symbols(view):
    """ Returns YAML key paths and associated regions for given sublime view.
        Paths calculated by key indentation level -- it's more efficient and
        secure, but doesn't support inline hashes.
    """
    symbols, path, references = [], [], {}
    content = get_view_content(view)
    regions = get_view_regions(view, 'entity.name.tag.yaml')
    for region in regions:
        # Get the indentation and current path
        # pop items from path while its indent is less than current indent
        key = content[region.begin():region.end()]
        indent = region.begin() - content.rfind('\n', 0, region.begin()) - 1
        while len(path) > 0 and path[-1]['indent'] >= indent:
            path.pop()
        path.append({'key': key, 'indent': indent})
        # Check this is an interesting symbol to keep
        section = path[0]['key']
        keepit = ((len(path) <= 2) or (section != 'paths' and path[-2]['key'] == 'properties'))
        # Generate a healthy name
        if keepit:
            fullpath = '.'.join(map(lambda item: item['key'], path[1:]))
            fullpath = fullpath.replace('.properties.', '.')
            fullpath = fullpath.replace('.responses.', '.')
            name = '{}: {}'.format(section, fullpath)
            symbols.append({'name': name, 'region': region})
        if path[-1]['key'] == '$ref' and section != 'paths':
            value = content[region.begin():content.find('\n', region.end(), region.end() + 80)]
            value = value.replace('$ref: ', '').strip('#/\'" ').replace('/', '.')
            references[name] = value
    _copy_refs(symbols, references)
    return symbols


def get_selected_yaml_symbol(symbols, view):
    """ Returns YAML symbol from given list for currently selected region in
        given sublime view.
    """
    if not symbols:
        return None
    selection = get_view_selected_lines(view)
    # 1 cursor
    if len(selection) == 1:
        # Reversing list because we are searching for the deepest key
        yaml_symbols = reversed(symbols)
        # Search for 1 intersection
        for selected_region in selection:
            for symbol in yaml_symbols:
                if selected_region.intersects(symbol["region"]):
                    return symbol
    else:
        # Ambigous symbol: multiple cursors
        return None


def get_view_regions(view, selector):
    """ Returns regions for given selector in given view. """
    return utils.execute_in_sublime_main_thread(lambda: view.find_by_selector(selector))


def get_view_content(view):
    """ Returns view content as string. """
    return utils.execute_in_sublime_main_thread(lambda: view.substr(sublime.Region(0, view.size())))


def get_view_selected_lines(view):
    """ Returns selected lines as regions in given view. """
    return utils.execute_in_sublime_main_thread(lambda: [line for sel in view.sel() for line in view.lines(sel)])
