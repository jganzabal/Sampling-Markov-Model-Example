import numpy as np

def get_state_probabilities(samples_per_second, runing_seconds, transition_vector_list = [0.1, 0.2, 0.05, 0]):
    # Redefine transition vector taking sampling into account
    transition_vector = np.array(transition_vector_list)/samples_per_second
    print('Transition vector:',transition_vector)
    # Transition matrix from transition_vector
    transition_matrix = np.array([[1-transition_vector[0], transition_vector[0], 0, 0],\
                                 [0, 1-transition_vector[1], transition_vector[1], 0], \
                                 [0, 0, 1-transition_vector[2], transition_vector[2]],
                                 [0, 0, 0, 1]])
    print('Transition matrix:')
    print(transition_matrix)
    # We start in state 1 with probability one
    next_state = np.array([1, 0, 0, 0])
    last_state_evol = []
    third_state_evol = []
    second_state_evol = []
    first_state_evol = []
    # Sample the markov model
    for i in range(int(runing_seconds*samples_per_second)):
        next_state = next_state.dot(transition_matrix)
        last_state_evol.append(next_state[3])
        third_state_evol.append(next_state[2])
        second_state_evol.append(next_state[1])
        first_state_evol.append(next_state[0])
        
    print('States probabilities after sampling:',next_state)
    # Return the samples of each state
    return first_state_evol, second_state_evol, third_state_evol, last_state_evol