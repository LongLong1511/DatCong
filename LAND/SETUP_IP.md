# 🚀 Hướng Dẫn Truy Cập qua IP 192.168.0.38

Hướng dẫn chi tiết để chạy server và truy cập bản đồ qua IP cục bộ.

---

## 📋 Yêu Cầu

- Python 3.6+ (đã cài đặt)
- Folder LAND tại: `C:\xampp\htdocs\LAND`
- Kết nối mạng hoạt động

---

## 🚀 Cách 1: Chạy Batch File (Dễ Nhất)

### Bước 1: Mở Batch File
```
Mở file: C:\xampp\htdocs\LAND\start-server.bat
```

Hoặc double-click:
```
start-server.bat
```

### Bước 2: Chờ Server Khởi Động
```
========================================
🗺️  Phường Long Hương - Bản Đồ Vệ Tinh
========================================

📡 Server đang chạy trên cổng 8000

🔗 Các URL để truy cập:

   Local (máy này):
   → http://localhost:8000
   → http://127.0.0.1:8000

   Từ máy khác cùng mạng:
   → http://192.168.0.38:8000

📍 Trang chủ:
   → http://192.168.0.38:8000/home.html
```

### Bước 3: Truy Cập
Mở trình duyệt và truy cập:
```
http://192.168.0.38:8000
```

---

## 🚀 Cách 2: Chạy Python Trực Tiếp

### Bước 1: Mở Terminal
```
Win + R → cmd → Enter
```

Hoặc PowerShell:
```
Win + X → PowerShell (Admin)
```

### Bước 2: Chuyển Đến Folder LAND
```bash
cd C:\xampp\htdocs\LAND
```

### Bước 3: Chạy Server
```bash
python server.py
```

### Bước 4: Chờ Và Truy Cập
```
http://192.168.0.38:8000
```

---

## 🚀 Cách 3: Dùng Python HTTP Server (Cơ Bản)

Nếu không muốn dùng script custom:

```bash
# Chuyển đến folder LAND
cd C:\xampp\htdocs\LAND

# Chạy HTTP server
python -m http.server 8000
```

---

## 🌐 Các URL Để Truy Cập

### Từ Máy Chính (PC Chạy Server)
```
Local:
http://localhost:8000
http://127.0.0.1:8000
```

### Từ Máy Khác (Điện Thoại, Laptop)
```
Trong mạng LAN:
http://192.168.0.38:8000
http://192.168.0.38:8000/home.html
http://192.168.0.38:8000/index.html
http://192.168.0.38:8000/qr-generator.html
```

---

## 📱 Truy Cập Từ Điện Thoại

### Bước 1: Chắc Chắn Cùng Mạng
```
Điện thoại phải kết nối WiFi cùng network với PC
```

### Bước 2: Mở Trình Duyệt
```
Chrome, Safari, Firefox, v.v.
```

### Bước 3: Nhập URL
```
http://192.168.0.38:8000
```

### Bước 4: Xem Bản Đồ
```
Bản đồ sẽ tải và hiển thị trên điện thoại
```

---

## 🔒 Lưu Ý Bảo Mật

⚠️ **Cảnh báo:**
- Server chỉ chạy trên mạng LAN cục bộ (an toàn)
- Không nên chạy trên Internet công cộng
- Để dừng server: `Ctrl + C` trong terminal

---

## 🐛 Xử Lý Sự Cố

### "Port 8000 đang được sử dụng"
**Giải pháp:**
```bash
# Sử dụng cổng khác
python -m http.server 8001
python -m http.server 9000
```

### "Không thể truy cập từ điện thoại"
**Kiểm tra:**
1. ✓ Điện thoại kết nối cùng WiFi?
2. ✓ IP đúng là 192.168.0.38?
3. ✓ Server đang chạy?
4. ✓ Firewall cho phép port 8000?

### "Lỗi Python không tìm thấy"
**Giải pháp:**
```bash
# Dùng đường dẫn đầy đủ
C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe server.py
```

Hoặc cài đặt lại Python:
- Download từ https://python.org
- Chọn "Add Python to PATH"

### "Bản đồ không tải"
**Kiểm tra:**
1. F12 → Console → xem error
2. Kiểm tra file DatCong.geojson tồn tại
3. Hard refresh: `Ctrl + F5`

---

## 📊 Tốc Độ Mạng

### Nhanh Nhất
```
PC → LAN → PC
(Cáp Ethernet trực tiếp)
```

### Bình Thường
```
PC WiFi → Router → Điện thoại WiFi
(Mạng WiFi)
```

### Chậm Hơn
```
Qua router yếu hoặc WiFi xa
```

---

## 🔄 Cập Nhật Bản Đồ

Khi sửa file:

### Bước 1: Dừng Server
```
Nhấn Ctrl + C trong terminal
```

### Bước 2: Sửa File
```
Chỉnh sửa index.html, DatCong.geojson, etc.
```

### Bước 3: Chạy Lại Server
```bash
python server.py
```

### Bước 4: Refresh Trình Duyệt
```
Ctrl + F5 (Hard refresh)
```

---

## 📦 Tệp Cần Thiết

```
C:\xampp\htdocs\LAND\
├── server.py              # ← Script server
├── start-server.bat       # ← Batch file
├── home.html              # Trang chủ
├── index.html             # Bản đồ
├── qr-generator.html      # QR generator
├── DatCong.geojson        # Dữ liệu
└── README.md              # Hướng dẫn
```

---

## 📝 Ví Dụ Đầy Đủ

### Quy Trình Hoàn Chỉnh

```
1. Mở start-server.bat (hoặc chạy python server.py)
   
2. Chờ "Server đang chạy..."

3. Mở trình duyệt → http://192.168.0.38:8000

4. Thấy home.html → Click vào các link

5. Xem bản đồ, tạo QR, quét code

6. Chia sẻ URL/QR với người khác cùng mạng

7. Dừng server: Ctrl + C
```

---

## 🎯 Test Nhanh

### Local Test
```bash
# Terminal 1: Chạy server
python server.py

# Terminal 2 (hoặc trình duyệt): Test
curl http://localhost:8000
# hoặc
http://127.0.0.1:8000
```

### Network Test
```
Điện thoại/Laptop: http://192.168.0.38:8000
```

---

## 🌍 IP Của Bạn

Để tìm IP chính xác:

### Windows (CMD)
```bash
ipconfig
```

Tìm dòng "IPv4 Address:" → ghi lại IP

Ví dụ:
```
IPv4 Address. . . . . . . . . . . : 192.168.0.38
```

### Hoặc Từ Terminal Khi Server Chạy
```
Server sẽ hiển thị IP tự động:
→ http://192.168.0.38:8000
```

---

## ✅ Checklist

- [x] Python 3.6+ cài đặt
- [x] Folder LAND tại C:\xampp\htdocs\LAND
- [x] File server.py tồn tại
- [x] File start-server.bat tồn tại
- [x] DatCong.geojson có dữ liệu
- [x] Cổng 8000 không bị dùng
- [x] Firewall cho phép port 8000
- [x] Mạng hoạt động

---

## 🚀 Bắt Đầu Ngay

### Cách Nhanh Nhất
```
1. Double-click: start-server.bat
2. Chờ console hiển thị IP
3. Mở trình duyệt: http://192.168.0.38:8000
4. Xong! 🎉
```

---

**Nếu gặp vấn đề, kiểm tra F12 Console trong trình duyệt!**

---

**Hài Lòng! Server sẵn sàng chạy! 🗺️**
