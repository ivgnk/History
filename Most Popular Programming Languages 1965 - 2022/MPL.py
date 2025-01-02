"""
Most Popular Programming Languages 1965 - 2022
https://www.youtube.com/watch?v=qQXXI5QFUfw
"""
import matplotlib.pyplot as plt
data=dict({'1970Q1': dict({'Fortran': 24.99, 'COBOL':6.343, 'Assembly': 4.835,
                 'ALGOL': 4.827, 'APL': 4.165, 'BASIC':3.737,
                 'Lisp':3.012, 'Pascal':0.429}),
           '1980Q1': dict({'Pascal': 26.015, 'Fortran': 23.818,
                           'BASIC':16.586, 'COBOL':12.454,
                           'C':10.087, 'Lisp':9.841,
                            'Assembly': 6.015,'Ada':4.453,
                            'APL': 4.273, 'ALGOL': 2.455,
                            'C++': 1.182})})
colors=dict({'Fortran': 'red', 'COBOL':'lightcoral',
             'Assembly': 'gray','ALGOL': 'navy',
             'APL': 'peru', 'BASIC': 'crimson',
             'Lisp':'teal', 'Pascal':'blue',
              'C':'yellow', 'Ada':'olive',
              'C++':'brown'})
the_h = [0.5, 0.5, 0.5] # список высот столбцов
print(type(data))
for k,v in data.items():
    print(k)
    print(v)
    name_= list(v.keys())
    val_ = list(v.values())
    the_h=[0.75]*len(val_)
    plt.figure(figsize=(10.1, 5))
    colo=[colors[n] for n in name_]
    # print(name_)
    # print(val_)
    # print(colo)
    plt.barh(name_, val_, height = the_h, color=colo) # задаем высоты столбцов
    plt.gca().invert_yaxis() # stackoverflow.com/questions/34076177/matplotlib-horizontal-bar-chart-barh-is-upside-down
    plt.title(k)
    plt.grid()
    plt.show()
