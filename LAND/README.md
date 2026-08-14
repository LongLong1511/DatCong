# 🗺️ Bản Đồ Phường Long Hương - QR Code System

Hệ thống bản đồ vệ tinh tương tác với khả năng tạo mã QR để chia sẻ vị trí các thửa đất.

## 🚀 Cách Sử Dụng

### 1. **Trang Chủ**
```
Mở: home.html
```
Trang chủ hiển thị các tùy chọn:
- 🛰️ Bản đồ vệ tinh
- 📱 Tạo mã QR
- 🔲 QR Demo

### 2. **Xem Bản Đồ**
```
Mở: index.html
```
**Hoặc click vào link bản đồ từ home.html**

Tính năng:
- Xem ảnh vệ tinh HD
- Zoom vào các thửa đất
- Tìm kiếm theo số thửa
- Xem tọa độ GPS

### 3. **Tạo Mã QR**
```
Mở: qr-generator.html
```
**Hoặc click vào "Tạo QR" từ home.html**

Hướng dẫn:
1. Nhập thông tin thửa đất (số thửa, tờ, tọa độ)
2. Bấm "🔲 Tạo Mã QR"
3. Tải PNG hoặc sao chép URL
4. Quét mã QR để zoom vào bản đồ

### 4. **QR Demo**
```
URL: index.html?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222
```
Demo thửa đất: **Số 222, Tờ 74**

## 🔗 URL Parameters

Bản đồ hỗ trợ các tham số URL:

| Parameter | Mô Tả | Ví Dụ |
|-----------|-------|-------|
| `lat` | Latitude (Vĩ độ) | `10.482466795764072` |
| `lng` | Longitude (Kinh độ) | `107.15473449851876` |
| `z` | Zoom Level (1-20) | `18` |
| `sothua` | Số thửa đất | `222` |

**Ví dụ URL đầy đủ:**
```
index.html?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222
```

## 📁 Cấu Trúc File

```
LAND/
├── home.html              # 🏠 Trang chủ
├── index.html             # 🗺️ Bản đồ vệ tinh
├── qr-generator.html      # 📱 Tạo mã QR
├── DatCong.geojson        # 📍 Dữ liệu thửa đất
└── README.md              # 📖 File này
```

## ✨ Tính Năng

### Bản Đồ
- ✅ Ảnh vệ tinh Esri HD
- ✅ GeoJSON rendering
- ✅ Tìm kiếm realtime
- ✅ Xem tọa độ GPS
- ✅ Chuyển basemap (OSM, CartoDB)
- ✅ Responsive mobile

### QR Code
- ✅ Tạo QR tự động
- ✅ Tải PNG để in
- ✅ Chia sẻ URL
- ✅ 3 demo thửa đất
- ✅ Thông tin chi tiết

## 🎯 Demo Thửa Đất

### Thửa 222 (Demo 1)
- **Tờ:** 74
- **Tọa độ:** 10.482466795764072, 107.15473449851876
- **Zoom:** 18
- **Link:** `?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222`

### Thửa 291 (Demo 2)
- **Tờ:** 74
- **Tọa độ:** 10.483541447590215, 107.15430162048429
- **Zoom:** 18
- **Link:** `?lat=10.483541447590215&lng=107.15430162048429&z=18&sothua=291`

### Thửa 221 (Demo 3)
- **Tờ:** 74
- **Tọa độ:** 10.483704588398470, 107.15418022536362
- **Zoom:** 18
- **Link:** `?lat=10.483704588398470&lng=107.15418022536362&z=18&sothua=221`

## 📱 QR Code Test

Mã QR demo được tạo sẵn cho thửa 222. Để test:

1. Mở `qr-generator.html`
2. Mã QR tự động được tạo
3. Quét bằng camera điện thoại
4. Bản đồ sẽ mở và zoom vào thửa đất

## 🎨 Màu Sắc

| Loại Đất | Màu | HEX |
|---------|------|-----|
| 🟦 Đất Công | Xanh | #0891b2 |
| 🟩 Đất Nông Nghiệp | Xanh lục | #059669 |
| 🟪 Đất Lâm Nghiệp | Tím | #7c3aed |
| 🟧 Khác | Cam | #ea580c |

## 🌐 Deploy

```bash
# Push to GitHub
git add .
git commit -m "Add QR code system for land plots"
git push origin main
```

URL: `https://username.github.io/LAND/home.html`

## 🚀 Sử Dụng Cục Bộ

```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server

# Mở trực tiếp (trong trình duyệt)
file:///C:\xampp\htdocs\LAND\home.html
```

## 💡 Cách Tạo Mã QR Mới

### Bước 1: Lấy Tọa Độ
1. Mở `index.html`
2. Hover trên thửa đất để xem tọa độ
3. Ghi lại: Latitude, Longitude

### Bước 2: Tạo QR
1. Mở `qr-generator.html`
2. Nhập số thửa, tờ, tọa độ
3. Bấm "🔲 Tạo Mã QR"
4. Tải PNG hoặc copy URL

### Bước 3: Chia Sẻ
- **In mã QR:** Bấm "⬇️ Tải Mã QR (PNG)"
- **Chia sẻ link:** Copy URL bản đồ
- **QR online:** Chia sẻ link qr-generator.html

## 🔍 Tìm Kiếm Thửa Đất

1. Mở `index.html`
2. Sidebar → "🔍 Tìm kiếm..."
3. Gõ số thửa hoặc số tờ
4. Bản đồ sẽ lọc hiển thị

## ⚙️ Công Nghệ

- **Frontend:** HTML5, CSS3, JavaScript ES6+
- **Map:** Leaflet.js
- **Basemaps:** Esri, OpenStreetMap, CartoDB
- **QR Code:** qrcodejs
- **Data:** GeoJSON

## 📖 Hướng Dẫn Chi Tiết

### Quét QR
1. Mở camera trên điện thoại
2. Quét mã QR
3. Bấm link → mở bản đồ
4. Bản đồ sẽ zoom vào thửa đất

### Chia Sẻ URL
1. Mở `qr-generator.html`
2. Tạo QR hoặc chọn demo
3. Copy URL từ "🔗 URL Bản Đồ"
4. Chia sẻ link với người khác

### Tải Mã QR
1. Tạo QR trong `qr-generator.html`
2. Bấm "⬇️ Tải Mã QR (PNG)"
3. File `qr-thuadat.png` sẽ download
4. Có thể in hoặc dán vào tài liệu

## ✅ Kiểm Tra

- [x] Home page tải được
- [x] Bản đồ vệ tinh hiển thị
- [x] QR generator hoạt động
- [x] URL parameters work
- [x] Demo thửa đất zoom đúng
- [x] Mobile responsive
- [x] QR code quét được

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Xóa cache: `Ctrl+Shift+Del`
2. Hard refresh: `Ctrl+F5`
3. Kiểm tra F12 Console

## 📝 Ghi Chú

- Demo thửa 222 được chọn làm ví dụ
- URL parameters hỗ trợ deep linking
- QR code tạo URL đầy đủ
- Mobile responsive trên tất cả thiết bị

---

**Made with ❤️ for Phường Long Hương**
