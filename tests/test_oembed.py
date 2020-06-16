import json
import pytest
import trioembed
from tests.naive_embedder import NaiveEmbedder


class TestOembed:
    def test_nominal_json(self):
        embedder = NaiveEmbedder()
        embedder.maxwidth = 800
        embedder.maxheight = 600
        response = embedder.respond()

        obj_keys = set(["version", "type", "html", "width", "height"])
        obj = json.loads(response)
        assert set(obj.keys()) == obj_keys
        assert obj['version'] == '1.0'
        assert obj['type'] == 'rich'
        assert obj['width'] == 800
        assert obj['height'] == 600
