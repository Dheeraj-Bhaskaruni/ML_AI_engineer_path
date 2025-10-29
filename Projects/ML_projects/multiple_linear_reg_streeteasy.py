import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

csv_path = "/datasets/manhattan.csv"
streeteasy = pd.read_csv(csv_path)

X = streeteasy[['size_sqft', 'building_age_yrs']]
y = streeteasy['rent']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.8, random_state=6
)

model = LinearRegression().fit(X_train, y_train)

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    X_train['size_sqft'],
    X_train['building_age_yrs'],
    y_train,
    c='k', marker='+', alpha=0.
)

# build a grid over the feature space
xs = np.linspace(X['size_sqft'].min(), X['size_sqft'].max(), 30)
ys = np.linspace(X['building_age_yrs'].min(), X['building_age_yrs'].max(), 30)
XS, YS = np.meshgrid(xs, ys)

# predict Z over the grid; use DataFrame with same column names to avoid warnings
grid = pd.DataFrame({
    'size_sqft': XS.ravel(),
    'building_age_yrs': YS.ravel()
})
Z = model.predict(grid).reshape(XS.shape)

# draw regression plane
ax.plot_surface(XS, YS, Z, alpha=0.6, linewidth=0, antialiased=True)

ax.set_xlabel('Size (ft$^2$)')
ax.set_ylabel('Building Age (years)')
ax.set_zlabel('Rent ($)')

# hide tick labels (replacement for deprecated w_*axis)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# set a nice view angle
ax.view_init(elev=43.5, azim=-110)

plt.tight_layout()
plt.show()






