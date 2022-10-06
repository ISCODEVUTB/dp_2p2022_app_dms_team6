

import pytest
from interfaces.multimedia import IMultimedia
from interfaces.online import IOnLine
from interfaces.pdf import IPdf


def test_imultimedia_class():
    IMultimedia.__abstractmethods__ = frozenset()
    multimedia = IMultimedia()

    with pytest.raises(NotImplementedError, match='Play is not implemented'):
        multimedia.play()


def test_ipdf_class():
    IPdf.__abstractmethods__ = frozenset()
    pdf = IPdf()

    with pytest.raises(NotImplementedError, match='Operation is not implemented'):
        pdf.operation()


def test_ionline_class():
    IOnLine.__abstractmethods__ = frozenset()
    pdf = IOnLine()

    with pytest.raises(NotImplementedError, match='Download is not implemented'):
        pdf.download()
