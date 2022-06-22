# import googlefinance
# import investpy.stocks
# import reuterspy
# import investpy.bonds
# import numpy
# import plotly.express as px

import yfinance as yf  # import_danych_YahooFinance

print("---------------------------------------------------------------------------------")
print("Witaj w aplikacji Altalite!\n"
      "Wpisz poniżej ticker spolki, ktore cie interesuje, a ja przeanalizuje ja dla ciebie")
print("---------------------------------------------------------------------------------")
WY = input("Wpisz ticker spolki:")


def start():
    majo = [
        "1.INFORMACJE_O_SPOLCE",
        "2.PODSTAWOWE_DANE",
        "3.WYCENA_WSKAZNIKOWA",
        "4.DYWIDENDA",
        "5.WYCENA_MODELOWA",
        "6.WZROST",
        "7.ZADLUZENIE",
        "8.RENTOWNOSC",
        "9.ZWROT",
        "10.PROGNOZA",
        "11.AKCJONARIAT",
        "12.WYKRES",
        "13.REKOMENDACJE_ANALITYKOW"
    ]
    for i in majo:
        print(i)
    print("---------------------------------------------------------------------------------")
    x = input("Wybierz_program:").upper()
    if x == "INFORMACJE_O_SPOLCE":
        return info()
    elif x == "PODSTAWOWE_DANE":
        return meta_dane()
    elif x == "WYCENA_WSKAZNIKOWA":
        return wycena_wskaznikowa()
    elif x == "DYWIDENDA":
        return dywidenda()
    elif x == "WYCENA_MODELOWA":
        return wartosc()
    elif x == "WZROST":
        return wzrost()
    elif x == "ZADLUZENIE":
        return dlug()
    elif x == "RENTOWNOSC":
        return rentownosc()
    elif x == "ZWROT" or "9":
        return zwrot()
    elif x == "PROGNOZA" or "10":
        return prognoza()
    elif x == "AKCJONARIAT" or "11":
        return akcjonariat()
    elif x == "WYKRES" or "12":
        return wykres()
    elif x == "REKOMENDACJE_ANALITKOW" or "13":
        return rekomendacje_analitykow()
    else:
        return start()


def info():  # Informacje_o_spolce
    i = yf.Ticker(WY).info['longBusinessSummary']
    print("INFORMACJE_NA_TEMAT_SPOLKI:", i)


def meta_dane():
    print("-------------")
    print("PODSTAWOWE_DANE")
    print("-------------")
    # -----
    nazwa = yf.Ticker(WY).info['shortName']  # Nazwa
    print("NAZWA:", nazwa)
    # ------
    sektor = yf.Ticker(WY).info['sector']  # Sektor
    print("SEKTOR:", sektor)
    # -----
    branza = yf.Ticker(WY).info['industry']  # BRANZA
    print("BRANZA:", branza)
    # -----
    kapitalizacja = yf.Ticker(WY).info['marketCap']  # KAPITALIZACJA
    print("KAPITALIZACJA_MLN_USD:", kapitalizacja)
    # -----
    cena = yf.Ticker(WY).info['currentPrice']  # cena_akcji
    print("CENA_AKCJI_W_USD:", cena)


