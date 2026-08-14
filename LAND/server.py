#!/usr/bin/env python3
"""
Simple HTTP Server for Phường Long Hương Map
Runs on 192.168.0.38:8000 (or any available IP)
"""

import http.server
import socketserver
import os
import socket
import sys

# Cấu hình
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Thêm headers để tránh cache
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

def get_ip_address():
    """Lấy IP address cục bộ"""
    try:
        # Cách 1: Kết nối đến một server ngoài để lấy IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        try:
            # Cách 2: Lấy hostname
            return socket.gethostbyname(socket.gethostname())
        except:
            return "127.0.0.1"

if __name__ == "__main__":
    os.chdir(DIRECTORY)

    # Tạo server
    handler = MyHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            ip = get_ip_address()

            print("\n" + "="*60)
            print("🗺️  Phường Long Hương - Bản Đồ Vệ Tinh")
            print("="*60)
            print(f"\n📡 Server đang chạy trên cổng {PORT}")
            print(f"\n🔗 Các URL để truy cập:\n")
            print(f"   Local (máy này):")
            print(f"   → http://localhost:{PORT}")
            print(f"   → http://127.0.0.1:{PORT}\n")
            print(f"   Từ máy khác cùng mạng:")
            print(f"   → http://{ip}:{PORT}")
            print(f"   → http://192.168.0.38:{PORT}\n")
            print(f"📍 Trang chủ:")
            print(f"   → http://192.168.0.38:{PORT}/home.html")
            print(f"   → http://192.168.0.38:{PORT}/index.html")
            print(f"   → http://192.168.0.38:{PORT}/qr-generator.html\n")
            print(f"📁 Thư mục: {DIRECTORY}")
            print(f"\n⚠️  Nhấn Ctrl+C để dừng server")
            print("="*60 + "\n")

            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\n🛑 Server đã dừng")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Port already in use
            print(f"\n❌ Lỗi: Cổng {PORT} đang được sử dụng")
            print(f"   Vui lòng đóng chương trình khác hoặc sử dụng cổng khác")
        else:
            print(f"\n❌ Lỗi: {e}")
        sys.exit(1)
