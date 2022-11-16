import plotly.graph_objects as go
import pandas as pd
import requests
from bs4 import BeautifulSoup
import collections
import yfinance as yf

collections.Callable = collections.abc.Callable

CompanyTickerFromUserInput = input("Enter company ticker you want analyze:")


def DisplayTitle():
    PrintSeparator()
    print("Welcome in app Altalite! \n"
          "Choose program which area of company you are interested in and I will analyze it for you")
    PrintSeparator()


def PrintSeparator():
    print("---------------------------------------------------------------------------------")


def start():
    DisplayTitle()
    program = [
        "BASIC_INFORMATION",
        "RATIO_VALUATION",
        "DIVIDEND",
        "MODEL_VALUTAION",
        "GROWTH",
        "LIABILITIES",
        "PROFITABILITY",
        "RETURN",
        "FORECAST",
        "SHAREHOLDERS",
        "CHART",
        "RECOMMENDATIONS",
        "CRITERIA"
    ]
    for i, index in enumerate(program):
        print(i + 1, ".", index)

    PrintSeparator()
    x = input("Choose_program:").upper()

    if x == "BASIC_INFORMATION" or 1:
        return BASIC_INFORMATION(), end()
    elif x == "RATIO_VALUATION" or 2:
        return RATIO_VALUATION(), end()
    elif x == "DIVIDEND" or 3:
        return DIVIDEND(), end()
    elif x == "MODEL_VALUATION" or 4:
        return MODEL_VALUTAION(), end()
    elif x == "GROWTH" or 5:
        return GROWTH(), end()
    elif x == "LIABILITIES" or 6:
        return LIABILITIES(), end()
    elif x == "PROFITABILITY" or 7:
        return PROFITABILITY(), end()
    elif x == "RETURN" or 8:
        return RETURN(), end()
    elif x == "FORECAST" or 9:
        return FORECAST(), end()
    elif x == "SHAREHOLDERS" or 10:
        return SHAREHOLDERS(), end()
    elif x == "CHART" or 11:
        return CHART(), end()
    elif x == "RECOMMENDATIONS" or 12:
        return RECOMMENDATIONS(), end()
    elif x == "CRITERIA" or 13:
        return CRITERIA(), end()


def BASIC_INFORMATION():
    PrintSeparator()
    # -----
    CompanyName = yf.Ticker(CompanyTickerFromUserInput).info['shortName']
    print("Name:", CompanyName)
    # ------
    Sector = yf.Ticker(CompanyTickerFromUserInput).info['sector']
    print("SECTOR:", Sector)
    # -----
    INDUSTRY = yf.Ticker(CompanyTickerFromUserInput).info['industry']
    print("INDUSTRY:", INDUSTRY)
    # -----
    MarketCap = yf.Ticker(CompanyTickerFromUserInput).info['marketCap']
    print("MARKET_CAP:", MarketCap)
    # -----
    CurrentPrice = yf.Ticker(CompanyTickerFromUserInput).info['currentPrice']
    print("CurrentPrice_USD:", CurrentPrice)


def RATIO_VALUATION():
    PrintSeparator()
    TrailingPE = yf.Ticker(CompanyTickerFromUserInput).info['trailingPE']
    if TrailingPE is None:
        print("Price_to_earnings:", "[COMPANY HAVE NEGATIVE PRICE_TO_EARNINGS RATIO]")
    elif round(TrailingPE, 2) > 20:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_OVERVALUED]")
    elif round(TrailingPE, 2) == 20:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_FAIRVALUED]")
    elif round(TrailingPE, 2) < 10:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_UNDERVALUED]")

    PriceToBook = yf.Ticker(CompanyTickerFromUserInput).info['priceToBook']
    if PriceToBook is None:
        print("PRICE_TO_BOOK:", "[COMPANY HAVE NEGATIVE PRICE_TO_BOOK RATIO]")
    elif round(PriceToBook, 2) > 2:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_OVERVALUED]")
    elif round(PriceToBook, 2) == 1:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_FAIRVALUED]")
    elif round(PriceToBook, 2) < 1:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_UNDERVALUED]")

    EV_EBITDA = yf.Ticker(CompanyTickerFromUserInput).info['enterpriseToEbitda']  # ENTERPRISE VALUE TO EBITDA
    if EV_EBITDA is None:
        print("EV_EBITDA:", "[COMPANY HAVE NEGATIVE EV_EBITDA RATIO]")
    elif round(EV_EBITDA, 2) > 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_OVERVALUED]")
    elif round(EV_EBITDA, 2) == 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_FAIRVALUED]")
    elif round(EV_EBITDA, 2) < 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_UNDERVALUED]")


