def create_figure_set():
    figure_set = set(i for i in range(10))
    return figure_set

def combine_sets(base_set, figure_set):
    base_set.update(base_set | figure_set)
def output_set(base_set):
    print("Об`єднана множина:", base_set)

base_set = {'c','d'}
figure_set = create_figure_set()
print("Захардкоджена множина:", base_set)
print("Множина цифр:", figure_set)

combine_sets(base_set, figure_set)

output_set(base_set)