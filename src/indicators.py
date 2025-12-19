def ROA(financials, balance_sheet):
    return financials.loc['NetIncome'] / balance_sheet.loc['TotalAssets']

def CurrentRatio(balance_sheet):
    return balance_sheet.loc['CurrentAssets'] / balance_sheet.loc['CurrentLiabilities']

def DebtRatio(balance_sheet):
    return balance_sheet.loc['TotalLiabilitiesNetMinorityInterest'] / balance_sheet.loc['TotalAssets']

def GrowthPotential(cash_flow, balance_sheet):
    # CAPEX / aktywa
    return cash_flow.loc['Capital Expenditure'] / balance_sheet.loc['TotalAssets']