def DIVIDEND():
    PrintSeparator()
    DividendYield = yf.Ticker(CompanyTickerFromUserInput).info['dividendYield']
    if DividendYield is None:
        print("COMPANY DON'T PAY DIVIDEND:", "[NONE]")
    elif 0.0500 >= round(DividendYield, 4) >= 0.0200:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[SECURE_DIVIDEND_YIELD_LEVEL]")
    elif round(DividendYield, 4) < 0.0190:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[LOW_YIELD_DIVIDEND]")
    elif round(DividendYield, 4) >= 0.0600:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[HIGH_YIELD_CHECK_SECURITY]")

    AVERAGE_5Y_DIV = yf.Ticker(CompanyTickerFromUserInput).info['fiveYearAvgDividendYield']
    if AVERAGE_5Y_DIV is None:
        print("AVERAGE_5y_DIVIDEND_YIELD:", "[The company has a shorter dividend record or will not pay it out]")
    elif round(AVERAGE_5Y_DIV, 2) >= 0.01:
        print("AVERAGE_5y_DIVIDEND_YIELD:", round(AVERAGE_5Y_DIV, 2), "%")

    PayoutRatio = yf.Ticker(CompanyTickerFromUserInput).info['payoutRatio']
    if PayoutRatio is None:
        print("COMPANY_DON'T_PAYOUT_EARNINGS:", "[NONE]")
    elif round(PayoutRatio, 6) <= 0.19:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT SMALL AMOUNT OF EARNINGS]")
    elif round(PayoutRatio, 2) > 0.60:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT HUGE AMOUNT OF EARNINGS]")
    elif 0.20 <= round(PayoutRatio, 2) <= 0.59:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT SECURE AMOUNT OF EARNINGS]")


def MODEL_VALUTAION():
    PrintSeparator()
    PEG_RATIO = yf.Ticker(CompanyTickerFromUserInput).info['pegRatio']
    if round(PEG_RATIO, 2) > 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_OVERVALUED]")
    elif round(PEG_RATIO, 2) == 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_FAIRVALUED]")
    elif round(PEG_RATIO, 2) < 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_UNDERVALUED]")

    soup = BeautifulSoup(requests.get("https://fred.stlouisfed.org/series/AAA").text, 'lxml')  # Web scrapping
    strona = soup.find('span', class_='series-meta-observation-value').get_text()
    hom = float(strona)
    graham = (round(yf.Ticker(CompanyTickerFromUserInput).info['trailingEps'], 2) *
              (8.5 + (2 * round(yf.Ticker(CompanyTickerFromUserInput).info['earningsGrowth'], 2))) * 4.4) / hom
    graham1 = round(yf.Ticker(CompanyTickerFromUserInput).info['currentPrice'], 2) / round(graham, 2)
    gh = round(graham1, 2)
    if gh == 1:
        print("GRAHAM_MODEL:", gh, "[COMPANY_FAIRVALUED]")
    elif 1.1 < gh < 1.5:
        print("GRAHAM_MODEL:", gh, "[COMPANY_SECURE]")
    elif gh > 1.5:
        print("GRAHAM_MODEL:", gh, "[COMPANY_OVERVALUED]")
    elif gh < 1:
        print("GRAHAM_MODEL:", gh, "[COMPANY_UNDERVALUED]")


# Todo
# DDM Model
# DCF Model
# FCF Model


def GROWTH():
    PrintSeparator()
    RevenueGrowth = yf.Ticker(CompanyTickerFromUserInput).info['revenueGrowth']
    print("RevenueGrowth:", (round(RevenueGrowth, 2) * 100), "%")
    EarningsGrowth = yf.Ticker(CompanyTickerFromUserInput).info['earningsGrowth']
    print("EarningsGrowth:", (round(EarningsGrowth, 2) * 100), "%")


