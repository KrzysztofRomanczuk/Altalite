#import googlefinance
#import investpy.stocks
#import reuterspy
#import investpy.bonds
#import numpy
#import plotly.express as px

import yfinance as yf  #import_danych_YahooFinance

WY = input("WPISZ_TICKER_SPOLKI:")

def INFO():  #Informacje_o_spolce
       I = yf.Ticker(WY).info['longBusinessSummary']
       return I

def META_DANE():
    print("PODSTAWOWE_DANE")
    print("-------------")
    #-----
    NAZWA = yf.Ticker(WY).info['shortName']  #Nazwa
    print("NAZWA:", NAZWA)
    #------
    SEKTOR = yf.Ticker(WY).info['sector']  #Sektor
    print("SEKTOR:", SEKTOR)
    #-----
    INDUSTRY = yf.Ticker(WY).info['industry']  #BRANZA
    print("BRANZA:", INDUSTRY)
    #-----
    MARKETCAP = yf.Ticker(WY).info['marketCap']  #KAPITALIZACJA
    print("KAPITALIZACJA_MLN_USD:", MARKETCAP)
    #-----
    CENA = yf.Ticker(WY).info['currentPrice']  #cena_akcji
    print("CENA_AKCJI_W_USD:", CENA)

def WYCENA_WSKAZNIKOWA(): #wycena wskaźnikowa
    print("-------------")
    print("WYCENA_WSKAZNIKOWA")
    print("-------------")

    P_E = yf.Ticker(WY).info['trailingPE']  #Cenadozysku
    if round(P_E, 2) > 20:
        print("CENA_DO_ZYSKU:", round(P_E, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(P_E, 2) == 20:
        print("CENA_DO_ZYSKU:", round(P_E, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(P_E, 2) < 10:
        print("CENA_DO_ZYSKU:", round(P_E, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")

    P_B = yf.Ticker(WY).info['priceToBook']  # Cena_do_wartosci_ksiegowej
    if round(P_B,2) > 2:
        print("CENA_DO_WARTOSCI_KSIEGOWEJ:", round(P_B, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(P_B,2) == 1:
        print("CENA_DO_ZYSKU:", round(P_B, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(P_B,2) < 1:
        print("CENA_DO_ZYSKU:", round(P_B, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")

    E_V = yf.Ticker(WY).info['enterpriseToEbitda']  #EV\EBITDA
    if round(E_V,2) > 12:
        print("EV\EBITDA:", round(E_V,2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(E_V,2) == 12:
        print("EV\EBITDA:", round(E_V,2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(E_V,2) < 12:
        print("EV\EBITDA:", round(E_V,2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")




def DIVIDEND():
    DIV = yf.Ticker(WY).info['dividendYield']  # Dividend_yield
    if DIV == None:
        print("SPÓŁKA_NIE_WYPLACA_DYWIDENDY:", "[BRAK]")
    elif round(DIV, 4) <= 0.0500 and round(DIV, 4) >= 0.0200:
        print("DYWIDENDA_YIELD_%:", round(DIV, 4), "[BEZPIECZNY_YIELD_DYWIDENDY]")
    elif round(DIV, 4) < 0.0190:
        print("DYWIDENDA_YIELD_%:", round(DIV, 4), "[NISKI_YIELD_DYWIDENDY]")
    elif round(DIV, 4) >= 0.0600:
        print("DYWIDENDA_YIELD_%:", round(DIV, 4), "[WYSOKI_YIELD_SPRAWDZ_BEZPIECZENSTWO]")

    print("SR_5Y_DYWIDEND_YILED:",round(yf.Ticker(WY).info['fiveYearAvgDividendYield'],4),"%")

    #Wzrost dywidendy

    PY = yf.Ticker(WY).info['payoutRatio']  # Poziom_wyplaty_zysku
    if round(PY, 6) <= 0:
        print("SPÓŁKA_NIE_WYPLACA_ZYSKU:", "[BRAK]")
    elif round(PY, 2) > 60:
        print("WYPŁATA_ZYSKU_PROCENT_%:", round(PY, 2), "[SPÓŁKA_WYPLACA_ZA_DUZO_ZYSKOW]")
    elif round(PY, 2) <= 50:
        print("WYPŁATA_ZYSKU_PROCENT_%:", round(PY, 2), "[SPÓŁKA_WYPLACA_BEZPIECZNA_ILOSC_ZYSKU]")


def VALUE(): #GRAHAM ,DCF, FCF, DDM
    PEG = yf.Ticker(WY).info['pegRatio']  # PEG == 0 (sprawiedliwie wyceniona) PEG > 1 ( przewartosciowana) PEG < 0 (niedowartosciowana
    if round(PEG, 2) > 1:
        print("PEG_RATIO:", round(PEG, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(PEG, 2) == 0:
        print("PEG_RATIO:", round(PEG, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(PEG, 2) < 0:
        print("PEG_RATIO:", round(PEG, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")
    #GRAHAM = (yf.Ticker(WY).info['forwardEps'] * (8.5 + (2 * yf.Ticker(WY).info['earningsGrowth'])))
    #GRAHAM = [EPS * (8.5 + 2g) * 4.4] /Y- 20letnia rentownosc obligacji korporacyjnych AAA (WEB SCRAPPING)

def WZROST(): #WZROST,EBITDA,DLUG
    REV_G = yf.Ticker(WY).info['revenueGrowth']
    print("SR_WZROST_PRZYCHODOW:",REV_G)
    EPS_G = yf.Ticker(WY).info['earningsGrowth']
    print("SR_WZROST_ZYSKU:",EPS_G)

def DLUG():
    CR = yf.Ticker(WY).info['currentRatio']
    if round(CR,2) >= 2.00:
        print("SPOLKA_ZLE_ZARZADZA_KAPITALEM:", round(CR,2), "[Current_Ratio]")
    elif round(CR,2) <= 1.00:
        print("SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA:", round(CR,2), "[Current_Ratio]")
    else:
        print("SPOLKA_ZDROWO_ZARZADZA_KAPITALEM:", round(CR,2), "[Current_Ratio]")

    QR = yf.Ticker(WY).info['quickRatio']
    if round(QR,2) >= 1:
        print("SPOLKA_DOBRZE_ZARZADZA_KAPITALEM:", round(QR,2), "[Quick_Ratio]")
    elif round(QR,2) <= 1:
        print("SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA:", round(QR,2), "[Quick_Ratio]")

    DTE = yf.Ticker(WY).info['debtToEquity']
    if round(DTE,2) >= 2:
        print("SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA:", round(DTE,2), "[Debt_To_Equity")
    elif round(DTE,2) <= 1:
        print("BEZPIECZNY_POZIOM_DLUGU:", round(DTE,2),"[Debt_To_Equity")
    else:
        print("SPOLKA_NA_NEUTRALNYM_POZIOMIE_DLUGU:", round(DTE, 2), "[Debt_To_Equity]")


def RENTOWNOSC():
    ROE = yf.Ticker(WY).info['returnOnEquity']  #ROE
    if round(ROE,2) >= 0.10 and round(ROE,2) <= 0.15:
        print("ZWROT_Z_KAPITALU:",round(ROE,2), "[ROE_JEST_NA_DOBRYM_POZIOMIE]")
    elif round(ROE,2) >= 0.20:
        print("ZWROT_Z_KAPITALU:",round(ROE,2), "[ROE_JEST_WYSOKIE]")
    elif round(ROE,2) <= 0.09:
        print("ZWROT_Z_KAPITALU:",round(ROE,2), "[ROE_JEST_NISKIE]")

    ROA = yf.Ticker(WY).info['returnOnAssets']  #ROA
    if round(ROA,2) >= 0.05 and round(ROA,2) <= 0.19:
        print("ZWROT_Z_AKTYWOW:", round(ROA, 2), "[ROA_JEST_DOBRYM_POZIOMIE]")
    elif round(ROA,2) >= 0.20:
        print("ZWROT_Z_AKTYWOW:",round(ROA, 2), "[ROA_JEST_WYSOKIE]")
    elif round(ROA,2) <= 0.04:
        print("ZWROT_Z_AKTYWOW:", round(ROA, 2), "[ROA_JEST_NISKIE]")

    GM = yf.Ticker(WY).info['grossMargins']  # MARŻA_ZYSKU_Netto
    if round(GM, 2) >= 0.50 and round(GM, 2) <= 0.70:
        print("MARZA_PRZYCHODU_%:", round(GM, 2), "[DOBRA_MARZA_PRZYCHODU]")
    elif round(GM, 2) >= 0.10 and round(GM, 2) <= 0.50:
        print("MARZA_PRZYCHODU_%:", round(GM, 2), "[NEUTRALNA_MARZA_PRZYCHODU]")
    elif round(GM, 2) >= 0.71:
        print("MARZA_PRZYCHODU_%:", round(GM, 2), "[BARDZO_WYSOKA_MARZA_PRZYCHODU]")
    elif round(GM, 2) <= 0.09:
        print("MARZA_PRZYCHODU_%:", round(GM, 2), "[BARDZO_NISKA_MARZA_PRZYCHODU]")

    OM = yf.Ticker(WY).info['operatingMargins']  # MARŻA_ZYSKU_Netto
    if round(OM, 2) >= 0.14 and round(GM, 2) <= 0.20:
        print("MARŻA_OPERACYJNA_%:", round(OM, 2), "[DOBRA_MARŻA_OPERACYJNA_]")
    elif round(OM, 2) >= 0.10 and round(OM, 2) <= 0.13:
        print("MARŻA_OPERACYJNA_%:", round(OM, 2), "[NEUTRALNA_MARŻA_OPERACYJNA_]")
    elif round(OM, 2) >= 0.21:
        print("MARŻA_OPERACYJNA_%:",round(OM, 2), "[BARDZO_WYSOKA_MARŻA_OPERACYJNA]")
    elif round(OM, 2) <= 0.09:
        print("MARŻA_OPERACYJNA_%:", round(OM, 2), "[BARDZO_NISKA_MARŻA_OPERACYJNA]")

    PM = yf.Ticker(WY).info['profitMargins']  #MARŻA_ZYSKU_Netto
    if round(PM, 2) >= 0.14 and round(PM, 2) <= 0.20:
        print("MARŻA_ZYSKU_NETTO_%:",round(PM, 2), "[DOBRA_MARŻA_ZYSKU_NETTO]")
    elif round(PM, 2) >= 0.10 and round(PM, 2) <= 0.13:
        print("MARŻA_ZYSKU_NETTO_%:", round(PM, 2), "[NEUTRALNA_MARŻA_ZYSKU_NETTO]")
    elif round(PM, 2) >= 0.21:
        print("MARŻA_ZYSKU_NETTO_%:",round(PM, 2), "[BARDZO_WYSOKA_MARŻA_ZYSKU_NETTO")
    elif round(PM, 2) <= 0.09:
        print("MARŻA_ZYSKU_NETTO_%:", round(PM, 2), "[BARDZO_NISKA_MARŻA_ZYSKU_NETTO]")



def ZWROT():
    print("-------------")
    print("ZWROT")
    print("-------------")
    #-----
    R_YTD = yf.Ticker(WY).info['ytdReturn']  # Zwrot od poczatku roku
    print("ZWROT_OD_POCZATKU_ROKU:", R_YTD)
    #-----
    R_5Y = yf.Ticker(WY).info['fiveYearAverageReturn']  # Zwrot z 5 lat srediorocznie
    print("ZWROT_Z_OSTATNICH_5_LAT_SR_ROCZNIE:", R_5Y)
    #-----

def HOLDERZY():
    print("-----------------------------------------")
    print("HOLDERZY")
    print("------------------------------------------------------------------")
    HOLD = yf.Ticker(WY).institutional_holders   #Holderzy
    print(HOLD)

def REKOMENDACJE_ANALITYKOW():
    SR_CENA_DOCELOWA = yf.Ticker(WY).info['targetMeanPrice']
    JK = round(yf.Ticker(WY).info['currentPrice'] / SR_CENA_DOCELOWA, 2)
    print("ŚREDNIA_CENA_DOCELOWA_ANALITYKOW:",SR_CENA_DOCELOWA,)
    print("AKTUALNA CENA / SREDNIA_CENA_DOCELOWA_ANALITYKOW:",JK,",","DO_CENY_DOCELOWEJ:",round((1 - JK)*100,2),"%")
    REKO = yf.Ticker(WY).recommendations
    print("REKOMENDACJE_ANALITYKOW:", REKO)

def ZOBACZ_WYKRES():
    pass
print(DIVIDEND())






#Pętla wybór programu z listy

# DIV growth,
# Dividend yield,
#Model Gordona
#GRAHAM model
#buffet model
#Wycena DCF/FCF
#Prognozowana wycena za 10lat
#punktacja wyceny wskaźnikowej
