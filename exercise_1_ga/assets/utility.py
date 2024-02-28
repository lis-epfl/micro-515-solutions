import numpy as np

def highlight_mutations(original, mutated):
    if original.shape != mutated.shape:
        raise ValueError("Original and mutated populations must have the same shape")

    # ANSI escape code for red text and reset
    RED = '\033[91m'
    RESET = '\033[0m'

    for i in range(original.shape[0]):
        highlighted_row = ''
        for j in range(original.shape[1]):
            if original[i, j] != mutated[i, j]:
                highlighted_row += f'{RED}{mutated[i, j]}{RESET} '
            else:
                highlighted_row += f'{mutated[i, j]} '
                
        if i == 0:
            print(f"[[{highlighted_row[:-1]}]")
            continue
            
        if i == original.shape[0]-1:
            print(f" [{highlighted_row[:-1]}]]")
            continue
            
        print(f" [{highlighted_row[:-1]}]")
        
def search_index_in_columns(population, winner):
    index = None
    for i in range(population.shape[0]):
        if np.array_equal(population[i, :].reshape(1, -1), winner):
            index = i
            break

    # Print the result
    if index is None:
        print("Winner not found in population!")
        
    return index