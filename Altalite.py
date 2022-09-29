import plotly.graph_objects as go
import pandas as pd
import requests
from bs4 import BeautifulSoup
import collections
import yfinance as yf

collections.Callable = collections.abc.Callable

print("---------------------------------------------------------------------------------")
print("Welcome in app Altalite!\n"
      "Enter below the ticker of the company you are interested in and I will analyze it for you")
print("---------------------------------------------------------------------------------")

CompanyTicker = input("Enter company ticker:")


def start():
    program = [
        "1.BASIC_INFORMATION",
        "3.RATIO_VALUATION",
        "4.DIVIDEND",
        "5.MODEL_VALUTAION",
        "6.GROWTH",
        "7.LIABILITIES",
        "8.PROFITABILITY",
        "9.RETURN",
        "10.FORECAST",
        "11.SHAREHOLDERS",
        "12.CHART",
        "13.RECOMMENDATIONS",
        "14.CRYTERIA"
    ]
    for i in program:
        print(i)
    print("---------------------------------------------------------------------------------")
    x = input("Choose_program:").upper()
    print("---------------------------------------------------------------------------------")

    if x == "BASIC_INFORMATION":
        return BASIC_INFORMATION(), end()
    elif x == "RATIO_VALUATION":
        return RATIO_VALUATION(), end()
    elif x == "DIVIDEND":
        return DIVIDEND(), end()
    elif x == "MODEL_VALUTAION":
        return MODEL_VALUTAION(), end()
    elif x == "GROWTH":
        return GROWTH(), end()
    elif x == "LIABILITIES":
        return LIABILITIES(), end()
    elif x == "PROFITABILITY":
        return PROFITABILITY(), end()
    elif x == "RETURN":
        return RETURN(), end()
    elif x == "FORECAST":
        return FORECAST(), end()
    elif x == "SHAREHOLDERS":
        return SHAREHOLDERS(), end()
    elif x == "CHART":
        return CHART(), end()
    elif x == "RECOMMENDATIONS":
        return RECOMMENDATIONS(), end()
    elif x == "CRYTERIA":
        return CRYTERIA(), end()


def BASIC_INFORMATION():
    print("-------------")
    print("BASIC_INFORMATION")
    print("-------------")
    # -----
    CompanyName = yf.Ticker(CompanyTicker).info['shortName']
    print("Name:", CompanyName)
    # ------
    Sector = yf.Ticker(CompanyTicker).info['sector']
    print("SECTOR:", Sector)
    # -----
    INDUSTRY = yf.Ticker(CompanyTicker).info['industry']
    print("INDUSTRY:", INDUSTRY)
    # -----
    MarketCap = yf.Ticker(CompanyTicker).info['marketCap']
    print("MARKET_CAP:", MarketCap)
    # -----
    CurrentPrice = yf.Ticker(CompanyTicker).info['currentPrice']
    print("CurrentPrice_USD:", CurrentPrice)


def RATIO_VALUATION():
    print("-------------")
    print("RATIO_VALUATION")
    print("-------------")

    TrailingPE = yf.Ticker(CompanyTicker).info['trailingPE']
    if round(TrailingPE, 2) > 20:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_OVERVALUED]")
    elif round(TrailingPE, 2) == 20:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_FAIRVALUED]")
    elif round(TrailingPE, 2) < 10:
        print("Price_to_earnings:", round(TrailingPE, 2), "[COMPANY_UNDERVALUED]")

    PriceToBook = yf.Ticker(CompanyTicker).info['priceToBook']
    if PriceToBook is None:
        print("PRICE_TO_BOOK:", "[COMPANY HAVE NEGATIVE PRICE_TO_BOOK RATIO]")
    elif round(PriceToBook, 2) > 2:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_OVERVALUED]")
    elif round(PriceToBook, 2) == 1:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_FAIRVALUED]")
    elif round(PriceToBook, 2) < 1:
        print("PRICE_TO_BOOK:", round(PriceToBook, 2), "[COMPANY_UNDERVALUED]")

    EV_EBITDA = yf.Ticker(CompanyTicker).info['enterpriseToEbitda']  # ENTERPRISE VALUE TO EBITDA
    if round(EV_EBITDA, 2) > 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_OVERVALUED]")
    elif round(EV_EBITDA, 2) == 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_FAIRVALUED]")
    elif round(EV_EBITDA, 2) < 12:
        print("EV_EBITDA:", round(EV_EBITDA, 2), "[COMPANY_UNDERVALUED]")


