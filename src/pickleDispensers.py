from Dispenser import Dispenser
import constants
import pickle



with open('pickles/drinks.pickle', 'wb') as handle:
    pickle.dump(drinks, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('pickles/dispensers.pickle', 'rb') as handle:
#      b = pickle.load(handle)
