def print_model(unprinted, printed):
    while unprinted:
        current_design = unprinted.pop()
        print(f'Printing: {current_design}')
        printed.append(current_design)
def show_printed(printed):
    print('The following models have been printed!')
    for pt in printed:
        print(pt)

unprinted = ['cake', 'ball', 'chair']
printed = []

print_model(unprinted[:], printed)
show_printed(printed)
print(unprinted)
print(printed)