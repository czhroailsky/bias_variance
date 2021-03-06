# Bias and Variance Tradeoff

The following equation represents the expected out-of-sample error in terms of <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{g}" title="\bar{g}" /></a> which is the 'average function' which can be interpreted as: Generate many data sets <a href="https://www.codecogs.com/eqnedit.php?latex=D_1,&space;...,&space;D_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_1,&space;...,&space;D_k" title="D_1, ..., D_k" /></a> and apply the learning algorithm to each data set to produce final hypotheses <a href="https://www.codecogs.com/eqnedit.php?latex=g_1,&space;...,&space;g_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_1,&space;...,&space;g_k" title="g_1, ..., g_k" /></a>. We can then estimate the average function for any <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a> by <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{g}(x)\approx&space;\frac{1}{k}&space;\sum_{k=1}^{K}&space;g_k(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{g}(x)\approx&space;\frac{1}{k}&space;\sum_{k=1}^{K}&space;g_k(x)" title="\bar{g}(x)\approx \frac{1}{k} \sum_{k=1}^{K} g_k(x)" /></a>. Essentialy, we are viewing <a href="https://www.codecogs.com/eqnedit.php?latex=g(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g(x)" title="g(x)" /></a> as a random variable, with the randomness coming from the randomness in the dataset;  <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{g}(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{g}(x)" title="\bar{g}(x)" /></a> is the expected value of this random variable (for a particular <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a>), and <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{g}" title="\bar{g}" /></a> is a function, the average function, composed of these expected values. 

<a href="https://www.codecogs.com/eqnedit.php?latex=E_D[(g^D(x)&space;-&space;f(x))^2]&space;=&space;E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]&space;&plus;&space;(\bar{g}(x)&space;-&space;f(x))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_D[(g^D(x)&space;-&space;f(x))^2]&space;=&space;E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]&space;&plus;&space;(\bar{g}(x)&space;-&space;f(x))^2" title="E_D[(g^D(x) - f(x))^2] = E_D[(g^D(x) - \bar{g}(x))^2] + (\bar{g}(x) - f(x))^2" /></a>


The term <a href="https://www.codecogs.com/eqnedit.php?latex=(\bar{g}(x)-f(x))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(\bar{g}(x)-f(x))^2" title="(\bar{g}(x)-f(x))^2" /></a> measures how much the average function that we would learn using different data sets <a href="https://www.codecogs.com/eqnedit.php?latex=D" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D" title="D" /></a> deviates from the target function that generated these data sets. This term is called bias.

<a href="https://www.codecogs.com/eqnedit.php?latex=bias(x)&space;=&space;(\bar{g}(x)&space;-&space;f(x))^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?bias(x)&space;=&space;(\bar{g}(x)&space;-&space;f(x))^2" title="bias(x) = (\bar{g}(x) - f(x))^2" /></a>

As it measures how much our learning model is biased away from the target function. This is because <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{g}" title="\bar{g}" /></a> has the benefit of learning from an unlimited number of datasets, so it is only limited by its ability to approximate <a href="https://www.codecogs.com/eqnedit.php?latex=f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f" title="f" /></a> by the limitation in the model learning itself.

The term <a href="https://www.codecogs.com/eqnedit.php?latex=E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]" title="E_D[(g^D(x) - \bar{g}(x))^2]" /></a> is the variance of the random variable <a href="https://www.codecogs.com/eqnedit.php?latex=g^D(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g^D(x)" title="g^D(x)" /></a>.

<a href="https://www.codecogs.com/eqnedit.php?latex=var(x)&space;=&space;E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?var(x)&space;=&space;E_D[(g^D(x)&space;-&space;\bar{g}(x))^2]" title="var(x) = E_D[(g^D(x) - \bar{g}(x))^2]" /></a>

The variance measures the variation in the final htpothesis, depending on the data set. We thus arrive at the bias-variance decomposition of out-of-sample error.

<a href="https://www.codecogs.com/eqnedit.php?latex=E_D[E_{out}(g^D)]&space;=&space;E_x[bias(x)&space;&plus;&space;var(x)]&space;=&space;bias&space;&plus;&space;var" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_D[E_{out}(g^D)]&space;=&space;E_x[bias(x)&space;&plus;&space;var(x)]&space;=&space;bias&space;&plus;&space;var" title="E_D[E_{out}(g^D)] = E_x[bias(x) + var(x)] = bias + var" /></a>

# Bias_variance_fx_b.py
Considering the target function <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;sin(\pi&space;x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;sin(\pi&space;x)" title="f(x) = sin(\pi x)" /></a> and a datset of size <a href="https://www.codecogs.com/eqnedit.php?latex=N=2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?N=2" title="N=2" /></a>. We sample <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a> uniformly in [-1, 1] to generate a data set <a href="https://www.codecogs.com/eqnedit.php?latex=(x_1,&space;y_1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_1,&space;y_1)" title="(x_1, y_1)" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=(x_2,&space;y_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_2,&space;y_2)" title="(x_2, y_2)" /></a>.

Fit the model using:

<a href="https://www.codecogs.com/eqnedit.php?latex=H_0:" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0" title="H_0" /></a>: Set of all lines of the form <a href="https://www.codecogs.com/eqnedit.php?latex=h(x)&space;=&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h(x)&space;=&space;b" title="h(x) = b" /></a>

For <a href="https://www.codecogs.com/eqnedit.php?latex=H_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0" title="H_0" /></a>, we choose the constant hypothesis that best fits the data (the horizontal line at the midpoint, <a href="https://www.codecogs.com/eqnedit.php?latex=b&space;=&space;\frac{y_1&plus;y_2}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b&space;=&space;\frac{y_1&plus;y_2}{2}" title="b = \frac{y_1+y_2}{2}" /></a>).


# Bias_variance_fx_ax_b.py

Consider a target function <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;sin(\pi&space;x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;sin(\pi&space;x)" title="f(x) = sin(\pi x)" /></a> and a data set of size <a href="https://www.codecogs.com/eqnedit.php?latex=N=2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?N=2" title="N=2" /></a>. We sample <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a> uniformly in [-1, 1] to generate a data set <a href="https://www.codecogs.com/eqnedit.php?latex=(x_1,&space;y_1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_1,&space;y_1)" title="(x_1, y_1)" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=(x_2,&space;y_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(x_2,&space;y_2)" title="(x_2, y_2)" /></a>.

Fit the model using:

<a href="https://www.codecogs.com/eqnedit.php?latex=H_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_1" title="H_1" /></a>: Set of all lines of the form <a href="https://www.codecogs.com/eqnedit.php?latex=h(x)&space;=&space;ax&plus;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h(x)&space;=&space;ax&plus;b" title="h(x) = ax+b" /></a>

With <a href="https://www.codecogs.com/eqnedit.php?latex=H_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_1" title="H_1" /></a>, the learned hypothesis is wilder and varies extensively depending on the dataset.

#
#
#
- Abu-Mostafa, Y. S., Magdon-Ismail, M., & Lin, H. T. (2012). Learning from data (Vol. 4). New York, NY, USA:: AMLBook.
