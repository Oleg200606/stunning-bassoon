import pandas as pd


df = pd.read_csv('/Users/oleg/Desktop/Питон практос/netflix_titles.csv')


dr = df.drop_duplicates()


print("Исходный размер датасета:", df.shape)
print("Размер датасета после удаления дубликатов:", dr.shape)


print("Наименования колонок:", df.columns.tolist())


for column in df.columns:
    print(f"Уникальные значения для {column}:", df[column].nunique())


df.info()


df.describe(include='all')


sorted_df = dr.sort_values(by='release_year', ascending=False)


reduced_df = sorted_df.drop(columns=['show_id'])


cleaned_df = reduced_df.fillna({'country': 'Unknown'})


sampled_data = cleaned_df.loc[:9, ['title', 'release_year']]


print(sampled_data)


newDataset = '/Users/oleg/Desktop/Питон практос/netflix_titles2.csv'
cleaned_df.to_csv(newDataset, index=False)
