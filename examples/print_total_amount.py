#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
from decimal import Decimal

from qifparse.parser import QifParser


def main():
    filename = environ.get('QIFPATH')
    if not filename:
        print("No filename set in environment variable QIFPATH")
        return

    with open(filename, 'rU') as f:
        qif = QifParser.parse(f)

    transactions = qif.get_transactions()[0]
    raw_amounts = map(lambda x: x.amount, transactions)
    amounts = filter(lambda x: x, raw_amounts)  # cleanup None amounts
    total = reduce(lambda x, y: x + y, amounts, Decimal(0))

    print("Total: ${0}".format(total))

if __name__ == '__main__':
    main()
