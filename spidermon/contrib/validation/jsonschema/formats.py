from jsonschema._format import FormatChecker, _draft_checkers
from jsonschema.compat import str_types

from spidermon.contrib.validation.utils import is_valid_url


def is_url(instance):
    if not isinstance(instance, str_types):
        return True
    return is_valid_url(instance)


_spidermon_checkers = {
    'url': (is_url, ()),
}

for format_name, (func, raises) in _spidermon_checkers.items():
    FormatChecker.cls_checks(format_name, raises)(func)

format_checker = FormatChecker(_draft_checkers["draft4"] + _spidermon_checkers.keys())