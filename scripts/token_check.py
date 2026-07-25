import sys
from pathlib import Path

# Ensure the repository root is on sys.path so we can import `template` when
# running this script from the `scripts/` directory.
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))
from template import count_tokens
text = ("Hà Nội là thủ đô của Việt Nam, một thành phố có lịch sử hàng nghìn năm và nhiều di tích văn hóa. "
"Trong lòng thành phố, nhịp sống hòa quyện giữa những con phố cổ, những quán cà phê nhỏ và các khu đô thị hiện đại. "
"Người dân nơi đây giữ truyền thống nhưng cũng nhanh chóng thích nghi với thay đổi: xe đạp cũ lặng lẽ nhường đường cho xe máy và ô tô, "
"trong khi các tòa nhà cao tầng và trung tâm thương mại mọc lên san sát. "
"Mùa xuân, các công viên ngập hoa khai phóng, và tiếng chuông chùa vọng vào buổi sớm. "
"Ẩm thực Hà Nội phong phú với phở, bún, chả cá và nhiều món ăn đường phố hấp dẫn. "
"Du khách tới đây thường bị cuốn hút bởi sự giao thoa giữa quá khứ và hiện tại, cùng nhịp sống vừa vội vừa thong thả của người dân địa phương.")
words = len(text.split())
tokens = count_tokens(text, model="gpt-4o")
estimate = words / 0.75
pct_diff = (estimate - tokens) / tokens * 100 if tokens!=0 else 0
print(f"WORDS={words}")
print(f"TOKENS={tokens}")
print(f"ESTIMATE(words/0.75)={estimate:.2f}")
print(f"PCT_DIFF={(pct_diff):.2f}%")
