from typing import List, Union

def find_the_gate(spots: List[str], vehicle: str) -> Union[int, bool]:
    """
    spots: ['w','n','n','w','n','n']
    vehicle: 'wide' or 'narrow'
    
    Returns:
        first index of an available gate
        or False if none are available
    """
    type = vehicle[0].upper()
    for i, spot in enumerate(spots):
        if spot == type or spot == 'W':
            return i
    return False

assert find_the_gate(
  ['w','n','N'], 'narrow'
) == 2

assert find_the_gate(
  ['w','n','N','W','n','W'],'wide'
) == 3

assert find_the_gate(
  ['w','n','n','w','n','n'], 'narrow'
) == False


        
print(find_the_gate(
  ['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide'
))  # 15

