import hmac

import pytest

from supplemental import randomness
from supplemental.key_derivation import derive_demo_keys


def test_three_way_counts_show_modulo_bias():
    assert randomness.three_way_counts() == ([3, 3, 2], [2, 2, 2])


def test_choose_bucket_uses_bounded_secure_sampling(monkeypatch):
    def randbelow(bound):
        assert bound == 3
        return 2

    monkeypatch.setattr(randomness.secrets, "randbelow", randbelow)
    assert randomness.choose_bucket() == 2


def test_demo_keys_match_hkdf_with_distinct_contexts():
    seed = bytes(range(32))
    salt = bytes(range(32, 64))
    extracted = hmac.digest(salt, seed, "sha256")
    # 32 字节为 SHA-256 的一个输出块，HKDF-Expand 的计数器为 1。
    encryption = hmac.digest(extracted, b"gxa-demo:v1:encryption\x01", "sha256")
    authentication = hmac.digest(extracted, b"gxa-demo:v1:authentication\x01", "sha256")

    assert derive_demo_keys(seed, salt) == (encryption, authentication)
    assert encryption != authentication
    assert derive_demo_keys(seed, salt[::-1]) != (encryption, authentication)


@pytest.mark.parametrize("seed_len,salt_len", [(31, 32), (32, 31)])
def test_demo_keys_require_32_byte_inputs(seed_len, salt_len):
    with pytest.raises(ValueError):
        derive_demo_keys(bytes(seed_len), bytes(salt_len))
