from sqlalchemy import Column, Boolean, Float, String, Text, ForeignKey, select, text, types
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


class TrainingAll(Base):
    __tablename__ = "training_all"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    user_name = Column(Text, nullable=False)
    weight = Column(Float, nullable=True)
    train1_uid = Column(types.Uuid, ForeignKey('train1.uid'), nullable=True)
    train2_uid = Column(types.Uuid, ForeignKey('train2.uid'), nullable=True)
    train3_uid = Column(types.Uuid, ForeignKey('train3.uid'), nullable=True)
    train4_uid = Column(types.Uuid, ForeignKey('train4.uid'), nullable=True)
    train5_uid = Column(types.Uuid, ForeignKey('train5.uid'), nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())

    train1 = relationship("Train1")
    train2 = relationship("Train2")
    train3 = relationship("Train3")
    train4 = relationship("Train4")
    train5 = relationship("Train5")

    def __repr__(self) -> str:
        return repr_table(self)


class Train1(Base):
    __tablename__ = "train1"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4= Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training")

    def __repr__(self) -> str:
        return repr_table(self)

class Train2(Base):
    __tablename__ = "train2"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4= Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training")

    def __repr__(self) -> str:
        return repr_table(self)

class Train3(Base):
    __tablename__ = "train3"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4= Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training")

    def __repr__(self) -> str:
        return repr_table(self)

class Train4(Base):
    __tablename__ = "train4"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4= Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training")

    def __repr__(self) -> str:
        return repr_table(self)

class Train5(Base):
    __tablename__ = "train5"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    ex1 = Column(Float, nullable=True)
    ex2 = Column(Float, nullable=True)
    ex3 = Column(Float, nullable=True)
    ex4= Column(Float, nullable=True)
    ex5 = Column(Float, nullable=True)
    ex6 = Column(Float, nullable=True)
    ex7 = Column(Float, nullable=True)
    ex8 = Column(Float, nullable=True)
    ex9 = Column(Float, nullable=True)
    ex10 = Column(Float, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    training = relationship("Training")

    def __repr__(self) -> str:
        return repr_table(self)

class Users(Base):
    __tablename__ = "users"

    uid: Mapped[uuid.UUID] = mapped_column(
        types.Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name = Column(Text, unique=True)
    last_date_license = Column(types.DateTime(timezone=True))
    allow_access = Column(Boolean)
    name_trainings = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)
    name_exer_train1 = Column(Text, nullable=True)

    date = Column(types.DateTime(timezone=True), server_default=func.now(),
                  server_onupdate=func.now())

    def __repr__(self) -> str:
        return repr_table(self)


def get_model(name: str):
    if name == "breast":
        return Breast
    elif name == "beak":
        return Beak
    elif name == "leg":
        return Leg
    elif name == "train1":
        return Train1
    elif name == "train2":
        return Train2
    elif name == "train3":
        return Train3
    elif name == "train4":
        return Train4
    elif name == "train5":
        return Train5
