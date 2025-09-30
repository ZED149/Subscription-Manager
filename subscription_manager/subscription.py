# This file contains the subscription class

class Subscription:
    """This class stores basic attribute of a subcription
    """

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
        pass