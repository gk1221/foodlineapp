import pygsheets


class Showgoosheet():
    def __init__(self):
        self.gc = pygsheets.authorize(service_account_file='client_secret.json')
        self.sht = self.gc.open_by_url(
            'https://docs.google.com/spreadsheets/d/1NwDQFagKUfw8xPI3oxR92LeIjv_11gtcjSXCgLQiTWg/edit?usp=sharing'
        )

    def select(self):
        wks = self.sht.worksheet_by_title('demo')
        df2 = wks.get_as_df(has_header=True, start='A1', index_colum=0, empty_value='',
                            include_tailing_empty=False)  # index 從 1 開始算

        #df2.to_csv('data/data.csv')
        dflist = [df2.iloc[i].values for i in range(len(df2))]
        return dflist
