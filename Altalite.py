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

def WYCENA(): #wycena wskaźnikowa
    print("-------------")
    print("WYCENA")
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

    PEG = yf.Ticker(WY).info['pegRatio']  #PEG == 0 (sprawiedliwie wyceniona) PEG > 1 ( przewartosciowana) PEG < 0 (niedowartosciowana
    if round(PEG,2) > 1:
        print("PEG_RATIO:", round(PEG,2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(PEG,2) == 0:
        print("PEG_RATIO:", round(PEG,2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(PEG,2) < 0:
        print("PEG_RATIO:", round(PEG,2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")
    # ----- #DEF dane dla dywidendy?
    DIV = yf.Ticker(WY).info['dividendYield']  # Dividend_yield
    if round(DIV,4) <= 0:
        print("SPÓŁKA_NIE_WYPLACA_DYWIENDY")
    elif round(DIV,4) <= 0.05:
        print("DYWIDENDA_YIELD_%:", round(DIV,4), "[BEZPIECZNY_YIELD_DYWIDENDY]")
    elif round(DIV,4) >= 0.06:
        print("DYWIDENDA_YIELD_%:", round(DIV,4), "[WYSOKI_YIELD_SPRAWDZ_BEZPIECZENSTWO]")
    #-----
    EPS_R = yf.Ticker(WY).info['earningsQuarterlyGrowth']  #EPS_growth_quarter
    print("ZYSK_NA_AKCJE_KWARTALNIE_WZROST_%:", EPS_R)
    #-----
    PY = yf.Ticker(WY).info['payoutRatio']  #Poziom_wyplaty_zysku
    if round(PY,6) <= 0:
        print("SPÓŁKA_NIE_WYPLACA_ZYSKU")
    elif round(PY,2) > 60:
            print("WYPŁATA_ZYSKU_PROCENT_%:", round(PY,2), "[SPÓŁKA_WYPLACA_ZA_DUZO_ZYSKOW]")
    elif round(PY,2) <= 50:
            print("WYPŁATA_ZYSKU_PROCENT_%:", round(PY,2), "[SPÓŁKA_WYPLACA_BEZPIECZNA_ILOSC_ZYSKU]")


def WZROST(): #PRZYCHODY,ZYSK,EBITDA,DLUG
    pass
def VALUE():
    pass
def RENTOWNOSC():
    PM = yf.Ticker(WY).info['profitMargins']  #MARŻA_ZYSKU_Netto
    print("MARŻA_ZYSKU_%:", PM)
    #-----
    #ROE,ROA,ROIC,MARZE


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
#print(META_DANE())


print(WYCENA())
#print(ZWROT())
#print(HOLDERZY())

#Pętla wybór programu z listy
#Aktualne dane
#cena akcji
# (P/E,
# EV/EBITDA,
# Zadluzenie,
# EPS growth,
# DIV growth,
# Dividend yield,
# net margin,
# market cap, value(over,fair,under))
#Model Gordona
#GRAHAM model
#buffet model
#Wycena DCF/FCF
#Prognozowana wycena za 10lat
#punktacja wyceny wskaźnikowej