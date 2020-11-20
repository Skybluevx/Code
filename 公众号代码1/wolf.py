import pandas as pd
import numpy as np

initial_state = [0, 0, 0, 0]  # the left side of river = 0
final_state = pd.Series([1, 1, 1, 1])
final_state.index = ['wolf', 'lamb', 'veg', 'farmer']
state = pd.DataFrame(columns=["wolf", "lamb", "veg", "farmer"])  # 8 3 5
state = state.append({'wolf': 0, 'lamb': 0, 'veg': 0, 'farmer': 0}, ignore_index=True)
state_col = state.columns


def farmer(state, num):
    current = state.loc[len(state) - 1][state_col]
    if (current == final_state).all():
        return state
    elif (current['farmer'] == 1 and current['wolf'] == 1 and current['veg'] == 1 and current['lamb'] == 0):
        current['farmer'] = 0  # 减少不必要的穷举次数
        state = state.append(current, ignore_index=True)
        current['farmer'] = 1
        current['lamb'] = 1
        state = state.append(current, ignore_index=True)
        state = farmer(state, 0)
        return state
    else:  # 每一趟都必须有农民 农民带或者不带与它在一边的物品
        row = current[current == current['farmer']]
        for id in range(num, len(row) - 1):
            current = state.loc[len(state) - 1][state_col]
            current['farmer'] = 1 - current['farmer']
            current[row.index[id]] = 1 - current[row.index[id]]

            if not (((current['wolf'] == current['lamb']) and (current['lamb'] != current['farmer'])) or \
                    ((current['lamb'] == current['veg']) and (current['lamb'] != current['farmer']))):
                state = state.append(current, ignore_index=True)
                if len(state) == len(state.drop_duplicates()):
                    state = farmer(state, 0)
                    return state
                else:
                    state = state.drop_duplicates()
                    if (id != len(row) - 1 - 1):  # 每次带一样东西或者单独返回
                        state = farmer(state, id + 1)
                        return state
                    else:
                        current = state.loc[len(state) - 1][state_col]
                        current['farmer'] = 1 - current['farmer']
                        state = state.append(current, ignore_index=True)
                        state = farmer(state, 0)
                        return state


output = farmer(state, 0)
print(output)
