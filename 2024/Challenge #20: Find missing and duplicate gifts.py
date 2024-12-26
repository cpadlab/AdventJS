
# Reto: https://adventjs.dev/es/challenges/2024/20


def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    
    received_count = {}
    expected_count = {}
    
    for gift in received:received_count[gift] = received_count.get(gift, 0) + 1
    for gift in expected:expected_count[gift] = expected_count.get(gift, 0) + 1
    
    missing = {}
    extra = {}
    
    for gift in expected_count:
        expected_qty = expected_count[gift]
        received_qty = received_count.get(gift, 0)
        
        if received_qty < expected_qty:missing[gift] = expected_qty - received_qty
            
    for gift in received_count:
        received_qty = received_count[gift]
        expected_qty = expected_count.get(gift, 0)
        
        if received_qty > expected_qty:extra[gift] = received_qty - expected_qty
    
    return { "missing": missing, "extra": extra }