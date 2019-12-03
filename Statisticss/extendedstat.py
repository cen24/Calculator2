try:
    from Statisticss.computation.extended.populationvar import populationvar
    from Statisticss.computation.extended.proportion import proportion
    from Statisticss.computation.extended.samplemean import samplemean
    from Statisticss.computation.extended.samplestdev import samplestdev
    from Statisticss.computation.extended.samplevar import samplevar
    from Statisticss.computation.extended.zscore import zscore
    from Statisticss.computation.extended.population_correlation_coefficient import population_correlation_coefficient
    from Statisticss.computation.extended.pvalue import pvalue
    from Statisticss.computation.extended.Variance_of_population_proportion import Variance_of_population_proportion
    from Statisticss.computation.extended.Variance_of_sample_proportion import Variance_of_sample_proportion
    from Statisticss.computation.extended.cinterval import cintreval
    from Statisticss.computation.sample import Sample


    class extendedstat:
        result = []

        def __init__(self):
            pass

        def populationvar(self, list):
            self.result = populationvar(list)
            return self.result

        def samplevar(self, list):
            self.result = samplevar(list)
            return self.result

        def zscore_(self, z, list):
            self.result = zscore(z, list)
            return self.result

        def proportion_(self, list):
            self.result = proportion(list)
            return self.result

        def samplestdev(self, list):
            self.result = samplestdev(list)
            return self.result

        def samplemean(self, list):
            self.result = samplemean(list)
            return self.result

        def population_correlation_coefficient_(self,a,b):
            self.result = population_correlation_coefficient(a,b)
            return self.result

        def pvalue_(self, a, b, c, d):
            self.result = pvalue(a, b, c, d)
            return self.result

        def Variance_of_population_proportion_(self, list):
            self.result = Variance_of_population_proportion(list)
            return self.result

        def Variance_of_sample_proportion(self,list):
            self.result = Variance_of_sample_proportion(list)
            return self.result

        def cintreval_(self, list):
            self.result = cintreval(list)
            return self.result

        def sample_(self,list ,num):
            self.result = Sample(list,num)
            return self.result


except ImportError as e:
    print("Extended Stat has Import Error -->", e)
except TypeError as e:
    print("Extended Stat has Type Error(Argument) -->", e)
except NameError as e:
    print("NameError",e)

# Variance of population proportion
# Variance of sample proportion
