
from enum import Enum
import sys
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from PumpkinMachineExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if self.quantity < 0:
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name

class Pumpkin(Usable):
    pass

class FaceStencil(Usable):
    pass

class Extra(Usable):
    pass

class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4

class PumpkinMachine:
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3

    def __init__(self):
        self.pumpkins = [Pumpkin(name="Mini Pumpkin", cost=1),
                    Pumpkin(name="Small Pumpkin", cost=2),
                    Pumpkin(name="Medium Pumpkin", cost=2.5),
                    Pumpkin(name="Large Pumpkin", cost=3)]
        self.face_stencils = [FaceStencil(name="Happy Face", quantity=10, cost=1),
                        FaceStencil(name="Scream Face", quantity=10, cost=1),
                        FaceStencil(name="Toothy Face", quantity=10, cost=1),
                        FaceStencil(name="Spooky Face", quantity=10, cost=1)]
        self.extras = [Extra(name="Small Candle", quantity=10, cost=.25),
                Extra(name="LED Candle", quantity=10, cost=.25),
                Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
                Extra(name="Sticker Pack", quantity=10, cost=1.00),
                Extra(name="Paint Kit", quantity=10, cost=3),
                Extra(name="Dry Ice", quantity=10, cost=.25),
                Extra(name="Googly Eyes", quantity=10, cost=.25),
                Extra(name="Glitter", quantity=10, cost=.25)]

        self.remaining_uses = PumpkinMachine.USES_UNTIL_CLEANING
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0

        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        print("The machine has been cleaned.")

    def handle_pumpkin_choice(self, _pumpkin):
        self.pick_pumpkin(_pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, _face_stencil):
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(_face_stencil)

    def handle_extra_choice(self, _extra):
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(_extra)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += expected
            print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_pumpkin(self):
        print(
            f"Current Pumpkin: {','.join([x.name for x in self.inprogress_pumpkin])}")

    def calculate_cost(self):
        total_cost = sum([item.cost for item in self.inprogress_pumpkin])
        return total_cost
    #UCID - sb2582 - 26/10/23 
    #Calculates the total cost without modifying the predefined costs.
    #It returns the sum of the costs directly in one line.

    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.pumpkins))))}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"What type of face stencil would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.face_stencils))))}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.extras))))}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                total = input(
                    f"Your total is {expected:.2f}, please enter the exact value.\n")
                self.handle_pay(expected, total)

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    print("Quitting the pumpkin machine")
                    return 1
        except KeyboardInterrupt:
            print("Quitting the pumpkin machine")
            sys.exit()
        except OutOfStockException:
            print(f"Out of stock in the {self.currently_selecting} stage.")
        except NeedsCleaningException:
            clean = input("The machine needs cleaning. Type 'clean' to clean the machine or any other key to continue.\n")
            if clean.lower() == "clean":
                self.clean_machine()
        except InvalidChoiceException:
            print(f"Invalid choice in the {self.currently_selecting} stage.")
        except ExceededRemainingChoicesException:
            print(f"Exceeded remaining choices in the {self.currently_selecting} stage.")
            self.currently_selecting = STAGE(self.currently_selecting.value + 1)
        except InvalidPaymentException:
            print("Invalid payment entered.")
        except Exception as e:
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()
    #UCID - sb2582 - 26/10/23
    #The run method serves as the central control for user interactions with the PumpkinMachine.
    #It uses conditional statements to determine the current stage of pumpkin creation,
    #Such as selecting a pumpkin type, a face stencil, extras, or making a payment.
    #At each stage, it presents the user with appropriate prompts and choices.
    #The method gracefully handles exceptions, including OutOfStockException, NeedsCleaningException, InvalidChoiceException, ExceededRemainingChoicesException, and InvalidPaymentException.
    #Users have the option to quit the machine, which results in program termination, or continue with their orders.

    def start(self):
        self.run()

if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()
