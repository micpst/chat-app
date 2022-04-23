from typing import Any, Dict


def to_dict(model: Any) -> Dict[str, Any]:
    return {column: getattr(model, column) for column in model.__table__.c.keys()}