# Todo
# CAGR
# start = float(input('Start Value: '))
# end = float(input('End Value: '))
# periods = float(input('How many years from beginning to the end: '))
# def CAGR(start, end, periods):
#    return (end / start) ** (1 / periods) - 1
# print('Your investment had a CAGR of {:.2%} '.format(CAGR(start, end, periods)))


# GROWTH RATE EBITDA, DIVIDEND, DEBT  #pandas data frame


# noinspection PyUnresolvedReferences
def LIABILITIES():
    PrintSeparator()
    Current_Ratio = yf.Ticker(CompanyTickerFromUserInput).info['currentRatio']
    if round(Current_Ratio, 2) >= 2.00:
        print("Current_Ratio:", round(Current_Ratio, 2), "[THE COMPANY DOES BAD MANAGEMENT OF THE CAPITAL]")
    elif round(Current_Ratio, 2) <= 1.00:
        print("Current_Ratio:", round(Current_Ratio, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")
    else:
        print("Current_Ratio:", round(Current_Ratio, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")

    QuickRatio = yf.Ticker(CompanyTickerFromUserInput).info['quickRatio']
    if QuickRatio is None:
        print("Quick_Ratio:", "[None data]")
    elif round(QuickRatio, 2) >= 1:
        print("Quick_Ratio:", round(QuickRatio, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")
    elif round(QuickRatio, 2) <= 1:
        print("Quick_Ratio:", round(QuickRatio, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")

    DebtToEquity = yf.Ticker(CompanyTickerFromUserInput).info['debtToEquity']
    if DebtToEquity is None:
        print("Debt_To_Equity:", "[None data]")
    elif 1 <= round(DebtToEquity, 2) < 150.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")
    elif round(DebtToEquity, 2) >= 100.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")
    elif round(DebtToEquity, 2) < 100.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")


def PROFITABILITY():
    PrintSeparator()
    ROE = yf.Ticker(CompanyTickerFromUserInput).info['returnOnEquity']  #
    if 0.10 <= round(ROE, 2) <= 0.15:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_HEALTHY]")
    elif round(ROE, 2) >= 0.20:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_HIGH]")
    elif round(ROE, 2) <= 0.09:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_LOW]")

    ROA = yf.Ticker(CompanyTickerFromUserInput).info['returnOnAssets']
    if 0.05 <= round(ROA, 2) <= 0.19:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_HEALTHY]")
    elif round(ROA, 2) >= 0.20:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_HIGH]")
    elif round(ROA, 2) <= 0.04:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_LOW]")

    GrossMargins = yf.Ticker(CompanyTickerFromUserInput).info['grossMargins']
    if 0.50 <= round(GrossMargins, 2) <= 0.70:
        print("GrossMargins:", round(GrossMargins, 2), "[GOOD_LEVEL_GROSS_MARGIN]")
    elif 0.10 <= round(GrossMargins, 2) <= 0.50:
        print("GrossMargins:", round(GrossMargins, 2), "[HEALTHY_GROSS_MARGIN]")
    elif round(GrossMargins, 2) >= 0.71:
        print("GrossMargins:", round(GrossMargins, 2), "[HIGH_LEVEL_GROSS_MARGIN]")
    elif round(GrossMargins, 2) <= 0.09:
        print("GrossMargins:", round(GrossMargins, 2), "[LOW_LEVEL_GROSS_MARGIN]")

    OperatingMargins = yf.Ticker(CompanyTickerFromUserInput).info['operatingMargins']
    if 0.14 <= round(OperatingMargins, 2) <= 0.20:
        print("OperatingMargins:", round(OperatingMargins, 2), "[GOOD_LEVEL_OPERATING_MARGIN]")
    elif 0.10 <= round(OperatingMargins, 2) <= 0.13:
        print("OperatingMargins:", round(OperatingMargins, 2), "[HEALTHY_LEVEL_OPERATING_MARGIN]")
    elif round(OperatingMargins, 2) >= 0.21:
        print("OperatingMargins:", round(OperatingMargins, 2), "[HIGH_LEVEL_OPERATING_MARGIN]")
    elif round(OperatingMargins, 2) <= 0.09:
        print("OperatingMargins:", round(OperatingMargins, 2), "[LOW_LEVEL_OPERATING_MARGIN]")

    ProfitMargins = yf.Ticker(CompanyTickerFromUserInput).info['profitMargins']
    if 0.14 <= round(ProfitMargins, 2) <= 0.20:
        print("ProfitMargins:", round(ProfitMargins, 2), "[GOOD_LEVEL_PROFIT_MARGINS]")
    elif 0.10 <= round(ProfitMargins, 2) <= 0.13:
        print("ProfitMargins:", round(ProfitMargins, 2), "[HEALTHY_LEVEL_PROFIT_MARGINS]")
    elif round(ProfitMargins, 2) >= 0.21:
        print("ProfitMargins:", round(ProfitMargins, 2), "[HIGH_LEVEL_PROFIT_MARGINS]")
    elif round(ProfitMargins, 2) <= 0.09:
        print("ProfitMargins:", round(ProfitMargins, 2), "[LOW_LEVEL_PROFIT_MARGINS]")


def RETURN():
    PrintSeparator()
    # -----
    ytdReturn = yf.Ticker(CompanyTickerFromUserInput).info['ytdReturn']  # Return from the beginning of the year
    print("Year_to_date_Return:", ytdReturn)
    # -----
    FiveYearAverageReturn = yf.Ticker(CompanyTickerFromUserInput).info['fiveYearAverageReturn']
    print("RETURN_FROM_LATEST_5_Years_AVG_ANNUAL:", FiveYearAverageReturn)
    # -----


def FORECAST():
    PrintSeparator()
    # Todo
    # Forecast with ML/AI model
    pass


def SHAREHOLDERS():
    PrintSeparator()
    _shareholders = yf.Ticker(CompanyTickerFromUserInput).institutional_holders
    print(_shareholders)


def RECOMMENDATIONS():
    PrintSeparator()
    TargetPrice = yf.Ticker(CompanyTickerFromUserInput).info['targetMeanPrice']
    jk = round(yf.Ticker(CompanyTickerFromUserInput).info['currentPrice'] / TargetPrice, 2)
    print("AVG_PRICE_TARGET:", TargetPrice, )
    price = yf.Ticker(CompanyTickerFromUserInput).info['currentPrice']
    print("Price:", price)
    print("CURRENT PRICE / AVERAGE_TARGET_PRICE_ANALITICS: ", jk, " TO_TARGET_PRICE: ", round((1 - jk) * 100, 2),
          "%")
    recommendations = yf.Ticker(CompanyTickerFromUserInput).recommendations
    print("Recommendations:", recommendations)


def CHART():
    _chart = yf.Ticker(CompanyTickerFromUserInput)
    hist = _chart.history(period='5y')
    hist.head()
    fig = go.Figure(data=go.Scatter(x=hist.index, y=hist['Close'], mode='lines'))
    fig.show()


def end():
    PrintSeparator()
    xx = input("If you want to check another function, write yes, if not write no:", ).upper()
    if xx == "YES":
        return start()
    elif xx == "NO":
        print("See you later!")
    else:
        print("Something is wrong")


def CRITERIA():
    PrintSeparator()
    payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    first_table = payload[0]
    df = first_table
    df.head()
    symbols = df['Symbol'].values.tolist()

    for ticker in symbols:
        if yf.Ticker(ticker).info['earningsGrowth'] >= 1 \
                and yf.Ticker(ticker).info['returnOnEquity'] >= 1 \
                and yf.Ticker(ticker).info['debtToEquity'] < 100.0000 \
                and yf.Ticker(ticker).info['operatingMargins'] > 0.2100 \
                and yf.Ticker(ticker).info['payoutRatio'] < 0.6000 \
                and yf.Ticker(ticker).info['dividendYield'] > 0.0300:
            print(yf.Ticker(ticker).info['shortName'])
        else:
            pass


def ValuePoints():
    # Todo
    pass


start()
# Todo
# Frontend in JS or Django
