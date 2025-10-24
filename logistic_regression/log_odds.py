import numpy as np
from exam import hours_studied, calculated_coefficients, intercept


# Calculate odds_of_rain
odds_of_rain = 0.4/0.6


# Calculate log_odds_of_rain

log_odds_of_rain = np.log(odds_of_rain)
print(log_odds_of_rain)
# Calculate odds_on_time

odds_on_time = 0.9/.1

# Calculate log_odds_on_time
log_odds_on_time = np.log(odds_on_time)
print(log_odds_on_time)