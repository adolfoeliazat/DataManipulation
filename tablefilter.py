# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: tablefilter.py
(#)Version: 1.0

Message me if you want me to add any functionality to the program or if you want to hire me for a job. 

WARNING: The program does not currently work from the commandline. However, the main aspects of the program work. I already
used them to filter out duplicate names from an excel document. Also, the --compare functionality has not been added yet.

Program Purpose: Program allows users to remove duplicate values from a column in a csv file (or from an Excel document 
that was converted to a csv). The actual purpose of the program was to remove duplicate rows from an excel table so that 
I could use the sample data in a database for a school project.

Inputs:
__file : Accepts String filename. Currently accepts only csv files.
__duplicate_column : Accepts a String. User determines the name of the column to remove duplicate rows based on 
    - I used 'Customer Name' in my program to remove duplicate customers.
__file_dest : Determines where the newly created csv file should save to. 
    - I need to rewrite the program so that it saves to the default working directory when I add commandline arguments.
__compare : Allows the user to determine an operator (>, <, !=, =) that they want to use to filter a value. 
__comp_value : Accepts a String, Float, or Integer that the user wants to filter a column compared to.

This program will be periodically updated to include much more functionality.
"""

import pandas as pd
import argparse
import os
import sys

class TableFilter(object):

    def __init__(self, file18 = '', duplicate = '', file_destination = '', comparison_op = '', comparison_value = '' ):
        self.__file = file18
        self.__duplicate_column = duplicate
        self.__file_dest = file_destination
        # Adding extra functionality to program
        self.__compare = comparison_op
        self.__comp_value = comparison_value

    """ Description: Method filters out the unique values in the column of a csv file.
        Return: DataFrame excluding the duplicate values """

    def populate_df(self):
        try:
            csv_file = self.__file
            df = pd.DataFrame()
            pop_df = df.from_csv(csv_file)
        except IOError as e:
            print( "I/O error: The file did not import properly." )
        return pop_df

        """        
        Create a column of boolean values 
        Check to see if the previous value in the column is equal
        """

    def filter_uniq(self):
        dup = self.__duplicate_column
        pop_df = self.populate_df
        pop_df['Unique'] = (pop_df[dup] == pop_df[dup].shift())
        filtered_df = pop_df[pop_df['Unique'] == False]
        return filtered_df

    """ Export to filtered DataFrame to CSV file. """

    def export_to_CSV(self):
        fileDestination = self.__file_dest
        df = self.filter_uniq()
        df.to_csv( fileDestination )

    """ Allows users to filter a column based on a given value and an operator """
    def filter_by(self):
        comparison_op = self.__compare.upper()
        comparison_value = self.__comp_value

        if isinstance(comparison_value, int) or isinstance(comparison_value, float):
            if comparison_op == 'EQ' or comparison_op == 'NEQ' or comparison_op == 'LTE' or comparison_op == 'GTE' or comparison_op == 'LT' or comparison_op == 'GT':
                if comparison_op == 'EQ':
                    # do this
                elif comparison_op == 'NEQ':
                    # do this
                elif comparison_op == 'LTE':
                    # do this
                elif comparison_op == 'GTE':
                    # do this
                elif comparison_op == 'LT':
                    # do this
                elif comparison_op == 'GT':
                    # do this
                else:
                    raise IOError("An exception was raised because you have deep psychological issues that affected your ability to use commandline tools.\n"
                                  "\n\tOnly 'EQ', 'NEQ', 'LTE', 'GTE', 'LT', or 'GT' can be used as operators.")
                    
        if isinstance(comparison_value, str):
            if comparison_op == 'EQ':
                # do this
            elif comparison_op == 'NEQ':
                # do this
            else:
                raise IOError(
                    'An error occurred because you have deep psychological issues that affected your ability to use commandline tools.\n'
                    '\n\tONLY "EQ" and "NEQ" operations can performed on values that include letters.')
        
        # NEED TO ADD DATETIME functionality!!!!!!!!        

    """ Process command-line arguments. """
    if __name__ == '__main__':

        """ Create commandline functionality to the program """
        parser = argparse.ArgumentParser( add_help = True, description = "Allows users to filter CSV file in a variety of ways." )

        # NEED TO ADD PARSER GROUP CALLED 'Positional Arguments'
        # parse.add_argument_group()
        parser.add_argument( '-f', '--file', dest = 'store', dest = 'file', help='Store the name of the csv file you want converted' )
        parser.add_argument( '-n', '--column', action = 'store', dest = 'column', help='Store the name of the column you want filtered.' )

        # NEED TO ADD PARSER GROUP CALLED 'Optional Arguments'
        # parser.add_argument_group()
        parser.add_argument( '-d', '--dest', action = 'store', dest = 'file_destination', default= str( os.getcwd() ) + "/filteredcsvfile.csv",
                                                                                          help = "Store the name of the file you'd like the program to create" )
        parser.add_argument( '-c', '--compare', action = 'store', dest = 'compare', help = 'Command allows user to filter a column based on an operator passed to -c and '
                                                                                           'a value (String or Float) passed to -z. \n'
                                                                                           'Accepted Values: \n\t"gt" for greater than, '
                                                                                           '\n\t"lt" for less than, '
                                                                                           '\n\t"ne" for not equal" '
                                                                                            '\n\t"lte" for less than or equal'
                                                                                           '\n\t"gte" for greater than or equal to'
                                                                                            '\n\t "eq" for equals' )
        parser.add_argument('-z', '--filter', action='store', dest='filter', help='Accepts a value to filter a column by.  '
                                                                                  'Currently only integer, float and strings are accepted' )
        parser.add_argument( '-v', '--verbose', action = 'store_true', help = 'Increase the verbosity of the program.' )

        if len(sys.argv) <= 2:
            parser.print_help()
            sys.exit(1)

        args = parser.parse_args()
        file = args.file
        duplicate_column = args.column
        file_dest = args.file_destination
        column = args.column
        filter = args.filter
        

        assert os.path.exists( str(os.getcwd()) + '/' + file )

        filter_object = TableFilter( file, column, dest, compare, filter )
        filter_object.export_to_CSV()

        if args.verbose:
            assert isinstance( args.dest )
            print( 'Your csv file has been filtered and saved to %s' % args.dest )

        """
        if file_destination is None:
            file_destination = os.getcwd() + "/filteredcsvfile.csv"
            """
