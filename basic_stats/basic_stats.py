def basic_stats(x):
    #This is a module to compute basic statics mean (mu), standard deviation (sigma).
    #This module also produces a graph (fig) of the distribution of elements in the sample.

    import matplotlib.pyplot as plt

    #Determine the length of x
    N = 0
    for i in x:
        N += 1

    # Compute the mean of the elements in list x
    mu = 0
    for i in x:
        mu_i = i/N
        mu += mu_i

    # Compute the std deviation, using the mean and the elements in list x.

    sumTerm = 0
    for i in x:
        termSq = (i - mu)**2
        sumTerm += termSq
    sigma = (sumTerm**.5)/(N-1)

    ### Use Matplotlb.pyplot to make a histogram of x.
    fig = plt.figure()
    plt.hist(x, bins=19)
    plt.title('Frequency Distribution of Sample Data')
    plt.ylabel('Frequency')
    plt.xlabel('Data')
    plt.close(fig)

    return mu, sigma, fig