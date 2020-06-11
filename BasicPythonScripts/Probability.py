import statistics

# Random Variable Mean
    # x_bar = sample
    # mu = population

def random_mean():
    x = [float(x) for x in input('Enter all values for x, separated by spaces: ').split()]

    #Calculate Mean
    mean = statistics.mean(x)
    print('\nMean of', x, 'is:', round(mean, 4))  

    #Calculate Std Dev
    std_dev = statistics.stdev(x)
    print('\nStandard Deviation of', x, 'is:', round(std_dev, 4))

    while True:
        random_mean()


# Probablility Distribution
    # Variance
        # sigma^2 = sum((x^2)*p(x)-mu^2)
    # Standard Variation
        # sigma = sqrt(variance)
    # Mean
        # mu = sum(x*p(x))

def probability_distribution():

    while True:
        probability_distribution()

try:
    random_mean()
    probability_distribution()
    
except statistics.StatisticsError:
    print('\nPlease enter at least 2 values.\n')
    random_mean()

except ValueError:
    print('\nThat did not work.  Please enter a numerical value.\n')
    random_mean()