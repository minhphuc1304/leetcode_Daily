diff --git a/README.md b/README.md
index 12e21281f649bf738165227e2236d24759b02629..57e898269f09badb6e857ceaf47c5ad8bb6a90d9 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,39 @@
-# leetcode_Daily
+# LeetCode Daily
+
+Kho lưu trữ này tổng hợp các lời giải LeetCode được thực hiện mỗi ngày. Mỗi thư mục con tương ứng với một tháng, đặt tên theo định dạng `YYYYMM<Month>` (ví dụ `202501Jan`). Bên trong các thư mục đó là các file solution được đánh số theo ngày tháng `DDMMYY`.
+
+## Cấu trúc thư mục
+
+```
+202501Jan/
+  040125.cpp   # lời giải ngày 04/01/2025 bằng C++
+  050125.py    # lời giải ngày 05/01/2025 bằng Python
+...
+202507July/
+  260725maxSubarrays/
+    Solution.swift
+```
+
+Ngoài ra còn thư mục `Helloworld` chứa ví dụ chương trình C++ đơn giản.
+
+Ví dụ, để biên dịch và chạy chương trình thử nghiệm này:
+
+```bash
+g++ Helloworld/helloworld.cpp -o helloworld && ./helloworld
+```
+
+## Chạy thử
+
+- Với file C++:
+
+  ```bash
+  g++ path/to/file.cpp -o program && ./program
+  ```
+
+- Với file Python:
+
+  ```bash
+  python3 path/to/file.py
+  ```
+
+Repo chỉ mang tính chất lưu trữ và tham khảo các giải pháp cá nhân.
