import QuantLib as ql
import pandas as pd

def OptionPricing():

    calculation_date = ql.Date(15, 1, 2023)
    ql.Settings.instance().evaluationDate = calculation_date
    spot_price = 100
    strike_price = 100
    risk_free_rate = 0.05
    volatility = 0.2
    maturity_date = ql.Date(15, 1, 2024)
    payoff = ql.PlainVanillaPayoff(ql.Option.Call, strike_price)
    exercise = ql.EuropeanExercise(maturity_date)
    european_option = ql.VanillaOption(payoff, exercise)
    spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
    rate_handle = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, ql.Actual365Fixed()))
    calendar = ql.NullCalendar()
    vol_handle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar,volatility, ql.Actual365Fixed()))

    bsm_proces = ql.BlackScholesProcess(spot_handle, rate_handle, vol_handle)
    european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_proces))
    option_price = european_option.NPV()
    print(" price = {}".format(option_price))


if __name__ == '__main__':
    print(ql.__version__)
    OptionPricing()
