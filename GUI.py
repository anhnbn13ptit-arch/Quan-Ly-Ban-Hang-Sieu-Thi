import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector # Thêm thư viện kết nối CSDL

# --- HÀM KẾT NỐI CSDL ---
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Tài khoản mặc định của XAMPP
            password="",        # XAMPP mặc định không có mật khẩu
            database="SieuThi"  # Tên CSDL của bạn
        )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi CSDL", f"Không thể kết nối XAMPP! Hãy chắc chắn đã bật MySQL.\nLỗi: {e}")
        return None

# --- HÀM TẢI DỮ LIỆU LÊN BẢNG ---
def load_data():
    # Xóa dữ liệu cũ trên bảng (nếu có)
    for row in tree.get_children():
        tree.delete(row)
        
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        # Truy vấn lấy dữ liệu từ bảng SAN_PHAM
        cursor.execute("SELECT MaSP, TenSP, DonGia, SoLuongTon FROM SAN_PHAM")
        records = cursor.fetchall()
        
        # Đổ dữ liệu vào Treeview
        for row in records:
            tree.insert("", tk.END, values=row)
            
        conn.close()

# --- CÁC HÀM XỬ LÝ NÚT BẤM (Sẽ code tiếp phần này sau) ---
def them_sp():
    messagebox.showinfo("Thông báo", "Chức năng Thêm đang đợi bạn code lệnh INSERT!")

def cap_nhat_sp():
    messagebox.showinfo("Thông báo", "Chức năng Cập nhật đang đợi bạn code lệnh UPDATE!")

def xoa_sp():
    messagebox.showinfo("Thông báo", "Chức năng Xóa đang đợi bạn code lệnh DELETE!")

def lam_moi():
    txt_ma_sp.delete(0, tk.END)
    txt_ten_sp.delete(0, tk.END)
    txt_gia.delete(0, tk.END)
    txt_so_luong.delete(0, tk.END)
    load_data() # Tải lại bảng

# --- TẠO GIAO DIỆN CHÍNH ---
root = tk.Tk()
root.title("Quản lý sản phẩm siêu thị")
root.geometry("700x450")

lbl_title = tk.Label(root, text="🛒 Quản lý sản phẩm siêu thị", font=("Arial", 16, "bold"))
lbl_title.pack(pady=15)

# Khu vực nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Mã SP:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
txt_ma_sp = tk.Entry(frame_input, width=10)
txt_ma_sp.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Tên SP:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
txt_ten_sp = tk.Entry(frame_input, width=25)
txt_ten_sp.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Giá:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
txt_gia = tk.Entry(frame_input, width=15)
txt_gia.grid(row=0, column=5, padx=5, pady=5)

tk.Label(frame_input, text="Số lượng:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
txt_so_luong = tk.Entry(frame_input, width=10)
txt_so_luong.grid(row=0, column=7, padx=5, pady=5)

# Khu vực nút bấm
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_them = tk.Button(frame_btn, text="Thêm", width=10, command=them_sp)
btn_them.grid(row=0, column=0, padx=10)
btn_cap_nhat = tk.Button(frame_btn, text="Cập nhật", width=10, command=cap_nhat_sp)
btn_cap_nhat.grid(row=0, column=1, padx=10)
btn_xoa = tk.Button(frame_btn, text="Xóa", width=10, command=xoa_sp)
btn_xoa.grid(row=0, column=2, padx=10)
btn_lam_moi = tk.Button(frame_btn, text="Làm mới", width=10, command=lam_moi)
btn_lam_moi.grid(row=0, column=3, padx=10)

# Khu vực bảng hiển thị
frame_tree = tk.Frame(root)
frame_tree.pack(pady=10, fill="both", expand=True)

columns = ("Mã SP", "Tên sản phẩm", "Giá", "Số lượng")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings", height=10)

tree.heading("Mã SP", text="Mã SP")
tree.column("Mã SP", width=80, anchor="center")
tree.heading("Tên sản phẩm", text="Tên sản phẩm")
tree.column("Tên sản phẩm", width=200, anchor="w")
tree.heading("Giá", text="Giá")
tree.column("Giá", width=100, anchor="center")
tree.heading("Số lượng", text="Số lượng")
tree.column("Số lượng", width=80, anchor="center")
tree.pack()

# --- KHỞI ĐỘNG ---
# Đảm bảo XAMPP đang chạy trước khi gọi hàm này!
load_data()

root.mainloop()
