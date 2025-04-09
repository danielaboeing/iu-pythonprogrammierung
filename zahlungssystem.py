
class ERPSystem:
    def transmitData(self, necessary_info):
        if necessary_info.get("checkForPaymentAfter"):
            print("Updated data in ERP!")        
        else:
            print("Transmitted data to ERP!")

class PaypalConnector:
    def connect(self, necessary_info):
        print("Connected to Paypal!")


class PaymentSystem:

    def __init__(self):
        self.erpsystem = ERPSystem()

    def _transmitPaymentInfo(self, necessary_info):
        necessary_info["payed"] = True
        self.erpsystem.transmitData(necessary_info)
        return True

    def executePayment(self, necessary_info):
        return self._transmitPaymentInfo(necessary_info)

class PaypalPayment(PaymentSystem):

    def __init__(self):
        super().__init__()
        self._paypal_connector = PaypalConnector()

    def _connectToPaypal(self, necessary_info):
        self._paypal_connector.connect(necessary_info)
        return True

    def executePayment(self, necessary_info):
        print("Connecting to Paypal ...")
        if self._connectToPaypal(necessary_info):
            return super().executePayment(necessary_info)
        else:
            return False
        
class InvoicePayment(PaymentSystem):

    def _addNoteForAccounting(self, necessary_info):
        print("Setting deadline for payment to 14 days ...")
        self.erpsystem.transmitData({"checkForPaymentAfter": "14d"})
        return True


    def executePayment(self, necessary_info):
        print("Prepare invoice payment ...")
        if self._addNoteForAccounting(necessary_info):
            return super().executePayment(necessary_info)
        else:
            return False
    

if __name__ == "__main__":
    payment_system = None 
    selection_invalid = True
    while selection_invalid:
        print("Select your payment method:")
        print("P) Paypal")
        print("I) Invoice")

        selection = input("Selection: ").lower()
        if selection == "p":
            payment_system = PaypalPayment()
            selection_invalid = False
        elif selection == "i":
            payment_system = InvoicePayment()
            selection_invalid = False
        else:
            print("\n\033[91mInvalid selection, please try again.\033[0m\n")

    payment_system.executePayment({"name": "Placeholder", "price": 99.99})
    print("Payment completed!")
    exit(0)
