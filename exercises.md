# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 14h00–18h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.7, 1.2 và 1.8 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Hà Nội."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi? Ở mức nào phản hồi bắt đầu
kém mạch lạc?** (2–3 câu)
> Temp :0.0 và 0.7 cho câu trả lời chung chung chưa rõ kết quả
Temp 1.2 trả lời không đúng trọng tâm
Temp 1.8 thì cho kết quả rõ ràng


### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý,
và bao nhiêu cho trợ lý viết slogan quảng cáo? Giải thích khác biệt.**
> Nếu dùng trợ lý soạn thảo hợp đồng pháp lý thì temp 0.0-0.2 vì nó có sự an toàn dù câu trả lời đưa ra khá chậm,còn trợ lý viết slohgan quảng cáo thì temp từ 0.8-1.0.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 20.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 2 lần,
mỗi lần trung bình ~500 token đầu ra.

**Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này
(dựa trên bảng giá trong template). Nêu một trường hợp model lớn xứng đáng
với chi phí và một trường hợp model nhỏ là lựa chọn đúng:**
> Nếu mà cần độ chính xác,đưa ra kết quả nhanh,chuyên môn cao hơn thì model lớn sẽ phù hợp,còn nếu trong những công việc trả lời đơn giản và ít phức tạp thì model nhỏ sẽ là lựa chọn đúng.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích máy học (machine learning) là gì?"** nhưng hai system prompt
khác nhau:
- "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
- "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."

**Hai phản hồi khác nhau như thế nào (giọng văn, độ dài, mức kỹ thuật)?
Từ đó rút ra system prompt điều khiển được những khía cạnh nào của phản hồi?**
(3–4 câu)
> Với promt nhà thơ thì model trả về giọng văn bay bổng hơn,trữ tình hơn.Còn với promt của kỹ sư senior thì câu trả lời nghiêm túc hơn,chính xác hơn. Từ đó ta thấy system promt có thể điều khiển được về phong cách trình bày với các câu hỏi có những yêu cầu khác nhau.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~150 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Nếu dùng ước lượng thô để dự
toán ngân sách API cho ứng dụng tiếng Việt, bạn sẽ dự toán thiếu hay thừa —
và vì sao?**
> Words = 160 từ(tokens = 211),estimate = word/0.75 = 2113.33,lớn hơn token thực 1.11%.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Xét ba ứng dụng: (a) chatbot văn bản, (b) trợ lý giọng nói đọc to phản hồi,
(c) pipeline dịch tài liệu chạy ngầm ban đêm. Ứng dụng nào hưởng lợi nhiều
nhất từ streaming, ứng dụng nào không cần — và tại sao?** (1 đoạn văn)
> Trợ lý giọng nói (b) hưởng lợi nhiều nhất: streaming cho phép bắt đầu phát âm ngay khi model sinh token đầu tiên, giảm độ trễ cảm nhận và cải thiện trải nghiệm nghe thực‑thời (đặc biệt với phản hồi dài). Chatbot văn bản (a) cũng có lợi nhưng ở mức vừa phải — streaming giúp UI hiện dần nội dung, tăng cảm giác tương tác, nhất là với câu trả lời dài; tuy nhiên với phản hồi ngắn lợi ích nhỏ. Pipeline dịch tài liệu chạy ngầm ban đêm (c) hầu như không cần streaming vì xử lý theo batch/offline, ưu tiên độ chính xác và throughput hơn là độ trễ hiển thị; dùng streaming ở đây chỉ làm tăng phức tạp mà ít mang lại giá trị.


### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**Khi API quá tải và hàng nghìn client cùng retry, exponential backoff giúp
gì so với delay cố định? Tra cứu thêm: kỹ thuật "jitter" (thêm độ trễ ngẫu
nhiên) giải quyết vấn đề gì còn sót lại?**
> Exponential backoff làm giảm tải khẩn cấp bằng cách tăng dần khoảng chờ giữa các lần retry (ví dụ 1s, 2s, 4s…), nên tổng số request trong khoảng thời gian ngắn giảm và hệ thống có thời gian phục hồi. Jitter (thêm độ trễ ngẫu nhiên) phá khả năng các client đồng bộ retry cùng lúc, tránh xảy ra “thundering herd” sau khi nhiều client đều backoff giống nhau — kết hợp cả hai là best practice khi xử lý retry ở hệ phân tán.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Viết lại system prompt bạn dùng cho trợ lý của mình. Chỉ ra 2 chỗ trong
prompt mà nếu xóa đi, hành vi trợ lý sẽ thay đổi rõ rệt — và mô tả thay đổi
đó:**
System prompt tôi dùng: "Bạn là một trợ lý kỹ thuật thân thiện, trả lời bằng tiếng Việt rõ ràng và cô đọng; khi câu hỏi mang tính kỹ thuật, đưa ví dụ code ngắn và chỉ ra bước tiếp theo hành động; luôn kiểm tra giả định trước khi trả lời và hỏi lại nếu thiếu thông tin."
> Nếu xóa phần "trả lời bằng tiếng Việt rõ ràng và cô đọng" → trợ lý có thể trả lời dài dòng, đa ngôn ngữ hoặc dùng phong cách không phù hợp với người dùng VN.
Nếu xóa phần "khi câu hỏi mang tính kỹ thuật, đưa ví dụ code ngắn" → trợ lý sẽ không cung cấp ví dụ thực tế, làm giảm tính hữu dụng cho người cần hướng dẫn triển khai.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn giữ history 4 lượt cuối. Hãy mô tả một tình huống hội thoại
cụ thể mà giới hạn này khiến trợ lý trả lời sai/mất ngữ cảnh, và đề xuất một
cách khắc phục (ví dụ: tóm tắt các lượt cũ, tăng giới hạn có chọn lọc...):**
> Tình huống: trong một phiên support, user mô tả chi tiết yêu cầu ở lượt 1–3 rồi hỏi ở lượt 7 một câu phụ thuộc vào thông tin ở lượt 2; vì chỉ giữ 4 lượt cuối, trợ lý đã bị cắt mất lượt có thông tin quan trọng và trả lời sai hoặc yêu cầu user nhắc lại.
Khắc phục: trước khi cắt history, tóm tắt (compress) các lượt cũ quan trọng thành 1–2 câu ngắn (summary) và lưu summary vào history; hoặc đánh dấu/ghi nhớ các "facts" quan trọng (ví dụ cấu hình, tên dịch vụ) và ưu tiên giữ các message đánh dấu khi cắt history. Phương án này giữ bối cảnh thiết yếu mà không tăng nhiều token.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên GitHub cá nhân và nộp link repo vào vlearn (theo hướng dẫn README)
