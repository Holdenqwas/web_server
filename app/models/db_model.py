from datetime import datetime
from sqlalchemy import (
    ARRAY,
    UUID,
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    BigInteger,
    Text,
    text,
    types,
    TIMESTAMP
)
from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
)
import uuid
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()


def repr_table(table) -> str:
    output = f"{table.__tablename__}: ("
    for item in dir(table):
        if not item.startswith("_"):
            output += f"\n\t{item}={getattr(table, item)}"
    output += "\n)"
    return output


class TrainingAll(Base):
    __tablename__ = "training_all"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id = Column(BigInteger, nullable=True)
    weight = Column(Float, nullable=True)
    train1_uid = Column(types.Uuid, ForeignKey("train1.uid"), nullable=True)
    train2_uid = Column(types.Uuid, ForeignKey("train2.uid"), nullable=True)
    train3_uid = Column(types.Uuid, ForeignKey("train3.uid"), nullable=True)
    train4_uid = Column(types.Uuid, ForeignKey("train4.uid"), nullable=True)
    train5_uid = Column(types.Uuid, ForeignKey("train5.uid"), nullable=True)

    index_train = Column(Integer, nullable=True)
    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    train1 = relationship("Train1", cascade="all,delete", lazy="noload")
    train2 = relationship("Train2", cascade="all,delete", lazy="noload")
    train3 = relationship("Train3", cascade="all,delete", lazy="noload")
    train4 = relationship("Train4", cascade="all,delete", lazy="noload")
    train5 = relationship("Train5", cascade="all,delete", lazy="noload")

    def __repr__(self) -> str:
        return repr_table(self)


class Train1(Base):
    __tablename__ = "train1"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4 = Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class Train2(Base):
    __tablename__ = "train2"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4 = Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class Train3(Base):
    __tablename__ = "train3"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4 = Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class Train4(Base):
    __tablename__ = "train4"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4 = Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class Train5(Base):
    __tablename__ = "train5"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4 = Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class Users(Base):
    __tablename__ = "users"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    username = Column(Text, unique=True, nullable=True)
    user_id = Column(BigInteger, unique=True)
    vefiry_code = Column(Integer, nullable=True)
    last_date_license = Column(types.DateTime(timezone=True))
    allow_access = Column(Boolean)
    name_trainings = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)
    name_exer_train2 = Column(Text, nullable=True)
    name_exer_train3 = Column(Text, nullable=True)
    name_exer_train4 = Column(Text, nullable=True)
    name_exer_train5 = Column(Text, nullable=True)

    array_shop_list = Column(ARRAY(UUID), nullable=True)
    default_shop_list_uid = Column(UUID, nullable=True)

    date = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)


class ShopList(Base):
    __tablename__ = "shop_list"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text, nullable=False)
    array_user_id = Column(ARRAY(BigInteger), nullable=True)
    items = Column(ARRAY(Text), nullable=True)

    update_time = Column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return repr_table(self)
    

class VerCode(Base):
    __tablename__ = "ver_code"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    code = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)
    expires_at = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return repr_table(self)

def get_model(name: str):
    if name == "train1":
        return Train1
    elif name == "train2":
        return Train2
    elif name == "train3":
        return Train3
    elif name == "train4":
        return Train4
    elif name == "train5":
        return Train5
