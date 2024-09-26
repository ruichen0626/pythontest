from datetime import datetime

def calculate_parking_fee(start_time, end_time):
    # 將時間字串轉換為 datetime 物件
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    
    # 計算停車總時間（以小時計）
    total_time = (end - start).total_seconds() / 3600
    
    # 計算費用
    if total_time <= 2:
        fee = total_time * 50
    else:
        fee = 2 * 50 + (total_time - 2) * 30
    
    return fee

# 測試範例
start_time = '2023-10-01 08:00:00'
end_time = '2023-10-01 11:30:00'
fee = calculate_parking_fee(start_time, end_time)
print(f'停車費用: {fee} 元')