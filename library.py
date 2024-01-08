def converter(cm: int) -> float:
    if type(cm) is float:
        raise ValueError("Can only convert integer")
    return round(cm * 0.3937008, 1)
