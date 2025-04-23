from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.config.database import get_async_db  # Đường dẫn tùy project của bạn
import asyncio
router = APIRouter()


@router.get("/healthcheck")
async def healthcheck(db: AsyncSession = Depends(get_async_db)):
    try:
        # Kiểm tra kết nối DB
        await db.execute(text("SELECT 1"))
        await asyncio.sleep(1)
        return {
            "status": "ok",
            "db_checked": True,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "db_checked": False
        }
