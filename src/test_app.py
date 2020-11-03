from app import index
from datetime import datetime


def test_index():
    assert index() == "Hello, world! " +datetime.now().strftime("%d/%m/%Y %H:%M:%SS")

