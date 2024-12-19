import pandas as pd

from parser import parse
from images_module import add_columns, filter_images, create_histogram


def main():
    args = parse()
    try:
        df = pd.read_csv(args.csv_path, sep='\t')
        print("DataFrame из csv:")
        print(df)

        print("\nдобавление колонок размера и глубины")
        add_columns(df)
        print(df)

        print("\nСтатистическа для столбцов размеров:")
        stats = df[['height', 'width', 'depth']].describe()
        print(stats)
        
        filtered_df = filter_images(df, args.max_height, args.max_width)
        print("\nОтфильтрованный DataFrame:")
        print(filtered_df)


        print("\nДобавление area")
        df['area'] = df['height'] * df['width']
        print(df)

        print("\nСортировка данных по площади изображения")
        df_sorted = df.sort_values(by='area')
        print(df_sorted)

        create_histogram(df)

    except Exception as error:
        print(f"Произошла ошибка: {error}")


if __name__ == "__main__":
    main()