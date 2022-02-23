# intro to regression

# OVERVIEW:
    # show some linear data
    # discuss correlation (R^2)
    # fit model, discuss error

    # show some quadratic data
    # discuss correlation: 0 correlation != no pattern
    # fit linear model - discuss underfitting
    # how to make this fit "better"?

    # fit polynomial model of high degree - discuss overfitting, bias/variance tradeoff



import numpy as np
import pandas as pd
from matplotlib import gridspec
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR, NuSVR, LinearSVR

# make some linear points (possibly play around with number of samples)
X, y = np.linspace(0, 10, 100), np.linspace(0, 10, 100)

# add some noise
noise = np.random.uniform(-2, 2, (100,))
y += noise

# and show the graph
plt.figure(figsize=(10,10))
plt.scatter(X, y)
plt.show()
plt.clf()

# firstly: is there correlation? does a linear model make sense?
X = np.reshape(X, (len(X), 1))
y = np.reshape(y, (len(y), 1))
print(np.corrcoef(X, y, rowvar=False)[0][1]) # this is a 2x2 correlation matrix, so the off-diagonal entries are what we want

# fuck yeah, that's (probably) pretty high. optionally, check out what happens when noise increases
correlations = []
noise_range = []
for i in np.arange(1,6,.1):
    X_temp, y_temp = np.linspace(0, 10, 100), np.linspace(0, 10, 100)
    y_temp += np.random.uniform(-i, i, (100,))
    X_temp = np.reshape(X_temp, (len(X_temp), 1))
    y_temp = np.reshape(y_temp, (len(y_temp), 1))
    noise_range.append(i)
    correlations.append(np.corrcoef(X_temp, y_temp, rowvar=False)[0][1])

plt.plot(noise_range, correlations)
plt.xlabel('Maximum size of noise')
plt.ylabel('Correlation')
plt.title('Effect of noise on correlation')
plt.show()
plt.clf()


# so let's fit a linear model to it
lin_reg = LinearRegression(fit_intercept=False)
lin_reg.fit(X, y)
print(lin_reg.coef_)

# the true slope of the line is 1, so this is pretty good. let's see!
def plot_best_fit_line(X, coef, ax=None):
    y_vals = X * coef
    y_vals = np.reshape(y_vals, (len(X),)) # y_vals defaults to (1, 100) for some reason
    if ax:
        ax.plot(X, y_vals, color='red')
    else:
        plt.plot(X, y_vals, color='red')

plt.scatter(X, y)
plot_best_fit_line(X, lin_reg.coef_)
# plt.show()
plt.clf()

# cool beans. this is good, but exactly how good is it?
print(lin_reg.score(X,y))

# this is the coefficient of determination, or R^2. defined as 1 - (residual sum of squares) / (total sum of squares)
# residual sum of squares is difference between each true value and prediction squared, and summed. so best case, residual sum = 0 -> R^2 = 1
# note R^2 has no lower bound - difference between true value and prediction can be arbitrarily high


# support vectors to the rescue!
# support vector regression has two parameters that control "goodness": epsilon and C
# one way to think about it: let's say you have your data, and some kind of model for it - a line 
# the error in your model is how far away your actual data is from this line
# epsilon is this distance, above and below your line. so small epsilon is generally good, but too small may be impractical/impossible
# one way to make small epsilon values possible is to give wiggle room for each data point to violate this epsilon distance boundary condition
# C controls the sum of the wiggle room
# so if C is low, you don't care about the wiggle room too much -> many points are more than epsilon away from your line. highly regularlized, potentially underfitting
# on the other hand, if C is high, you care about the wiggle room a LOT -> very few points are more than epsilon away from your line. low regularization, potentially overfitting

# let's see it!
def plot_epsilon_boundary(X, ax, coef, epsilon):
    y_vals = X * coef
    y_vals_positive = np.reshape(y_vals+epsilon, (len(X),)) # y_vals defaults to (1, 100) for some reason
    y_vals_negative = np.reshape(y_vals-epsilon, (len(X),))
    ax.plot(X, y_vals_positive, '--', color='black')
    ax.plot(X, y_vals_negative, '--', color='black')

e_vals = [1, 2, 3]
fig = plt.figure(figsize=(15,5))
gs = gridspec.GridSpec(1, 3)
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
axes = [ax0, ax1, ax2]
# fig, axes = plt.subplots(1,3)
for epsilon, ax in zip(e_vals, axes):
    lin_svr = LinearSVR(epsilon=epsilon, fit_intercept=False, max_iter=10000)
    lin_svr.fit(X, y.ravel())
    ax.scatter(X, y)
    plot_best_fit_line(X, lin_svr.coef_, ax)
    plot_epsilon_boundary(X, ax, lin_svr.coef_, epsilon)
    ax.title.set_text(f'$\epsilon$={epsilon}')

plt.show()
plt.clf()

for epsilon in e_vals:
    lin_svr = LinearSVR(epsilon=epsilon, fit_intercept=False, max_iter=10000)
    lin_svr.fit(X, y.ravel())
    plt.scatter(X, y)
    plot_best_fit_line(X, lin_svr.coef_)
    plot_epsilon_boundary(X, lin_svr.coef_, epsilon)
    plt.title(f'$\epsilon$={epsilon}')
    plt.show()
    plt.clf()


# linear data is nice and easy. but what happens with non linear data?
X = np.linspace(-1, 1, 20)
noise = np.random.uniform(-.2, .2, (20,))
y = (X + noise) ** 2
plt.scatter(X, y)
plt.show()
plt.clf()

# what do you think the correlation coefficient is?
print(np.corrcoef(X, y, rowvar=False)[0][1])

# remember - just because R^2 is close to 0, doesn't mean there's no pattern!
# for fun, let's fit a linear model
X = np.reshape(X, (len(X), 1))
y = np.reshape(y, (len(y), 1))
lin_reg.fit(X, y)
plt.scatter(X, y)
plot_best_fit_line(X, lin_reg.coef_)
plt.show()
plt.clf()

# sad:
print(lin_reg.score(X,y))


# we "know" that this this data probably probably has a quadratic relationship. but what if all we wanted to do was minimize error?
poly_reg = PolynomialFeatures(degree=20, include_bias=False)
temp_lin_reg = LinearRegression(fit_intercept=False)
X_poly = poly_reg.fit_transform(X)
temp_lin_reg.fit(X_poly, y)
plt.scatter(X, y)
plt.plot(X, temp_lin_reg.predict(X_poly), color='red')
plt.show()
plt.clf()

# this has low error.... but is it good?
print(temp_lin_reg.score(X_poly, y))

# as a sanity check: predicts 1.5
print(temp_lin_reg.coef_[0][0]) 
