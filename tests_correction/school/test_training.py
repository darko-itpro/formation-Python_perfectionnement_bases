import pytest
from demos.obj.school import Training

def test_create_training():
    training = Training("essentiel python", 5)
    assert training.subject == 'Essentiel Python'
    assert len(training.students) == 0

def test_traininig_low_duration_must_raise():
    with pytest.raises(ValueError, match="duration"):
        Training("essentiel python", 0)
