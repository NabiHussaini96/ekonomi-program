class Konto:
    def __init__(self, saldo=0):
        self.saldo = saldo
        def sätt_in(self, belopp):
            self.saldo += belopp
            def ta_ut(self, belopp):
                if belopp <= self.saldo:
                    self.saldo -= belopp
                else:
                    print("Otillräckligt saldo")
                    def visa_saldo(self):
                        return self.saldo
                    