from src.datas.data import initialize_data_balance,initialize_data_gastos,initialize_data_ingresos

balancedb: list[dict] = initialize_data_balance()

fmes_ingresos: list[dict] = initialize_data_ingresos()

fmes_gastos: list[dict] = initialize_data_gastos()