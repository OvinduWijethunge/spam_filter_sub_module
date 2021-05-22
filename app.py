import pandas as pd
import pickle
from youtubeData_v3 import download_comments_and_content
from comments_downlod_to_hate_module import get_ham_comments
from dataframe_modify import data_modification
model = pickle.load(open('gboostv4.pkl', 'rb'))
if __name__ == "__main__":

    videoId = input('Enter Video id : ') #tD0K9cUd2ys  PrCSvG8gCFg
    download_comments_and_content(str(videoId))
    df = pd.read_csv('data.csv')
    data_frame = data_modification(df)
    prediction = model.predict(data_frame.values.tolist())
    print(prediction)
    prediction_series = pd.Series(prediction)
    df1 = pd.concat([df,prediction_series], axis=1)
    df1 = df1.rename(columns={0: 'is_spam'})
    id_group = df1.groupby(['is_spam'])
    spam_group = id_group.get_group(1)
    ham_group = id_group.get_group(0)
    spam_list = spam_group['cid'].tolist()
    ham_list = ham_group['cid'].tolist()
    total_comments = len(prediction_series)
    spam_commnets = len(spam_list)
    spam_presentage = (spam_commnets/total_comments)*100
    print('spam precentage is {}'.format(spam_presentage))
    # make a dataframe without spam commnets
    df_comments = pd.read_excel('comments.xlsx')
    index_names = (df_comments[ df_comments['comment_id'].isin(spam_list) ].index).tolist()
    df_ham_comments = df_comments.drop(index_names) # legitimate comments dataframe for next step.....
    print("----------------")
    print(df_ham_comments)
    get_ham_comments(videoId,spam_list)
    

