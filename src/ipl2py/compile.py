import logging

from .parse import parse
from .symbols import create_symbol_table
from .tree import Tree

logger = logging.getLogger(__name__)


def compile(content: str, include_comments=True) -> Tree:
    tree = parse(content, include_comments=include_comments)
    symbol_table = create_symbol_table(tree)
    logger.debug("symbol_table=%s", symbol_table)
    return tree