def DIVIDEND():
    print("-------------")
    print("DIVIDEND_DATA")
    print("-------------")
    DividendYield = yf.Ticker(CompanyTicker).info['dividendYield']
    if DividendYield is None:
        print("COMPANY DON'T PAY DIVIDEND:", "[NONE]")
    elif 0.0500 >= round(DividendYield, 4) >= 0.0200:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[SECURE_DIVIDEND_YIELD_LEVEL]")
    elif round(DividendYield, 4) < 0.0190:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[LOW_YIELD_DYWIDENDY]")
    elif round(DividendYield, 4) >= 0.0600:
        print("DIVIDEND_YIELD:", (round(DividendYield, 4) * 100), "[HIGH_YIELD_CHECK_SECURITY]")

    AVERAGE_5Y_DIV = yf.Ticker(CompanyTicker).info['fiveYearAvgDividendYield']
    if AVERAGE_5Y_DIV is None:
        print("AVERAGE_5y_DIVIDEND_YIELD:", "[The company has a shorter dividend record or will not pay it out]")
    elif round(AVERAGE_5Y_DIV, 2) >= 0.01:
        print("AVERAGE_5y_DIVIDEND_YIELD:", round(AVERAGE_5Y_DIV, 2), "%")

    PayoutRatio = yf.Ticker(CompanyTicker).info['payoutRatio']
    if PayoutRatio is None:
        print("COMPANY_DON'T_PAYOUT_EARNINGS:", "[NONE]")
    elif round(PayoutRatio, 6) <= 0.19:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT SMALL AMOUNT OF EARNINGS]")
    elif round(PayoutRatio, 2) > 0.60:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT HUGE AMOUNT OF EARNINGS]")
    elif 0.20 <= round(PayoutRatio, 2) <= 0.59:
        print("PayOutRATIO:", round(PayoutRatio, 2), "[COMPANY PAYOUT SECURE AMOUNT OF EARNINGS]")


def MODEL_VALUTAION():
    print("-------------")
    print("MODEL_VALUTAION")
    print("-------------")
    PEG_RATIO = yf.Ticker(CompanyTicker).info['pegRatio']
    if round(PEG_RATIO, 2) > 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_OVERVALUED]")
    elif round(PEG_RATIO, 2) == 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_FAIRVALUED]")
    elif round(PEG_RATIO, 2) < 1.00:
        print("PEG_RATIO:", round(PEG_RATIO, 2), "[COMPANY_UNDERVALUED]")

    soup = BeautifulSoup(requests.get("https://fred.stlouisfed.org/series/AAA").text, 'lxml')  # Web scrapping
    strona = soup.find('span', class_='series-meta-observation-value').get_text()
    hom = float(strona)
    graham = (round(yf.Ticker(CompanyTicker).info['trailingEps'], 2) *
              (8.5 + (2 * round(yf.Ticker(CompanyTicker).info['earningsGrowth'], 2))) * 4.4) / hom
    graham1 = round(yf.Ticker(CompanyTicker).info['currentPrice'], 2) / round(graham, 2)
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
    print("-------------")
    print("Growth")
    print("-------------")
    RevenueGrowth = yf.Ticker(CompanyTicker).info['revenueGrowth']
    print("RevenueGrowth:", (round(RevenueGrowth, 2) * 100), "%")
    EarningsGrowth = yf.Ticker(CompanyTicker).info['earningsGrowth']
    print("EarningsGrowth:", (round(EarningsGrowth, 2) * 100), "%")


# Todo
# GROWTH RATE EBITDA, DIVIDEND, DEBT  #pandas data frame


