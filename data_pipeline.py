import pandas as pd
import requests
import eurostat
from io import StringIO

# ==========================================
# 1. HÀM KÉO DỮ LIỆU TỪ ECB API
# ==========================================
def fetch_ecb_raw(series_key):
    """Gọi API của ECB và trả về raw DataFrame"""
    url = f"https://data-api.ecb.europa.eu/service/data/{series_key}?format=csvdata"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        print(f"Lỗi khi kéo {series_key} - Status code: {response.status_code}")
        return None

print("=== BẮT ĐẦU KÉO DỮ LIỆU ECB ===")

# 1.1 Lãi suất Policy Rate (Deposit Facility Rate) - Monthly
print("1. Đang tải ECB Policy Rate...")
df_ecb_rate = fetch_ecb_raw("FM/D.U2.EUR.4F.KR.DFR.CHG")
if df_ecb_rate is not None:
    df_ecb_rate.to_csv("Raw_ECB_PolicyRate.csv", index=False)
    print("   -> Đã lưu file: Raw_ECB_PolicyRate.csv")

# 1.2 Tỷ giá EUR/USD - Monthly
print("2. Đang tải EUR/USD Exchange Rate...")
df_eur_usd = fetch_ecb_raw("EXR/M.USD.EUR.SP00.A")
if df_eur_usd is not None:
    df_eur_usd.to_csv("Raw_ECB_EURUSD.csv", index=False)
    print("   -> Đã lưu file: Raw_ECB_EURUSD.csv")


# ==========================================
# 2. HÀM KÉO DỮ LIỆU TỪ EUROSTAT API
# ==========================================
print("\n=== BẮT ĐẦU KÉO DỮ LIỆU EUROSTAT ===")

# 2.1 HICP Inflation (prc_hicp_manr)
print("3. Đang tải HICP Inflation...")
df_inflation = eurostat.get_data_df('prc_hicp_manr')
if df_inflation is not None:
    df_inflation.to_csv("Raw_Eurostat_Inflation.csv", index=False)
    print("   -> Đã lưu file: Raw_Eurostat_Inflation.csv")

# 2.2 Real GDP Growth (nama_10_gdp)
print("4. Đang tải Real GDP Growth...")
df_gdp = eurostat.get_data_df('nama_10_gdp')
if df_gdp is not None:
    df_gdp.to_csv("Raw_Eurostat_GDP.csv", index=False)
    print("   -> Đã lưu file: Raw_Eurostat_GDP.csv")

# 2.3 Unemployment Rate (une_rt_m)
print("5. Đang tải Unemployment Rate...")
df_unemp = eurostat.get_data_df('une_rt_m')
if df_unemp is not None:
    df_unemp.to_csv("Raw_Eurostat_Unemployment.csv", index=False)
    print("   -> Đã lưu file: Raw_Eurostat_Unemployment.csv")

print("\n=== HOÀN TẤT NHIỆM VỤ KÉO DỮ LIỆU ===")
