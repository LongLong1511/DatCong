# 🗺️ Phường Long Hương - Bản Đồ Vệ Tinh

Ứng dụng web bản đồ vệ tinh tương tác cho Phường Long Hương, Quận 7, TP.HCM.

🔗 **Live Demo**: [Xem bản đồ trực tuyến](./home.html)

---

## ✨ Tính Năng

| Tính Năng | Chi Tiết |
|----------|---------|
| 🛰️ **Bản Đồ Vệ Tinh** | Ảnh vệ tinh HD từ Esri |
| 🔍 **Tìm Kiếm** | Tìm kiếm thửa đất theo số thửa |
| 📍 **Xem Tọa Độ** | Hiển thị GPS khi hover |
| 📱 **QR Code** | Tạo mã QR để chia sẻ vị trí |
| 🎯 **Deep Linking** | URL trực tiếp zoom vào thửa đất |
| 📱 **Mobile First** | Responsive design, hiệu ứng mượt mà |
| ⚡ **Nhanh** | Không cần backend, tĩnh 100% |

---

## 🚀 Cách Sử Dụng

### Mở Bản Đồ

1. Bấm vào **"📍 Mở Bản Đồ"** từ trang chủ
2. Hoặc truy cập trực tiếp: [index.html](./index.html)

### Tìm Kiếm Thửa Đất

1. Mở sidebar: bấm nút **"☰"** góc trên trái
2. Nhập số thửa hoặc số tờ
3. Kết quả sẽ lọc hiển thị

### Tạo Mã QR

1. Bấm **"🔲 Tạo QR"** từ trang chủ
2. Nhập tọa độ và zoom level
3. Tạo QR → Tải PNG hoặc copy URL
4. Quét QR trên điện thoại để zoom vào bản đồ

### Xem Demo

Thửa đất demo: **Số 222, Tờ 74**
- [Xem trực tiếp](./index.html?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222)

---

## 📁 Cấu Trúc File

```
📦 LAND/
├── 📄 home.html              # Trang chủ chính
├── 📄 index.html             # Bản đồ vệ tinh
├── 📄 qr-generator.html      # Tạo mã QR
├── 📊 DatCong.geojson        # Dữ liệu thửa đất
└── 📖 README.md              # File này
```

---

## 🔗 URL Tham Số

Bản đồ hỗ trợ URL parameters để zoom vào vị trí cụ thể:

```
index.html?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222
```

| Parameter | Mô Tả | Ví Dụ |
|-----------|-------|-------|
| `lat` | Latitude (Vĩ độ) | `10.482466795764072` |
| `lng` | Longitude (Kinh độ) | `107.15473449851876` |
| `z` | Zoom Level (1-20) | `18` |
| `sothua` | Số thửa đất | `222` |

---

## 🎨 Thiết Kế Mobile

✅ **Mobile-First Design**
- Thẻ card rộng full màn hình
- Nút bấm tối thiểu 44x44px
- Sidebar ẩn/hiện mượt mà
- Safe area support (iPhone X+)

✅ **Responsive Breakpoints**
- Mobile: < 480px
- Phablet: < 768px
- Tablet: ≥ 768px
- Desktop: ≥ 1024px

---

## 🛠️ Công Nghệ

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Map Library**: Leaflet.js
- **Basemaps**: Esri, OpenStreetMap, CartoDB
- **QR Code**: qrcodejs
- **Data Format**: GeoJSON
- **Hosting**: GitHub Pages (100% static)

---

## 📊 Demo Thửa Đất

| Thửa | Tờ | Tọa Độ | Zoom | Link |
|------|----|----|------|------|
| 222 | 74 | 10.48, 107.15 | 18 | [Xem](index.html?lat=10.482466795764072&lng=107.15473449851876&z=18&sothua=222) |
| 291 | 74 | 10.48, 107.15 | 18 | [Xem](index.html?lat=10.483541447590215&lng=107.15430162048429&z=18&sothua=291) |
| 221 | 74 | 10.48, 107.15 | 18 | [Xem](index.html?lat=10.483704588398470&lng=107.15418022536362&z=18&sothua=221) |

---

## 🚀 Deploy lên GitHub Pages

### Bước 1: Tạo Repository
```bash
git init
git add .
git commit -m "Initial commit: Phuong Long Huong Map"
git remote add origin https://github.com/YOUR_USERNAME/LAND.git
git push -u origin main
```

### Bước 2: Enable GitHub Pages
1. Vào **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, Folder: `/ (root)`
4. Bấm **Save**

### Bước 3: Truy Cập
```
https://YOUR_USERNAME.github.io/LAND/
```

---

## 📱 Truy Cập

### Desktop
- Chrome, Firefox, Safari, Edge

### Mobile
- iOS 12+ (Safari, Chrome)
- Android 5+ (Chrome, Firefox)

### QR Code
- Quét mã QR từ ứng dụng Camera hoặc QR Scanner

---

## 🐛 Xử Lý Sự Cố

### "Bản đồ không tải"
- Xóa cache: `Ctrl+Shift+Del`
- Hard refresh: `Ctrl+F5`
- Kiểm tra F12 → Console

### "Không truy cập được từ điện thoại"
- Kiểm tra URL đúng: `https://username.github.io/LAND/`
- Đợi 1-2 phút GitHub Pages deploy
- Refresh trang: `Ctrl+F5`

### "QR không quét được"
- Kiểm tra QR có hình chữ nhật đủ
- Đảm bảo ánh sáng tốt
- Sử dụng ứng dụng Camera native

---

## 📝 Cập Nhật Dữ Liệu

### Thêm Thửa Đất Mới

1. Chỉnh sửa `DatCong.geojson`
2. Thêm GeoJSON feature mới
3. Commit & push

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[...]]
  },
  "properties": {
    "Sothua": "123",
    "So_To": 74
  }
}
```

### Thêm Basemap Mới

Sửa trong `index.html`, function `BASEMAPS`:
```javascript
'tên_basemap': {
  url: 'https://url-tiles/{z}/{x}/{y}.png',
  attribution: '© Source'
}
```

---

## 🎯 Roadmap

- [x] Bản đồ vệ tinh cơ bản
- [x] Tìm kiếm thửa đất
- [x] Tạo mã QR
- [x] Mobile responsive
- [x] GitHub Pages deploy
- [ ] Layers (đất công, đất nông nghiệp, etc.)
- [ ] Measurement tool
- [ ] Export GeoJSON
- [ ] Offline mode

---

## 📄 License

MIT License - Xem chi tiết trong file LICENSE

---

## 👤 Tác Giả

Dự án được phát triển cho **Phường Long Hương, Quận 7, TP.HCM**

---

## 🤝 Đóng Góp

Mọi đóng góp đều được chào đón! 

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push branch: `git push origin feature/name`
5. Tạo Pull Request

---

## 📞 Liên Hệ

- 📧 Email: [Liên hệ]
- 🐛 Issues: [GitHub Issues](../../issues)
- 💬 Discussions: [GitHub Discussions](../../discussions)

---

## 📚 Tài Liệu

- [Leaflet Documentation](https://leafletjs.com)
- [GeoJSON Specification](https://geojson.org)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [MDN Web Docs](https://developer.mozilla.org)

---

## ⭐ Stars

Nếu bạn thích dự án này, hãy cho ⭐!

```
⭐ Star: https://github.com/YOUR_USERNAME/LAND
🍴 Fork: https://github.com/YOUR_USERNAME/LAND/fork
```

---

**Made with ❤️ for Phường Long Hương**

*v1.0 - 2024*
