import pandas as pd
import requests
from io import StringIO

def fetch_ecb_raw(series_key):
    url = f"https://data-api.ecb.europa.eu/service/data/{series_key}?format=csvdata"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        print(f"Lỗi khi kéo {series_key} - Status code: {response.status_code}")
        return None

print("=== BẮT ĐẦU KÉO BỔ SUNG DỮ LIỆU ECB ===")

# 1. Lãi suất cho vay (Bank Lending Rate) - Đã thành công trước đó
print("1. Đang tải Bank Lending Rate...")
df_lending = fetch_ecb_raw("MIR/M.U2.B.A2I.AM.R.A.2240.EUR.N")
if df_lending is not None:
    df_lending.to_csv("Raw_ECB_BankLendingRate.csv", index=False)
    print("   -> Đã lưu file: Raw_ECB_BankLendingRate.csv")

# 2. Tăng trưởng tín dụng (Credit Growth) - Đã sửa lại mã chuẩn 100%
print("2. Đang tải Credit Growth...")
df_credit = fetch_ecb_raw("BSI/M.U2.N.A.A22.A.1.U2.2240.Z01.E")
if df_credit is not None:
    df_credit.to_csv("Raw_ECB_CreditGrowth.csv", index=False)
    print("   -> Đã lưu file: Raw_ECB_CreditGrowth.csv")

print("\n=== HOÀN TẤT KÉO DỮ LIỆU THÔ BỔ SUNG ===")