def LIABILITIES():
    print("-------------")
    print("DEBT_RATIO")
    print("-------------")
    Current_Ratio = yf.Ticker(CompanyTicker).info['currentRatio']
    if round(Current_Ratio, 2) >= 2.00:
        print("Current_Ratio:", round(Current_Ratio, 2), "[THE COMPANY DOES BAD MANAGEMENT OF THE CAPITAL]")
    elif round(Current_Ratio, 2) <= 1.00:
        print("Current_Ratio:", round(Current_Ratio, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")
    else:
        print("Current_Ratio:", round(Current_Ratio, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")

    QuickRatio = yf.Ticker(CompanyTicker).info['quickRatio']
    if QuickRatio is None:
        print("Quick_Ratio:", "[None data]")
    elif round(QuickRatio, 2) >= 1:
        print("Quick_Ratio:", round(QuickRatio, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")
    elif round(QuickRatio, 2) <= 1:
        print("Quick_Ratio:", round(QuickRatio, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")

    DebtToEquity = yf.Ticker(CompanyTicker).info['debtToEquity']
    if DebtToEquity is None:
        print("Debt_To_Equity:", "[Brak_danych]")
    elif 1 <= round(DebtToEquity, 2) < 150.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")
    elif round(DebtToEquity, 2) >= 100.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[COMPANY MAY HAVE PROBLEMS WITH LIQUIDITY]")
    elif round(DebtToEquity, 2) < 100.00:
        print("Debt_To_Equity:", round(DebtToEquity, 2), "[THE COMPANY DOES GOOD MANAGEMENT OF THE CAPITAL]")


def PROFITABILITY():
    print("-------------")
    print("PROFITABILITY_RATIO")
    print("-------------")
    ROE = yf.Ticker(CompanyTicker).info['returnOnEquity']  #
    if 0.10 <= round(ROE, 2) <= 0.15:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_HEALTHY]")
    elif round(ROE, 2) >= 0.20:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_HIGH]")
    elif round(ROE, 2) <= 0.09:
        print("ReturnOnEquity:", round(ROE, 2), "[ROE_IS_LOW]")

    ROA = yf.Ticker(CompanyTicker).info['returnOnAssets']
    if 0.05 <= round(ROA, 2) <= 0.19:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_HEALTHY]")
    elif round(ROA, 2) >= 0.20:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_HIGH]")
    elif round(ROA, 2) <= 0.04:
        print("ReturnOnAssets:", round(ROA, 2), "[ROA_IS_LOW]")

    GrossMargins = yf.Ticker(CompanyTicker).info['grossMargins']
    if 0.50 <= round(GrossMargins, 2) <= 0.70:
        print("GrossMargins:", round(GrossMargins, 2), "[GOOD_LEVEL_GROSS_MARGIN]")
    elif 0.10 <= round(GrossMargins, 2) <= 0.50:
        print("GrossMargins:", round(GrossMargins, 2), "[HEALTHY_GROSS_MARGIN]")
    elif round(GrossMargins, 2) >= 0.71:
        print("GrossMargins:", round(GrossMargins, 2), "[HIGH_LEVEL_GROSS_MARGIN]")
    elif round(GrossMargins, 2) <= 0.09:
        print("GrossMargins:", round(GrossMargins, 2), "[LOW_LEVEL_GROSS_MARGIN]")

    OperatingMargins = yf.Ticker(CompanyTicker).info['operatingMargins']
    if 0.14 <= round(OperatingMargins, 2) <= 0.20:
        print("OperatingMargins:", round(OperatingMargins, 2), "[GOOD_LEVEL_OPERATING_MARGIN]")
    elif 0.10 <= round(OperatingMargins, 2) <= 0.13:
        print("OperatingMargins:", round(OperatingMargins, 2), "[HEALTHY_LEVEL_OPERATING_MARGIN]")
    elif round(OperatingMargins, 2) >= 0.21:
        print("OperatingMargins:", round(OperatingMargins, 2), "[HIGH_LEVEL_OPERATING_MARGIN]")
    elif round(OperatingMargins, 2) <= 0.09:
        print("OperatingMargins:", round(OperatingMargins, 2), "[LOW_LEVEL_OPERATING_MARGIN]")

    ProfitMargins = yf.Ticker(CompanyTicker).info['profitMargins']
    if 0.14 <= round(ProfitMargins, 2) <= 0.20:
        print("ProfitMargins:", round(ProfitMargins, 2), "[GOOD_LEVEL_PROFIT_MARGINS]")
    elif 0.10 <= round(ProfitMargins, 2) <= 0.13:
        print("ProfitMargins:", round(ProfitMargins, 2), "[HEALTHY_LEVEL_PROFIT_MARGINS]")
    elif round(ProfitMargins, 2) >= 0.21:
        print("ProfitMargins:", round(ProfitMargins, 2), "[HIGH_LEVEL_PROFIT_MARGINS]")
    elif round(ProfitMargins, 2) <= 0.09:
        print("ProfitMargins:", round(ProfitMargins, 2), "[LOW_LEVEL_PROFIT_MARGINS]")


def RETURN():
    print("-------------")
    print("RETURN")
    print("-------------")
    # -----
    ytdReturn = yf.Ticker(CompanyTicker).info['ytdReturn']  # Return from the beginning of the year
    print("Year_to_date_Return:", ytdReturn)
    # -----
    FiveYearAverageReturn = yf.Ticker(CompanyTicker).info['fiveYearAverageReturn']
    print("RETURN_FROM_LATEST_5_Years_AVG_ANNUAL:", FiveYearAverageReturn)
    # -----


def FORECAST():
    # Todo
    # Forecast with ML/AI model
    pass


def SHAREHOLDERS():
    print("-----------------------------------------")
    print("SHAREHOLDERS")
    print("------------------------------------------------------------------")
    SHAREHOLDERS = yf.Ticker(CompanyTicker).institutional_holders
    print(SHAREHOLDERS)


def RECOMMENDATIONS():
    TargetPrice = yf.Ticker(CompanyTicker).info['targetMeanPrice']
    jk = round(yf.Ticker(CompanyTicker).info['currentPrice'] / TargetPrice, 2)
    print("AVG_PRICE_TARGET:", TargetPrice, )
    price = yf.Ticker(CompanyTicker).info['currentPrice']
    print("Price:", price)
    print("CURRENT PRICE / AVERAGE_TARGET_PRICE_ANALITICS: ", jk, " TO_TARGET_PRICE: ", round((1 - jk) * 100, 2),
          "%")
    recommendations = yf.Ticker(CompanyTicker).recommendations
    print("Recommendations:", recommendations)


def CHART():
    CHART = yf.Ticker(CompanyTicker)
    hist = CHART.history(period='5y')
    hist.head()
    fig = go.Figure(data=go.Scatter(x=hist.index, y=hist['Close'], mode='lines'))
    fig.show()


def end():
    xx = input("If you want to check another function, write yes, if not write no:", ).upper()
    if xx == "YES":
        return start()
    elif xx == "NO":
        print("See you later!")
    else:
        print("Something is wrong")


def CRYTERIA():
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

print(start())

# Todo
# Frontend in JS or Django
