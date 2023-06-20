from math import ceil, floor


class StockEarn():
    def __init__(self, buyprice, sellprice, count, trade):
        self.buyprice = int(buyprice)
        self.sellprice = int(sellprice)
        self.count = int(count)

        self.trade = trade

    def countearn(self):
        hand_tax = 0.001425*0.6
        if self.trade == "現貨":
            tax = 0.003
        else:
            tax = 0.0015

        buy_cost = self.buyprice * self.count   # 整張
        sell_cost = self.sellprice * self.count
        hand_cost = floor(buy_cost * hand_tax) + \
            floor(sell_cost * hand_tax)  # 手續費
        tax_cost = floor(sell_cost * tax)  # 交易稅
        earn = sell_cost - buy_cost - hand_cost - tax_cost
        per = earn / buy_cost * 100
        ans = "獲利:  {} \n%:  {}% \n手續費: {}+{}".format(
            str(earn),
            str(round(per, 2)),
            str(hand_cost),
            str(tax_cost)
        )

        return ans
