from sqlalchemy import Integer, String, DateTime, func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    tg_id: Mapped[int] = mapped_column(Integer, primary_key=True) # id пользователя в телеграме
    tg_username: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, nullable=False)

    order: Mapped["Order"] = relationship(
        "Order",
        back_populates="users",
        uselist=True
    )


class Order(Base):
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    music_title: Mapped[Text] = mapped_column(Text, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id'))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders"
    )

