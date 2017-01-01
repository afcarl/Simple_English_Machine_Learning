#!/usr/bin/env python
"""
coding=utf-8

A playground to test out implementations with a real data set

"""
import logging
import os
import sys

import pandas

from lib.Trees import BinaryClassificaitonTree

logging.basicConfig(level=logging.DEBUG)
sys.path.insert(0, os.getcwd())


def load_sapphire_df():
    # TODO docstring
    # Read in data
    sapphire_df = pandas.read_csv('data/input/sapphire_reserve.csv')

    # Remove null columns
    sapphire_df = sapphire_df[sapphire_df['credit_score'].notnull()]
    sapphire_df = sapphire_df[sapphire_df['initial_status'].notnull()]

    # Feature engineering
    sapphire_df['application_in_branch'] = sapphire_df['application_method'] == 'In-branch'
    sapphire_df['gender_male'] = sapphire_df['gender'] == 'Male'
    sapphire_df['instant_approval'] = sapphire_df['initial_status'] == 'Instant approval'

    logging.info('Created sapphire data set, with columns: {}'.format(sapphire_df.columns))

    return sapphire_df


def gen_X_list():
    return ['cards_in_24_months', 'num_chase_cards', 'stated_income', 'application_in_branch', 'age',
            'chase_relationship_age', 'relationship_status']


def main():
    """
    Main function documentation template
    :return: None
    :rtype: None
    """
    # TODO docstring
    sapphire_df = load_sapphire_df()
    print sapphire_df.columns

    X = sapphire_df[gen_X_list()]
    y = sapphire_df[['instant_approval']]

    clf = BinaryClassificaitonTree()
    clf.fit(X, y)


# Main section
if __name__ == '__main__':
    main()
