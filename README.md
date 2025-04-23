#Cấu hình Alembic:
alembic init alembic
Mở file alembic.ini và chỉnh sửa dòng sau để trỏ tới database của bạn:
sqlalchemy.url = mysql+aiomysql://root:password@localhost/yourdb
Trong file alembic/env.py, bạn cần import các model để Alembic có thể tạo migration từ chúng.
from myapp.models import Base  # Thêm dòng này
target_metadata = Base.metadata
. Tạo Migration Files:
Sau khi bạn định nghĩa các models, bạn có thể tạo migration file để theo dõi thay đổi.
alembic revision --autogenerate -m "Create users table"
Áp dụng Migration vào Database:
alembic upgrade head
