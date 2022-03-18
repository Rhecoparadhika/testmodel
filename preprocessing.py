import numpy as np

def outlier(data, features):

  outlier = data.copy()

  for i in features:
    
    Q1 = np.percentile(outlier[i], 25, interpolation = 'midpoint')
    Q2 = np.percentile(outlier[i], 50, interpolation = 'midpoint')  
    Q3 = np.percentile(outlier[i], 75, interpolation = 'midpoint')

    IQR = Q3 - Q1
    low_lim = Q1 - 1.5 * IQR
    up_lim = Q3 + 1.5 * IQR

    outlier[i].clip(low_lim, up_lim, inplace=True)

  return outlier

def imput_missing(train):
  cateogry_columns = train.select_dtypes(include=['object']).columns.tolist()

  for column in train:
      if train[column].isnull().any():
          if(column in cateogry_columns):
              train[column] = train[column].fillna(train[column].mode()[0])
          else:
              train[column] = train[column].fillna(train[column].median())

  return train