try:
    import unittest
    from CSVreader.csvreader import csvreader
    from Statisticss.extendedstat import extendedstat


    class MyTestCase(unittest.TestCase):


        def setUp(self) -> None:
            self.extendedstat = extendedstat()


        def test_zscore(self):

                test_data = csvreader('Tests/csvdata/Array3.csv').data
                test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

                for column in test_result:
                    result_test = float(column['zscore'])
                    z = float(column['zvalue4zscore'])

                listx = []


                for row in test_data:
                    result = float(row['Array'])
                    listx.append(result)


                self.assertEqual(round(self.extendedstat.zscore_(z,listx)), round(result_test))


        def test_samplevar(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['samplevar'])


            listx = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)


            self.assertEqual(round(self.extendedstat.samplevar(listx)), round(result_test))

        def test_proportion(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['proportion'])

            listx = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)


            self.assertEqual(round(self.extendedstat.proportion_(listx)), round(result_test))

        def test_populationvar(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['populationvar'])


            listx = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)


            self.assertEqual(round(self.extendedstat.populationvar(listx)), round(result_test))

        # def test_samplemean(self):
        #
        #     test_data = csvreader('Tests/csvdata/Array3.csv').data
        #     test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        #
        #     for column in test_result:
        #         result_test = float(column['samplemean'])
        #
        #     listx = []
        #
        #     for row in test_data:
        #         result = float(row['Array'])
        #         listx.append(result)
        #
        #
        #     self.assertEqual(round(self.extendedstat.samplemean(listx)), round(result_test))

        def test_population_correlation_coefficient(self):
            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['population_correlation_coefficient'])

            listx = []
            listy = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)
                result2 = float(row['Array2'])
                listy.append(result2)

            self.assertAlmostEqual(float(self.extendedstat.population_correlation_coefficient_(listx,listy)), float(result_test))

        def test_pvalue(self):

            test_data = csvreader('Tests/csvdata/UnitArgument.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['pvalue'])

            for column in test_data:
                a = float(column['a'])
                b = float(column['b'])
                c = float(column['c'])
                d = float(column['d'])

            self.assertAlmostEqual(self.extendedstat.pvalue_(a,b,c,d), result_test)

        # def test_samplestdev(self):
        #
        #     test_data = csvreader('Tests/csvdata/Array3.csv').data
        #     test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        #
        #     for column in test_result:
        #         result_test = float(column['samplestdev'])
        #
        #     listx = []
        #
        #     for row in test_data:
        #         result = float(row['Array'])
        #         listx.append(result)
        #
        #     self.assertAlmostEqual(self.extendedstat.samplestdev(listx),result_test)

        def test_Variance_of_population_proportion(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test = float(column['Variance_of_population_proportion'])

            listx = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)

            self.assertAlmostEqual(self.extendedstat.Variance_of_population_proportion_(listx), result_test)

        # def test_Variance_of_sample_proportion(self):
        #
        #     test_data = csvreader('Tests/csvdata/Array3.csv').data
        #     test_result = csvreader('Tests/csvdata/Array3_result2.csv').data
        #
        #     for column in test_result:
        #         result_test = float(column['Variance_of_sample_proportion'])
        #
        #     listx = []
        #
        #     for row in test_data:
        #         result = float(row['Array'])
        #         listx.append(result)
        #
        #     self.assertAlmostEqual(self.extendedstat.Variance_of_sample_proportion(listx), result_test)

        def test_cinterval(self):

            test_data = csvreader('Tests/csvdata/Array3.csv').data
            test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            for column in test_result:
                result_test1 = float(column['cintreval1'])
                result_test2 = float(column['cintreval2'])

            listx = x = []

            for row in test_data:
                result = float(row['Array'])
                listx.append(result)
            x = self.extendedstat.cintreval_(listx)

            try:
                self.assertAlmostEqual(x[0], result_test1)
                self.assertAlmostEqual(x[1], result_test2)
            except AssertionError as e:
                print("Cintreval has AsserstionError:", e)
                assert 0

        def test_sample(self):
            test_data = csvreader('Tests/csvdata/Array3.csv').data
            #test_result = csvreader('Tests/csvdata/Array3_result2.csv').data

            listx = []
            #since this not a sudo random number genrator we can predict the lenght!
            for row in test_data:
                result = float(row['Array'])
                listx.append(result)
                self.extendedstat.sample_(listx,50)
            self.assertEqual(len(listx),309)


except IndentationError as e :
    print("Indentation Error in Extended Stat:", e)
except ImportError as e :
    print("Import Error in Extended Stat:", e)
except Exception as e :
    print("Any Other Kind of Exception:", e)
except AttributeError as e :
    print("Attribute Error", e)

