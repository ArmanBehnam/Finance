"""
Optuna script to create studies and a list of objective functions.

1. Set study name for optuna.
2. Create study for each dataset.
3. List of all the objective functions for OLPS straegies.
"""
import optuna

# Study name for given strategies.
study_name = ['eg', 'ftrl', 'ftl', 'pamr', 'cwmr', 'olmar1', 'olmar2', 'rmr',
              'corn', 'cornk', 'cornu', 'scorn', 'scornk', 'fcorn', 'fcornk']

# Create studies for each strategy for different dataset: data1, data2, data3.
for s_name in study_name:
    # We choose direction='maximize' to maximize returns as a goal.
    temp1 = optuna.create_study(study_name=name, storage='sqlite:///db/data1.db', direction='maximize')
    temp2 = optuna.create_study(study_name=name, storage='sqlite:///db/data2.db', direction='maximize')
    temp3 = optuna.create_study(study_name=name, storage='sqlite:///db/data3.db', direction='maximize')


# Objective functions for tuning.

# EG
def obj(trial):
    eta = trial.suggest_loguniform('eta', 0.01, 50)

    # Multiplicative update
    temp = EG('MU', eta)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# FTRL
def obj(trial):
    beta = trial.suggest_uniform('beta', 1, 100)
    temp = FTRL(beta)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# PAMR1
def obj(trial):
    epsilon = trial.suggest_uniform('epsilon',0,1.5)
    agg = trial.suggest_uniform('agg',0,100)
    temp = PAMR(1, epsilon, agg)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# OLMAR1
def obj(trial):
    epsilon = trial.suggest_uniform('epsilon', 1, 25)
    window = trial.suggest_int('window', 1, 30)
    temp = OLMAR(1, epsilon=epsilon, window=window)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# OLMAR2
def obj(trial):
    epsilon = trial.suggest_uniform('epsilon', 1, 25)
    alpha = trial.suggest_uniform('alpha', 0, 1)
    temp = OLMAR(2, epsilon=epsilon, alpha=alpha)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# RMR
def obj(trial):
    epsilon = trial.suggest_uniform('epsilon',1,25)
    n_iteration = trial.suggest_int('n_iteration',2, 500)
    window = trial.suggest_int('window', 2, 30)
    temp = RMR(epsilon, n_iteration, window)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# CORN
def obj(trial):
    window = trial.suggest_int('window', 1, 30)
    rho = trial.suggest_uniform('rho', -1, 1)
    temp = CORN(window, rho)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# CORNU
def obj(trial):
    window = trial.suggest_int('window', 1, 10)
    rho = trial.suggest_uniform('rho', -1, 1)
    temp = CORNU(window, rho)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# SCORN
def obj(trial):
    window = trial.suggest_int('window', 1, 30)
    rho = trial.suggest_uniform('rho', 0, 1)
    temp = SCORN(window, rho)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]

# FCORN
def obj(trial):
    window = trial.suggest_int('window', 1, 30)
    rho = trial.suggest_uniform('rho', 0, 1)
    lambd = trial.suggest_uniform('lambd', 0, 100)
    temp = FCORN(window, rho, lambd)
    temp.allocate(data, verbose=True)

    data_len, period = data.shape[0], 10
    for i in range(0, period):
        time = data_len * i // period
        trial.report(temp.portfolio_return.iloc[time][0], step=time)

    return temp.portfolio_return.iloc[-1][0]
