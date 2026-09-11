# One ECB, Five Different Stories: A Macroeconomic & Financial Transmission Analysis (2019–2026)

Dự án phân tích định lượng và trực quan hóa tác động của chính sách tiền tệ Ngân hàng Trung ương Châu Âu (ECB) đến 5 nền kinh tế lớn nhất khu vực đồng Euro (Đức, Pháp, Ý, Tây Ban Nha, Hà Lan) trong giai đoạn 2019–2026.

---

## 👥 Thông Tin Nhóm & Phân Công Công Việc
* **Đề tài:** One ECB, Five Different Stories (Một chính sách - Năm câu chuyện khác nhau)
* **Quy mô nhóm:** 13 thành viên
* **Phạm vi nghiên cứu:** Đức (DE), Pháp (FR), Ý (IT), Tây Ban Nha (ES), Hà Lan (NL)
* **Khung thời gian:** Tháng 01/2019 – Tháng 12/2026

---

## 📂 Cấu Trúc Repository
```text
gois1-1109/
│
├── data_raw/                  # Chứa các file dữ liệu thô tải từ ECB Data Portal & Eurostat
│   ├── Raw_ECB_PolicyRate.csv
│   ├── Raw_ECB_EURUSD.csv
│   ├── Raw_ECB_BankLendingRate.csv
│   ├── Raw_ECB_BankCreditGrowth.csv
│   ├── Raw_Eurostat_Inflation.csv
│   ├── Raw_Eurostat_Unemployment.csv
│   └── Raw_Eurostat_GDP.csv
│
├── data_clean/                # Chứa file dữ liệu tổng hợp sạch sau khi qua pipeline
│   └── master_dataset.csv
│
├── notebooks/                 # Chứa các Jupyter Notebook phân tích và trực quan hóa
│   ├── 10_merge_master.ipynb  # Pipeline xử lý, làm sạch và hợp nhất dữ liệu
│   ├── 11_eda_findings.ipynb  # Phân tích tìm kiếm ngoại lệ và insights (EDA)
│   └── 12_visual_story.ipynb  # Trực quan hóa 5 câu chuyện vĩ mô (Charts 1-5)
│
├── README.md                  # Tài liệu hướng dẫn sử dụng dự án
└── requirements.txt           # Danh sách thư viện Python cần thiết

🚀 Hướng Dẫn Cài Đặt & Chạy Dự Án
Bước 1: Clone Repository về máy
Mở Terminal (hoặc Git Bash) và chạy lệnh sau:

Bash
git clone [https://github.com/nguynhoanggiaviethung-beep/gois1-1109.gi…ttps://github.com/nguynhoanggiaviethung-beep/gois1-1109.git)
cd gois1-1109
Bước 2: Cài đặt các thư viện phụ thuộc
Đảm bảo máy tính đã cài đặt Python (khuyến nghị phiên bản 3.10 trở lên). Cài đặt các thư viện cần thiết bằng lệnh:

Bash
pip install -r requirements.txt
(Hoặc cài đặt thủ công các thư viện cốt lõi: pip install pandas numpy matplotlib seaborn)

Bước 3: Chạy Pipeline xử lý dữ liệu
Mở thư mục dự án bằng VSCode.

Mở file notebooks/10_merge_master.ipynb.

Chạy toàn bộ các ô (Run All) để hệ thống tự động đọc dữ liệu thô từ data_raw/, chuẩn hóa, xử lý lệch tần suất thời gian (Daily/Monthly/Quarterly) và xuất file tổng hợp vào data_clean/master_dataset.csv.

Bước 4: Chạy Phân Tích & Trực Quan Hóa
Khám phá số liệu (EDA): Mở và chạy file notebooks/11_eda_findings.ipynb để xem các bảng thống kê so sánh giữa giai đoạn trước và sau cú sốc thắt chặt (2022–2023).

Xem bộ biểu đồ trực quan (Visual Story): Mở và chạy file notebooks/12_visual_story.ipynb để trực quan hóa toàn bộ 5 biểu đồ trọng tâm:

Chart 1: Cú sốc lãi suất ECB và biến động tỷ giá EUR/USD.

Chart 2: Kênh truyền dẫn qua lãi suất cho vay (Lending Rate).

Chart 3: Quỹ đạo lạm phát HICP của 5 quốc gia so với mục tiêu 2%.

Chart 4: Biến động tăng trưởng GDP thực tế.

Chart 5: Biểu đồ độ dốc (Slope Chart) so sánh tỷ lệ Thất nghiệp Trước vs. Sau khi ECB thắt chặt tiền tệ.
