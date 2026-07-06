import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import PrintQueue, pages_left, printer, processed


def test_printer_queue_challenge():
    assert isinstance(printer, PrintQueue)
    assert processed == ["invoice", "notes", "slides"]
    assert pages_left == 20
