from bf_funcs import bf_calculation
from read_shortcut import check_metrics

respath = '/Users/kosmo/Desktop/scripts/calculate_result.txt'
result = check_metrics()
if result:
    first, second, third, fourth = result
    #Run script
    bf_calculation(weight=first,fold1=second,fold2=third,fold3=fourth)
    with open(respath, 'w') as file:
        file.write('True')
else:
    print("⛔️ Invalid input")
    with open(respath, 'w') as file:
        file.write('False')