from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, select, text, types
from sqlalchemy.orm import declarative_base, DeclarativeBase, Mapped, MappedAsDataclass, mapped_column
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


class Training(Base):
    __tablename__ = "training"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    weight = Column(Float, nullable=True)
    leg_uid = Column(types.Uuid, ForeignKey('leg.uid'), nullable=True)
    beak_uid = Column(types.Uuid, ForeignKey("beak.uid"), nullable=True)
    breast_uid = Column(types.Uuid, ForeignKey('breast.uid'), nullable=True)
    date = Column(types.DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    name_training = Column(String, nullable=True)

    breast = relationship("Breast", back_populates="training")
    beak = relationship("Beak", back_populates="training")
    leg = relationship("Leg", back_populates="training")

    def __repr__(self) -> str:
        return repr_table(self)


class Breast(Base):
    __tablename__ = "breast"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    bench_press = Column(Float, nullable=True)
    bench_press_inclined = Column(Float, nullable=True)
    pullover = Column(Float, nullable=True)
    dumbbells = Column(Float, nullable=True)
    block = Column(Float, nullable=True)
    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training", back_populates="breast")

    def __repr__(self) -> str:
        return repr_table(self)


class Beak(Base):
    __tablename__ = "beak"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    triceps_bench_press = Column(Float, nullable=True)
    french_bench_press = Column(Float, nullable=True)
    kettlebell = Column(Float, nullable=True)
    gravitron = Column(Float, nullable=True)
    upper_block = Column(Float, nullable=True)
    lower_block = Column(Float, nullable=True)
    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training", back_populates="beak")

    def __repr__(self) -> str:
        return repr_table(self)


class Leg(Base):
    __tablename__ = "leg"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    army_bench_press = Column(Float, nullable=True)
    craving_for_chin = Column(Float, nullable=True)
    head_press = Column(Float, nullable=True)
    knee_bend = Column(Float, nullable=True)
    platform_press = Column(Float, nullable=True)
    extension_of_block = Column(Float, nullable=True)
    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training", back_populates="leg")

    def __repr__(self) -> str:
        return repr_table(self)


def get_model(name: str):
    if name == "breast":
        return Breast
    elif name == "beak":
        return Beak
    elif name == "leg":
        return Leg