def wycena_wskaznikowa():  # wycena wskaźnikowa
    print("-------------")
    print("WYCENA_WSKAZNIKOWA")
    print("-------------")

    p_e = yf.Ticker(WY).info['trailingPE']  # Cenadozysku
    if round(p_e, 2) > 20:
        print("CENA_DO_ZYSKU:", round(p_e, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(p_e, 2) == 20:
        print("CENA_DO_ZYSKU:", round(p_e, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(p_e, 2) < 10:
        print("CENA_DO_ZYSKU:", round(p_e, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")

    p_b = yf.Ticker(WY).info['priceToBook']  # Cena_do_wartosci_ksiegowej
    if p_b is None:
        print("CENA_DO_WARTOSCI_KSIEGOWEJ:", "[Spolka_ma_ujemna_wartosc_ksiegowa]")
    elif round(p_b, 2) > 2:
        print("CENA_DO_WARTOSCI_KSIEGOWEJ:", round(p_b, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(p_b, 2) == 1:
        print("CENA_DO_WARTOSCI_KSIEGOWEJ:", round(p_b, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(p_b, 2) < 1:
        print("CENA_DO_WARTOSCI_KSIEGOWEJ:", round(p_b, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")

    e_v = yf.Ticker(WY).info['enterpriseToEbitda']  # EV\EBITDA
    if round(e_v, 2) > 12:
        print("EV_EBITDA:", round(e_v, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(e_v, 2) == 12:
        print("EV_EBITDA:", round(e_v, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(e_v, 2) < 12:
        print("EV_EBITDA:", round(e_v, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")


def dywidenda():
    print("-------------")
    print("DANE_DYWIDENDA")
    print("-------------")
    div = yf.Ticker(WY).info['dividendYield']  # Dividend_yield
    if div is None:
        print("SPÓŁKA_NIE_WYPLACA_DYWIDENDY:", "[BRAK]")
    elif 0.0500 >= round(div, 4) >= 0.0200:
        print("DYWIDENDA_YIELD_%:", (round(div, 4) * 100), "[BEZPIECZNY_YIELD_DYWIDENDY]")
    elif round(div, 4) < 0.0190:
        print("DYWIDENDA_YIELD_%:", (round(div, 4) * 100), "[NISKI_YIELD_DYWIDENDY]")
    elif round(div, 4) >= 0.0600:
        print("DYWIDENDA_YIELD_%:", (round(div, 4) * 100), "[WYSOKI_YIELD_SPRAWDZ_BEZPIECZENSTWO]")
    else:
        pass

    div_5y = yf.Ticker(WY).info['fiveYearAvgDividendYield']
    if div_5y is None:
        print("SR_5Y_DYWIDEND_YILED:", "[Spółka ma krótsza historie dywidendy lub jej nie wyplaca]")
    elif round(div_5y, 2) >= 0.01:
        print("SR_5Y_DYWIDEND_YILED:", round(div_5y, 2), "%")
    else:
        pass

    # Wzrost dywidendy

    py = yf.Ticker(WY).info['payoutRatio']  # Poziom_wyplaty_zysku
    if py is None:
        print("SPÓŁKA_NIE_WYPLACA_ZYSKU:", "[BRAK]")
    elif round(py, 6) <= 0.19:
        print("WYPŁATA_ZYSKU_PROCENT_%:", "[SPÓŁKA_WYPLACA_MAŁO_ZYSKOW]")
    elif round(py, 2) > 0.60:
        print("WYPŁATA_ZYSKU_PROCENT_%:", round(py, 2), "[SPÓŁKA_WYPLACA_ZA_DUZO_ZYSKOW]")
    elif 0.20 <= round(py, 2) <= 0.59:
        print("WYPŁATA_ZYSKU_PROCENT_%:", round(py, 2), "[SPÓŁKA_WYPLACA_BEZPIECZNA_ILOSC_ZYSKU]")


def wartosc():  # GRAHAM ,DCF, FCF, DDM
    print("-------------")
    print("WARTOSC")
    print("-------------")
    peg = yf.Ticker(WY).info[
        'pegRatio']  # PEG == 0 (sprawiedliwie wyceniona) PEG > 1 ( przewartosciowana) PEG < 0 (niedowartosciowana
    if round(peg, 2) > 1:
        print("PEG_RATIO:", round(peg, 2), "[SPÓŁKA_PRZEWARTOSCIOWANA]")
    elif round(peg, 2) == 0:
        print("PEG_RATIO:", round(peg, 2), "[SPÓŁKA_SPRAWIEDLIWIE_WYCENIONA]")
    elif round(peg, 2) < 0:
        print("PEG_RATIO:", round(peg, 2), "[SPÓŁKA_NIEDOWARTOSCIOWANA]")

    # GRAHAM = (yf.Ticker(WY).info['forwardEps'] * (8.5 + (2 * yf.Ticker(WY).info['earningsGrowth'])))
    # GRAHAM.2.0 = [EPS * (8.5 + 2g) * 4.4] /Y- 20letnia rentownosc obligacji korporacyjnych AAA (WEB SCRAPPING)
    # DDM
    # DCF
    # FCF
    # BUFFET


def wzrost():  # WZROST,EBITDA,DLUG  #pandas data frame
    print("-------------")
    print("WZROST")
    print("-------------")
    rev_g = yf.Ticker(WY).info['revenueGrowth']
    print("SR_WZROST_PRZYCHODOW:", (round(rev_g, 2) * 100), "%")
    eps_g = yf.Ticker(WY).info['earningsGrowth']
    print("SR_WZROST_ZYSKU:", (round(eps_g, 2) * 100), "%")


def dlug():
    print("-------------")
    print("ZADLUZENIE_WSKAZNIKI")
    print("-------------")
    cr = yf.Ticker(WY).info['currentRatio']
    if round(cr, 2) >= 2.00:
        print("Current_Ratio:", round(cr, 2), "[SPOLKA_ZLE_ZARZADZA_KAPITALEM]")
    elif round(cr, 2) <= 1.00:
        print("Current_Ratio:", round(cr, 2), "[SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA]")
    else:
        print("Current_Ratio:", round(cr, 2), "[SPOLKA_ZDROWO_ZARZADZA_KAPITALEM]")

    qr = yf.Ticker(WY).info['quickRatio']
    if qr is None:
        print("Quick_Ratio:", "[Brak danych]")
    elif round(qr, 2) >= 1:
        print("Quick_Ratio:", round(qr, 2), "[SPOLKA_DOBRZE_ZARZADZA_KAPITALEM]")
    elif round(qr, 2) <= 1:
        print("Quick_Ratio:", round(qr, 2), "[SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA]")

    dte = yf.Ticker(WY).info['debtToEquity']
    if dte is None:
        print("Debt_To_Equity:", "[Brak_danych]")
    elif 1 <= round(dte, 2) < 1.5:
        print("Debt_To_Equity:", round(dte, 2), "[SPOLKA_NA_NEUTRALNYM_POZIOMIE_DLUGU]")
    elif round(dte, 2) >= 2:
        print("Debt_To_Equity:", round(dte, 2), "[SPOLKA_MOZE_MIEC_PROBLEMY_Z_PLYNNOSCIA]")
    elif round(dte, 2) < 1:
        print("Debt_To_Equity:", round(dte, 2), "[BEZPIECZNY_POZIOM_DLUGU]")


def rentownosc():
    print("-------------")
    print("RENTOWNOSC_WSKAZNIKI")
    print("-------------")
    roe = yf.Ticker(WY).info['returnOnEquity']  # ROE
    if 0.10 <= round(roe, 2) <= 0.15:
        print("ZWROT_Z_KAPITALU:", round(roe, 2), "[ROE_JEST_NA_DOBRYM_POZIOMIE]")
    elif round(roe, 2) >= 0.20:
        print("ZWROT_Z_KAPITALU:", round(roe, 2), "[ROE_JEST_WYSOKIE]")
    elif round(roe, 2) <= 0.09:
        print("ZWROT_Z_KAPITALU:", round(roe, 2), "[ROE_JEST_NISKIE]")

    roa = yf.Ticker(WY).info['returnOnAssets']  # ROA
    if 0.05 <= round(roa, 2) <= 0.19:
        print("ZWROT_Z_AKTYWOW:", round(roa, 2), "[ROA_JEST_DOBRYM_POZIOMIE]")
    elif round(roa, 2) >= 0.20:
        print("ZWROT_Z_AKTYWOW:", round(roa, 2), "[ROA_JEST_WYSOKIE]")
    elif round(roa, 2) <= 0.04:
        print("ZWROT_Z_AKTYWOW:", round(roa, 2), "[ROA_JEST_NISKIE]")

    gm = yf.Ticker(WY).info['grossMargins']  # MARŻA_PRZYCHODU
    if 0.50 <= round(gm, 2) <= 0.70:
        print("MARZA_PRZYCHODU_%:", round(gm, 2), "[DOBRA_MARZA_PRZYCHODU]")
    elif 0.10 <= round(gm, 2) <= 0.50:
        print("MARZA_PRZYCHODU_%:", round(gm, 2), "[NEUTRALNA_MARZA_PRZYCHODU]")
    elif round(gm, 2) >= 0.71:
        print("MARZA_PRZYCHODU_%:", round(gm, 2), "[BARDZO_WYSOKA_MARZA_PRZYCHODU]")
    elif round(gm, 2) <= 0.09:
        print("MARZA_PRZYCHODU_%:", round(gm, 2), "[BARDZO_NISKA_MARZA_PRZYCHODU]")

    om = yf.Ticker(WY).info['operatingMargins']  # MARŻA_ZYSKU_OPERACYJNEGO
    if 0.14 <= round(om, 2) <= 0.20:
        print("MARŻA_OPERACYJNA_%:", round(om, 2), "[DOBRA_MARŻA_OPERACYJNA_]")
    elif 0.10 <= round(om, 2) <= 0.13:
        print("MARŻA_OPERACYJNA_%:", round(om, 2), "[NEUTRALNA_MARŻA_OPERACYJNA_]")
    elif round(om, 2) >= 0.21:
        print("MARŻA_OPERACYJNA_%:", round(om, 2), "[BARDZO_WYSOKA_MARŻA_OPERACYJNA]")
    elif round(om, 2) <= 0.09:
        print("MARŻA_OPERACYJNA_%:", round(om, 2), "[BARDZO_NISKA_MARŻA_OPERACYJNA]")

    pm = yf.Ticker(WY).info['profitMargins']  # MARŻA_ZYSKU_Netto
    if 0.14 <= round(pm, 2) <= 0.20:
        print("MARŻA_ZYSKU_NETTO_%:", round(pm, 2), "[DOBRA_MARŻA_ZYSKU_NETTO]")
    elif 0.10 <= round(pm, 2) <= 0.13:
        print("MARŻA_ZYSKU_NETTO_%:", round(pm, 2), "[NEUTRALNA_MARŻA_ZYSKU_NETTO]")
    elif round(pm, 2) >= 0.21:
        print("MARŻA_ZYSKU_NETTO_%:", round(pm, 2), "[BARDZO_WYSOKA_MARŻA_ZYSKU_NETTO]")
    elif round(pm, 2) <= 0.09:
        print("MARŻA_ZYSKU_NETTO_%:", round(pm, 2), "[BARDZO_NISKA_MARŻA_ZYSKU_NETTO]")


def zwrot():
    print("-------------")
    print("ZWROT")
    print("-------------")
    # -----
    r_ytd = yf.Ticker(WY).info['ytdReturn']  # Zwrot od poczatku roku
    print("ZWROT_OD_POCZATKU_ROKU:", r_ytd)
    # -----
    r_5y = yf.Ticker(WY).info['fiveYearAverageReturn']  # Zwrot z 5 lat sredniorocznie
    print("ZWROT_Z_OSTATNICH_5_LAT_SR_ROCZNIE:", r_5y)
    # -----


def prognoza():  # ML
    pass


def akcjonariat():
    print("-----------------------------------------")
    print("AKCJONARIAT")
    print("------------------------------------------------------------------")
    hold = yf.Ticker(WY).institutional_holders  # Holderzy
    print(hold)


def rekomendacje_analitykow():
    sr_cena_docelowa = yf.Ticker(WY).info['targetMeanPrice']
    jk = round(yf.Ticker(WY).info['currentPrice'] / sr_cena_docelowa, 2)
    print("ŚREDNIA_CENA_DOCELOWA_ANALITYKOW:", sr_cena_docelowa, )
    print("AKTUALNA CENA / SREDNIA_CENA_DOCELOWA_ANALITYKOW:", jk, ",", "DO_CENY_DOCELOWEJ:", round((1 - jk) * 100, 2),
          "%")
    reko = yf.Ticker(WY).recommendations
    print("REKOMENDACJE_ANALITYKOW:", reko)


def wykres():
    pass


print(start())

# Pętla wybór programu z listy


# punktacja wyceny wskaźnikowej
