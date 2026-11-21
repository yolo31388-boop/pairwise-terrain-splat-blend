import pytest
import math
from render import terrain_splat_blend as mod

CASES = [
    ("sum", 'm.weight_sum([1, 2, 3]) == 6'),
    ("norm", 'm.normalize([1, 1, 2]) == approx([0.25, 0.25, 0.5])'),
    ("top", 'm.top_layer([1, 3, 2]) == 1'),
    ("wrap", 'm.wrap_u(1.2) == approx(0.2)'),
    ("blend", 'm.blend_scalar(0, 10, 0.5) == 5'),
    ("mip", 'm.mip(8) == 3'),
    ("precision", 'm.precision(8) == 256'),
    ("slope", 'm.slope_weight(1) == approx(0.5)'),
    ("tri", 'm.triplanar((0, 0, 2)) == approx([0, 0, 1])'),
    ("shadow", 'm.shadow(True) is True'),
    ("fade", 'm.fade(5, 10) == approx(0.5)'),
    ("key", 'm.key(4) == "tile:4"'),
    ("clamp", 'm.clamp01(1.2) == 1.0'),
    ("count", 'm.count([1, 2]) == 2'),
    ("index", 'm.layer_index([1, 3, 2]) == 1')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
