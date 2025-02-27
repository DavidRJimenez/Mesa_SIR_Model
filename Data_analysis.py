import pandas as pd
import numpy as np

def get_column_data(model):
    """Convierte los datos del modelo en formato amplio para facilitar la visualización."""
    agent_state = model.datacollector.get_agent_vars_dataframe()
    X = pd.pivot_table(
        agent_state.reset_index(), 
        index='Step', 
        columns='State', 
        aggfunc=np.size, 
        fill_value=0
    )    
    labels = ['Susceptible', 'Infected', 'Removed']
    X.columns = labels[:len(X.columns)]
    return X
