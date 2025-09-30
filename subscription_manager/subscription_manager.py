# This file contains the subscription class

import pandas as pd
from .subscription import Subscription


class SM:
    """This class is responsible for hanling an excel file in a certain pattern.
    It reads the excel file and performs various tasks such as updating the next bill month, notifying the admin for his upcoming subscriptions e.t.c
    """

    # private data members
    __df = None                             # data frame
    __current_month = None                  # current month of the subscription
    __next_month = None                     # next month of the subscription
    __subscriptions = []                    # List of Subscriptions

    # utility functions
    def __read_excel_file(self, filename) -> None:
        """Reads an excel file and store it in private data_frame member
        """
        # reading excel file
        self.__df = pd.read_excel(filename)
        print(self.__df)
        self.__current_month = self.__df['Last Billed Date']
        self.__next_month = self.__df['Next Billing Date']
        # print(self.__current_month)
        # print(self.__next_month)
        print('*' * 10)
        for rows, cols in self.__df.iterrows():
            self.__subscriptions.append(Subscription(sname=cols['Subscription Name'], sstatus=cols['Status'],
                                                    sbciu=cols['Bank Card In Use'], sa=str(cols['Amount']),
                                                    slbd=str(cols['Last Billed Date']), snbd=str(cols['Next Billing Date']))
                                                    )
        
        for s in self.__subscriptions:
            print(s)
    

    # constructor
    def __init__(self, filename=None) -> None:
        """Reads an excel file and store it in private data_frame

        Args:
            filename (str, required): Name of the file to be read. Defaults to None.
        """
        # filename
        assert type(filename) == str, "filename needs to a string"
        assert filename != '' or None, "filename cannot be none"

        # reading excel file
        self.__read_excel_file(filename=filename)

        