from fastapi.logger import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base 
from app.config.config import settings
# logger.info(f"DATABASE_URL in database.py: {settings.DATABASE_URL} ({type(settings.DATABASE_URL)})")
# DATABASE_URL = "mysql+aiomysql://root:12345@localhost/sakila"
# Tạo engine bất đồng bộ
engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=300,        
    max_overflow=200,       
    pool_timeout=30.0,     
    pool_recycle=1800,
    pool_pre_ping=True,
    echo=True,
)

# Tạo async session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,  # Tắt autoflush để tăng performance
    future=True       # Bật tính năng tương lai của SQLAlchemy 2.0
)

# Base dùng như bình thường
Base = declarative_base()

# Hàm lấy session async
async def get_async_db():
    session = async_session()
    try:
        yield session
    finally:
        await session.close()  # Quan trọng: luôn đảm bảo session được đóng
