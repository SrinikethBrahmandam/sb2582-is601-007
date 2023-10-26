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

def test_face_stencil_in_stock(machine):
    stencil_name = "Happy Face"
    selected_stencil = next(s for s in machine.face_stencils if s.name == stencil_name)
    
    while selected_stencil.in_stock():
        selected_stencil.use()
        
    machine.handle_pumpkin_choice("Mini Pumpkin")
    with pytest.raises(OutOfStockException):
        machine.handle_face_stencil_choice(stencil_name)

def test_extras_in_stock(machine):
    extra_name = "LED Candle"
    selected_extra = next(e for e in machine.extras if e.name == extra_name)
    
    while selected_extra.in_stock():
        selected_extra.use()
        
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    
    with pytest.raises(OutOfStockException):
        machine.handle_extra_choice(extra_name)

def test_up_to_three_face_stencils(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("Toothy Face")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_face_stencil_choice("Spooky Face")

def test_up_to_three_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("Sticker Pack")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_extra_choice("Dry Ice")

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

def test_clean_machine_resets_remaining_uses(machine):
    machine.remaining_uses = 0
    machine.clean_machine()
    assert machine.remaining_uses == PumpkinMachine.USES_UNTIL_CLEANING, f"Expected remaining_uses to be {PumpkinMachine.USES_UNTIL_CLEANING}, but got {machine.remaining_uses}"

def test_reset_method_clears_inprogress_pumpkin(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.reset()
    assert len(machine.inprogress_pumpkin) == 0, "Expected inprogress_pumpkin to be empty after calling reset"
