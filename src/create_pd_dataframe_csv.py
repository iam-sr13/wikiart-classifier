import pickle
import pandas as pd
from image_scraper import *
from multiprocessing import Pool


def save_csv(file_name, N_rows=None, file_url_list='artworks_urls_full.pkl'):
    """Downloads all the metadata in the pickled url list and saves to csv.

    Arguments:
        file_name: name of the csv file in which data would be saved
        N_rows: number of urls to download, by default downloads all of them
        url_list: picked file. Each line is one that will be downloaded

    Returns:
        None

    Examples:
        For N_rows=2, this function saves the file with following entry
        ,_id,title,artistname,image,year,style,genre,file_name
        0,5772847bedc2cb3880fded05,self-portrait,hans von aachen,https://uploads4.wikiart.org/images/hans-von-aachen/self-portrait-1574.jpg,1574,mannerism (late renaissance),self-portrait,self-portrait-1574.jpg!Large.jpg
        1,5772847bedc2cb3880fded75,two laughing men (double self-portrait),hans von aachen,https://uploads1.wikiart.org/images/hans-von-aachen/two-laughing-men-double-self-portrait-1574.jpg,1574,mannerism (late renaissance),self-portrait,two-laughing-men-double-self-portrait-1574.jpg!Large.jpg


    Todo:
        1. It should ignore the urls which give error and move on to the other urls in the list.
    """

    with open('../data/'+file_url_list, 'rb') as f:
        if N_rows is None:
            url_list = pickle.load(f)
        else:
            url_list = pickle.load(f)[:N_rows]

    pool = Pool(processes=4)
    list_data = pool.map(get_meta_data, url_list)

    pd.DataFrame(list_data).to_csv("database.csv",index=False)


if __name__ == '__main__':
    save_csv("database.csv",100)