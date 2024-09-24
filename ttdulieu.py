import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn tệp CSV

# Đọc tệp CSV với dấu phân cách là dấu chấm phẩy ';'
df_cleaned = pd.read_csv('AirQuality.csv', delimiter=';')

# Chuyển đổi các cột số từ chuỗi với dấu phẩy thành giá trị số đúng
for col in ['CO(GT)', 'C6H6(GT)', 'T', 'RH', 'AH']:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col].str.replace(',', '.'), errors='coerce')

# Chuyển đổi cột Date và Time thành định dạng datetime
df_cleaned['Datetime'] = pd.to_datetime(df_cleaned['Date'] + ' ' + df_cleaned['Time'], format='%d/%m/%Y %H.%M.%S')

# Vẽ biểu đồ các tham số CO(GT), Temperature, và Relative Humidity theo thời gian
plt.figure(figsize=(14, 7))

# Biểu đồ nồng độ CO
plt.subplot(3, 1, 1)
plt.plot(df_cleaned['Datetime'], df_cleaned['CO(GT)'], label='CO(GT)', color='blue')
plt.title('Nồng độ CO theo thời gian')
plt.ylabel('CO(GT) [mg/m^3]')

# Biểu đồ nhiệt độ
plt.subplot(3, 1, 2)
plt.plot(df_cleaned['Datetime'], df_cleaned['T'], label='Nhiệt độ', color='red')
plt.title('Nhiệt độ theo thời gian')
plt.ylabel('Nhiệt độ [°C]')

# Biểu đồ độ ẩm tương đối
plt.subplot(3, 1, 3)
plt.plot(df_cleaned['Datetime'], df_cleaned['RH'], label='Độ ẩm tương đối', color='green')
plt.title('Độ ẩm tương đối theo thời gian')
plt.ylabel('RH [%]')
plt.xlabel('Thời gian')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
