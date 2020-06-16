import os
import pandas as pd
import math
import operator

BASE_path = os.path.abspath(os.pardir)
DATASET_PATH = os.path.join(BASE_path,'DataSet')
def readFile(file_name):
    df = pd.read_excel(open(os.path.join(DATASET_PATH,file_name), 'rb'),header = None)
    return df 

def value(x):
    _max = x.max()
    _min = x.min()
    x = (x - _min) / (_max - _min)
    return x

def featureSacle(df):
    df = df.apply(lambda x:value(x))
    return df  

def priorProb(df):
    last_col = df.iloc[:,-1]
    unique   = last_col.unique()
    count   = last_col.count()
    prior_prob = {}
    for u in unique:
        cou  = last_col[last_col == u].shape[0]
        prior_prob[u] = cou / count
    return prior_prob

def meanAndvariance(df):
    df = df.groupby(df.iloc[:,-1])
    m = df.mean()
    v = df.var()
    return{'mean':m,'variance' :v}

def workForTraining():
    df           = readFile('parktraining.xlsx')
    df           = featureSacle(df)
    # print('FEATURE SCALE TRAINING DATA: ')
    # print(df)
    prior_prob   = priorProb(df)
    MeanVairance = meanAndvariance(df)
    return (prior_prob,MeanVairance)

def CalculateProb(classProb , testData,row_mean,row_variance):
    probabilty = 1
    pi = math.pi
    # print('CLASS PROB  :',classProb)
    # print('************************************************************')
            
    for value,mean,variance in zip(testData,row_mean,row_variance):
        # print('X : ',value)
        # print('MEAN : ',mean)
        # print('VARIANCE : ',variance)
        X = ((math.exp(-((value-mean)**2)/(2*variance)))/(math.sqrt(2*math.pi*variance)))
        # print('PROBAB : ',X)
        probabilty = probabilty * X
        # print('-----------------------------------------------------------')
            
    
    return probabilty*classProb 

def workForTesting(data):
    df           = readFile('parktesting.xlsx')
    df           = featureSacle(df)
    # print('FEATURE SCALE TEST DATA: ')
    # print(df)
    last_col     = df.iloc[:,-1]
    label        = list(last_col.unique())
    label.sort()
    df           = df.iloc[:,:-1]
    prior_prob   = data[0]
    mean = data[1]['mean']
    variance = data[1]['variance']
    testProb = {}
    cnt = 0
    for acctual, (index, rowData) in zip(last_col,df.iterrows()) :
        for (index_mean, row_mean),(index_variance,row_variance) in zip(mean.iterrows() , variance.iterrows()) :
            # print('INDEX ' ,index)
            prob = CalculateProb(prior_prob[index_mean],rowData , row_mean  , row_variance)
            # print('FINAL PROB', prob,'OF CLASS: ',index_mean)
            # print('************************************************************')
            testProb[index_mean] = prob
        _sum = sum(testProb.values())
        for key,value in testProb.items():
            testProb[key] = value / _sum 
        answer = max(testProb.items(), key=operator.itemgetter(1))[0]
        print('INDEX',index,'\t','ACCTUAL : ',acctual,'\t','PREDICTED:',answer,'\t','PROBABLITY : ',testProb,'\t','SUM : ',sum(testProb.values()) )
        if acctual-answer == 0:
            cnt  = cnt + 1
        testProb = {}
    return (cnt/len(df))*100
    
if __name__ == "__main__":
   data = workForTraining()
   
   prior_prob   = data[0]
   mean = data[1]['mean']
   variance = data[1]['variance']
    
   Accuracy = workForTesting(data)

   print('MEAN : ','\n',mean)
   print('VARIANCE : ','\n',variance)
   print('PRIOR PROB : ',prior_prob) 
   print('ACCURACY : ',Accuracy,' %')

