# This file contains the subscription class

class Subscription:
    """This class stores basic attribute of a subcription
    """

    # private data members
    __sname = None                          # Name of the subscription
    __sstatus = None                        # Status of the subsctiption
    __sbciu = None                          # Bank card in use
    __sa = None                             # Amount for that subscription
    __slbd = None                           # Last billed date
    __snbd = None                           # Next billing date

    # constructor
    def __init__(self, sname, sstatus, sbciu, sa, slbd, snbd) -> None:
        """Instanciates a subcription object

        Args:
            sname (str, required): Name of the Subscription
            sstatus (str, required): Status of the Subscription, either Active or Canceled
            sbciu (str, required): Bank card in use for this active subscription
            sa (str, required): Amount for it
            slbd (str, required): Last billed date of that subscription, e.g. Tuesday, September 30, 2025
            snbd (str, required): Next billing date of that subscription, e.g. Thursday, October 30, 2025
        """
        # sname
        assert type(sname) == str, "sname needs to a string"
        assert sname != None or '', "sname cannot be none"

        # sstatus
        assert type(sstatus) == str, "sstatus needs to a string"
        assert sstatus != None or '', "sstatus cannot be none"

        # sbciu
        assert type(sbciu) == str, "sbciu needs to a string"
        assert sbciu != None or '', "sbciu cannot be none"

        # sa
        assert type(sa) == str, "sa needs to a string"
        assert sa != None or '', "sa cannot be none"

        # slbd
        assert type(slbd) == str, "slbd needs to a string"
        assert slbd != None or '', "slbd cannot be none"

        # snbd
        assert type(snbd) == str, "snbd needs to a string"
        assert snbd != None or '', "snbd cannot be none"
        
        # initializing private data members
        self.__sname = sname
        self.__sstatus = sstatus
        self.__sbciu = sbciu
        self.__sa = sa
        self.__slbd = slbd
        self.__snbd = snbd

    # __str__
    def __str__(self):
        return f"[Subscription Name]: {self.__sname}, [Status]: {self.__sstatus}, [Bank Card In Use]: {self.__sbciu}, [Amount]: {self.__sa}, [Last Billing Date]: {self.__slbd}, [Next Billing Date]: {self.__snbd}"