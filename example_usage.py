# -*- coding: utf-8 -*-
from client import GenParkAgentCryptographicAuditTrailMerkleSealer

def main():
    sealer = GenParkAgentCryptographicAuditTrailMerkleSealer()
    print("=== GenPark Agent Cryptographic Merkle Audit Sealer ===")

    # Ingest agent actions
    sealer.record_event("autonomous_trader", "authorize_payment", {"amount": 500, "token": "USDC"})
    sealer.record_event("autonomous_trader", "execute_swap", {"pool": "ETH-USDC", "slippage": 0.005})
    sealer.record_event("autonomous_trader", "withdraw_to_vault", {"destination": "0xABC..."})

    root = sealer.compute_merkle_root()
    print(f"Current Merkle Root: {root}")

    # Generate cryptographic proof for event 1 (execute_swap)
    proof_info = sealer.generate_inclusion_proof(1)
    print(f"Proof for Event #1: {len(proof_info['proof_path'])} intermediate steps")

    # Cryptographic verification
    is_valid = GenParkAgentCryptographicAuditTrailMerkleSealer.verify_proof(
        proof_info["leaf_hash"],
        proof_info["proof_path"],
        root
    )
    print(f"Tamper-evidence Verification: is_valid={is_valid}")

if __name__ == "__main__":
    main()
