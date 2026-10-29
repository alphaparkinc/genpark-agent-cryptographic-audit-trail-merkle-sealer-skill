# -*- coding: utf-8 -*-
"""
GenPark Agent Cryptographic Audit Trail Merkle Sealer
Standard Library only: hashlib, json, math, typing.
Constructs tamper-evident append-only Merkle tree from agent execution telemetry,
generates logarithmic inclusion proofs, and verifies audit integrity.
"""

import hashlib
import json
import math
from typing import Dict, List, Tuple, Any

class GenParkAgentCryptographicAuditTrailMerkleSealer:
    def __init__(self):
        self.leaves: List[str] = []
        self.events: List[Dict[str, Any]] = []

    def _hash_pair(self, left: str, right: str) -> str:
        return hashlib.sha256((left + right).encode("utf-8")).hexdigest()

    def record_event(self, actor: str, action: str, details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Appends an event to the audit trail and computes its deterministic SHA-256 leaf hash.
        """
        canonical_event = {
            "index": len(self.events),
            "actor": actor,
            "action": action,
            "details": details
        }
        event_str = json.dumps(canonical_event, sort_keys=True, separators=(',', ':'))
        leaf_hash = hashlib.sha256(event_str.encode("utf-8")).hexdigest()

        self.events.append(canonical_event)
        self.leaves.append(leaf_hash)

        return {
            "event_index": canonical_event["index"],
            "leaf_hash": leaf_hash,
            "current_chain_length": len(self.leaves)
        }

    def compute_merkle_root(self) -> str:
        """
        Computes the current cryptographic root of the Merkle tree.
        """
        if not self.leaves:
            return hashlib.sha256(b"").hexdigest()

        current_level = list(self.leaves)
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i+1 < len(current_level) else left
                next_level.append(self._hash_pair(left, right))
            current_level = next_level

        return current_level[0]

    def generate_inclusion_proof(self, index: int) -> Dict[str, Any]:
        """
        Generates logarithmic audit proof path for verifying event inclusion.
        """
        if index < 0 or index >= len(self.leaves):
            raise IndexError("Event index out of range")

        proof_path = []
        current_level = list(self.leaves)
        idx = index

        while len(current_level) > 1:
            sibling_idx = idx + 1 if idx % 2 == 0 else idx - 1
            if sibling_idx < len(current_level):
                direction = "right" if idx % 2 == 0 else "left"
                proof_path.append({"hash": current_level[sibling_idx], "direction": direction})
            else:
                proof_path.append({"hash": current_level[idx], "direction": "right"})

            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i+1 < len(current_level) else left
                next_level.append(self._hash_pair(left, right))

            idx = idx // 2
            current_level = next_level

        return {
            "event_index": index,
            "leaf_hash": self.leaves[index],
            "merkle_root": self.compute_merkle_root(),
            "proof_path": proof_path
        }

    @staticmethod
    def verify_proof(leaf_hash: str, proof_path: List[Dict[str, str]], expected_root: str) -> bool:
        """
        Cryptographically verifies an inclusion proof against the expected root.
        """
        current_hash = leaf_hash
        for step in proof_path:
            sibling = step["hash"]
            if step["direction"] == "right":
                current_hash = hashlib.sha256((current_hash + sibling).encode("utf-8")).hexdigest()
            else:
                current_hash = hashlib.sha256((sibling + current_hash).encode("utf-8")).hexdigest()

        return current_hash == expected_root
