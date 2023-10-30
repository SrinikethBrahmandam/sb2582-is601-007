import pytest
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException

@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    return first_order

def test_pumpkin_selection_first(machine):
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("LED Candle")
    machine.handle_pumpkin_choice("Mini Pumpkin")
    assert machine.inprogress_pumpkin[0].name == "Mini Pumpkin"
#sb2582 - 26/10/23
#This test case ensures that selecting a pumpkin is the first valid step
#And it raises an InvalidStageException when trying to choose a face stencil or extra before selecting a pumpkin.
#It then verifies that the pumpkin selected is "Mini Pumpkin."

def test_face_stencil_in_stock(machine):
    stencil_name = "Happy Face"
    selected_stencil = next(s for s in machine.face_stencils if s.name == stencil_name)
    
    while selected_stencil.in_stock():
        selected_stencil.use()
        
    machine.handle_pumpkin_choice("Mini Pumpkin")
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice(stencil_name)
#sb2582 - 26/10/23
# It is raised when trying to select a face stencil that is out of stock.



def test_extras_in_stock(machine):
    extra_name = "LED Candle"
    selected_extra = next(e for e in machine.extras if e.name == extra_name)
    
    while selected_extra.in_stock():
        selected_extra.use()
        
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    
    with pytest.raises(OutOfStockException):
        machine.handle_extra_choice(extra_name)
#sb2582 - 26/10/23
#It depletes the stock of the selected extra and then tries to choose it after selecting a pumpkin and advancing to the extras stage.

def test_up_to_three_face_stencils(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")
#sb2582 - 26/10/23
#This is raised when attempting to select more than the allowed three face stencils for a pumpkin, specifically by choosing a fourth face stencil

def test_up_to_three_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("Sticker Pack")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Dry Ice")
#sb2582 - 26/10/23
#This is raised when attempting to select more than the allowed three extras for a pumpkin, specifically by choosing a fourth extra.

def test_total_products_increment(machine):
    initial_total_products = machine.total_products
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("done")
    calculated_cost = machine.calculate_cost()
    formatted_cost = str(calculated_cost)
    machine.handle_pay(calculated_cost, formatted_cost)
    assert machine.total_products == initial_total_products + 1, f"Expected total_products to be {initial_total_products + 1}, but got {machine.total_products}"
#sb2582 - 26/10/23
#This test case ensures that the "total_products" variable increments correctly when a valid purchase is made.
#including selecting a pumpkin, face stencil, extras, and completing the payment process.

def test_clean_machine_resets_remaining_uses(machine):
    machine.remaining_uses = 0
    machine.clean_machine()
    assert machine.remaining_uses == PumpkinMachine.USES_UNTIL_CLEANING, f"Expected remaining_uses to be {PumpkinMachine.USES_UNTIL_CLEANING}, but got {machine.remaining_uses}"
#sb2582 - 26/10/23
#This test verifies that the "clean_machine" method properly resets the "remaining_uses" variable to its initial value when called.

def test_reset_method_clears_inprogress_pumpkin(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.reset()
    assert len(machine.inprogress_pumpkin) == 0, "Expected inprogress_pumpkin to be empty after calling reset"
#sb2582 - 26/10/23
#This test ensures that the "reset" method correctly clears the "inprogress_pumpkin" list,
#resulting in an empty list after calling the reset method.