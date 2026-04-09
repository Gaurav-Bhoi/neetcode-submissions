class Solution:

    def encode(self, strs: List[str]) -> str:
        return ",".join([string.encode("utf-16").hex() for string in strs])
    def decode(self, s: str) -> List[str]:
        if not s: return []
        return [bytes.fromhex(item).decode("utf-16") for item in s.split(",")]
