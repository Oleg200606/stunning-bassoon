import pandas as pd

# Чтение датасета
df = pd.read_csv('/Users/oleg/Desktop/Питон практос/netflix_titles.csv')

#Проверка на совпадения и их удаление
dr = df.drop_duplicates()

#Вывод информации о датасете
print("Исходный размер датасета:", df.shape)
print("Размер датасета после удаления дубликатов:", dr.shape)

# Вывод наименований колонок
print("Наименования колонок:", df.columns.tolist())

# Вывод уникальных значений для каждой колонки
for column in df.columns:
    print(f"Уникальные значения для {column}:", df[column].nunique())

# Отображение информации о датасете
df.info()

# Отображение статистического описания датасета
df.describe(include='all')

# Отсортировать датасет по определенным параметрам 
sorted_df = dr.sort_values(by='release_year', ascending=False)

#Удаление ненужных столбцов
reduced_df = sorted_df.drop(columns=['show_id'])

# Замена пустых значений 
cleaned_df = reduced_df.fillna({'country': 'Unknown'})

#Выборка данных  в моём случае первых 10
sampled_data = cleaned_df.loc[:9, ['title', 'release_year']]

# Вывод примера выборки
print(sampled_data)

#Сохранение нового датасета
newDataset = '/Users/oleg/Desktop/Питон практос/netflix_titles2.csv'
cleaned_df.to_csv(newDataset, index=False)
