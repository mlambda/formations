from sqlalchemy import select

user = session.scalars(select(User).where(User.name == "hugo")).first()
